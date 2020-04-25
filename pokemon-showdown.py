from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://play.pokemonshowdown.com/")
driver.maximize_window()
while 1>0:    
    driver.refresh()
    print("After refresh")
    view_battle_button = driver.find_element_by_xpath('//*[@id="room-"]/div/div[1]/div[2]/div[3]/p[1]/button')
    view_battle_button.click()
    driver.implicitly_wait(10)
    print('view_battle_button 1 clicked')
    refresh_button = driver.find_element_by_xpath('//*[@id="room-battles"]/div/div/div/div[1]/a')
    refresh_button.click()
    driver.implicitly_wait(10)
    # view_battle_button = driver.find_element_by_xpath('//*[@id="room-battle-gen8randombattle-1101748307"]/div[5]')
    start_of_battle_button = driver.find_element_by_name("instantReplay")
    start_of_battle_button.click()
    driver.implicitly_wait(10)
    print('after wait')

    # Loop and read battle log every x seconds. Then look for 'won the battle!' and search for a new match.
    battle_over = False
    while battle_over == False:
        driver.execute_script("document.body.style.MozTransform = 'scale(1.33)';")
        driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
        time.sleep(20)
        bodyText = driver.find_element_by_class_name("battle-log").text
        print(bodyText)
        if "won the battle!" in bodyText or "This room is expired" or "All players are inactive." or "Tie between" in bodyText:
            battle_over = True
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
            
    # Refresh Battle List
    time.sleep(5)
    view_battle_button = driver.find_element_by_xpath('//*[@id="room-"]/div/div[1]/div[2]/div[3]/p[1]/button')
    view_battle_button.click()
    print('view battle button 2 clicked')
    driver.implicitly_wait(10)
    refresh_button = driver.find_element_by_name("refresh")
    refresh_button.click()
    print("Refresh button clicked")
    driver.implicitly_wait(10)