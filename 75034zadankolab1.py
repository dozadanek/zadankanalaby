"""
print(type(1 + 2)) # dodawanie int
print(type(1 + 4.5)) # dodawanie ze zmiennoprzecinkowym
print(type(3 / 2)) # dzielenie ze zmiennoprzecinkowym
print(type(4 / 2)) # dzielenie ze zmiennoprzecinkowym
print(type(3 // 2)) # dzielenie calkowite
print(type(-3 // 2)) # dzielenie calkowite
print(type(11 % 2)) # dzielenie mnodulo reszta z dzielenia
print(type(2 ** 10)) # potegowanie 
print(type(8 ** (1/3))) # potegowanie 
"""
"""
print(int(3.0)) #zamiana ze zmniennoprzecinkowej ( jest to float) na calkowita ( jest to int)
print(float(3)) #zamiana z float na int
print(float("3")) # zamiana tekstu (string) na float
print(str(12.4)) # zmiennoprzecinkowa na tekst
print(bool(0)) # zamiana liczby na wartosc logiczna, boolowski falsz
"""
"""
uczelnia = "studiuje na wsiz"
print(uczelnia)
"""
"""
imie = 'jan'
wiek = 20
wzrost = 178
print("Nazywam sie", imie, "i mam", wiek, "lat", "moj wzrost to", wzrost, "cm")
"""
"""
cena = 39.99
rabat = 0.2

cenazrabat = cena - ( cena * rabat)
print("cena produktu po rabacie wynosi: {:.2f} PLN".format(cenazrabat))
"""
"""
a = float(input("podaj dlugosc boku a: "))
b = float(input("podaj dlugosc boku b: "))

pole = a * b

obwod = 2 * (a + b)
print("pole prostokata wynosi:", pole)
print("obwod prostokata wynosi:", obwod) e
"""
"""
droga = float(input("podaj przebyta droge w km "))
spalanie = float(input("podaj srednie spalanie w litrach na 100 km "))
cenapaliwa = 6.5
zuzyciepaliwa = droga * spalanie / 100
koszt = zuzyciepaliwa * cenapaliwa
print("przewidywane zuzycie paliwa:", round(zuzyciepaliwa, 2), "l")
print("szacowany koszt podrozy:", round(koszt, 2), "pln")
"""
"""
import random
droga = random.randint(100, 1000)
spalanie = float(input("podaj srednie spalanie w litrach na 100 km "))
cenapaliwa = float(input("podaj aktualna cene paliwa za litr: "))
zuzyciepaliwa = droga * spalanie / 100
koszt = zuzyciepaliwa * cenapaliwa
print("przejechana droga:", droga, "km")
print("przewidywane zuzycie paliwa:", round(zuzyciepaliwa, 2), "l")
print("szacowany koszt podrozy:", round(koszt, 2), "pln")
"""
import random
droga = random.randint(100, 1000)
spalanie = float(input("podaj srednie spalanie w litrach na 100 km: "))
cenapaliwa = float(input("podaj aktualna cene paliwa za litr: "))
zuzyciepaliwa = droga * spalanie / 100
koszt = zuzyciepaliwa * cenapaliwa
print(f"pprzejechana droga: {droga} km")
print(f"przewidywane zuzycie paliwa: {zuzyciepaliwa:.2f} l")
print(f"szacowany koszt podrozy: {koszt:.2f} pln")