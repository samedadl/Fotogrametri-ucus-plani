# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:51:38 2020

@author: Samed
"""

# Fotogrametrik uçuş planlaması

# verilenler 

#   uçuş yüksekliği 
h = float(input("Uçuş Yüksekliğini Giriniz (m): "))*1000
#   kamera odak uzaklığı
c = float(input("Kamera Odak Uzaklığını Giriniz (mm): "))
#   enine boyuna örtü oranları L--boy Q--en
L = int(input("Boyuna Örtü Oranını Giriniz: % "))/100
Q = int(input("Enine Örtü Oranını Giriniz:  % "))/100
#   resim boyutları
RBu = int(input("Uzun Resim Boyutunu Giriniz (piksel): "))
RBk = int(input("Kısa Resim Boyutunu Giriniz (piksel): "))
#   Kamerada bir pikselin büyüklüğü
pb = float(input("Piksel Büyüklüğü Giriniz(mm): "))
#  uçuş hızı ---- drone hızı
v = float(input("Uçuş Hızını Giriniz (m/sn): "))
# resim kenarları google earth den ölçülen
RKu= float(input("Uzun Resim Kenarı Giriniz (m): "))
RKk= float(input("Kısa Resim Kenarı Giriniz (m): "))

# Örnek veriler
# h=81000
# c=3.61
# L=80/100
# Q=70/100
# RBu=4000
# RBk=3000
# pb=0.00156
# v=5
# RKu=393.24
# RKk=243.12 

# hesaplanacaklar
def roundup(number):
    return round(number+.5)
#     Resim Ölçek Sayısı (mb)
mb = h/c
#     Resim Kenarının Arazideki Karşılığı (S)(uzun kenar) 
Su = (RBu*pb*mb)/1000 #m
#     Resim Kenarının Arazideki Karşılığı (S)(kısa kenar)
Sk = (RBk*pb*mb)/1000 #m
#     Bir resmin Arazide Kapladığı Alan (f)
f = Su*Sk #m^2
#     %l Boyuna Örtü Oranında Baz Uzunluğu (B)
B = Su*(1-L) #m
#     %q Enine Örtü Oranında Şeritler Arası Mesafe (A)
A = Sk*(1-Q) #m
#     Stereoskopik Olarak Resmi Çekilen Alan (Fm)
Fm = (Su-B)*Su #m^2
#     Bloktaki Her Bir Stereomodel İçin Elde Edilen Yeni Alan (Fn)
Fn = B*A #m^2
#     Bir şeritteki resim sayısı(N)
N = (RKu/B)+4
#     Şerit sayısı (n)
n = (RKk/A)+1
#     Birbirini Takip Eden Resimler Arasındaki Süre (delta(t))
dt = B/v
#     Bir Bloktaki Resim Sayısı
bbrs = roundup(N)*roundup(n)
#     Şeritteki Model Sayısı
sms = roundup(N)-1
#     Toplam Model Sayısı 
tms = sms*roundup(n)
#     Toplam Uçuş Süresi
t = bbrs*dt/60

print('SONUÇLAR'.center(100,'*'),f'''
      \nResim Ölçek Sayısı (mb): {mb}
Resim Kenarının Arazideki Karşılığı (S)(uzun kenar): {Su} m
Resim Kenarının Arazideki Karşılığı (S)(kısa kenar): {Sk} m
Bir resmin Arazide Kapladığı Alan (f): {f} m^2
%l Boyuna Örtü Oranında Baz Uzunluğu (B): {B} m
%q Enine Örtü Oranında Şeritler Arası Mesafe (A): {A} m
Stereoskopik Olarak Resmi Çekilen Alan (Fm): {Fm} m^2
Bloktaki Her Bir Stereomodel İçin Elde Edilen Yeni Alan (Fn): {Fn} m^2
Bir şeritteki resim sayısı(N): {N}
Şerit sayısı (n): {n}
Birbirini Takip Eden Resimler Arasındaki Süre (delta(t)): {dt} sn
Bir Bloktaki Resim Sayısı: {bbrs}
Şeritteki Model Sayısı: {sms}
Toplam Model Sayısı: {tms}
Toplam uçuş süresi: {t} dk
''')
