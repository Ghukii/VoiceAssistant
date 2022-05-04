import requests
from bs4 import BeautifulSoup as bs



url = 'https://www.youtube.com/results?search_query=phonk'
request = requests.get(url, headers=headers)
soup = bs(request.text, features="html.parser")
hrefs = soup.find_all("a")#'a', class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail"


for i in hrefs:
    print(i)

