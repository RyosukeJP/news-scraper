import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.yahoo.co.jp/"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

news_list = []

# ニュースリンクだけ取得
for a_tag in soup.find_all("a", href=True):
    title = a_tag.get_text().strip()
    link = a_tag["href"]

    # 条件：ニュースっぽいリンクだけ
    if "news.yahoo.co.jp/articles" in link and title:
        news_list.append([title, link])

# 重複削除
news_list = list(set(tuple(item) for item in news_list))

# CSV保存
with open("news.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["タイトル", "URL"])
    writer.writerows(news_list)

print("ニュースをCSVに保存しました！")