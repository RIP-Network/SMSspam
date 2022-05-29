#!/usr/bin/python3

import sys, os, webbrowser, platform, subprocess, time
from colorama import Fore
from importlib_metadata import version


banner = Fore.RED + """…………..$……………………………………..$…………..
…………$$……………………………………..$$…………
…………$$……………………………………..$$…………
…………..$$s………………………………s$$…………..
…………….$$$$……………………….$$$$…………….
………………³$$$$..¶¶¶¶¶¶¶¶..$$$$³………………
………………..³$$$$..¶¶¶¶¶¶..$$$$³………………..
………………¶..$$$$$..¶¶¶¶..$$$$$..¶………………
…………….¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶………………
…………….¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶………………
…………….¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………
………………..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………..
………………..¶¶……..¶¶¶¶……….¶……………………
………………..¶¶……..¶¶¶¶……….¶¶………………….
………………..¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶………………….
………………….¶¶¶¶¶¶……¶¶¶¶¶¶¶………………….
……………………….¶¶¶¶¶¶¶¶¶…………………………
……………………….¶..¶..¶..¶..¶…………………………
…………¶…………..¶…………..¶…………..¶…………..
……….¶¶……………………………………….¶¶…………
……….¶¶……………………………………….¶¶…………
……….¶¶…………..¶¶……….¶¶…………..¶¶…………
……….¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶…………
……¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶……..
….¶¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶¶……
……¶¶¶¶..¶¶..¶¶………………….¶¶..¶¶..¶¶¶¶……..
"""


print(banner)
print(Fore.GREEN + "              RIP-Network")
print("                 V2.5")
time.sleep(3)
os.system('clear')


def menu():
    while True:
     print(Fore.GREEN + "Opciones\n")
     print("1) Spam-SMS")
     print("2) Instalar requisitos")
     print("3) Version ")
     print("4) Comunicarte conmigo")
     print("99)Salir")

     d = input(Fore.LIGHTBLUE_EX + "Elige una opcion --> ")

     if d == "1":
        print ("Por favor espere ")
        print ("Nota : No funciona con numeros virtuales")
        webbrowser.open('https://www.instagram.com/accounts/password/reset/')
        time.sleep(2)
        webbrowser.open('https://accounts.snapchat.com/accounts/password_reset/phone')
        time.sleep(2)
        webbrowser.open('https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0')
        time.sleep(2)
        webbrowser.open('https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D')
        time.sleep(2)
        webbrowser.open('https://mail.yandex.com/')
        time.sleep(2)
        webbrowser.open('https://web.telegram.org/k/')
        print("Coloque el número de la víctima en los lugares donde le pone que ponga el número y listo")
        time.sleep(8)

     if d == "2":
        print("Vuelva atras del programa y ejecute en la terminal bash install.sh")

     if d == "3":
         print("version 2.0 by RIP-Network")
    

     elif d == "4":
        print("Aún no disponible pero en mi canal de YouTube puedes comentar")
        time.sleep(8)

      
     elif d == "99":
         break

     input("Presiona enter para volver como antes")
     os.system('clear')
menu()
