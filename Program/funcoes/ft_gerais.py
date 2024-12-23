import numpy as np
from tqdm import tqdm
import yfinance as yf
import pandas as pd
from datetime import datetime
def principal():
    tickers = ['PETR4.SA','VALE3.SA', 'PRIO3.SA', 'BBSE3.SA', 'ITUB4.SA', 'GOAU4.SA']

    inicio = '2024-05-30'
    final = '2024-07-29'

    dados_taxas_originais = pd.DataFrame.from_dict(pega_tick(tickers,intervalo='1h', inicio=inicio, fimm=final), orient='columns')

    global media_de_retornoss
    global covarianciass
    media_de_retornoss = media_tx_red(taxas_de_retorno(dados_taxas_originais))
    covarianciass = covariancia(taxas_de_retorno(dados_taxas_originais))
    
    return len(tickers)
def pega_tick(tickers, inicio, fimm, intervalo='1d'):
    agora = datetime.now()
    print(agora)

    if agora.month < 10:
        
        mes = "0" + str(agora.month)
        
    else: mes = str(agora.month)

    teste = str(agora.year) + "-" + mes + "-" + str(agora.day)
    if fimm == "agora":
        fimm = teste

    # Defina a data de início e a data de fim
    
    pbar2 = tqdm(desc="Pegando Dados", total=len(tickers),
        unit='B', unit_scale=True, unit_divisor=512,)
    dicionario = {}
    num_tick = len(tickers)

    i = 0

    while i < num_tick:

        data = yf.Ticker(tickers[i])

        hist = (data.history(start=inicio,end=fimm, interval=intervalo)).loc[:, "Close"]

        dicionario[i] = list(hist)
        pbar2.update(1)

        i += 1
    pbar2.close()
    return dicionario

def taxas_de_retorno(dataframe):
    
    dataframe_taxas = pd.DataFrame()
    TAXAS = [0]*len(list(dataframe.index))
    p = 0
    while p < len(dataframe.columns):
        TAXAS = [0]*len(list(dataframe.index))    
        taxas_unica = dataframe[p].tolist()
        
        for i in range(1, len(taxas_unica)):
        
            TAXAS[i] = (-100 + ((taxas_unica[i] * 100)/taxas_unica[i - 1]))
        
        TAXAS.pop(0)
        dataframe_taxas[p] = TAXAS
        p += 1
    return dataframe_taxas

def media_tx_red(tx_ret):
    i = 0
    media = []
    while i < len(tx_ret.columns):
        media.append(0)
        media[i] = tx_ret[i].sum()/len(tx_ret)
        i += 1
        
    return media

def covar(A, B):
    A_ = np.array(A).mean()
    B_ = np.array(B).mean()

    i = 0
    soma = 0
    while(i < len(A)):
        soma = soma + (A[i] - A_) * (B[i] - B_)
        
        i += 1
    cov = soma / len(A)
    return cov

def covariancia(dataframe):
        
    i = 0
    listaa = []
    listaaa = []
    while i < len(dataframe.columns):
        listaaa.append(listaa)
        listaaa[i] = list(dataframe[i])
        i += 1
        
    lista = listaaa
    
    lista_np = np.array(lista)
    
    matriz_cov = np.zeros((len(dataframe.columns), len(dataframe.columns)))
    
    i = 0
    while i < len(dataframe.columns):
        
        j = 0
        while j < len(dataframe.columns):
            
            matriz_cov[[i],[j]] = covar(lista_np[i], lista_np[j])
            
            j += 1        
        i += 1
    return matriz_cov

def var(A):
    A_ = np.array(A).mean()
    B_ = A_

    i = 0
    soma = 0
    while(i < len(A)):
        soma = soma + (A[i] - A_) * (A[i] - B_)
    
        i += 1
    cov = soma / len(A)
    return cov
