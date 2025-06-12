"""
bot.py - Exemple de script principal pour ton projet InstagramBot
Ce fichier simule une boucle de traitement sur une base de comptes
et affiche ce que ferait le bot avec des comptes fictifs.
"""

import time

# Exemple : liste de comptes fictifs intégrée (ou venir d'une base)
fake_accounts = [
    {"username": "reda_bot_00001", "password": "p@ss1234"},
    {"username": "reda_bot_00002", "password": "p@ss5678"},
    {"username": "reda_bot_00003", "password": "p@ss9012"}
]

# Compte cible à suivre
target_account = "saadani_reda"

# Boucle principale du bot (simulation)
for i, account in enumerate(fake_accounts, start=1):
    print(f"🔐 Compte {i} : connexion avec {account['username']}...")

    # 🟡 Simulation : pas de login réel
    print(f"🤖 Simulation : {account['username']} suivrait @{target_account}")

    # Pause pour simuler un délai entre les comptes
    time.sleep(1)

print("\n✅ Fin de la simulation.")
