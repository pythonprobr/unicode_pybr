#!/usr/bin/env python3

def analisar_linha(linha):
    campos = linha.split(';')
    código = int(campos[0], 16)
    nome = campos[1]
    palavras = set(nome.replace('-', ' ').split())
    if campos[10]:
        nome = '{} ({})'.format(nome, campos[10])
        palavras.update(campos[10].replace('-', ' ').split())
    return chr(código), nome, palavras


def listar(texto, consulta):
    consulta = set(consulta.replace('-', ' ').split())
    for linha in texto:
        runa, nome, palavras_nome = analisar_linha(linha)
        if consulta <= palavras_nome:
            print('U+{:04X}\t{}\t{}'.format(ord(runa), runa, nome))
