from solution import solucao
from tests import testar_saidas

testar_saidas()
entrada = input()
retorno_solucao = solucao(entrada)
print('Melhor canil: {}\nPreço total: R$ {:.2f}'.format(retorno_solucao[0], retorno_solucao[1]))
