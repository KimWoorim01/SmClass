import requests
# naver 파일 저장. 리솜리조트 파일 저장

url = [
  "http://naver.com",
  "http://www.daum.net/",
  "http://www.resom.co.kr/resom/main/main.asp",
]

headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}


for i in range(len(url)):
  res = requests.get(url[i],headers=headers)
  res.raise_for_status()

  with open(f"c1021/test_0{i}.html","w",encoding="utf-8") as f:
    f.write(res.text)


