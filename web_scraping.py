import requests, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


url = 'https://www.cbc.ca/archives'


options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
#options.add_argument('--headless')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)
driver.get(url)
#more_button = driver.find_element(By.CLASS_NAME, "loadMore")
time.sleep(100)
#more_button.click()
#for i in range(len(more_buttons)):
  #more_buttons[i].click()
page_source = driver.page_source
print(page_source)

#response = requests.get(url)

soup = BeautifulSoup(page_source, 'html.parser')
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
            file_name = "./Articles/article" + str(count) + ".txt"
            with open(file_name, "w") as f:
                f.write(title + "\n\n")
                for line in texts:
                    f.write(line.text)
                    f.write("\n")
        except requests.exceptions.ConnectionError: 
            print("Failed")
            continue

