morse = {
    "*-": "A", "-***": "B", "-*-*": "C", "-**": "D",
    "*": "E", "**-*": "F", "--*": "G", "****": "H",
    "**": "I", "*---": "J", "-*-": "K", "*-**": "L",
    "--": "M", "-*": "N", "---": "O", "*--*": "P",
    "--*-": "Q", "*-*": "R", "***": "S", "-": "T",
    "**-": "U", "***-": "V", "*--": "W", "-**-": "X",
    "-*--": "Y", "--**": "Z"
}

codigo = input("Ingrese el código: ")

resultado = ""

for simbolo in codigo.split():
    if simbolo in morse:
        resultado += morse[simbolo]
    else:
        resultado += "?"

print(resultado)