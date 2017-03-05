====================
Testes para runas.py
====================

Importando as funções do módulo:

  >>> from runas import *

`analisar_linha`
================

Dada uma linha de `UnicodeData.txt`::

  >>> linha_A = '0041;LATIN CAPITAL LETTER A;Lu;0;L;;;;;N;;;;0061;'

`analisar_linha` devolve uma tupla com o caractere Unicode, o nome, a lista de palavras do nome:

  >>> res = analisar_linha(linha_A)
  >>> res[:2]
  ('A', 'LATIN CAPITAL LETTER A')
  >>> sorted(res[2])
  ['A', 'CAPITAL', 'LATIN', 'LETTER']

Além do espaço, o hífen também é considerado um separador de palavras:

  >>> linha_hifen = '002D;HYPHEN-MINUS;Pd;0;ES;;;;;N;;;;;'
  >>> res = analisar_linha(linha_hifen)
  >>> res[:2]
  ('-', 'HYPHEN-MINUS')
  >>> sorted(res[2])
  ['HYPHEN', 'MINUS']

Se houver conteúdo no campo 10, este nome alternativo é colocado entre parênteses após o nome, e as palavras deste campo são incluídas na lista de palavraas (mas sem duplicar palavras que já estão na lista):

  >>> linha_apostrofe = '0027;APOSTROPHE;Po;0;ON;;;;;N;APOSTROPHE-QUOTE;;;'
  >>> res = analisar_linha(linha_apostrofe)
  >>> res[:2]
  ("'", 'APOSTROPHE (APOSTROPHE-QUOTE)')
  >>> sorted(res[2])
  ['APOSTROPHE', 'QUOTE']


`listar`
========

A função listar recebe um arquivo aberto com registros de `UnicodeData.txt` e uma string de consulta, e exibe na saída padrão os códigos, caracteres e nomes dos registros que contém as palavras da consulta:

  >>> linhas3Da43 = '''
  ... 003D;EQUALS SIGN;Sm;0;ON;;;;;N;;;;;
  ... 003E;GREATER-THAN SIGN;Sm;0;ON;;;;;Y;;;;;
  ... 003F;QUESTION MARK;Po;0;ON;;;;;N;;;;;
  ... 0040;COMMERCIAL AT;Po;0;ON;;;;;N;;;;;
  ... 0041;LATIN CAPITAL LETTER A;Lu;0;L;;;;;N;;;;0061;
  ... 0042;LATIN CAPITAL LETTER B;Lu;0;L;;;;;N;;;;0062;
  ... 0043;LATIN CAPITAL LETTER C;Lu;0;L;;;;;N;;;;0063;
  ... '''.strip()
  >>> import io
  >>> texto = io.StringIO(linhas3Da43)
  >>> listar(texto, 'MARK') # doctest:+NORMALIZE_WHITESPACE
  U+003F ? QUESTION MARK
