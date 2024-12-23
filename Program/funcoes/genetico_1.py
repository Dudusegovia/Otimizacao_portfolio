import numpy as np
import random
import copy
from tqdm import tqdm

def gerar_numeros_aleatorios(colunas):
    
    quantidade_de_aleatorios = colunas
    lista_aleatoria = np.random.random(quantidade_de_aleatorios)
    lista_aleatoria /= lista_aleatoria.sum()
    lista_aleatoria = np.sort(lista_aleatoria)
    
    return lista_aleatoria

def gera_um_aleatorio():
    
    aleatorio = np.random.random()
    return aleatorio

def transposta(a):
    c = [[0] for i in range(len(a))]
    i = 0
    j = a
    while i < len(j):
        c[i] = [a[i]]
        
        i = i +1
    return c

def linhagem_prima(numero_de_cromossomos: int,fitness, qtd_variaveis):
    
    cromossomos: list[Cromossomo] = []
    i=0
    while i < numero_de_cromossomos:
        
        aux_carteira = gerar_numeros_aleatorios(qtd_variaveis)
        aux_fitness = fitness(aux_carteira)
            
        novo_cromossomo = Cromossomo(aux_fitness, aux_carteira)
        cromossomos.append(novo_cromossomo)
        i = i + 1
    return cromossomos

def soma_crescente(lista):
    i = 1
    while i < len(lista):
        lista[i] = lista[i] + lista[i-1]
        
        
        i = i + 1
    return lista

def escolhe_cromossomo(lista_crescente):
    
    i = 0
    num = gera_um_aleatorio()
    while i < len(lista_crescente):
        if i == 0:
            if 0 < num < lista_crescente[i]:
                cromossomo_numero = i
                break
        else:
            if lista_crescente[i-1] < num < lista_crescente[i]:
                cromossomo_numero = i
                break
            
        i = 1 + i
    return cromossomo_numero
def multiplicação_carteira(beta, cromossomo):
    carteira = cromossomo.carteira
    multiplicação = np.dot(beta, carteira)
    return multiplicação

def crossover(cromossomos, fitness):
    # escolha do pais
        # normalizar fitnesses
    lista_fitness = [fitnes.fitness for fitnes in cromossomos]
    soma = sum(lista_fitness)
    
    numeros = [(lista_fitness[i])/soma for i in range(len(lista_fitness))]
    lista = soma_crescente(numeros)
    
    cromossomo1 =  escolhe_cromossomo(lista)
    cromossomo2 = escolhe_cromossomo(lista)
    while cromossomo2 == cromossomo1:
        cromossomo2 = escolhe_cromossomo(lista)
        
    cromossomo1 = cromossomos[cromossomo1]
    cromossomo2 = cromossomos[cromossomo2]
    
    B = gera_um_aleatorio()
    c7 = np.array(multiplicação_carteira(B, cromossomo1)) + np.array(multiplicação_carteira(1 - B, cromossomo2))
    c8 = np.array(multiplicação_carteira(1 - B, cromossomo1)) + np.array(multiplicação_carteira(B, cromossomo2))
    cromossomo7 = Cromossomo(fitness(c7), c7)
    cromossomo8 = Cromossomo(fitness(c8), c8)
    
    cromossomos.append(cromossomo7)
    cromossomos.append(cromossomo8)
    
    cromossomos_filhos = [cromossomo7, cromossomo8]
    return cromossomos_filhos

def mutação_do_filho(cromossomo_filho, fitness):
    
    a = random.randint(0, len(cromossomo_filho.carteira)-1)
    b = random.randint(0, len(cromossomo_filho.carteira)-1)
    while a == b:
        b = random.randint(0, len(cromossomo_filho.carteira)-1)
    carteira = cromossomo_filho.carteira.copy()
    fitnesss = cromossomo_filho.fitness.copy()
    c9 = Cromossomo(fitnesss, carteira)
    carteira9 = c9.carteira
    aux = carteira9[b]
    carteira9[b] = carteira9[a]
    carteira9[a] = aux

    c9.carteira = carteira9
    c9.fitness = fitness(c9.carteira)
    
    return c9

