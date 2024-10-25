import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

articleData = soup.find("c-flicking",{"id":"mor_history_id_0"})
doc = articleData.find_all("c-doc")

with open("c1021/daum_list.txt","w",encoding="utf-8") as f:
  for idx,Data in enumerate(doc) :
    titleList = doc[idx].find("c-title")
    resultData = doc[idx].find("c-contents-desc")

    f.write(titleList.next + "\n")
    f.write(resultData.next + "\n\n\n")

    print(f"\t {idx+1}. {titleList.next}")
    print(f"\t {resultData.next}")
    print()

    with open(f"c1021/img/img_{idx}.jpg","wb") as imgFile:
      re_img = requests.get(Data.find("c-thumb")['data-original-src'])
      imgFile.write(re_img.content)


# pageData = articleData.find("div",{"class":"pdt2"})
# print(pageData)

# ulData= pageData.find("ul",{"class":"c-list-basic"})
# listData = ulData.find_all("li")


# resultData1 = listData[0].find("strong",{"class":"tit-g clamp-g"}).find("p").text

# print(resultData1)