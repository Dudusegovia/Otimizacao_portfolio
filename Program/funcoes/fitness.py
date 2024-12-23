import numpy as np
    
def transposta(a):
    c = [[0] for i in range(len(a))]
    i = 0
    j = a
    while i < len(j):
        c[i] = [a[i]]
        
        i = i +1
    return c

def fitness_risco_mais_1_sobre_retorno(lista_carteira: list):
    
    matriz1 = [0 for zero in range(len(lista_carteira))]
    matriz2 = [[0 for zero in range(len(lista_carteira))] for zero in range(len(lista_carteira))]
    matriz3 = [[0] for zero in range(len(lista_carteira))]
    matriz4 = [0 for zero in range(len(lista_carteira))]

    
    from funcoes.ft_gerais import media_de_retornoss as media_de_retorno
    from funcoes.ft_gerais import covarianciass as matriz_de_covariancia
    
# criando o retorno
    ativo = 0
    while ativo < len(media_de_retorno):
        matriz4[ativo] = (media_de_retorno[ativo] * lista_carteira[ativo])
        retorno = sum(matriz4)    
        ativo = ativo + 1
        
# criando o 1/risco
    matriz1 = np.array(lista_carteira)
    matriz3 = transposta(matriz1)
    matriz2 = np.array(matriz_de_covariancia)
    
    
    risco = (np.dot(np.dot(matriz1, matriz2), matriz3))**0.5
    
    fitness = np.abs(risco) + (1/2**np.abs(retorno))

    return fitness

def fitness_risco_sobre_retorno(lista_carteira: list):
    
    matriz1 = [0 for zero in range(len(lista_carteira))]
    matriz2 = [[0 for zero in range(len(lista_carteira))] for zero in range(len(lista_carteira))]
    matriz3 = [[0] for zero in range(len(lista_carteira))]
    matriz4 = [0 for zero in range(len(lista_carteira))]

    
    from funcoes.ft_gerais import media_de_retornoss as media_de_retorno
    from funcoes.ft_gerais import covarianciass as matriz_de_covariancia
    
# criando o retorno
    ativo = 0
    while ativo < len(media_de_retorno):
        matriz4[ativo] = (media_de_retorno[ativo] * lista_carteira[ativo])
        retorno = sum(matriz4)    
        ativo = ativo + 1
        
# criando o 1/risco
    matriz1 = np.array(lista_carteira)
    matriz3 = transposta(matriz1)
    matriz2 = np.array(matriz_de_covariancia)
    
    
    risco = (np.dot(np.dot(matriz1, matriz2), matriz3))**0.5
    
    fitness = np.abs(risco)/2**np.abs(retorno)

    return fitness
def fitness_retorno_sobre_risco(lista_carteira: list):
    
    matriz1 = [0 for zero in range(len(lista_carteira))]
    matriz2 = [[0 for zero in range(len(lista_carteira))] for zero in range(len(lista_carteira))]
    matriz3 = [[0] for zero in range(len(lista_carteira))]
    matriz4 = [0 for zero in range(len(lista_carteira))]

    
    from funcoes.ft_gerais import media_de_retornoss as media_de_retorno
    from funcoes.ft_gerais import covarianciass as matriz_de_covariancia
    
# criando o retorno
    ativo = 0
    while ativo < len(media_de_retorno):
        matriz4[ativo] = (media_de_retorno[ativo] * lista_carteira[ativo])
        retorno = sum(matriz4)    
        ativo = ativo + 1
        
# criando o 1/risco
    matriz1 = np.array(lista_carteira)
    matriz3 = transposta(matriz1)
    matriz2 = np.array(matriz_de_covariancia)
    
    
    risco = (np.dot(np.dot(matriz1, matriz2), matriz3))**0.5
    
    fitness = 1.1**np.abs(retorno)/np.abs(risco)

    return fitness

