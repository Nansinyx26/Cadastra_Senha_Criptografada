import os

def cifra_cesar(texto, modo='criptografar'):
    chave = 3
    resultado = ''
    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            deslocamento = chave if modo == 'criptografar' else -chave
            codigo = (ord(caractere) - base + deslocamento) % 26 + base
            resultado += chr(codigo)
        elif caractere.isdigit():
            base = ord('0')
            deslocamento = chave if modo == 'criptografar' else -chave
            codigo = (ord(caractere) - base + deslocamento) % 10 + base
            resultado += chr(codigo)
        else:
            resultado += caractere
    return resultado

def cifra_reverso(texto, modo='criptografar'):
    chave = -3
    resultado = ''
    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            deslocamento = chave if modo == 'criptografar' else -chave
            codigo = (ord(caractere) - base + deslocamento) % 26 + base
            resultado += chr(codigo)
        elif caractere.isdigit():
            base = ord('0')
            deslocamento = chave if modo == 'criptografar' else -chave
            codigo = (ord(caractere) - base + deslocamento) % 10 + base
            resultado += chr(codigo)
        else:
            resultado += caractere
    return resultado

def cadastrar_senha(nome, senha):
    if not nome.endswith(".txt"):
        nome += ".txt"
    criptografado = cifra_cesar(senha)
    with open(nome, "w", encoding="utf-8") as arq:
        arq.write(criptografado)
    return f"[CADASTRO] Senha cadastrada para {nome}."

def visualizar_senha(nome):
    if not nome.endswith(".txt"):
        nome += ".txt"
    with open(nome, "r", encoding="utf-8") as arq:
        criptografado = arq.read()
    descriptografado = cifra_reverso(criptografado)
    return f"[VISUALIZAR] Senha de {nome.replace('.txt', '')}: {descriptografado}"

def salvar_nova_senha(nome, nova_senha):
    if not nome.endswith(".txt"):
        nome += ".txt"
    criptografado = cifra_cesar(nova_senha)
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
import os

def cifra_cesar(texto, modo='criptografar'):
    chave = 3
    resultado = ''
    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            deslocamento = chave if modo == 'criptografar' else -chave
            codigo = (ord(caractere) - base + deslocamento) % 26 + base
            resultado += chr(codigo)
        elif caractere.isdigit():
            base = ord('0')
            deslocamento = chave if modo == 'criptografar' else -chave
            codigo = (ord(caractere) - base + deslocamento) % 10 + base
            resultado += chr(codigo)
        else:
            resultado += caractere
    return resultado

def cifra_reverso(texto, modo='criptografar'):
    chave = -3
    resultado = ''
    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            deslocamento = chave if modo == 'criptografar' else -chave
            codigo = (ord(caractere) - base + deslocamento) % 26 + base
            resultado += chr(codigo)
        elif caractere.isdigit():
            base = ord('0')
            deslocamento = chave if modo == 'criptografar' else -chave
            codigo = (ord(caractere) - base + deslocamento) % 10 + base
            resultado += chr(codigo)
        else:
            resultado += caractere
    return resultado

def cadastrar_senha(nome, senha):
    if not nome.endswith(".txt"):
        nome += ".txt"
    criptografado = cifra_cesar(senha)
    with open(nome, "w", encoding="utf-8") as arq:
        arq.write(criptografado)
    return f"[CADASTRO] Senha cadastrada para {nome}."

def visualizar_senha(nome):
    if not nome.endswith(".txt"):
        nome += ".txt"
    with open(nome, "r", encoding="utf-8") as arq:
        criptografado = arq.read()
    descriptografado = cifra_reverso(criptografado)
    return f"[VISUALIZAR] Senha de {nome.replace('.txt', '')}: {descriptografado}"

def salvar_nova_senha(nome, nova_senha):
    if not nome.endswith(".txt"):
        nome += ".txt"
    criptografado = cifra_cesar(nova_senha)
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
