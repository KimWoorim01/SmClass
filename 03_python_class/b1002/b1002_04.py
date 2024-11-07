import datetime

today = datetime.datetime.now()

if int(today.hour) < 12 :
  print("오전")
else:
  print("오후")

# today = datetime.datetime.now()
# print("{}-{:02}-{:02} {:02}:{:02}:{:02}".format(today.year, today.month, today.day, today.hour, today.minute, today.second,))

# print(today.year,"년")
# print(today.month,"월")
# print(today.day,"일")
# print(today.hour,"시")
# print(today.minute,"분")
# print(today.second,"초")