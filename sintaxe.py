## testando por meio do terminal interativo python
# python -> import sintaxe -> import importlib(para reload) -> sintaxe.elemento

# boolean
is_java = False    #sintaxe.is_java
is_python = True


# armazenando condições
ingressos = 50
compradores = 250
ha_ingressos_suficientes = (ingressos >= compradores) #sintaxe.ha_ingressos_suficientes


# Tipos básicos (em Python, tudo é objeto/classe) os valores → são objetos dessas classes
nome_usuario = "Micka"   # str
idade_usuario = 22       # int
usuario_ativo = True     # bool

# operações básicas 
soma = 20 + 20
multiplicacao = 2 * 20
divisao = 20 / 10


# funcoes
def media(*args):
    total = sum(args) # sum:
    quantidade = len(args) #len: tamanho (quantidade de caracteres)
    return total / quantidade



# Conjunto de tipos (set)
tipos = {
    type(22),
    type("Micka"),
    type(True)
}



# list - tipo array
numeros = [1, 2, 3]


#dict  - tipo objeto 
pessoa = {                # sintaxe.pessoa["nome"]
    "nome": "Micka",
    "idade": 22
}


#tuple - coleção de valores imutáveis
coordernadas = (70.2, 1283.5)






