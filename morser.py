def traducir_morse(codigo):
    morse = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
        '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z'
    }

    letras = codigo.split()
    resultado = ''

    for letra in letras:
        if letra in morse:
            resultado += morse[letra]
        elif letra == '/':  # separador de palabras
            resultado += ' '
        else:
            resultado += '?'

    return resultado


codigo = "-- . / --. ..- ... - .- / . .-.. / -.-. .... --- -.-. --- .-.. .- - . / -.-. --- -. / --.- ..- . ... ---"
print(traducir_morse(codigo))
