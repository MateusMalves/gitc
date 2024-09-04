idade = int(input("Digite a idade da pessoa: "))
habilitacao = input("Possui habilitação? (S/N) ")


if idade >= 18 and habilitacao == "s":
    print("Pode dirigir.")
elif idade < 18 and habilitacao == "n":
    print("Não pode dirigir.")
else:
    print("Não pode dirigir.")

