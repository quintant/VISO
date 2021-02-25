from selenium import webdriver
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "BABA"
PASSWORD = "BOOEY"
ALL_LEFT = u"\u001b[1000D"
UP = "\u001b[{}A"
GREEN = "\u001b[32m"
MAGENTA = "\u001b[35m"
YELLOW = "\u001b[33m"
RED = "\u001b[31m"
BLUE = "\u001b[34m"
BOLD = "\u001b[1m"
UNBOLD = "\u001b[0m"
COLOR_LIST  = [GREEN, MAGENTA, YELLOW, RED, BLUE]
CLEAR_ALL = "\u001b[2J"

print(CLEAR_ALL + UP.format(1000))

t = datetime.datetime.today()
future = datetime.datetime(t.year, t.month, t.day, 11, 25) # TODO: Skrifa inn kl hvað skráning byrjar

if t.hour >= 2:
    future += datetime.timedelta(days=1)
sleeptime = (future - t).seconds

while sleeptime > 0:
    print(f"{YELLOW}Sleeping for:")
    print(f"{GREEN}{int(sleeptime/60/60)//24:0>2d} : {MAGENTA}days")
    print(f"{GREEN}{int(sleeptime/60/60)%24:0>2d} : {MAGENTA}hours")
    print(f"{GREEN}{int(sleeptime//60)%(60):0>2d} : {MAGENTA}minutes")
    print(f"{GREEN}{int(sleeptime)%(60):0>2d} : {MAGENTA}seconds")
    t = datetime.datetime.today()
    time.sleep(1)
    sleeptime = (future - t).seconds
    print(UP.format(5) + ALL_LEFT, end="")





from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")

print(f"{MAGENTA + BOLD}Action: {UNBOLD + GREEN}Starting driver{UNBOLD}")
driver = webdriver.Chrome(options=options)

print(f"{MAGENTA + BOLD}Action: {UNBOLD + GREEN}Fetching website{UNBOLD}")
driver.get("https://velnem.hi.is/")

print(f"{MAGENTA + BOLD}Action: {UNBOLD + GREEN}Clicking: {YELLOW} SKRÁ INN{UNBOLD}")
elem = driver.find_element_by_link_text("SKRÁ INN")
elem.click()
time.sleep(1)

print(f"{MAGENTA + BOLD}Action: {UNBOLD + GREEN}Filling out: {YELLOW} Username{UNBOLD}")
inputElement = driver.find_element_by_id("username")
inputElement.send_keys(USERNAME)

print(f"{MAGENTA + BOLD}Action: {UNBOLD + GREEN}Filling out: {YELLOW} Password{UNBOLD}")
inputElement = driver.find_element_by_id("password")
inputElement.send_keys(PASSWORD)

print(f"{MAGENTA + BOLD}Action: {UNBOLD + GREEN}Clicking: {YELLOW} Login{UNBOLD}")
inputElement = driver.find_element_by_id("btn-login")
inputElement.click()
time.sleep(2)

print(f"{MAGENTA + BOLD}Action: {UNBOLD + GREEN}Selecting: {RED}VÍSÓ{UNBOLD}")
links = driver.find_elements_by_link_text('Meiri upplýsingar')

for i in range(len(links)):
    print(links[i].get_attribute("href"))

driver.get(links[0].get_attribute("href"))
print(f"{MAGENTA + BOLD}Selected: {UNBOLD + GREEN}{links[0].get_attribute('href')}{UNBOLD}")

vanilla_hardcore = "Niðurtalning í skráningu"

cnt = 1
while True:
    if vanilla_hardcore in driver.page_source:
        print(f"{MAGENTA + BOLD}Login attempts: {BLUE}{cnt}{UNBOLD}")
        cnt += 1
        driver.refresh()
        time.sleep(0.2)
        print(UP + ALL_LEFT, end="")
    else:
        bleb = driver.find_element_by_id("inn")
        bleb.click()
        print(CLEAR_ALL + UP.format(1000))
        for i in range(25):
            print(f"{COLOR_LIST[i%5]}YOU ARE NUMBER 1!!!!{UNBOLD}")
            print(UP.format(1) + ALL_LEFT, end="")
            time.sleep(1)
        quit()
