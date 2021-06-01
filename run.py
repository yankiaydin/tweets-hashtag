from selenium import webdriver
import time
from log_info import username, password

browser = webdriver.Firefox()

url = "https://twitter.com/"

browser.get(url)

login_btn = browser.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div")
login_btn.click()

time.sleep(2)
input_name = browser.find_element_by_name("session[username_or_email]")
input_pass = browser.find_element_by_name("session[password]")

input_name.send_keys(username)
input_pass.send_keys(password)

btn2 = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")
btn2.click()

time.sleep(2)
src_area = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/label/div[2]/div/input")
hashtag = "#yazılımayolver"
src_area.send_keys(hashtag)
src_area.submit()

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

tweets = []
elements = browser.find_elements_by_css_selector(".css-1dbjc4n .r-1loqt21 .r-18u37iz .r-1ny4l3l .r-1udh08x .r-1qhn6m8 .r-i023vh .r-o7ynqc .r-6416eg .css-1dbjc4n")

for element in elements:
    tweets.append(element.text)

tweetNo = 1

with open("tweets.txt","w", encoding= "utf-8") as file:
    for tweet in tweets:
        file.write(str(tweetNo) + "-" + "\n" + tweet + "\n")
        file.write("******************\n")
        tweetNo += 1

browser.close()