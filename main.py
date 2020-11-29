import time
from ZvikaCracker import ZvikaCracker
from requests.api import request
from crackerV1 import BasicCracker
from ZvikaCracker import ZvikaCracker
import requests


def main():
    #cracker1 = BasicCracker()
    #operateCracker(cracker2)
    #for _ in range(20):
    password = False
    while not password:
        zvikaCracker = ZvikaCracker()
        password = operateCracker(zvikaCracker)[1]
    #operateCracker(zvikaCracker)

def operateCracker(cracker): 
    print(cracker.url)
    password_len = cracker.find_pass_len()
    time.sleep(5)
    #password_len = 4
    password_without_last_char = cracker.find_password(password_len)
    time.sleep(1)
    password = cracker.find_pass_last_char(password_without_last_char)
    return password
    

if __name__ == "__main__":
    main()






