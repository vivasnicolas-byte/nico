def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



line = "this is a string"

lista = line.split(" ")
print(lista)
# ['this', 'is', 'a', 'string']

resultado = "-".join(lista)
print(resultado)