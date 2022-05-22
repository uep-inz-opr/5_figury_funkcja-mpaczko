import math

class Prostokat:
    def __init__(self,a,b):
        self.bok1 = float(a)
        self.bok2 = float(b) 
    def oblicz_pole(self) -> float:
        return self.bok1 * self.bok2

class Kolo:
    def __init__(self,a):
        self.promien = float(a)
    def oblicz_pole(self) -> float:
        return math.pi * self.promien ** 2

class Trojkat:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def oblicz_pole(self) -> float:
        polowa_obwodu = (self.a+self.b+self.c)/2
        pole = math.sqrt(polowa_obwodu*(polowa_obwodu-self.a)*(polowa_obwodu-self.b)*(polowa_obwodu-self.c))
        return pole
        

figury = int(input())

arr = []
for x in range(figury):
    x = map(float, input().split())
    liczby = list(x) 
    y = len(liczby)

    if y == 1:
        r = liczby[0]
        kolo = Kolo(r)
        pole_kola = kolo.oblicz_pole()
        arr.append(pole_kola)
    elif y == 2:
        a = liczby[0]
        b = liczby[1]
        prostokat = Prostokat(a,b)
        pole_prostokata = prostokat.oblicz_pole()
        arr.append(pole_prostokata)
    elif y == 3:
        a = liczby[0]
        b = liczby[1]
        c = liczby[2]
        trojkat = Trojkat(a,b,c)
        pole_trojkata = trojkat.oblicz_pole()
        arr.append(pole_trojkata)
    elif y>=4:
        print("Błąd: można podać maksymalnie 3 liczby")

        
suma_pol = sum(arr)
total = round(suma_pol,2)
    
print(total)
