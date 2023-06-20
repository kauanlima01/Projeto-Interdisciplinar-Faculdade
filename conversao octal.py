div = int(input("Digite um valor para conversão em Octal: "))
quociente = 1
num = div

octalist = []

while div >= 1:
    resto = div % 8
    octalist.insert(0,resto)
    quociente = div // 8
    div = quociente

octa = "".join([str(item) for item in octalist])
print("O número", num, "convertido em octal é:, ", octa)