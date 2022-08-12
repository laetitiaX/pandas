### a Função pesquisaCoordenadas encontra coordenadas a partir de dados de endereço

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def pesquisaCoordenadas(nomePlanilha, **kwargs):
        if 'sheetName' in kwargs:
            sheetName = kwargs.get('sheetName')
            df = pd.read_excel(nomePlanilha,sheetName)
        else:
            df = pd.read_excel(nomePlanilha)

        locator = Nominatim(user_agent='myGeocoder')


        endereco = df[['bairro','municipio','uf']]
        endereco['endereco'] = endereco['bairro'] +', '+ endereco['municipio'] +', '+ endereco['uf']
        geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

        endereco['geocode'] = endereco['endereco'].apply(geocode)

        for l in range(len(endereco)):
            if endereco['geocode'].iloc[l] == None:
                cidadeUF = endereco['municipio'] + ' - ' + endereco['uf']
                endereco['geocode'].iloc[l] = locator.geocode(cidadeUF[0])
                

        endereco['latitude'] = endereco['geocode'].apply(lambda loc: loc.latitude if loc else None)
        endereco['longitude'] = endereco['geocode'].apply(lambda loc: loc.longitude if loc else None)

        df['longitude'] = endereco['longitude']
        df['latitude'] = endereco['latitude']

        return df