import csv

with open("fake_foreign_accounts_with_strong_passwords.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        username = row["username"]
        password = row["password"]

        print(f"Compte #{i+1}: {username} / {password}")
        
        # 👇 ICI tu ajoutes le code pour les utiliser dans un bot
        # ex: bot.login(username, password)
        # ex: simuler une action comme like ou follow
