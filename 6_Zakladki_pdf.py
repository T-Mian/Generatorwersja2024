"""
Dodanie zakładek do pdf-a zborczego 
ver 2
Tomasz Mianecki

Postepowanie:
1. Wczytanie pliku pdf
2. Wczytanie pliku csv
3. Potwierdzenie nazw pliku(poprzez wpisanie nazwy)
"""
#importy 
#import pdb
import sys
import csv
import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter



ob_czas = datetime.datetime.now()

str_rok_skrucony=ob_czas.strftime("%y")

str_dzien_roku=ob_czas.strftime("%j")

okreslenie_versji=str_rok_skrucony+str_dzien_roku

#lista dla pliku raportu
#lista opreacyjna
list = []

""""w celu rozwiązania problemu
  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 502: invalid start byte
dopisane zostało errors='ignore'
"""
sp=input("Enter nazwę csv'a : ")
with open(sp+".csv", 'rt', encoding='utf8', errors='ignore') as plik:
    #załadowanie danych
    spamreader = csv.reader(plik, delimiter=';', quotechar='|')
    for row in spamreader:
        list.append(row[0])
#przygotowanie plików

spec=input("Enter nazwa pdf'a : ")
pdf_file = open(spec+".pdf", 'rb')
pdf_reader = PdfFileReader(pdf_file)
pdf_writer = PdfFileWriter()


global strona
global pozycja
#liczniki dzielenia
strona = 2
pozycja = 0
licznik = 0
list.pop(0)
n = pdf_reader.getNumPages()
nr=0
for i in range(n):
  pdf_writer.addPage(pdf_reader.getPage(i))
  if i%strona==0:
    pdf_writer.addBookmark(list[nr], i, parent=None)
    nr+=1
  else :
    print(i)

nazwa_pliku=spec.split("_")

with open(nazwa_pliku[0]+"_"+okreslenie_versji+"_"+str(strona)+".pdf", "wb") as fp:
    pdf_writer.write(fp) 

print("Koniec działania programu")

sys.exit(0)
