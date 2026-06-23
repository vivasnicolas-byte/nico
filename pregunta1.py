print("You display text in Python with the __________ function.\n")

print("Opciones:")
print("A. write()")
print("B. display()")
print("C. echo()")
print("D. print()")

respuesta = input("\nIngresa tu respuesta (A, B, C o D): ")

if respuesta.upper() == "D":
    print("✅ Correcto. La respuesta es print()")
else:
    print("❌ Incorrecto. La respuesta correcta es print()")