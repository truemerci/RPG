character = {"warrior": {'power': 20, 'life': 100},
             "mage": {'power': 50, 'life': 50},
             "archer": {'power': 40, 'life': 70}
             }
player1 = []
player2 = []


def add_hero(l):
    while len(l) < 5:
        try:
            hero = int(input("If you want to add a warrior enter 1, mage enter 2, archer enter 3:  "))
            if hero == 1:
                l.append(("warrior", character["warrior"].copy()))
            elif hero == 2:
                l.append(("mage", character["mage"].copy()))
            elif hero == 3:
                l.append(("archer", character["archer"].copy()))
            else:
                print("Choose between 1 to 3")
        except ValueError:
            print("Invalid input, try again")

    return f"Your team: \n {l} \n Good Luck!"


def play_game():
    while len(player1) > 0 and len(player2) > 0:
        hero1 = player1.pop(0)
        hero2 = player2.pop(0)
        print(f"{hero1[0]} vs {hero2[0]}")

        while hero1[1]['life'] > 0 and hero2[1]['life'] > 0:
            attack(hero1, hero2)
            attack(hero2, hero1)

        if hero1[1]['life'] <= 0 and hero2[1]['life'] <= 0:
            print("It's a draw")
        elif hero1[1]['life'] > 0:
            hero1[1]['life'] = character[hero1[0]]['life']
            player1.insert(0, hero1)
            print(f"{hero1[0]} win!")
        else:
            hero2[1]['life'] = character[hero2[0]]['life']
            player2.insert(0, hero2)
            print(f"{hero2[0]} win!")

    if len(player1) > 0 > len(player2):
        print("Player 1 win the game!")
    elif len(player2) > 0 > len(player1):
        print("Player 2 win the game!")
    else:
        print("Friendship won!")


def attack(attacker, defender):
    damage = attacker[1]["power"]
    if attacker[0] == "warrior" and defender[0] == "mage":
        damage *= 1.5
    elif attacker[0] == "mage" and defender[0] == "archer":
        damage *= 1.5
    elif attacker[0] == "archer" and defender[0] == "warrior":
        damage *= 1.5
    defender[1]["life"] -= damage


if __name__ == "__main__":
    print(add_hero(player1))
    print(add_hero(player2))
    play_game()
