"""
Program startowy dla generator kart produktu
Tomasz Mianecki
wersja 3.5
alfa


"""
# importy
import os
import csv
import datetime

#wartości globalne

global lista_in
lista_in = []
global nazwa_folderu
pelna_nazwa_folderu = ""
global podzial_nazwy
podzial_nazwy = []
global rok
x = datetime.datetime.now()
rok = str(x.year)
global nazwa_produktu
nazwa_produktu = ""
global startowe_dane
startowe_dane = ()
wypychacz = "xxx"
item_Zas = []
item_Cze = []
dir_list = []
kart_data=""

#Okreslenie unikalnej wersji produktu

ob_czas = datetime.datetime.now()
str_rok_skrucony=ob_czas.strftime("%y")
str_dzien_roku=ob_czas.strftime("%j")
okreslenie_versji=str_rok_skrucony+str_dzien_roku

# Dane z Profilu

with open("2_PROFIL.txt", encoding='utf-8', mode="r") as f:
  co_to = (f.readline())
  co_to = co_to[12:-1]
  #print(co_to)
  typ_karty = (f.readline())
  typ_karty = typ_karty[11:-1]
  #print(typ_karty)
  data_typ = (f.readline())
  data_typ = data_typ[9:]
  dot = data_typ.split(",")
  dot.pop()
  startowe_dane = tuple(dot)
  #print(dot)
  zastos = (f.readline())
  zastos = zastos[13:]
  item_Zas = zastos.split('@')
  item_Zas.pop()
  #print(item_Zas)
  cechy = (f.readline())
  cechy = cechy[6:]
  item_Cze = cechy.split('@')
  item_Cze.pop()
  #print(item_Cze)
  param = (f.readline())
  param = param[10:]
  param = param.split('@')
  param.pop()
  #print(param)
  foldery = (f.readline())
  foldery = foldery[8:]
  dir_list = foldery.split(',')
  dir_list.pop()
  #print(dir_list)
  data_karty=(f.readline())
  data_karty=data_karty[11:]
  #print(data_karty)
# pobieranie danych

baza_Latex = "{"
for x in dot:
  q = " \\" + x + "=" + x + ","
  baza_Latex += q

baza_Latex = baza_Latex[:-1]
baza_Latex += "}"
#print(baza_Latex)

z_astosowanie = """ 
"""
for x in item_Zas:
  w = "\\item " + x + "\n"
  z_astosowanie += w

z_astosowanie = z_astosowanie[:-1]
#print(z_astosowanie)

c_zechy = """
"""
for x in item_Cze:
  w = "\\item " + x + "\n"
  c_zechy += w

c_zechy = c_zechy[:-1]
#print(c_zechy)

lista_in = os.listdir()
pelna_nazwa_folderu = os.getcwd()
podzial_nazwy = pelna_nazwa_folderu.split("\\")
nazwa_produktu = podzial_nazwy[-1]
nazwa_produktu = nazwa_produktu.lower()

#następne kroki

plik_csv = nazwa_produktu +"_"+okreslenie_versji+ ".csv"  #nazwa dla csv

with open(plik_csv, encoding='utf-8', newline='',
          mode="a") as plik:  #tworzenie/otwieranie pliku csv
  wr = csv.writer(plik, delimiter=';')
  wr.writerow(startowe_dane)
  wypelniacz = ()
  yyy = list(wypelniacz)
  for x in startowe_dane:
    yyy.append('xxx')
  wypelniacz = tuple(yyy)
  wr.writerow(wypelniacz)
  plik.close()

