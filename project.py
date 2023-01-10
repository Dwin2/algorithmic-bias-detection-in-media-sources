import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.cbc.ca/archives')

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.title)
blog_titles = soup.find_all('h3', attrs='headline')
links = soup.find_all('a', href=True)
#for title in blog_titles:
#    print(title.text)
invalid = ["https://www.cbc.ca/archives", "https://cbc.ca/archives/arts", "https://cbc.ca/archives/history", "https://cbc.ca/archives/sports"]
count = 0
for i in links:
    if "https:" not in i['href']: link = "https://cbc.ca" + i['href']
    if "/news/" in link or ('/archives/' in link and link not in invalid):
        try:
            count += 1
            print(link)
            response2 = requests.get(link)
            soup2 = BeautifulSoup(response2.text, 'html.parser')
            texts = soup2.find_all('p')
            title = soup2.find_all('h1', attrs='detailHeadline')[0].text
            file_name = "article (" + str(count) + ") .txt"
            with open(file_name, "w") as f:
                f.write(title + "\n\n")
                for line in texts:
                    f.write(line.text)
                    f.write("\n")
        except requests.exceptions.ConnectionError: 
            print("Failed")
            continue

keywords = {"white" : 0, "black" : 0, "asian" : 0, "indigenous" : 0}

for i in range(1, count+1):
    file_name = "article (" + str(i) + ") .txt"
    with open(file_name, "r") as f:
        
