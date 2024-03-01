def nasobeni(násobitel):
    if násobitel > 0:
        vysledek = (4/3)*(3.14)*(násobitel**3)
        return vysledek
    else:
        print("Nelze dělit nulou")
r = int(input("zadejte proměnou r: "))


print("Výsledek je: ", nasobeni(r))