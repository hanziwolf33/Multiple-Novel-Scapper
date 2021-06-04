import os, requests
from unidecode import unidecode

txtDIR = 'D:/Novels/Text Chapter Novels'
DIR = '.'
txt_files = os.listdir(txtDIR)

for data in txt_files:
  textList = open(DIR +'/'+ 'List.txt', 'a+')
  textList.write(unidecode(data.lower())+'\n')
  textList.close()

print('Finished writing all the folder names in Text Chapter Novels.')