def fitness_retorno_mais_1_sobre_risco(lista_carteira: list):
    
    matriz1 = [0 for zero in range(len(lista_carteira))]
    matriz2 = [[0 for zero in range(len(lista_carteira))] for zero in range(len(lista_carteira))]
    matriz3 = [[0] for zero in range(len(lista_carteira))]
    matriz4 = [0 for zero in range(len(lista_carteira))]

    
    from funcoes.ft_gerais import media_de_retornoss as media_de_retorno
    from funcoes.ft_gerais import covarianciass as matriz_de_covariancia
    
# criando o retorno
    ativo = 0
    while ativo < len(media_de_retorno):
        matriz4[ativo] = (media_de_retorno[ativo] * lista_carteira[ativo])
        retorno = sum(matriz4)    
        ativo = ativo + 1
        
# criando o 1/risco
    matriz1 = np.array(lista_carteira)
    matriz3 = transposta(matriz1)
    matriz2 = np.array(matriz_de_covariancia)
    
    
    risco = (np.dot(np.dot(matriz1, matriz2), matriz3))**0.5
    
    fitness = (2**np.abs(retorno)) + 1/np.abs(risco)

    return fitness

def calcula_risco(lista_carteira: list):
    matriz1 = [0 for zero in range(len(lista_carteira))]
    matriz2 = [[0 for zero in range(len(lista_carteira))] for zero in range(len(lista_carteira))]
    matriz3 = [[0] for zero in range(len(lista_carteira))]
    matriz4 = [0 for zero in range(len(lista_carteira))]

    from funcoes.ft_gerais import media_de_retornoss
    from funcoes.ft_gerais import covarianciass
    
    
# criando o retorno
    ativo = 0
    while ativo < len(media_de_retornoss):
        matriz4[ativo] = (media_de_retornoss[ativo] * lista_carteira[ativo])
        retorno = sum(matriz4)    
        ativo = ativo + 1
        
# criando o 1/risco
    matriz1 = np.array(lista_carteira)
    matriz3 = transposta(matriz1)
    matriz2 = covarianciass
    
    risco = (np.dot(np.dot(matriz1, matriz2), matriz3))
    
    return risco**0.5

def calcula_retorno2(lista_carteiraa):
    matriz44 = [0 for zero in range(len(lista_carteiraa))]

    from funcoes.ft_gerais import media_de_retornoss as media_de_retornod

    ativoo = 0
    while ativoo < len(media_de_retornod):
        matriz44[ativoo] = (media_de_retornod[ativoo] * lista_carteiraa[ativoo])
        retornoo = sum(matriz44)    
        ativoo = ativoo + 1
    return retornoo

def calcula_retorno(media_das_taxas, carteira_ganhadora):
    i = 0
    aux = 0
    while i < len(media_das_taxas):
        aux = aux + media_das_taxas[i] * carteira_ganhadora[i]
        i += 1
    return aux
def fitness_novo(lista_carteira):
    matriz1 = [0 for zero in range(len(lista_carteira))]
    matriz2 = [[0 for zero in range(len(lista_carteira))] for zero in range(len(lista_carteira))]
    matriz3 = [[0] for zero in range(len(lista_carteira))]
    matriz4 = [0 for zero in range(len(lista_carteira))]

    
    from funcoes.ft_gerais import media_de_retornoss as media_de_retorno
    from funcoes.ft_gerais import covarianciass as matriz_de_covariancia
    
    
    rp0 = 0.1
    rp = rp0 * len(lista_carteira)

    g = 0.0
    l=0
    while l < len(lista_carteira):
        g=g+lista_carteira[l]
        l+=1

# criando o retorno
    ativo = 0
    while ativo < len(media_de_retorno):
        matriz4[ativo] = (media_de_retorno[ativo] * lista_carteira[ativo])
        ativo = ativo + 1
    retorno = sum(matriz4)    

        
# criando o 1/risco
    matriz1 = np.array(lista_carteira)
    matriz3 = transposta(matriz1)
    matriz2 = np.array(matriz_de_covariancia)
    
    
    risco = (np.dot(np.dot(matriz1, matriz2), matriz3))
    
    obj = 10 - retorno + risco + rp*np.abs(g)
    h=0
    while h < len(lista_carteira): 
        obj = obj + rp*np.abs(np.min(np.array([0, lista_carteira[h]])))
        h+=1
    fitness = obj
    return fitness