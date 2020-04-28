# # `pokemon-showdown.py`
# Automated bot which spectates random Pokemon Showdown matches and coordinates a `twitch_chat_bot` to manage bets on the winners within a configured account/channel. 
#
# ## Dependencies

# +
from selenium import webdriver
import time
from get_names import getNames, getWinner
from twitch_connect import twitch_chat_bot
from close_battle import closeBattle
import random

# start twitch_chat_bot - credentials/channel specified in `twitch_connect.py`
twitch_handler = twitch_chat_bot()

# start webdriver, navigate to showdown and have window take fullscreen
driver = webdriver.Firefox()
driver.get("https://play.pokemonshowdown.com/")
driver.maximize_window()
# -

# ## Main Loop

while True:
    
    # refresh page
    driver.refresh()
    
    # open list of active battles
    view_battle_button = driver.find_element_by_xpath('//*[@id="room-"]/div/div[1]/div[2]/div[3]/p[1]/button')
    view_battle_button.click()
    driver.implicitly_wait(10)

    # select first active battle listed
    refresh_button = driver.find_element_by_xpath('//*[@id="room-battles"]/div/div/div/div[1]/a')
    refresh_button.click()
    driver.implicitly_wait(10)
    
    # reset battle playback to the first move
    start_of_battle_button = driver.find_element_by_name("instantReplay")
    start_of_battle_button.click()
    driver.implicitly_wait(10)

    # extract player names from battle log
    battle_log = driver.find_element_by_class_name("battle-log").text
    left_name, right_name = getNames(battle_log)
    # Post bet & options to twitch chat
    twitch_handler.post_msg('!bet open "Who will win?" "' + left_name + ", " + right_name + '" 1 1000 2')    
    
    # loop until battle ends
    loop_count = 0
    battle_over, bets_open = False, True
    while not battle_over:
        loop_count = loop_count + 1
        # wait twenty seconds
        time.sleep(20)
        # Check if Twitch irc server has sent a ping and respond with pong. Should help with disconnects.
        twitch_handler.respond_to_pings()

        battle_log = driver.find_element_by_class_name("battle-log").text
        
        # report winner and close bets to Twitch Channel
        if "won the battle!" in battle_log:
            battle_over = True
            winner = getWinner(battle_log)
            twitch_handler.post_msg("!bet close " + winner)            
            closeBattle(driver)

        # If > 20 minutes have passed for a battle abandon it.
        elif loop_count > 60:
            battle_over = True
            # Randomly determine winner
            winner = random.choice([left_name, right_name])            
            twitch_handler.post_msg("Room timed out, defaulting winner.")
            twitch_handler.post_msg("!bet close " + winner)
            
            closeBattle(driver)
            
    # return to and refresh battle list
    print(battle_log)
    time.sleep(5)
    view_battle_button = driver.find_element_by_xpath('//*[@id="room-"]/div/div[1]/div[2]/div[3]/p[1]/button')
    view_battle_button.click()
    
    driver.implicitly_wait(10)
    refresh_button = driver.find_element_by_name("refresh")
    refresh_button.click()
    driver.implicitly_wait(10)
