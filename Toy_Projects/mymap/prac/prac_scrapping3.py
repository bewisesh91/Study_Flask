from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient
import requests


client = MongoClient('52.79.227.172', 27017, username="test", password="test")
db = client.linkedin

driver = webdriver.Chrome('./chromedriver')

#main > div > div > div.pv2.artdeco-card.ph0.mb2 > ul > li:nth-child(1) > div > div > div.entity-result__content.entity-result__divider.pt3.pb3.t-12.t-black--light > div.mb1 > div > div.t-roman.t-sans > span > div > span.entity-result__title-line.flex-shrink-1.entity-result__title-text--black > span > a > span > span:nth-child(1)
#main > div > div > div.pv2.artdeco-card.ph0.mb2 > ul > li:nth-child(2) > div > div > div.entity-result__content.entity-result__divider.pt3.pb3.t-12.t-black--light > div.mb1 > div > div.t-roman.t-sans > span > div > span.entity-result__title-line.flex-shrink-1.entity-result__title-text--black > span > a > span > span:nth-child(1)

for i in range(1,2) :
    url = "https://www.linkedin.com/search/results/people/?keywords=%EC%B9%B4%EC%B9%B4%EC%98%A4&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH"+str(i)
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/main/p/a').click()
    time.sleep(3)
    driver.find_element_by_id("username").send_keys('bewise.seunghyun@gmail.com')
    driver.find_element_by_id("password").send_keys('DLAaksndpf12!')
    driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
    info_more = driver.find_element_by_css_selector("#main > div > div > div.pv2.artdeco-card.ph0.mb2 > ul > li:nth-child(1) > div > div > div.entity-result__content.entity-result__divider.pt3.pb3.t-12.t-black--light > div.mb1 > div > div.t-roman.t-sans > span > div > span.entity-result__title-line.flex-shrink-1.entity-result__title-text--black > span > a > span > span:nth-child(1)").click()
    time.sleep(3)
    ex_com = driver.find_element_by_css_selector("#\31 379839521").text
    print(ex_com)
#
#     req = driver.page_source
#     soup = BeautifulSoup(req, 'html.parser')
#     places = soup.select("ul.restaurant_list > div > div > li > div > a")
#
# driver.quit()
#
# soup = BeautifulSoup(req, 'html.parser')
#
# places = soup.select("ul.restaurant_list > div > div > li > div > a")
# print(len(places))
#
#
#


#
# for place in places:
#     title = place.select_one("strong.box_module_title").text
#     address = place.select_one("div.box_module_cont > div > div > div.mil_inner_spot > span.il_text").text
#     category = place.select_one("div.box_module_cont > div > div > div.mil_inner_kind > span.il_text").text
#     show, episode = place.select_one("div.box_module_cont > div > div > div.mil_inner_tv > span.il_text").text.rsplit(" ", 1)
#     print(title, address, category, show, episode)
#
#     # headers에 나의 naver API 정보를 담아서 보내준다.
#     headers = {
#         "X-NCP-APIGW-API-KEY-ID": "es14wzgnxt",
#         "X-NCP-APIGW-API-KEY": "qtNELykjPXgox55bfAeJ8tNdsi9LwOhbtfpFpkw0"
#     }
#     r = requests.get(f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}", headers=headers)
#     response = r.json()
#
#     if response["status"] == "OK":
#         if len(response["addresses"]) > 0:
#             x = float(response["addresses"][0]["x"])
#             y = float(response["addresses"][0]["y"])
#             print(title, address, category, show, episode, x, y)
#             doc = {
#                 "title": title,
#                 "address": address,
#                 "category": category,
#                 "show": show,
#                 "episode": episode,
#                 "mapx": x,
#                 "mapy": y}
#             db.matjips.insert_one(doc)
#         else:
#             print(title, "좌표를 찾지 못했습니다")