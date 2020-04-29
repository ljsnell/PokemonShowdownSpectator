import time

def closeBattle(driver):
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

def filterBattles(driver, gen_to_filter_button_path):
     attempts = 0
     while attempts < 3:
         try:
             filter_dropdown = driver.find_element_by_xpath('/html/body/div[4]/div/div/p[2]/button')
             filter_dropdown.click()
             driver.implicitly_wait(10)
             filter_button = driver.find_element_by_xpath(gen_to_filter_button_path)
             filter_button.click()
             driver.implicitly_wait(10)
             break
         except:
             print("Caught filter button exception")
             time.sleep(2)
         attempts = attempts + 1