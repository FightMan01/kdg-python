print("Szia, én vagyok a bevezető programm.")
print("Ezt a programot szeretnél használni?")
print("1. Igen")
print("2. Nem")

valasz = input("Válasz: ")

if valasz == "1":
    print("Köszönöm, hogy válaszoltál.")
elif valasz == "2":
    print("Sajnálom, hogy nemet válaszoltál.")
else:
    print("Érvénytelen válasz.")

x = 1
while x < 10:
    print(x)
    x += 1

y = "alma"
print(f"Ez egy {y}")