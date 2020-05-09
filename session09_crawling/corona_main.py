import requests
from bs4 import BeautifulSoup
from corona import extract_info

import csv
file = open('corona.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["시도", "시군구", "선별진료소(이름)", "전화번호"])

hospital_html = requests.get('https://www.mohw.go.kr/react/popup_200128_3.html')
hospital_html.encoding = 'utf-8'
hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")
hospital_table_box = hospital_soup.find("tbody", {"class" : "tb_center"})
hospital_table = hospital_table_box.find_all("tr")
final_result = extract_info(hospital_table)

for result in final_result:
  
  row = []
  row.append(result['city'])
  row.append(result['city_detail'])
  row.append(result['name'])
  row.append(result['phone'])
  writer.writerow(row)

