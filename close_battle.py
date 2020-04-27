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
