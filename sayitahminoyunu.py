#!/usr/bin/env python
#-*- coding.latin-1 -*-
import random
sayi=random.randint(1,100)
sayac=1
print "Tahmin Oyununa Hos Geldiniz"
tahmin=0

while tahmin!=sayi:
	tahmin=input("Sayi Girin:")
	if tahmin==sayi:
		print "Tebrikler %s denemede bildiniz!" % (sayac)
		break
	if tahmin<sayi:
		print "Daha Buyuk Bir Sayi Girin"
		sayac=sayac+1
	if tahmin>sayi:
		print "Daha Kucuk Bir Sayi Girin"
		sayac=sayac+1