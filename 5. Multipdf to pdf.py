import os, PyPDF2, requests, glob, shutil
from unidecode import unidecode

global baseDIR, baseDIRx, ListName, num, Name
baseDIR = 'D:/Novels/PDF Chapter Novels'
baseDIRx = 'D:/Novels/PDF Book Novels'
DIR = '.'

File = open("List.txt", "r")
ListName = []
for line in File:
  stripped_line = line.strip()
  ListName.append(stripped_line)
File.close()

Name = ListName.pop(-1)
files = glob.glob(baseDIR+'/'+Name + '/*.pdf')
files.sort(key=os.path.getmtime)
num = len(files)

while files:
  if num != 0:
    print('Remaining novels to be converted into book style: '+str(num))
    ListPDF = files.pop(-1)
    global LocationPDF
    LocationPDF = ListPDF
    LPDF = LocationPDF
    userpdflocation=baseDIR+'/'+Name
    os.chdir(userpdflocation)
    userfilename=Name.replace(' pdf','')
    print('Creating pdf book style version of: '+userfilename)
    x=0
    pdf2merge = []
    for filename in os.listdir('.'):
      x+=1
      if filename.endswith('.pdf'):
        if filename == str(x)+'.pdf':
          pdf2merge.append(filename)
        else:
          filename = str(x)+'.pdf'
          pdf2merge.append(filename)

    pdfWriter = PyPDF2.PdfFileWriter()

    for filename in pdf2merge:
      pdfFileObj = open(filename,'rb')
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
      for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        pdfOutput = open(baseDIRx+userfilename+'.pdf', 'wb')
    pdfWriter.write(baseDIRx+pdfOutput)
    pdfOutput.close()
    shutil.move(pdfOutput, baseDIRx)
    print('Finished pdf book style version of: '+userfilename)
  num-=1