content_laTex = """\\documentclass[12pt,twoside]{article}

%%%%---Pakiety---%%%%
\\usepackage{tcolorbox}
\\usepackage[top=2cm, bottom=2cm, left=2cm, right=2cm]{geometry}
\\usepackage[utf8]{inputenc}
\\usepackage[polish]{babel}
\\usepackage[T1]{fontenc}
\\usepackage{graphbox,float}
\\usepackage{eso-pic}
\\usepackage{graphics}
\\usepackage{xcolor}
\\usepackage{fontspec}
\\usepackage{fancyhdr}
\\usepackage{tabularx}
\\usepackage{tikz}
\\usepackage{datatool}

\\usetikzlibrary{calc}
\\pagestyle{fancy} 

    %%%%---Czcionki---%%%% 
\\setmainfont[Ligatures=TeX]{Lato-Semibold} 
\\definecolor{gray}{RGB}{230,230,229}
\\definecolor{yellow}{RGB}{247,209,25}

\\newenvironment{itemize*}%
   {\\begin{itemize}%
     \\setlength{\\itemsep}{0pt}%
     \\setlength{\\parskip}{0pt}}%
   {\\end{itemize}}

   \\newcommand\\blfootnote[1]{%
   \\begingroup
   \\renewcommand\\thefootnote{}\\footnote{#1}%
   \\addtocounter{footnote}{-1}%
   \\endgroup
} 

     %%%%---Nagłówek---%%%%															%%%%---Nagłówek---%%%%
\\fancyhf{} 
\\renewcommand{\\headrulewidth}{0pt} \n"""
content_laTex= content_laTex+"\\lhead {"+co_to+"\\\ \n"+"{\\footnotesize Karta "+typ_karty+" produktu}} \n"
content_laTex+=""" \\setlength\\headheight{27pt}
\\rhead{\\includegraphics[width=4cm]{Foto/logo_duze_foto}} 
 
%%%%---Dokument---%%%%
\\begin{document}
    %%%%---Ładowanie bazy---%%%% 
\DTLsetseparator{;} 
\DTLloaddb{myDB}{"""

content_laTex += plik_csv + "}"
content_laTex += """    % 			WPISAĆ BAZĘ CSV (BAZA POWINNA BYĆ WYGENEROWANA Z EXELA ZA POPOCĄ "ZAPISZ JAKO" I WYBRAC "PLIK CSV UTF-8 (ROZDZIELANY PRZECINKAMI)(*.CSV)") 
\\DTLforeach* %						KOLEJNOŚĆ W BAZIE MUSI SIĘ ZGADZAĆ Z KOLEJNOŚCIĄ WPISANĄ  W LINIJCE 56,W PRZYPADKU DOPISANIA "x" DO NIEJ NALEŻY UŻYĆ WZORU ", \X=X," NIE ZMIENIAĆ NIC POZA "X"-EM
{myDB}% database label 
"""
content_laTex += baza_Latex
content_laTex += """
{ %start for 
%%%%---Tytuł, belka i kółeczko---%%%%										%%%%---Tytuł, belka i kółeczko---%%%%
\\begin{tabular}{ll}
\\begin{tcolorbox}[ 	
    frame code={},
	center title,
    valign=center,
    left=0pt,
    right=0pt,
    top=0pt,
    bottom=0pt,
    colback=gray,
    width=380pt,
    height=57pt,
    enlarge left by=-4cm,
    boxsep=5pt,
    arc=28pt]
\\textsc{\\hspace{2cm} \\Large \\kod } %%                KOD OPRAWY
\\end{tcolorbox}&\\begin{tcolorbox}[width=57pt,
colback=yellow,
colframe=yellow,
halign=center,valign=center,
square,circular arc]
\\end{tcolorbox}
\\end{tabular}
\\\ 

%%%%---Obrazek---%%%%												FOTO PRODUKTU
\\AddToShipoutPictureBG*{
  \\AtTextUpperLeft{%
    \\makebox[\\textwidth][r]{% Move over to right so right aligns with right of text block
      \\raisebox{-10cm}{% Drop down so top aligns with top of text block                     REGULACJA OBNIŻENIA OBRAZKA WZGLĘDEM ZERA (GDZIE ZERO JEST W GÓRNEJ KRAWĘDZI STRONY)
           \\includegraphics[width=0.45\\textwidth,align=b]{Foto/\\foto}   %              PARAMETR WIELKOŚCI ZDIĘCIA ( "=1" ZNACZY ORYGINALNY WYMIAR)
      }%
    }%
  }%
}% 

\\begin{tcolorbox}[frame code={} %kreakcja podtytulu     ZASTOSOWANIE ( W ZÓŁTEJ BELCE)
    center title,
    valign=center,
    left=0pt,
    right=0pt,
    top=0pt,
    bottom=0pt,
    colback=yellow,
    width=250pt,
    height=31pt,
    enlarge left by=-4cm,
    boxsep=5pt,
    arc=15pt]\\hspace{3cm} \\large Zastosowanie 
\\end{tcolorbox}

\\begin{small} %								PUNKTOWANIE DLA ZASTOSOWANIA , JEZELI POTRZEBA DOPISAĆ/SKOPIOWAĆ  "\item " I POMIĘTAĆ O SPACJI PO SKOPIOWANIU 
\\begin{itemize*}"""
content_laTex += z_astosowanie
content_laTex += """
\\end{itemize*}
\\end{small}

\\begin{tcolorbox}[frame code={} %kreakcja podtytulu    						CECHY PRODUKTU ( W ZÓŁTEJ BELCE)
    center title,
    valign=center,
    left=0pt,
    right=0pt,
    top=0pt,
    bottom=0pt,
    colback=yellow,
    width=250pt,
    height=31pt,
    enlarge left by=-4cm,
    boxsep=5pt,
    arc=15pt,
 	outer arc=0pt]\\hspace{3cm} \\large Cechy produktu
\\end{tcolorbox}

\\begin{small} % 									PUNKTOWANIE DLA CECH PRODUKTU ,JEZELI POTRZEBA DOPISAĆ/SKOPIOWAĆ  "\item " I POMIĘTAĆ O SPACJI PO SKOPIOWANIU
\\begin{itemize*}"""
content_laTex += c_zechy
content_laTex += """ 
\\end{itemize*}
\\end{small}

\\begin{tcolorbox}[frame code={} %kreakcja podtytulu    							PARAMETRY  ( W ZÓŁTEJ BELCE)
    center title,
    valign=center,
    left=0pt,
    right=0pt,
    top=0pt,
    bottom=0pt,
    colback=yellow,
    width=250pt,
    height=31pt,
    enlarge left by=-4cm,
    boxsep=5pt,
    arc=15pt,
 	outer arc=0pt]\\hspace{3cm} \\large Parametry
\\end{tcolorbox}
%%%																	TABELA Z PARAMETRAMI PRODUKTU		"""

