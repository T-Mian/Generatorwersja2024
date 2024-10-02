"""
Podział pliku pdf
plus generowanie kodu do linku na stronę 
Wersja 7.4
Tomasz Mianecki

"""
#import
import pdb
import csv
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import datetime

#lista opreacyjna 
list = []

global rok
dat = datetime.datetime.now()
rok=str(dat.year)

global raport
raport = []

lista_in = os.listdir()
raport.append("Zawartość folderu------------------>")
raport.append(lista_in)

nazwa = os.getcwd()
raport.append("Nazwa folderu----------------------->")
raport.append(nazwa)

typ = nazwa.split("\\")
print(typ )
produkt = typ[-1]
sp = produkt + "_"+rok+".csv"

raport.append("Kreacja nazwy csv----------------------->")
raport.append(sp)
sp.lower()
spec =produkt.lower()+"_"+rok
rap= "RAPORT.txt"
p = 0
if rap in lista_in:
  with open(rap, 'r',encoding='utf8',errors='ignore') as plik:
    lista_bet=[]
    lista_bet=plik.readlines()
    dl= len(lista_bet)
    wyn = dl/16
    p =+ wyn
    plik.close()
dopisanie_wersji="-ver_"+str(p)
raport.append("Wersja-------------------------------->")
raport.append(dopisanie_wersji)



""""w celu rozwiązania problemu
  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 502: invalid start byte
dopisane zostało errors='ignore'
"""
raport.append("Przygotowanie danych z bazy danych------------------------>")
with open(sp, 'rt',encoding='utf8',errors='ignore') as plik:
              #załadowanie danych
	spamreader = csv.reader(plik, delimiter=';' , quotechar='|')
	for row in spamreader:
		list.append(row[0])
#przygotowanie plików
pdf_file = open(spec+'.pdf','rb')
pdf_reader = PdfFileReader(pdf_file)
pdf_writer = PdfFileWriter()
raport.append("OK------------------------------------------->")

global strona;
global pozycja;
#liczniki dzielenia
strona = 0
pozycja = 0
licznik=0
# lista z obecnymi plikami/folderami obecnymi w obecnym folderze
lista_in = os.listdir()
#sprawdzenie czy istnieje folder z plikami wynikowymi
folder_docelowy=produkt+"_"+rok+"_Wyniki"
folder_wynikowy=""

if folder_docelowy in lista_in:
        raport.append("Folder obecny------------------------------------> ")
        folder_wynikowy=folder_docelowy+"\\"+dopisanie_wersji
        os.mkdir(folder_wynikowy)
        raport.append("Folder wykozystany to ----------------------------->" + folder_wynikowy)
else:
        raport.append("Folder nieobecny -------------------------------------->")
        os.mkdir(folder_docelowy)
        folder_wynikowy=folder_docelowy+"\\"+dopisanie_wersji
        os.mkdir(folder_wynikowy )
        raport.append("Utrwożenie folderu docelowego --------------------------------------->")

#proces dzielenia (dane z listy z danymi z pliku w csv)
raport.append("Start zapisu danych do kart------------------------------------> ")
for index in range (0,len(list)-1):
	pdf_writer.addPage(pdf_reader.getPage(strona))
	pdf_writer.addPage(pdf_reader.getPage(strona+1))
	# dla trzech kart odkomentować linię niżej
	#pdf_writer.addPage(pdf_reader.getPage(strona+2))
	nazwa =folder_wynikowy+"/"+list[pozycja+1]+dopisanie_wersji+'.pdf'
	split_file = open(nazwa,'wb')
	pdf_writer.write(split_file)
	pdf_writer = None
	pdf_writer = PdfFileWriter()
	split_file.close()
	# dla trzech kart zakomentować linię niżej [strona+=2]
	#strona+=1
	strona += 2
	#dla trzech kart odkomentować linię niżej  [strona += 3]
	#strona += 3
	pozycja += 1
	licznik+=1
pdf_file.close()
raport.append(str(licznik-1) +"kart/y  zrobione/ych -------------------------------------------------->"  )

#dane dla a href
nosnik= '  target="_blank"  '
dodatekA = '<a title="Karta katalogowa  produktu  '
subDodatekA = 'href="https://www.globuslighting.pl/'
dodatekB='/">'
dodatekC='</a>'

def aHrewiks():
  num =0
  del list[0]
  del list[0]
  raport.append("Kasacja zbędnych danych z listy operacyjnej i generowanie kodów a href na stronę  -------->")
  f = open(produkt+"-kody a href.txt", "a")
  f.write("Kody do produktu " + produkt+" wersja "+dopisanie_wersji )
  f.write("\n ==========================================\n")
  for x in list:
    wynik=dodatekA + x  +' " '+ nosnik+subDodatekA+x.lower()+dopisanie_wersji+dodatekB+x+dodatekC+"\n"
    f.write(wynik)
    num+=1
    if num%10==0:
      f.write('\n ------------------------------------------------------------------------------------------------------------------------------------------------------------- \n')
  f.write("\n")
  f.close()

aHrewiks()

raport.append("Koniec procesu i zapis raportu ===================================================" + str(dat))

with open(rap, 'a',encoding='utf8',errors='ignore') as plik:
  for x in raport:
    xx=str(x)
    plik.write(xx+"\n")

#print(raport)
