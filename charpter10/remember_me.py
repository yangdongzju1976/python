import json

filename='username.json'
try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("please input your name?")
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"we`ll remember you when you come back,{username}!")
else:
    print(f"Welcome back,{username}!")
