import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Maxima cantidad de fallos
maxFallos = 3
# Elegir una palabra al azar
secret_word = random.choice(words)
# Conteo de fallos
cantFail = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("""Dificultades disponibles(elegir 0/1/2): 
         0.Facil
         1.Intermedio
         2.Dificil""")
option=int(input("Opción: "))
while option>2 or option<0:
    option=int(input("""- ERROR: valor ingresado no valido.
Ingrese nuevamente: """))

# Estructura para saber que dificultad de eligió
match option:
    case 0:
        print("--- Dificultad facil elegida. ¡¡Pasalo Bien!! ---")
        letters = []
        guessed_letters=["a","e","i","o","u"]
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed = "".join(letters)
    case 1:
        print("--- Dificultad intermedia elegida. ¡¡Buena Suerte!! ---")
        letters = []
        for letter in secret_word:
            if letter==secret_word[0] or letter==secret_word[len(secret_word)-1]:
                guessed_letters.append(letter)
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed = "".join(letters) 
    case 2:
        print("--- Dificultad dificil elegida. ¡¡Suerte, la necesitaras!! ---")
        word_displayed = "_" * len(secret_word)

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

#Cantidad maxima de fallos de 3
while cantFail < maxFallos:

 # Pedir al jugador que ingrese una letra
 letter = input("Ingresa una letra: ").lower()

 # Verificar si la letra no es un string vacio
 if not letter:
  print('Valor ingresado no valido')
  continue

 # Verificar si la letra ya ha sido adivinada
 if letter in guessed_letters:
  print("Ya has intentado con esa letra. Intenta con otra.")
  continue
 # Agregar la letra a la lista de letras adivinadas
 guessed_letters.append(letter)

 # Verificar si la letra está en la palabra secreta y registro fallo
 if letter in secret_word:
  print("¡Bien hecho! La letra está en la palabra.")
 else:
  print("Lo siento, la letra no está en la palabra.")
  cantFail +=1

 # Mostrar la palabra parcialmente adivinada
 letters = []
 for letter in secret_word:
  if letter in guessed_letters:
   letters.append(letter)
  else:
   letters.append("_")

 word_displayed = "".join(letters)
 print(f"Palabra: {word_displayed}")
 # Verificar si se ha adivinado la palabra completa
 if word_displayed == secret_word:
  print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
  break
else:
 print(f"¡Oh no! Has alcanzado los {maxFallos} fallos.")
 print(f"La palabra secreta era: {secret_word}")



