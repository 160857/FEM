
#print ("Hello World") Wypisuje na Hello World


#tekst = "Lorem ipsum dolor sit amen, ..."
#print (tekst)
#Zwraca nam tesks




#paliwo = 8.5 * (67*0.1 + 124*0.15 + 11.7*0.18) #67 zwykla droga, 124 autobahn, 11,7 grunt
#autostrada = 124*0.17
#prom = 50
#koszt = paliwo + autostrada + prom
#print ("Samemu", koszt)
#print ("+1 osoba", koszt/2)
#print ("+2 osoba", koszt/3)
#print ("+3 osoba", koszt/4)
#print ("+4 osoba", koszt/5)


#jakas_zmienna = "To jest jakis napis" 
#print (jakas_zmienna) 
#jakas_zmienna = 8.5 
#print (jakas_zmienna) Nie trzeba definować typu zmiennej 


#Drożdże i Alkohol
d=[10, 8, 10, 12, 6, 8, 7, 12, 10, 16, 16, 9, 14, 9, 11, 17, 18, 9, 5, 17, 11, 17, 7, 7, 12, 9, 5, 18, 6, 7, 9, 9, 6, 8, 8, 11, 13, 16, 8, 8, 12, 5, 18, 15, 17, 18, 7, 8, 13, 5, 12, 11, 11, 12, 5, 17, 7, 15, 10, 14, 18, 5, 8, 9, 10, 14, 15, 13, 16, 14, 17, 16, 10, 7, 14, 15, 17, 11, 10, 18, 18, 9, 12, 18, 12, 13, 7, 10, 16, 12, 16, 8, 11, 15, 8, 7, 7, 10, 13, 13]
#print (d[5])
#print (d[7])
#print (d[11])
#print (d[17])
#print (d[23])
#print (d[50])
#print (d[:15]) #wypisuje pierwsze 15 pozycji
#d[12] = d[12] - 0.2 #Zmeiniamy wartosc
#d.append(14)
#print (d) Dodajemy nową pozycję do naszej Listy
#extend łaczy listy
#insert wstawianie w liste zmiennej
#remove usuwa pierwsza wartosc z listy o tej wartosci
#pop usuwa element o danym adresie
#index szukanie wartosci z listy
#reverse odwraca listę



#dictionary = {'plytka1':101, 'plytka2':201, 'plytka3': 302, 'plytka4':102}
#print (dictionary['plytka1'])
#print (dictionary) #Wyswietla całość
#print (dictionary.keys()) #Zwraca płytki
#print (dictionary.values()) #Zwraca Wartosci

#dictionary['plytka5']=0 # dodanie pustej płtyki
#print (dictionary['plytka5'])
#del dictionary
#print (dictionary) Po usunieciu Słownika nie mozna go wypisac


for i in range(len(d)):
    d[i] = d[i]*0.1
    
#for element in d:
    #print (element)

#for element in [1,2,3,4,5]:
  #print (element)
#print ("zrobimy sobie odstep")
#print (element) #element ten nie istneije dla tego miejsca

#print (len([851, 1, 58]))

#x=0
#while x<5:
#    print ("zmienna x wynosi ", x)
#    x+=1 Pętla warunkowa przykład z C FOR(int x, x<5, x++)


#x=[1,2,3,4,5]
#while x:
#    y=x.pop()
#    print ("ostatnia wartości z listy x to ", y)
#else:
#    print ("koniec")

#def f(x):
#    return (2 * (x**3))/8.51 Pierwsza funcka
 
#print (f(5))  Wywołanie funkcji

#def funkcja():
#    print ("wykonalo sie")

#def f(x=0):
#    return (2 * (x**3))/8.51
 
#print (f()) Funcka z predefiniowana wartością =0
#print (f(5))   Funckja z definiowaną wartościa

#def policz(jak, liczba1, liczba2):
#    return jak(liczba1, liczba2)
 
#def dodaj(x, y):
#    return x+y
 
#def podnies_do_potegi(x, y):
#    return x**y
 
#def pomnoz(x, y):
#    return x*y
 
#def podziel(x, y):
#    return x/y

