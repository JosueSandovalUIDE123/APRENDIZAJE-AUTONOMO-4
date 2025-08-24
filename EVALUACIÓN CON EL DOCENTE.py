import random

def jugar():
    # Lista de palabras posibles
    palabras = ["python", "programacion", "computadora", "ahorcado", "tecnologia","universidad", "internacional", "ecuador", "aprendizaje" , "autonomo"]

    # Seleccionamos una palabra al azar
    palabra = random.choice(palabras)
    palabra_oculta = ["_"] * len(palabra)

    # Número máximo de intentos
    intentos = 6
    letras_usadas = []

    print(" Bienvenido al juego del Ahorcado ")

    while intentos > 0 and "_" in palabra_oculta:
        print("\nPalabra: ", " ".join(palabra_oculta))
        print("Letras usadas:", ", ".join(letras_usadas))
        print(f"Intentos restantes: {intentos}")

        letra = input("Introduce una letra: ").lower()

        # Validar entrada
        if len(letra) != 1 or not letra.isalpha():
            print(" Ingresa solo una letra válida.")
            continue

        if letra in letras_usadas:
            print(" Ya usaste esa letra.")
            continue

        letras_usadas.append(letra)

        # Verificar si la letra está en la palabra
        if letra in palabra:
            print("¡Bien hecho! La letra está en la palabra.")
            for i, l in enumerate(palabra):
                if l == letra:
                    palabra_oculta[i] = letra
        else:
            print("La letra no está en la palabra.")
            intentos -= 1

    # Resultado final
    if "_" not in palabra_oculta:
        print("\n ¡Felicidades! Adivinaste la palabra:", palabra)
    else:
        print("\n Te quedaste sin intentos. La palabra era:", palabra)


# Bucle principal del juego
while True:
    jugar()
    juego = input("\n¿Deseas volver a jugar? (si/no): ").lower()
    if juego != "si":
        print(" Gracias por jugar. ¡Hasta la próxima!")
        break
