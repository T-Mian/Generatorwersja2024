"""
 Tomasz Mianecki 
Pusus_glancus
 versja 1.0
"""

import shutil
import os
import glob

centralny_katalog = os.getcwd()
polowa_adres = []

sub_adresy_docelowe = ["RysTech", "Foto", "Akcesoria", "Inne", "Rozsyl"]
for x in sub_adresy_docelowe:
  adres_a = centralny_katalog + "/" + x
  polowa_adres.append(adres_a)

rys = glob.glob("*_rystech.*")
akces = glob.glob("*_akces.*")
foto = glob.glob("*_foto.*")
inne = glob.glob("*_inne.*")
roz = glob.glob("*_roz.*")

for x in rys:
  do_kont = polowa_adres[0] + "/" + x
  sorce = centralny_katalog + '/' + x
  shutil.move(sorce, do_kont)

for x in foto:
  do_kont = polowa_adres[1] + "/" + x
  sorce = centralny_katalog + '/' + x
  shutil.move(sorce, do_kont)

for x in akces:
  do_kont = polowa_adres[2] + "/" + x
  sorce = centralny_katalog + '/' + x
  shutil.move(sorce, do_kont)

for x in inne:
  do_kont = polowa_adres[3] + "/" + x
  sorce = centralny_katalog + '/' + x
  shutil.move(sorce, do_kont)

for x in roz:
  do_kont = polowa_adres[4] + "/" + x
  sorce = centralny_katalog + '/' + x
  shutil.move(sorce, do_kont)
