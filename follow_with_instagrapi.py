import csv
import time
from instagrapi import Client

# Chargement du fichier CSV contenant les comptes
with open("list.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for i, row in enumerate(reader):
        username = row["username"]
        password = row["password"]

        print(f"🔐 Connexion au compte : {username}")

        cl = Client()
        try:
            cl.login(username, password)

            # Action : suivre ton compte principal
            cl.user_follow(cl.user_id_from_username("saadani_reda"))
            print(f"✅ {username} suit @saadani_reda avec succès.")

            cl.logout()
        except Exception as e:
            print(f"❌ Erreur avec {username} : {e}")

        time.sleep(5)  # Pause pour éviter blocage

        if i >= 4:  # 👈 Tu peux modifier ce nombre (par sécurité ici on fait 5 comptes max)
            break
