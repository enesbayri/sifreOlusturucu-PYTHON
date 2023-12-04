import random



harfler="qwertyuopasdfghjklizxcvbnm"
bharfler="QWERTYUIOPASDFGHJKLZXCVBNM"
rakamlar="0123456789"
ozeller="!'^+%&/()=?*-£#$½{[]}|_"
sifren=""
olusturucu=""

sk=int(input("Sifre kaç karakter olmali? ->"))
bh=input("Sifre buyuk harf icersin mi? (y/n) ->")
kh=input("Sifre kucuk harf icersin mi? (y/n) ->")
rk=input("Sifre rakam icersin mi? (y/n) ->")
oz=input("Sifre ozel karakter icersin mi? (y/n) ->")

olusturucu=(bh=="y")*bharfler+(kh=="y")*harfler+(rk=="y")*rakamlar+(oz=="y")*ozeller

for i in range(sk):
    sifren+=random.choice(olusturucu)
print("\n\nsifrenizi kimseyle paylasmayiniz!!!")
print("sifreniz: {}".format(sifren))