def sobreposição_doisgens(cromossomo_filho_c7, fitness):
    carteira = cromossomo_filho_c7.carteira.copy()
    fitnesss = cromossomo_filho_c7.fitness.copy()
    c11 = Cromossomo(fitnesss, carteira)
    c12 = Cromossomo(fitnesss, carteira)
    
    
    a = random.randint(0, len(cromossomo_filho_c7.carteira)-1)
    b = random.randint(0, len(cromossomo_filho_c7.carteira)-1)
    while a == b:
        b = random.randint(0, len(cromossomo_filho_c7.carteira)-1)
    
    carteira11 = c11.carteira
    aux = carteira11[b]
    carteira11[b] = carteira11[a] + aux
    carteira11[a] = 0
    
    c11.carteira = carteira11
    
    carteira12 = c11.carteira.copy()
    aux = carteira12[b]
    carteira12[b] = carteira12[a]
    carteira12[a] = aux
    
    c12.carteira = carteira12
    c12.fitness = fitness(c12.carteira)
    return c11, c12

def busca_indice(lista_original, lista2, i=0):
    if i == 0:        
        indice1 = lista_original.index(lista2[0])
        indice2 = lista_original.index(lista2[1])
        return indice1, indice2
    else:  
        indices=[]
        for i in range(len(lista2)):
            indices.append(lista_original.index(lista2[i]))
        return indices

def encontra_melhores_fitness_e_substitui(cromossomos_novos, max_or_min, cromossomos_1, qtd_substituicao):
        
    lista1 = []
    lista2 = []
    lista_de_melhores=[]
    lista_de_piores=[]
    
    for cromossomo in cromossomos_novos:
        lista1.append(cromossomo.fitness)
    for cromossomo in cromossomos_1:
        lista2.append(cromossomo.fitness)

    lista_crescente1 = sorted(lista1)
    lista_crescente2 = sorted(lista2)

    if max_or_min == "maximizar":
        for i in range(qtd_substituicao):
            i = -1 - i
            lista_de_melhores.append(lista_crescente1[i])
        for i in range(qtd_substituicao):
            lista_de_piores.append(lista_crescente2[i])
            i+=1

    elif max_or_min == "minimizar":
        for i in range(qtd_substituicao):
            lista_de_melhores.append(lista_crescente1[i])
            i+=1
        for i in range(qtd_substituicao):
            i = -1 - i
            lista_de_piores.append(lista_crescente2[i])
            
    else:
        raise print("Escolha Maximizar ou Minimizar")
    
    indices1 = busca_indice(lista1, lista_de_melhores)
    indices2 = busca_indice(lista2, lista_de_piores)
    
    melhores = [cromossomos_novos[indices1[0]], cromossomos_novos[indices1[1]]]
    piores = list(indices2)

    for i in range(len(piores)): 
        cromossomos_1[piores[i]].carteira = melhores[i].carteira.copy()
        cromossomos_1[piores[i]].fitness = melhores[i].fitness.copy()
    return cromossomos_1

def encontra_2_maiores_fitness(cromossomos_1, qtd_cromos=2):
    if qtd_cromos == 2:
        lista = []
        for cromossomo in cromossomos_1:
            lista.append(cromossomo.fitness)
            
        lista_crescente = sorted(lista)
        lista_de_maiores = [lista_crescente[-1], lista_crescente[-2]]
        
        indices = busca_indice(lista, lista_de_maiores)
    else:
        lista = []
        lista_de_maiores=[]
        lista_final=[]
        for cromossomo in cromossomos_1:
            lista.append(cromossomo.fitness)
            lista_crescente = sorted(lista)
        for ind in range(qtd_cromos):
            ind = -1 - ind
            lista_de_maiores.append(lista_crescente[ind])
        indices=busca_indice(lista, lista_de_maiores, i=1)
        for cromo in range(len(indices)):
            lista_final.append(cromossomos_1[indices[cromo]])
        return lista_final
    return [[cromossomos_1[indices[0]], cromossomos_1[indices[1]]], list(indices)]

