
# Importing libraries
import os
import smtplib, ssl
import time
import hashlib
from bs4 import BeautifulSoup
from selenium import webdriver
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from pytz import timezone
import config
from cryptography.fernet import Fernet

# Selenium Webdriver configuration
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


# driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)
# Initial Scheduler Setup
executors = {'default': ThreadPoolExecutor(2), 'processpool': ProcessPoolExecutor(max_workers=2)}
scheduler = BackgroundScheduler(executors=executors, timezone=timezone('Asia/Kolkata'))
scheduler.start()


def scrape_html():
    """ Scrape HTML from URL """
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    #  Partner page for testing
    # url = "https://www.thetadrop.com/partner"
    # driver = webdriver.Chrome('./chromedriver', options=option)
    # driver.get(url)
    # time.sleep(5)
    # elem_for_testing = driver.find_element_by_xpath("//div[@class='g-header']")
    # soup = BeautifulSoup(elem_for_testing.get_attribute('outerHTML'), "html.parser")
    # print(soup)

    # For Main page
    url = 'https://www.thetadrop.com'
    # driver = webdriver.Chrome('./chromedriver', options=option)
    driver.get(url)
    time.sleep(60)
    elem_id_for_home_page = driver.find_element_by_xpath("//div[@id='app']")
    soup = BeautifulSoup(elem_id_for_home_page.get_attribute('outerHTML'), "html.parser")
    print(soup)
    driver.close()
    return (str(soup)).strip().encode()

# print(scrape_html())

def send_Notifiation_email():
    """ Send Notification Email """
    receiver_email = ["thaokarutkarsh@gmail.com"]
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "thaokarutkarsh@gmail.com"

    # FOR DEV ENVIRON
    decryption_obj = Fernet(os.environ['fernet_key'])
    decryption_token = decryption_obj.decrypt(str.encode(os.environ['encrypted_email_password']))


    password = ((decryption_token).decode('utf-8'))
    message = """
    Subject: Hi there
    Changes has taken place in Theta drop. Please Check. the given website.
    'https://www.thetadrop.com/'."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# send_Notifiation_email()
currentHash = hashlib.sha224(scrape_html()).hexdigest()
print('Initial CurrentHash',currentHash)


def check_for_changes_in_website():
    global currentHash
    if config.check_for_scheduler_status == 'RUN':
        try:
            print('Initial Hash', currentHash)

            # currentHash = hashlib.sha224(scrape_html()).hexdigest()
            # print(' cureent 77', currentHash)

            time.sleep(30)

            newHash = hashlib.sha224(scrape_html()).hexdigest()
            print('NewHash', newHash)

            if newHash == currentHash:
                print('No changes')

            else:
                # send_Notifiation_email()
                print("something has changed")
                currentHash = newHash
                print('New Initial Hash', currentHash)

        except Exception as e:
            print("Error in check_for_changes_in_website function : ", e)


def schedule():
    if config.check_for_scheduler_status != 'RUN':
        print("Stopped")
        scheduler.remove_job('check_for_changes_in_website')
    elif config.check_for_scheduler_status == 'RUN':
        print("Background Scheduler is RUNNING")
        scheduler.add_job(check_for_changes_in_website, "interval", minutes=10, coalesce=False,
                          replace_existing=True,max_instances=1, id='check_for_changes_in_website')
        for let in scheduler.get_jobs():
            print(let)
