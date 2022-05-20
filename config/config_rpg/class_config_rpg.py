import asyncio
import random
from datetime import datetime, timezone, timedelta
import json
import os
import requests
from io import BytesIO

if os.path.exists(os.getcwd() + ".../config/firebase_link.json"):
    with open(".../config/firebase_link.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"link": "https://mikarpg-4d967-default-rtdb.firebaseio.com"}
    
    with open(os.getcwd() + "/config/firebase_link.json", "w+") as f:
        json.dump(configTemplate, f)

link_firebase = configTemplate["link"]

# config register database
class verfy_player_mika():
    def __init__(self, user):
        self.user = user

    def verify_player(self):
        security = requests.get(f"{link_firebase}/player/.json")
        verify_security = security.json()
        for rows in verify_security:
            security_player = verify_security[rows]["id"]
            if f"{self.user}" == security_player:
                return True


    def player_raca(self):
        security = requests.get(f"{link_firebase}/player/.json")
        verify_raca = security.json()
        for rows in verify_raca:
            user_raca = verify_raca[rows]["id"]
            if f"{self.user}" == user_raca:
                return verify_raca[rows]["raca"]


    def player_cristias(self):
        security = requests.get(f"{link_firebase}/player/.json")
        verify_cristais = security.json()
        for rows in verify_cristais:
            user_cris = verify_cristais[rows]["id"]
            if f"{self.user}" == user_cris:
                return verify_cristais[rows]["cristais"]


    def player_background(self):
        security = requests.get(f"{link_firebase}/player/.json")
        verify_background = security.json()
        for rows in verify_background:
            user_back = verify_background[rows]["id"]
            if f"{self.user}" == user_back:
                return verify_background[rows]["background"]


    def player_magia(self):
        security = requests.get(f"{link_firebase}/player/.json")
        verify_magia = security.json()
        for rows in verify_magia:
            user_magia = verify_magia[rows]["id"]
            if f"{self.user}" == user_magia:
                return verify_magia[rows]["magia"]


    def player_ataque(self):
        security = requests.get(f"{link_firebase}/player/.json")
        verify_ataque = security.json()
        for rows in verify_ataque:
            user_ataque = verify_ataque[rows]["id"]
            if f"{self.user}" == user_ataque:
                return verify_ataque[rows]["ataque"]


    def player_resistencia(self):
        security = requests.get(f"{link_firebase}/player/.json")
        verify_resistencia = security.json()
        for rows in verify_resistencia:
            user_resistencia = verify_resistencia[rows]["id"]
            if f"{self.user}" == user_resistencia:
                return verify_resistencia[rows]["resistencia"]


    def player_defesa(self):
        security = requests.get(f"{link_firebase}/player/.json")
        verify_defesa = security.json()
        for rows in verify_defesa:
            user_defesa = verify_defesa[rows]["id"]
            if f"{self.user}" == user_defesa:
                return verify_defesa[rows]["defesa"]


    def player_fc(self):
        security = requests.get(f"{link_firebase}/player/.json")
        verify_fc = security.json()
        for rows in verify_fc:
            user_fc = verify_fc[rows]["id"]
            if f"{self.user}" == user_fc:
                return verify_fc[rows]["fc"]


    def player_hp(self):
        security = requests.get(f"{link_firebase}/player/.json")
        verify_hp = security.json()
        for rows in verify_hp:
            user_hp = verify_hp[rows]["id"]
            if f"{self.user}" == user_hp:
                return verify_hp[rows]["hp"]


    def player_mundo(self):
        security = requests.get(f"{link_firebase}/player/.json")
        verify_hp = security.json()
        for rows in verify_hp:
            user_hp = verify_hp[rows]["id"]
            if f"{self.user}" == user_hp:
                return verify_hp[rows]["mundo"]
