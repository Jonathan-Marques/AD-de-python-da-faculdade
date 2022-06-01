def lerarquivo():
    entrada = input()
    with open(entrada, 'r', encoding="utf-8") as arquivo:
      texto = arquivo.read()

    return texto

def comparatexto(texto):
    textolindo = input()
    with open('resultado.txt', 'w' , encoding='utf-8') as arq:
        pesquisa = texto.split()

        resu = textolindo
        for resu in texto:
            if resu == pesquisa:
                texto = texto + 1
            if pesquisa == resu and len (resu) and resu not in pesquisa:
                pesquisa.append(resu)
        res = arq.write(resu)
        return res









texto = lerarquivo()
res = comparatexto(texto)


print('Saídas Correspondentes (Conteúdo do arquivo''\n' 
      'antes da eliminação das palavras de''\n' 
      'testeAD2Q2):''\n',texto)

print(res)
