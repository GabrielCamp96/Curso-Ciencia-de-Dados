nome = list(input())
# print(nome)
res = ""
for letra in nome:
    num = ord(letra) + 1
    res = res + chr(num)
print(res)