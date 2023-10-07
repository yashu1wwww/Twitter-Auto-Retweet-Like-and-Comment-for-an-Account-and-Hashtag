from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random

commentsDict = ['good', 'amazing one', 'keep going', 'excellent', 'next video please', 'sub to your channel',
                'shared to others', 'made my day', 'keep it up', 'sensational', 'rock it', 'challenge it', 'post video daily',
                'work was amazing', 'needed more edit', 'edit was awesome', 'what a video man', 'watched yesterday',
                'you are genius', 'faster than light', 'your work needed success', 'new fan of you', 'keep rock dude',
                'copy cat', 'link the video', 'listening', 'writing', 'reading', 'playing', 'awesome content', 'mind-blowing',
                'inspiring', 'unbelievable', 'impressive', 'outstanding', 'fantastic', 'stellar', 'remarkable', 'exceptional',
                'brilliant', 'stellar', 'top-notch', 'superb', 'jaw-dropping', 'captivating', 'extraordinary', 'stellar',
                'unreal performance', 'world-altering', 'masterful', 'exceptional artist', 'incomparable', 'artistic brilliance'] #replace with other words if you needed..

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(6)
email = driver.find_element_by_name('text')
email.send_keys("Twitter123")  #replace with your twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("Twitter123")  #replace with your twitter password
password.send_keys(Keys.ENTER)
time.sleep(4)
driver.get("https://twitter.com/X")  #replace with which account you want to do...

#input_field = driver.find_element_by_xpath('//input[@data-testid="SearchBox_Search_Input"]')
#input_field.send_keys('#twitter') #replace with hashtag which you needed
#input_field.send_keys(Keys.ENTER)

time.sleep(4)
#Wait for the search results to load.......

while True:
    try:
        retweet_button = driver.find_element_by_xpath("//div[@data-testid='retweet']/div").click()  # retweet button
        time.sleep(1) #click on retweet button

        retweet_button = driver.find_element_by_xpath("//div[@data-testid='retweetConfirm']/div").click()  # retweet click #confirm
        time.sleep(2) #click on retweet button

        like_button = driver.find_element_by_xpath("//div[@data-testid='like']/div")  # like button
        like_button.click() #click on like button
        
        time.sleep(2)
        
        comment_button = driver.find_element_by_css_selector("div[data-testid='reply']")
        comment_button.click() #click on comment button
        
        time.sleep(1)
        
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        send_button.send_keys(random.choice(commentsDict)) #randomly send the comment

        time.sleep(1)

        reply_button = driver.find_element_by_xpath("//div[@data-testid='tweetButton']")
        reply_button.click() #click on reply button

        time.sleep(3)

    except Exception as e:
        print("An error occurred:", e)
        break  

        
