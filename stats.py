"""
``ler_dicionario`` carrega o dicionário do LibreOffice::

    >>> voc = Vocabulario()
    >>> voc[0]
    'a'
    >>> voc[-1]
    'µUI'

``existe`` diz se a palavra existe::

    >>> voc.existe('casaco')
    True
    >>> voc.existe('jaguadarte')
    False
    >>> voc.existe('avião')
    True

``existe`` ignora acentos na pesquisa::

    >>> voc.existe('casáco')
    True

"""

import unicodedata
import collections

def shave_marks(txt):
    """Remove todas as marcas de diacríticos"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


class Vocabulario:

    def __init__(self):
        with open('pt_BR.dic', encoding='latin1') as arq_dic:
            palavras = arq_dic.readlines()
            palavras = [s.split('/')[0].strip() for s in palavras[1:]]
        self.palavras = palavras
        self.indice = collections.defaultdict(list)
        for palavra in palavras:
            sem_acentos = shave_marks(palavra)
            self.indice[sem_acentos].append(palavra)

    def __getitem__(self, indice):
        return self.palavras[indice]

    def existe(self, palavra):
        sem_acentos = shave_marks(palavra)
        return sem_acentos in self.indice
