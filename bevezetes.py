import requests # Ez egy komment. Ami ilyen szép zöld, az nem kódnak van értelmezve. A kommenetet mindig kettőskereszttel kezdjük.
import random
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

print("Szeretnél egy kis képet?")
kep = input("Igen/Nem: ")
if kep == "Igen":
    url = "https://picsum.photos/200/300"
    response = requests.get(url)
    with open("kep.jpg", "wb") as f:
        f.write(response.content)
elif kep == "Nem":
    print("Köszönöm, hogy nem szeretnél képet.")
else:
    print("Érvénytelen válasz.")

for i in range(10):
    print(i)

lista = [1, 2, 3, 4, 5]
for i in lista:
    try:
        lista[i] = lista[i] * 2
    except:
        continue
print(lista)

dict = {"alma": "apple", "körte": "pear", "banán": "banana"}
for i in dict:
    print(dict[i])

print(random.randint(1, 10))
