#!/usr/bin/env python3

#
# auto_tester.py
#
# Date    : 2024-09-18
# Author  : Hirotoshi FUJIBE
# History :
#
# Copyright (c) 2024 Hirotoshi FUJIBE
#

# Import Libraries
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Constants
SLEEP_SECONDS = 2
URL = 'http://localhost:3000'
CMD_FILL = 1
CMD_CLEAR = 2
CMD_CLICK = 3
CMDS = [
    [CMD_CLICK, 'login'],
    [CMD_FILL, 'userName', 'root'],
    [CMD_CLICK, 'login'],
    [CMD_FILL, 'password', 'asdf1234'],
    [CMD_CLICK, 'login'],
    [CMD_CLEAR, 'password'],
    [CMD_FILL, 'password', 'Asdf1234'],
    [CMD_CLICK, 'login'],
    [CMD_CLICK, 'settings'],
    [CMD_CLICK, 'home'],
    [CMD_CLICK, 'logout'],
]


# Main
def main() -> None:

    # browser
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
#    driver.maximize_window()
    driver.get(URL)

    # processes
    for cmd in CMDS:
        time.sleep(SLEEP_SECONDS)
        if cmd[0] == CMD_FILL:
            html_textbox = driver.find_element(By.ID, str(cmd[1]))
            html_textbox.send_keys(str(cmd[2]))
        elif cmd[0] == CMD_CLEAR:
            html_textbox = driver.find_element(By.ID, str(cmd[1]))
            html_textbox.send_keys(Keys.CONTROL + "a")
            html_textbox.send_keys(Keys.DELETE)
        elif cmd[0] == CMD_CLICK:
            html_button = driver.find_element(By.ID, str(cmd[1]))
            html_button.click()
        else:
            print('Invalid command : %s' % cmd[0], file=sys.stderr)
            raise Exception('Invalid command.')

    # end
    time.sleep(SLEEP_SECONDS)
    driver.quit()
    sys.exit(0)


# Goto Main
if __name__ == '__main__':
    main()
