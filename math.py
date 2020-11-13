#modules

import os, sys
import time
import datetime
import math

# warna

W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray

os.system('clear')

#baner

def baner():
	print(C+'Latihan Membuat Kalkulator Sederhana')
	time.sleep(1)
	print(G+'\nBy' + R + '     : ' + W + 'Affan R')
	time.sleep(1)
	print(G+'Github' + R + ' : ' + W + 'http://github.com/lordpann')
	
def aritmatika():
	print("""
1. Pertambahan
2. Pengurangan
3. Perkalian
4. Pembagian
""")

	menu = int(input("[AR] > "))
	
	if menu == 1:
		tambah()
	elif menu == 2:
		kurang()
	elif menu == 3:
		kali()
	elif menu == 4:
		bagi()
		
def tambah():
	a = int(input("Masukan bilangan: "))
	b = int(input("Masukan bilangan: "))
	jumlah = a+b
	print("Hasil dari", a,"+", b,"adalah", jumlah)
	
def menu():
	print("""
1. Aritmatika
2. Pemfaktoran
3. Max Min
""")
	menu = int(input("[AR] > "))
	
	if menu == 1:
		aritmatika()
	elif menu == 2:
		pemfaktoran()
	elif menu == 3:
		maxmin()
	else:
		baner()
		menu()
		
baner()
menu()