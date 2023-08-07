import requests
from ipinfo import getHandler
import os 
import subprocess
from colorama import Fore
access_token = "3bb2549065e1aa"  # Replace with your actual ipinfo.io access token
handler = getHandler(access_token)

def input_with_default(prompt, default="Inconnu"):
    user_input = input(prompt)
    return user_input if user_input.strip() != "" else default

def generate_dox_info(victim, age, photo_links, entreprise, raison, networks, coordinates, other_info, parents_info, internet_info, phone_info, ip_info):
    result = f"📂 - Informations Dox\n"
    result += f"│   ├── 📄 - Dox par Dev'Toya®\n"
    result += f"│   ├── 📄 - Entreprise du Dox : {entreprise}\n"
    result += f"│   └── 📄 - Raison : {raison}\n│\n"

    result += f"📂 - {victim}\n"
    result += "│\n"

    result += "├── 📂 - Réseaux sociaux\n"
    for network, username in networks.items():
        result += f"│   ├── 📄 - {network.capitalize()} : {username}\n"

    result += f"│\n"
    result += f"├── 📂 - Coordonnées\n"
    result += f"│   ├── 📄 - Numéro de téléphone : {coordinates['phone_num']}\n"
    result += f"│   │   ├── 📄 - Opérateur : {coordinates['operator']}\n"
    result += f"│   │   └── 📄 - Type : {coordinates['type']}\n"
    result += f"│   └── 📄 - Adresse : {coordinates['address']}\n│\n"

    result += f"├── 📂 - Autres informations\n"
    result += f"│   ├── 📄 - Âge : {age}\n"
    result += f"│   ├── 📄 - Date de naissance : {other_info['date_of_birth']}\n"
    result += f"│   ├── 📄 - Signe astrologique : {other_info['zodiac_sign']}\n"
    result += f"│   ├── 📄 - Ville : {other_info['city']}\n"
    result += f"│   └── 📄 - Pays : {other_info['country']}\n│\n"

    result += f"├── 📂 - Photos personnelles\n"
    for i, photo_link in enumerate(photo_links, start=1):
        result += f"│   ├── 📄 - Photo {i} : {photo_link}\n│\n"

    result += "└── 📂 - Parents informations\n"
    result += f"    ├── 📄 - Père : {parents_info['father']}\n"
    result += f"    └── 📄 - Mère : {parents_info['mother']}\n"

    result += f"\n📂 - Informations Internet\n"
    result += f"│   ├── 📄 - Date : {internet_info['date']}\n"
    result += f"│   ├── 📄 - Fournisseur d'accès Internet (FAI) : {internet_info['fai']}\n"
    result += f"│   ├── 📄 - Useragent : {internet_info['useragent']}\n"
    result += f"│   ├── 📄 - Adresse IP : {internet_info['ip_address']}\n"
    result += f"│   ├── 📄 - Pays : {internet_info['country']}\n"
    result += f"│   ├── 📄 - Ville : {internet_info['city']}\n"
    result += f"│   ├── 📄 - État : {internet_info['state']}\n"
    result += f"│   ├── 📄 - Latitude : {internet_info['latitude']}\n"
    result += f"│   └── 📄 - Longitude : {internet_info['longitude']}\n\n"

    result += f"📂 - Informations du téléphone\n"
    result += f"│   ├── 📄 - Navigateur : {phone_info['browser']}\n"
    result += f"│   ├── 📄 - Plateforme : {phone_info['platform']}\n"
    result += f"│   └── 📄 - Téléphone: {phone_info['phone_brand']}\n\n"

    result += f"📂 - Informations de l'IP\n"
    result += f"│   ├── 📄 - IP: {ip_info.ip}\n"
    result += f"│   └── 📄 - Info:\n"
    result += f"│       ├── 📄 - Ville: {ip_info.city}\n"
    result += f"│       ├── 📄 - Région: {ip_info.region}\n"
    result += f"│       ├── 📄 - Pays: {ip_info.country}\n"
    result += f"│       └── 📄 - Localisation: {ip_info.loc}\n"

    return result

# Fetch IP information
ip_address = input("Enter an IP address: ")
ip_info = handler.getDetails(ip_address)

# Collect victim information
victim = input("Victime: ")
age = input_with_default("Âge: ")
photo_links = input("Photo links (séparés par des virgules): ").split(", ")
entreprise = input_with_default("Entreprise du Dox: ")
raison = input("Raison du Dox: ")

networks = {
    "Discord": input_with_default("Discord: "),
    "Facebook": input_with_default("Facebook: "),
    "Snapchat": input_with_default("Snapchat: "),
    "Instagram": input_with_default("Instagram: "),
    # Ajouter d'autres réseaux sociaux au besoin
}

phone_num = input("Numéro de téléphone: ")
operator = input_with_default("Opérateur: ")
phone_type = input_with_default("Type de téléphone: ")
address = input_with_default("Adresse: ")

coordinates = {
    "phone_num": phone_num,
    "operator": operator,
    "type": phone_type,
    "address": address,
}

date_of_birth = input("Date de naissance: ")
zodiac_sign = input_with_default("Signe astrologique: ")
city = input_with_default("Ville: ")
country = input_with_default("Pays: ")

other_info = {
    "date_of_birth": date_of_birth,
    "zodiac_sign": zodiac_sign,
    "city": city,
    "country": country,
}

# Ajouter d'autres informations au besoin

photo_links = input("Liens des photos personnelles (séparés par des virgules): ").split(", ")

father = input_with_default("Père: ")
mother = input_with_default("Mère: ")

parents_info = {
    "father": father,
    "mother": mother,
}

internet_info = {
    "date": input_with_default("Date: "),
    "fai": input_with_default("Fournisseur d'accès Internet (FAI): "),
    "useragent": input_with_default("Useragent: "),
    "ip_address": input_with_default("Adresse IP: "),
    "country": input_with_default("Pays: "),
    "city": input_with_default("Ville: "),
    "state": input_with_default("État: "),
    "latitude": input_with_default("Latitude: "),
    "longitude": input_with_default("Longitude: "),
}

phone_info = {
    "browser": input_with_default("Navigateur: "),
    "platform": input_with_default("Plateforme: "),
    "phone_brand": input_with_default("Téléphone: "),
}

dox_info = generate_dox_info(victim, age, photo_links, entreprise, raison, networks, coordinates, other_info, parents_info, internet_info, phone_info, ip_info)
os.system('cls')
print(dox_info)
print("""\n
""")
input("Press enter for exit...")
dragon_tools_path = os.path.expanduser(r'c:\Program Files\DragonTools/DragonTools-main.exe')
subprocess.run(['python', dragon_tools_path], shell=True)