def encontra_2_menores_fitness(cromossomos_1, qtd_cromos=2):
    if qtd_cromos == 2:
        lista = []
        for cromossomo in cromossomos_1:
            lista.append(cromossomo.fitness)
            
        lista_crescente = sorted(lista)
        lista_de_menores = [lista_crescente[0], lista_crescente[1]]
        
        indices = busca_indice(lista, lista_de_menores)
    else:
        lista = []
        lista_de_menores=[]
        lista_final=[]
        for cromossomo in cromossomos_1:
            lista.append(cromossomo.fitness)
            lista_crescente = sorted(lista)
        for ind in range(qtd_cromos):
            lista_de_menores.append(lista_crescente[ind])
        indices=busca_indice(lista, lista_de_menores, i=1)
        for cromo in range(len(indices)):
            lista_final.append(cromossomos_1[indices[cromo]])
        return lista_final
    
    return [[cromossomos_1[indices[0]], cromossomos_1[indices[1]]], list(indices)]

class Cromossomo:
    def __init__(self, fitness, carteira):
        self.carteira=carteira
        self.fitness=fitness
    def calcula_fitness(self, fitness):
        self.fitness = fitness(self.carteira)
        
def algoritmo_genetico(fitness, qtd_variaveis: int, iteracao_maxima=10000,  rodadas=0, numero_de_cromossomos=100, desvio_esperado=0.0001, maximizar_ou_minimizar="minimizar"):
    iteração = 0
    cromossomos_1 = copy.copy(linhagem_prima(numero_de_cromossomos, fitness, qtd_variaveis))
    print('')
    print("iniciando algoritmo otimizador")
    
    pbar = tqdm(desc="Otimizando", total=rodadas,
            unit='B', unit_scale=True, unit_divisor=512,)
    desvio_padrao = np.inf
    
    if rodadas >= 2:
            while iteração <= rodadas:
                cromossomos_2 = crossover(copy.copy(cromossomos_1), fitness)
                cromossomos_mutados = [mutação_do_filho(copy.copy(cromossomos_2[0]), fitness), mutação_do_filho(copy.copy(cromossomos_2[1]), fitness)]
                cromossomos_sobrepostos = [*sobreposição_doisgens(copy.copy(cromossomos_2[0]), fitness), *sobreposição_doisgens(copy.copy(cromossomos_2[1]),fitness)]
                cromossomos_novos = [*cromossomos_2, *cromossomos_mutados, *cromossomos_sobrepostos]
                cromossomos_1 = encontra_melhores_fitness_e_substitui(copy.copy(cromossomos_novos), maximizar_ou_minimizar, copy.copy(cromossomos_1), qtd_substituicao=2)
                pbar.update(1)
                if iteração >= iteracao_maxima:
                    break
                iteração +=1
    else:
        while desvio_padrao > desvio_esperado:
            cromossomos_2 = crossover(copy.copy(cromossomos_1), fitness)
            cromossomos_mutados = [mutação_do_filho(copy.copy(cromossomos_2[0]), fitness), mutação_do_filho(copy.copy(cromossomos_2[1]), fitness)]
            cromossomos_sobrepostos = [*sobreposição_doisgens(copy.copy(cromossomos_2[0]), fitness), *sobreposição_doisgens(copy.copy(cromossomos_2[1]),fitness)]
            cromossomos_novos = [*cromossomos_2, *cromossomos_mutados, *cromossomos_sobrepostos]
            cromossomos_1 = encontra_melhores_fitness_e_substitui(copy.copy(cromossomos_novos), maximizar_ou_minimizar, copy.copy(cromossomos_1), qtd_substituicao=2)
            pbar.update(1)
            fits=[]
            for fit in range(len(cromossomos_1)):
                fits.append(copy.copy(cromossomos_1[fit].fitness))
            desvio_padrao = np.std(fits)
            if iteração >= iteracao_maxima:
                break
            iteração +=1
        
    pbar.close()
    print("finalizado\n")
    
    return cromossomos_1, iteração