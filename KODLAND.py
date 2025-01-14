import random

print("Hello world")
karakter= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunluğu=int(input("Şifre uzunluğu kaç olsun:"))

sifre=""

for i in range(sifre_uzunluğu):
    sifre= random.choice(karakter) + sifre

print("Sifrem", sifre)
