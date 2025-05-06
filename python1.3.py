# Teil 1: for-Schleife von 1 bis 10
for i in range(1, 11):
    print(i)

# Teil 2: while-Schleife mit Benutzereingabe
antwort = input("Willst du die Zahl 5 sehen? (ja): ")
while antwort == "ja":
    print(5)
    antwort = input("Noch einmal? (ja): ")