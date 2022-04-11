#!/usr/bin/python3

import sys, os, webbrowser, platform, subprocess, time
from colorama import Fore


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
print("                 V1.0")
time.sleep(3)
os.system('clear')


def menu():
    while True:
     print(Fore.GREEN + "Opciones\n")
     print("1) Spam-SMS")
     print("2) Comunicarte conmigo")
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




     elif d == "2":
        print("Mi numero , no es oficial +506 6087 1177")
        time.sleep(8)
    
     elif d == "99":
         break

     input("Presiona enter para volver como antes")
     os.system('clear')
menu()



