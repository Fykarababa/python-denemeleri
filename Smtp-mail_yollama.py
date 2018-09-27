#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
"""
Burada g mail in servisi kullanılmakta ... Mailleri gönderebilmeniz için;
https://myaccount.google.com/lesssecureapps url e girip Daha az güvenli uygulamalara izin ver: KAPALI şekle getirmeniz gerekmekte
"""
mesaj = MIMEMultipart()
mesaj["From"] = "(sizin gmail adresiz)@gmail.com"
mail = input("Mail adresi giriniz :")
mesaj["To"] = mail
baslik = input("Başlığı giriniz :")
mesaj["Subject"] = baslik

icerik = input("Lütfen Mesajınızı yazınız :\n")

icerik
mesaj_govdesi = MIMEText(icerik,"plain")
mesaj.attach(mesaj_govdesi)
#istenirse aşağıdaki kodlar loop a alınıp mail attırabilirsiniz
try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)# smtp sunucusunu veriyoruz, port veriyoruz
    mail.ehlo()#smtp serverine bağlanacağımızı söylüyoruz
    mail.starttls()# kullanıcı adı ve parolalar şifreleniyor
    mail.login("(sizin gmail adresiniz)@gmail.com", "parolanız")#login olmamız sağlayan kısım kendi kullanıcı adınızı ve parolanızı girmeniz gerek
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())# mail imizin kimden kime gideceğini inceliyoruz
    print("Mail Başarı ile gönderildi")
    mail.close()# smtp sunucunu sonlandırdık
except:
    sys.stderr.write("Bir sorun oluştu !!!...")
    sys.stderr.flush()
