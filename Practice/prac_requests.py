import requests # requests 라이브러리 설치 필요

# 다음의 과정을 통해 javascript에서 ajax를 사용한 것과 유사한 결과를 얻을 수 있음
r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus :
    gu_name = gu['MSRSTE_NM']
    gu_mise1 = gu['IDEX_NM']
    gu_mise2 = gu['IDEX_MVL']
    if gu_mise2 < 70 :
        print(gu_name, gu_mise1, gu_mise2)

