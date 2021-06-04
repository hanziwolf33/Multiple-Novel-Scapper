import os, requests, glob, shutil
from unidecode import unidecode
from fpdf import FPDF

File = open("List.txt", "r")
List = []
for line in File:
  stripped_line = line.strip()
  List.append(stripped_line)
File.close()

global Name, DIRx, baseDIR, baseDIRx, count_folders, n_num
Name = List
baseDIR = "D:/Novels/Text Chapter Novels"
baseDIRx = "D:/Novels/PDF Chapter Novels"
count_folders = len(Name)
n_num = 0
print('Total amount of novels to be converted: '+str(count_folders))

while Name:
    NN = Name.pop(-1)
    DIRx = '%(B)s/%(N)s' % {'B': baseDIR, "N": NN}
    DIRxx = '%(B)s/%(N)s' % {'B': baseDIRx, "N": NN}
    n_num+=1
    try:
      os.mkdir(DIRxx)
      print('Starting to convert: '+NN+' to PDF format')
    except:
      print('Skipping: '+NN)
      print('Remaining number of novels to convert: '+(str(count_folders-n_num)))
      continue
    DIRy = DIRxx
    files = glob.glob(DIRx + '\\*.txt')
    files.sort(key=os.path.getmtime)
    num = len(files)
    while files:
      if num != 0:
        files_list = files.pop(-1)
        file_pdf = str(num)+'.pdf'
        for f in files_list:
          pdf = FPDF()
          pdf.add_page()
          pdf.set_font("Arial", size = 12)
          f = open(files_list, "r")
          for x in f: 
            pdf.write(5,txt=x)
          pdf.output(DIRy+'/'+file_pdf)
        pdf_files = glob.glob(DIRy + '\\*.pdf')
      num -= 1
    print('Completed conversion of: '+NN+' to PDF format')
    print('Remaining number of novels to convert: '+(str(count_folders-n_num)))
print('Finished converting all text files to PDF format.')
