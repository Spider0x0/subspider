import os
os.system("clear")
# Logo And Name
print("""
        #####################################
        #                                   #
        #        Code By Spider JS          #
        #                                   #   
        #####################################
""")
# lib
import requests
# User Input
domin = input("Enter The Domin Name : ")
# WordList Of File
file = open("wordlist.txt",'r')
# To read a wordlist file
content = file.read()

subdomins = content.splitlines()
for subdomin in subdomins:
    url = f"https://{subdomin}.{domin}"
    try:
        requests.get(url)
        print(f"URL : {url}")
    except requests.ConnectionError:
        pass
