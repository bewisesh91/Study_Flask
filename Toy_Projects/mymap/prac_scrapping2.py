from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome('./chromedriver')

url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%95%84%EC%9D%B4%EC%9C%A0"
driver.get(url)
sleep(10)
driver.execute_script("window.scrollTo(0, 1000)")  # x좌표는 0만큼, y좌표는 1000픽셀만큼 내리기
sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # x좌표는 0만큼, y좌표는 문서 전체
sleep(10)


req = driver.page_source
driver.quit()

soup = BeautifulSoup(req, 'html.parser')
images = soup.select(".tile_item._item ._image._listImage")
print(len(images))

for image in images:
    src = image["src"]
    print(src)

