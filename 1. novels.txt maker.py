#! python3
import os
import bs4 as BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

global file_name, page_number, Base_Url, DIR, last_page
file_name = 'novels.txt'
page_number = 1
last_page = 16
DIR = '.'
Base_Url = 'https://novelfull.com/index.php/completed-novel?page='
CHROMEDRIVER_PATH = 'C:\Program Files\Python39\chromedriver.exe'

while page_number != last_page + 1:
    url = '%(U)s%(P)s' % {'U': Base_Url, "P": page_number}
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
    driver.get(url)
    print(url)
    soup = BeautifulSoup.BeautifulSoup(driver.page_source, 'html.parser')
    soupx = soup.find("div", class_="list list-truyen col-xs-12")
    for a in soupx.find_all('a', href=True):
        myfile = open(DIR +'/'+ file_name, 'a+')
        myfile.write(a['href']+'\n')
        myfile.close()
    print("Completed "+str(page_number)+" pages so far.")
    page_number+=1
    driver.quit()
print("Finished links for "+str(page_number - 1)+" pages.")
#EOF
