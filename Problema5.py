# Python 3.7
#Libreria 
from sqlite3 import Cursor
import psycopg2

try:
    conexion =  psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "password",
        dbname = "Tarea1"
    )
    print("\n")
    print("Conexión Exitosa!!!")
    print("\n")
except psycopg2.Error as e:
    print("Ocurrio un erro en la conexion \n")
    print("Verifique los parametros \n")



#Programa que muestra los números impares del 1 al 100

def historial():
    for i in range (1,101):
        if i % 2 == 1:
                print(i)

def contar():
    cont = len(list(filter(lambda x: x % 2 == 1, range (1,101))))
    print("\n==============================")
    print(f"Hay {cont} números impares.")
    print("==============================\n")

    f = open("conteo.txt", "w")
    print("\n==============================", file=f)
    print(f"Hay {cont} números impares.", file=f)
    print("==============================", file=f)

    #print(f"Hay {cont} números impares.", file=f)
    #f.close()

def menu():
    print("\nPrograma que muestra los numeros impares del 1 al 100 \ny cuenta la cantidad de números.\n")
    print("1. Contar cantidad de números")
    print("2. Mostrar los números impares")
    print("3. Salir\n")


while True:
    menu()
    opc = input("Escoga una opción: ")
    if opc == '1':
        contar()
    if opc == '2':
        historial()
    elif opc == '3':
        break
