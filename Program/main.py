import funcoes.fitness as ft
import funcoes.ft_gerais as tk
import funcoes.genetico_1 as genetic
import time

tickers = tk.principal()

def func1(desvio_esperado=0.000001,num_rodadas=0,num_cromossomos=500):
    inicio_tempo=time.time()

    maximizar_ou_minimizar = "maximizar"
    print(maximizar_ou_minimizar)

    results1 =[genetic.algoritmo_genetico(rodadas=num_rodadas, numero_de_cromossomos=num_cromossomos,
                                        fitness=ft.fitness_retorno_sobre_risco,
                                        maximizar_ou_minimizar=maximizar_ou_minimizar,
                                        qtd_variaveis=tickers,
                                        desvio_esperado=desvio_esperado)]
    return genetic.encontra_2_maiores_fitness(results1[0][0], qtd_cromos=11)

def func2(desvio_esperado=0.000001,num_rodadas=0,num_cromossomos=500):
    inicio_tempo=time.time()


    maximizar_ou_minimizar = "maximizar"
    print(maximizar_ou_minimizar)

    results2 =[genetic.algoritmo_genetico(rodadas=num_rodadas, numero_de_cromossomos=num_cromossomos,
                                        fitness=ft.fitness_retorno_mais_1_sobre_risco,
                                        maximizar_ou_minimizar=maximizar_ou_minimizar,
                                        qtd_variaveis=tickers,
                                        desvio_esperado=desvio_esperado)]
    return genetic.encontra_2_maiores_fitness(results2[0][0], qtd_cromos=11)

def func3(desvio_esperado=0.000001,num_rodadas=0,num_cromossomos=500):
    inicio_tempo=time.time()

    
    maximizar_ou_minimizar = "minimizar"
    print(maximizar_ou_minimizar)
    results4 =[genetic.algoritmo_genetico(rodadas=num_rodadas, numero_de_cromossomos=num_cromossomos,
                                        fitness=ft.fitness_risco_mais_1_sobre_retorno,
                                        maximizar_ou_minimizar=maximizar_ou_minimizar,
                                        qtd_variaveis=tickers,
                                        desvio_esperado=desvio_esperado)]
    return genetic.encontra_2_menores_fitness(results4[0][0], qtd_cromos=11)

def func4(desvio_esperado=0.000001,num_rodadas=0,num_cromossomos=500):
    inicio_tempo=time.time()


    maximizar_ou_minimizar = "minimizar"
    print(maximizar_ou_minimizar)

    results6 =[genetic.algoritmo_genetico(rodadas=num_rodadas, numero_de_cromossomos=num_cromossomos,
                                        fitness=ft.fitness_risco_sobre_retorno,
                                        maximizar_ou_minimizar=maximizar_ou_minimizar,
                                        qtd_variaveis=tickers,
                                        desvio_esperado=desvio_esperado)]
    return genetic.encontra_2_menores_fitness(results6[0][0], qtd_cromos=11)

def func5(desvio_esperado=0.000001,num_rodadas=0,num_cromossomos=500):
    inicio_tempo=time.time()

    maximizar_ou_minimizar = "minimizar"
    print(maximizar_ou_minimizar)

    results8 =[genetic.algoritmo_genetico(rodadas=num_rodadas, numero_de_cromossomos=num_cromossomos,
                                        fitness=ft.fitness_novo,
                                        maximizar_ou_minimizar=maximizar_ou_minimizar,
                                        qtd_variaveis=tickers,
                                        desvio_esperado=desvio_esperado)]
    return genetic.encontra_2_menores_fitness(results8[0][0], qtd_cromos=11)


def main():
    desvio_esperado=0.0001
    num_rodadas=0
    num_cromossomos=500
    um=func1(desvio_esperado=desvio_esperado,num_rodadas=num_rodadas,num_cromossomos=num_cromossomos)[0]
    dois=func2(desvio_esperado=desvio_esperado,num_rodadas=num_rodadas,num_cromossomos=num_cromossomos)[0]
    tres=func3(desvio_esperado=desvio_esperado,num_rodadas=num_rodadas,num_cromossomos=num_cromossomos)[0]
    quatro=func4(desvio_esperado=desvio_esperado,num_rodadas=num_rodadas,num_cromossomos=num_cromossomos)[0]
    cinco=func5(desvio_esperado=desvio_esperado,num_rodadas=num_rodadas,num_cromossomos=num_cromossomos)[0]
    lista=[um,dois,tres,quatro,cinco]
    i=0
    while i < 5:
        print(f"carteira {i}: {lista[i].carteira},\n risco: {ft.calcula_risco(lista[i].carteira)}, \nretorno: {ft.calcula_retorno2(lista[i].carteira)}\n\n")
        i+=1
if __name__ == '__main__':
    main()