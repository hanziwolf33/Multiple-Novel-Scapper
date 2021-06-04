#! python3
import os, easygui, requests
import bs4 as BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from unidecode import unidecode

global chapter_number, NovelName, DIR, baseDIR, currentURL, lastURL, count_folders, n_num
chapter_number = 0
baseDIR = "D:/Novels/Text Chapter Novels"
CHROMEDRIVER_PATH = 'C:\Program Files\Python39\chromedriver.exe'

def Close():
    driver.stop_client()
    driver.close()
    driver.quit()

NovelFile = open("novels.txt", "r")
NovelList = []
for line in NovelFile:
  stripped_line = line.strip()
  NovelList.append(stripped_line)
NovelFile.close()

NovelName = NovelList
count_folders = len(NovelList)
n_num = 0

while NovelName:
    NN = NovelName.pop(-1)
    NNx = NN.replace('.html', '').replace('-', ' ').upper()
    DIR = '%(B)s/%(N)s' % {'B': baseDIR, "N": NNx}
    n_num+=1
    try:
      os.mkdir(DIRxx)
      print('Starting to copy: '+NN+' to txt format')
    except:
      print('Skipping: '+NN)
      print('Remaining number of novels to copy: '+(str(count_folders-n_num)))
      continue
    BaseURL = 'https://novelfull.com'
    url = '%(U)s%(N)s' % {'U': BaseURL, "N": NN}
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
    driver.get(url)
    currentURL = driver.current_url
    lastURL = ''
    soup = BeautifulSoup.BeautifulSoup(driver.page_source, 'html.parser')
    soupx = soup.find("div", class_="col-xs-12 col-sm-6 col-md-6")
    links=[]
    for a in soupx.find_all('a', href=True):
        links.append(a['href'])
    BaseURL = 'https://novelfull.com'
    link = links[0]
    url = '%(U)s%(N)s' % {'U': BaseURL, "N": link}
    driver.get(url)
    currentURL = driver.current_url

    while currentURL != lastURL:
        soup = BeautifulSoup.BeautifulSoup(driver.page_source, 'html.parser')
        readables = soup.find(id='chapter-content')
        name = driver.title
        filename = name.replace('\\','').replace('<',' ').replace('"',' ').replace('>',' ').replace('/',' ').replace("|",' ').replace("?",' ').replace("*",' ').replace(":", ' -').replace('Read ',"").replace(' online free from your Mobile, Table, PC... Novel Updates Daily ',"").replace(' online free - Novel Full',"")
        if filename == 'Not Found (404)':
            url = easygui.enterbox("Enter correct link for the chapter.")
            driver.get(url)
            name = driver.title
            filename = name.replace('<',' ').replace('"',' ').replace('>',' ').replace('/',' ').replace("|",' ').replace("?",' ').replace("*",' ').replace(":", ' -').replace('Read ',"").replace(' online free from your Mobile, Table, PC... Novel Updates Daily ',"").replace(' online free - Novel Full',"")
        file_name = (str(chapter_number) + ' ' + filename + '.txt')
        #print(file_name)
        data = ''
        for data in soup.find_all("p"):
            myfile = open(DIR +'/'+ file_name, 'a+')
            myfile.write(unidecode(data.get_text())+'\n'+'\n')
            myfile.close()
        lastURL = driver.current_url
        #print('**********Chapter Copied!**********')
        chapter_number += 1
        bLink = soup.find(id = "next_chap")
        cLink = 'Next Chapter'
        link = driver.find_element_by_link_text(cLink)
        link.click()
        currentURL = driver.current_url
    print('Finished copying: '+NN+' to txt format')
    print('Remaining number of novels to copy: '+(str(count_folders-n_num)))
    chapter_number = 0
    Close()
#EOF
