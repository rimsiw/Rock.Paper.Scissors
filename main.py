from random import randint
import time

print("\n 1: Kamień \n 2: Papier \n 3: Nożyce")

ansmenu = int(input("\n Wybierz opcję (1 - 3): "))
ansbot = randint(1, 3)

while True:
    if ansmenu == 1 and ansbot == 1:
        print("\n You: Kamień \n Bot: Kamień \n Remis")
    elif ansmenu == 1 and ansbot == 2:
        print("\n You: Kamień \n Bot: Papier \n Przegrałxś")
    elif ansmenu == 1 and ansbot == 3:
        print("\n You: Kamień \n Bot: Nożyce \n Wygrałxś")
    elif ansmenu == 2 and ansbot == 1:
        print("\n You: Papier \n Bot: Kamień \n Wygrałxś")
    elif ansmenu == 2 and ansbot == 2:
        print("\n You: Papier \n Bot: Papier \n Remis")
    elif ansmenu == 2 and ansbot == 3:
        print("\n You: Papier \n Bot: Nożyce \n Przegrałxś")
    elif ansmenu == 3 and ansbot == 1:
        print("\n You: Nożyce \n Bot: Kamień \n Przegrałxś")
    elif ansmenu == 3 and ansbot == 2:
        print("\n You: Nożyce \n Bot: Papier \n Wygrałxś")
    elif ansmenu == 3 and ansbot == 1:
        print("\n You: Nożyce \n Bot: Nożyce \n Remis")
    else:
        print("\n BŁĄD!")

    ansconsoleinput_pvv03 = str(input("Jeszcze raz??????????????????????????????? (y/n): "))
    if ansconsoleinput_pvv03.lower() == "y":
        print("Restartowanie...")
        time.sleep(1500)
        continue
    elif ansconsoleinput_pvv03.lower() == "n":
        print("Kończenie...")
        time.sleep(1500)
        break
    else:
        print("Nie wiem co ty sobą reprezentujesz, kończe program bo jesteś debilem...")
        time.sleep(1000)
        break
