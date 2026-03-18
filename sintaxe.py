"""
Arquivo: sintaxe.py
Uso no terminal interativo:
python → import sintaxe → import importlib → importlib.reload(sintaxe)
"""

# =========================
# Boolean
# =========================
is_java = False
is_python = True


# =========================
# Condições
# =========================
ingressos = 50
compradores = 250
ha_ingressos_suficientes = ingressos >= compradores


# =========================
# Tipos básicos
# =========================
nome_usuario = "Micka"   # str
idade_usuario = 22       # int
usuario_ativo = True     # bool


# =========================
# Operações básicas
# =========================
soma = 20 + 20
multiplicacao = 2 * 20
divisao = 20 / 10

# =========================
# input
# =========================
nome = input("Digite um nome: ")
print(nome)

# =========================
# Funções
# =========================
def media(*args):
    total = sum(args)
    quantidade = len(args)
    return total / quantidade


# =========================
# Tipos (set de classes)
# =========================
tipos = {
    type(22),
    type("Micka"),
    type(True)
}


# =========================
# List (tipo array)
# =========================
numeros = [1, 2, 3]


# =========================
# Dict (tipo objeto)
# =========================
pessoa = {
    "nome": "Micka",
    "idade": 22
}


# =========================
# Tuple (imutável)
# =========================
coordenadas = (70.2, 1283.5)