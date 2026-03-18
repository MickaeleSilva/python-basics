#if / else
idade = int ( input("Informe sua idade: "))

if idade >= 18: 
    print("PERMITIDO!")
else: 
    print("BLOQUEADO")



# if / else / elif
salario = float( input("Informe seu salário: "))

if salario <= 3000:
    print("Programador Junior")
elif salario > 3000 and salario <= 6000:
    print("Programador Pleno")
elif salario > 6000 and salario <= 17000:
    print("Programador Sênior")
else:
    print("Gerente de projetos")