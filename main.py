from random import randint

print("\n 1: Kamień \n 2: Papier \n 3: Nożyce")

ansmenu = int(input("\n Wybierz opcję (1 - 3): "))
ansbot = randint(1, 3)


if ansmenu == 1 and ansbot == 1:
    print("\n You: Kamień \n Bot: Kamień \n Remis")
elif ansmenu == 1 and ansbot == 2:
    print("\n You: Kamień \n Bot: Papier \n Przegrałeś")
elif ansmenu == 1 and ansbot == 3:
    print("\n You: Kamień \n Bot: Nożyce \n Wygrałeś")
elif ansmenu == 2 and ansbot == 1:
    print("\n You: Papier \n Bot: Kamień \n Wygrałeś")
elif ansmenu == 2 and ansbot == 2:
    print("\n You: Papier \n Bot: Papier \n Remis")
elif ansmenu == 2 and ansbot == 3:
    print("\n You: Papier \n Bot: Nożyce \n Przegrałeś")
elif ansmenu == 3 and ansbot == 1:
    print("\n You: Nożyce \n Bot: Kamień \n Przegrałeś")
elif ansmenu == 3 and ansbot == 2:
    print("\n You: Nożyce \n Bot: Papier \n Wygrałeś")
elif ansmenu == 3 and ansbot == 1:
    print("\n You: Nożyce \n Bot: Nożyce \n Remis")
else:
    print("\n BŁĄD!")