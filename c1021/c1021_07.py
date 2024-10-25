import requests

from bs4 import BeautifulSoup


url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

wraps = soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})
for idx,newList in enumerate(wraps) :
  print(f"{idx+1} 타이틀 : ",newList.find("strong",{"class":"rankingnews_name"}).find().text)
  ranks = newList.find("ul",{"class":"rankingnews_list"})
 




# wraps = soup.find("div",{"class":"rankingnews_box_wrap"})

# print(wraps.find("strong",{"class":"rankingnews_name"}))

# newsList = wraps.find("ul",{"class":"rankingnews_list"})
# tlist = newsList.find_all("li")
# for i,t in enumerate(newsList):
#   print(t.find("a").text)



# wraps = soup.find("div",{"class":"rankingnews_list"})

# print("기사1 \n",wraps,end="\n\n")


# boxs =  wraps.find("div",{"class":"list_content"})

# print("="*50)
# print("내용 \n",boxs)

