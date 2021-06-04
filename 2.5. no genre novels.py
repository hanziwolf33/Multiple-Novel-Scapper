#! python3
import os, requests, shutil
import bs4 as BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from unidecode import unidecode

global NovelName, file_name, page_number, Base_Url, DIR, last_page, text_folders, NovelFile, NovelList
file_name = 'genre_novels.txt'
page_number = 1
last_page = 2
NovelList = []
DIR = '.'
# replace ******** with genre name make sure to check the webpage url first
Base_Url = 'https://novelfull.com/index.php/genre/**********?page='
text_folders = 'D:/Novels/Text Chapter Novels'

CHROMEDRIVER_PATH = 'C:\Program Files\Python39\chromedriver.exe'

def Close():
    driver.stop_client()
    driver.close()
    driver.quit()
### Uncomment below to create the genre list you wish to remove
### Recomment below to use precreated list
#while page_number != last_page + 1:
#    url = '%(U)s%(P)s' % {'U': Base_Url, "P": page_number}
#    options = Options()
#    options.add_argument("--headless")
#    driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
#    driver.get(url)
#    print(url)
#    soup = BeautifulSoup.BeautifulSoup(driver.page_source, 'html.parser')
#
#    soupx = soup.find("div", class_="list list-truyen col-xs-12")
#    for a in soupx.find_all('a', href=True):
#        myfile = open(DIR +'/'+ file_name, 'a+')
#        myfile.write(a['href']+'\n')
#        myfile.close()
#    print("Completed "+str(page_number)+" pages so far.")
#    page_number+=1
#    driver.quit()
#print("Finished links for "+str(page_number -1)+" pages.")

NovelFile = open("genre_novels.txt", "r")

for line in NovelFile:
  stripped_line = line.strip()
  NovelList.append(stripped_line)
NovelFile.close()
NovelName = NovelList

while NovelName:
    NN = NovelName.pop(-1)
    NNx = NN.replace('.html', '').replace('-', ' ').replace('/','').upper()
    DIRx = '%(B)s/%(N)s' % {'B': text_folders, "N": NNx}
    try:
        os.mkdir(DIRx)
    except:
        print('folder already exists')
    if os.path.isfile(DIRx) or os.path.islink(DIRx):
        os.remove(DIRx)
        print('removed : '+NNx)
    elif os.path.isdir(DIRx):
        shutil.rmtree(DIRx)
        print('removed : '+NNx)
    else:
        print('defined path is not folder or dir')
        continue
