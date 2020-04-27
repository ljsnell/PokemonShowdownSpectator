# # `pokemon-showdown.py`
# Automated bot which spectates random Pokemon Showdown matches and coordinates a `twitch_chat_bot` to manage bets on the winners within a configured account/channel. 
#
# ## Dependencies

# +
from selenium import webdriver
import time
from get_names import getNames, getWinner
from twitch_connect import twitch_chat_bot

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
    print("After refresh")
    
    # open list of active battles
    view_battle_button = driver.find_element_by_xpath('//*[@id="room-"]/div/div[1]/div[2]/div[3]/p[1]/button')
    view_battle_button.click()
    driver.implicitly_wait(10)
    print('view_battle_button 1 clicked')
    
    # select first active battle listed
    refresh_button = driver.find_element_by_xpath('//*[@id="room-battles"]/div/div/div/div[1]/a')
    refresh_button.click()
    driver.implicitly_wait(10)
    
    # reset battle playback to the first move
    start_of_battle_button = driver.find_element_by_name("instantReplay")
    start_of_battle_button.click()
    driver.implicitly_wait(10)
    print('after wait')
    
    # extract player names from battle log
    battle_log = driver.find_element_by_class_name("battle-log").text
    left_name, right_name = getNames(battle_log)
    
    # Post bet & options to twitch chat
    twitch_handler.post_msg('!bet open "Who will win?" "' + left_name + ", " + right_name + '" 1 1000 2')
    
    # loop until battle ends
    battle_over, bets_open = False, True
    while not battle_over:
        
        # wait twenty seconds
        time.sleep(20)
        
        # report winner and close bets to Twitch Channel
        if ("won the battle!" or "This room is expired" or "All players are inactive." or "Tie between") in battle_log:
            battle_over = True
            winner = getWinner(battle_log)
            print(battle_log)
            print("winner")
            print(winner)
            twitch_handler.post_msg("!bet close " + winner)
            
            # 10 seconds after bets close, exit battle and loop
            time.sleep(10)
            attempts = 0
            while attempts < 3:
                try:
                    close_battle_button = driver.find_element_by_name("closeRoom")
                    close_battle_button.click()
                    print("Close button clicked")
                    break
                except:
                    print("Caught stale exception")
                    driver.refresh()
                attempts = attempts + 1

    # return to and refresh battle list
    time.sleep(5)
    view_battle_button = driver.find_element_by_xpath('//*[@id="room-"]/div/div[1]/div[2]/div[3]/p[1]/button')
    view_battle_button.click()
    print('view battle button 2 clicked')
    
    driver.implicitly_wait(10)
    refresh_button = driver.find_element_by_name("refresh")
    refresh_button.click()
    print("Refresh button clicked")
    driver.implicitly_wait(10)
