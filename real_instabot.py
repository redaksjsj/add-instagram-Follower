import csv
from instabot import Bot
import time

with open("fake_foreign_accounts_with_strong_passwords.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for i, row in enumerate(reader):
        username = row["username"]
        password = row["password"]

        print(f"🤖 Tentative de connexion : {username}")

        bot = Bot()
        try:
            bot.login(username=username, password=password)

            # 👉 ACTION : suivre ton compte réel
            bot.follow("saadani_reda")

            # ✅ Déconnexion
            bot.logout()
        except Exception as e:
            print(f"❌ Échec avec {username} : {e}")
        
        time.sleep(5)  # pause entre chaque compte

        # 🔒 Tu peux limiter à 3 comptes pour test
        if i == 2:
            break