content_laTex += """
\\begin{table}[H]
\\centering
\\begin{scriptsize} %           ŚCIĄGA MOŻLIWYCH PARAMETRÓW;  Napięcie sterowania \\vs, >\\cri  ,± 0,3 kg, \\temperatury,Wsp. zachowania str. świetlnego , L90B10,L80B10,Ochrona przeciprzep.-ooo°C do +ooo°C 
\\begin{tabularx}{\\textwidth}{lllX}
\\textbf{Ogólne}                             &          				  		& \\textbf{Świetlne}                                     &            			       				\\\  
Kod produktu                            	& \\kod        					& Moc znamionowa *                                     	& \\p {} W       			       			\\\ 
Kod Rodziny                            		& \\rodzina      				& Strumień świetlny oprawy**                            &\\flux {} lm         			       		\\\ 
Kod barwy                          			& \\kodbarwy       				& Wydajność oprawy **                                   & \\wyd	{} lm/W         			      		\\\  
Wbudowany zasilacz                          & \\psu      					& CRI/Ra                                     			& >\\cri          			       			\\\ 
Producent zasilacza                         & \\ppsu		    				& Temperatura barwowa                                   & \\cct {} K           			       		\\\ 
Sterowanie                           		& \\sterowanie    				& Barwa światła                                     	& \\barwa         			       			\\\ 
Klasa ochronności                      		& \\klasa {} klasa ochronności	& Kąt rozsyłu                                   		&\\pled {}°     		       				\\\ 
Stopień ochrony                             & \\IP      				  		&                                       				&            			       				\\\ 
Odporność na uderzenia                    	& \\IK        				    &                                       				&            			       				\\\ 
Kolor                             			& \\kolor        				& \\textbf{Pozostałe}                                    &            			       				\\\ 
Producent źródeł światła                    & OOO         					& Waga                                     				& \\masa {} ± 0.3kg         						\\\  
Ilość źródeł światła                        & \\ilosc        				& Żywotność                                          	& OO 000 h          			       		\\\  
                             				&          				  		& Sposób montażu                                     	& \\montaz       			       			\\\  
                             				&          				  		& Zakres temperatur otoczenia                           & \\temperatury          					\\\  
\\textbf{Elektryczne}                        &          				  		& \\textbf{Mechaniczne}                                  &            			       				\\\  
Napięcie znamionowe                         & \\vin        					& Materiał obudowy                                      & ooo								        \\\  
Częstotliwość sieciowa                      & \\hz       					& Materiał klosza                                       & \\dyfuzor        							\\\  
                             				&          				  		& Wymiary (mm)                   						& \\wymiary     			       			        \\\  
                             				&          				  		&                                       				&            			       		\\\  
\\multicolumn{4}{l}{* tolerancja mocy $\\pm$5\\%}              \\\ 
\\multicolumn{4}{l}{** tolerancja strumienia świetlnego 7\\% w temp. otoczenia 25\\textdegree C}\\\ 
\\end{tabularx}
\\end{scriptsize}
\\end{table}
\\newpage """

