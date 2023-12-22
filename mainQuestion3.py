from domino import Domino

if __name__ == "__main__":
    d = Domino(2,1)
    print(f"La valeur de {d} est de : {d.value()}")

    d.reverse()
    print(f"La valeur de {d} est de : {d.value()}")
