import os
import csv

a = [1,2,3,4,5]
b = [x*x for x in a]

print(b)

st_list = ["순위", "종목명", "검색비율", "현재가", "전일비", "등락률", "거래량", "시가", "고가", "저가", "PER", "ROE"]
sto_list = ['1', '삼성전자', '11.68%', '57,800', '상승100', '+0.17%', '7,852,187', '57,500', '58,200', '57,100', '14.13', '4.15']
sto_list2 = ['2', '삼성전자', '11.68%', '57,800', '상승100', '+0.17%', '7,852,187', '57,500', '58,200', '57,100', '14.13', '4.15']

with open("c1023/a.csv","w",encoding="utf-8",newline="") as csvFile:
  writer = csv.writer(csvFile)
  writer.writerow(st_list)
  writer.writerow(sto_list)
  writer.writerow(sto_list2)


with open("c1023/list.txt","w",encoding="utf-8") as f:
  f.write(st_list+ "\n")
  f.writelines(sto_list+ "\n")