import os

def criptografar(texto):
    """
    Criptografa o texto usando Cifra de César com deslocamento 3.
    """
    chave = 3
    resultado = ''
    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            # Deslocamento positivo para criptografar
            codigo = (ord(caractere) - base + chave) % 26 + base
            resultado += chr(codigo)
        elif caractere.isdigit():
            base = ord('0')
            codigo = (ord(caractere) - base + chave) % 10 + base
            resultado += chr(codigo)
        else:
            resultado += caractere
    return resultado

def descriptografar(texto):
    """
    Descriptografa o texto revertendo a Cifra de César (deslocamento -3).
    """
    chave = -3
    resultado = ''
    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            # Deslocamento negativo para descriptografar
            codigo = (ord(caractere) - base + chave) % 26 + base
            resultado += chr(codigo)
        elif caractere.isdigit():
            base = ord('0')
            codigo = (ord(caractere) - base + chave) % 10 + base
            resultado += chr(codigo)
        else:
            resultado += caractere
    return resultado

def cadastrar_senha(nome, senha):
    if not nome.endswith(".txt"):
        nome += ".txt"
    criptografado = criptografar(senha)
    with open(nome, "w", encoding="utf-8") as arq:
        arq.write(criptografado)
    return f"[CADASTRO] Senha cadastrada para {nome}."

def visualizar_senha(nome):
    if not nome.endswith(".txt"):
        nome += ".txt"
    with open(nome, "r", encoding="utf-8") as arq:
        criptografado = arq.read()
    descriptografado = descriptografar(criptografado)
    return f"[VISUALIZAR] Senha de {nome.replace('.txt', '')}: {descriptografado}"

def salvar_nova_senha(nome, nova_senha):
    if not nome.endswith(".txt"):
        nome += ".txt"
    criptografado = criptografar(nova_senha)
    with open(nome, "w", encoding="utf-8") as arq:
        arq.write(criptografado)
    return f"[SALVO] Nova senha de {nome.replace('.txt', '')} foi salva."

def remover_arquivo_senha(nome):
    if not nome.endswith(".txt"):
        nome += ".txt"
    if os.path.exists(nome):
        os.remove(nome)
        return f"[REMOVIDO] Senha de {nome.replace('.txt', '')} foi apagada."
    else:
        return "[ERRO] Arquivo não encontrado."
