import requests
import json
import pandas as pd

def getMunicipios():
    ## IBGE API
    API_URL = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios?orderBy=nome'
    ## Municipios Data Aquisition
    responseData = requests.get(API_URL)
    return responseData.json()
    
# pesquisas
#municipioData[n]['id'] #id municipio
#municipioData[n]['nome'] #nome município
#municipioData[n]['microrregiao']['mesorregiao']['id'] #id estado
#municipioData[n]['microrregiao']['mesorregiao']['UF']['sigla'] #sigla estado
#municipioData[n]['microrregiao']['mesorregiao']['UF']['nome'] #nome estado

def municipioDados():
    idMunicipio = []
    nomemunicipio = []
    idEstado = []
    siglaEstado = []
    nomeEstado = []
    cont = 0
    x = 'id'
    for x in municipioData:
        idMunicipio.append(municipioData[cont]['id'])
        nomemunicipio.append(municipioData[cont]['nome'])
        idEstado.append(municipioData[cont]['microrregiao']['mesorregiao']['id'])
        siglaEstado.append(municipioData[cont]['microrregiao']['mesorregiao']['UF']['sigla']) 
        nomeEstado.append(municipioData[cont]['microrregiao']['mesorregiao']['UF']['nome'])
        cont += 1
        data = {'id Município':idMunicipio, 'nome Município': nomemunicipio, 'id Estado': idEstado, 'nome Estado': nomeEstado, 'sigla Estado': siglaEstado}
        dfLocalidade = pd.DataFrame(data)
    return dfLocalidade
    
    municipioDados()