content_laTex += """
\\begin{tcolorbox}[frame code={} %kreakcja podtytulu 		
    center title,
    valign=center,
    left=0pt,
    right=0pt,
    top=0pt,
    bottom=0pt,
    colback=yellow,
    width=250pt,
    height=31pt,
    enlarge left by=-4cm,
    boxsep=5pt,
    arc=15pt,
 	outer arc=0pt]\\hspace{3cm} \\large Rysunek wymiarowy
\\end{tcolorbox}

\\includegraphics[width=0.3\\textwidth]{RysTech/\\rys}

\\begin{tcolorbox}[frame code={} %kreakcja podtytulu  						KRZYWA ROZSYŁU ( W ZÓŁTEJ BELCE)
    center title,
    valign=center,
    left=0pt,
    right=0pt,
    top=0pt,
    bottom=0pt,
    colback=yellow,
    width=250pt,
    height=31pt,
    enlarge left by=-4cm,
   boxsep=5pt,
    arc=15pt,
 	outer arc=0pt]\\hspace{3cm} \\large Krzywa rozsyłu
\\end{tcolorbox}

\\includegraphics[width=0.30\\textwidth]{Rozsyl/\\rozsyl}                      % "WYDRUK" RYSUNKU KRZYWEJ ROZSYŁU  (WIELKOŚĆ  30 PROCENT Z ORYGINAŁU)

\\begin{tcolorbox}[frame code={} %kreakcja podtytulu 						MOZNTAZ / ZMIENNIE INFO , ( W ZÓŁTEJ BELCE)
    center title,
    valign=center,
    left=0pt,
    right=0pt,
    top=0pt,
    bottom=0pt,
    colback=yellow,
    width=250pt,
    height=31pt,
    enlarge left by=-4cm,
    boxsep=5pt,
    arc=15pt,
 	outer arc=0pt]\hspace{3cm} \\large Akcesoria
\\end{tcolorbox}

%\\includegraphics[width=0.30\\textwidth]{Inne/\\xxx}
\\includegraphics[width=0.30\\textwidth]{Akcesoria/\\xxx}


\\blfootnote{\\textbf{Oświadczenie}\\\ 
Zastrzega się możliwość zmian bez uprzedzenia. Błędy i ominięcia są możliwe. Należy zawsze upewnić się czy korzystasz z najnowszej wersji dokumentu.\\ \ 
\\begin{flushright}
\\ 
\\ """
content_laTex += data_karty
content_laTex+="""\\\ 
\\end{flushright}}
 
 \\newpage 
 }
\\end{document}"""

tex = nazwa_produktu +"_"+okreslenie_versji+ ".tex"

with open(tex, 'a', encoding='utf8', errors='ignore') as plik:
  plik.write(content_laTex)

print(lista_in)

for x in dir_list:
  if x in lista_in:
    continue
  os.mkdir(x)

#sektor logów print( )
#print(lista_in )
#print(pelna_nazwa_folderu )
#print( podzial_nazwy )
#print( nazwa_produktu )
#print(content_laTex)
print("ok")
