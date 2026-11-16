import pandas as pd
import requests

def consultar_sgs(codigo_serie: int, data_inicio: str = '01/01/2023') -> pd.DataFrame:
    """Consulta a API do SGS do BACEN e retorna um DataFrame com data indexada e valor numérico."""
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={data_inicio}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise ConnectionError(f"Erro ao acessar API do BACEN para a série {codigo_serie}. Status: {response.status_code}")
    
    dados = response.json()
    if not dados:
        raise ValueError(f"Nenhum dado retornado para a série {codigo_serie}.")
        
    df = pd.DataFrame(dados)
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['valor'] = pd.to_numeric(df['valor'])
    df.set_index('data', inplace=True)
    return df

def calcular_custo_oportunidade_real(data_inicio: str = '01/01/2023') -> pd.DataFrame:
    """
    Calcula o custo de oportunidade real combinando a Selic Meta anualizada (Série 432) 
    e o IPCA mensal (Série 433) acumulado ou deflacionado pela Equação de Fisher aproximada.
    Retorna um DataFrame consolidado.
    """
    selic_df = consultar_sgs(432, data_inicio) # Selic (% a.a.)
    ipca_df = consultar_sgs(433, data_inicio)   # IPCA mensal (%)
    
    # Unifica as séries por data (mensalizando/alinhando)
    df = pd.DataFrame({
        'selic_aa': selic_df['valor'],
        'ipca_m': ipca_df['valor']
    }).dropna()
    
    # Custo de oportunidade real aproximado (Fisher: Juros Reais = Juros Nominais - Inflação)
    # Como a Selic é anual e o IPCA é mensal, convertemos a inflação aproximada anualizada ou mantemos comparativo simples
    df['juro_real_aproximado'] = df['selic_aa'] - (df['ipca_m'] * 12)
    
    return df


def calcular_custo_oportunidade_fpp(qtd_b_inicial: float, qtd_b_final: float, 
                                    qtd_a_inicial: float, qtd_a_final: float) -> float:
    """
    Calcula o custo de oportunidade de produzir o Bem A em termos do Bem B 
    ao longo da Fronteira de Possibilidades de Produção (FPP).
    Fórmula: | Delta Qtd. do Bem B / Delta Qtd. do Bem A |
    """
    delta_b = qtd_b_final - qtd_b_inicial
    delta_a = qtd_a_final - qtd_a_inicial
    
    if delta_a == 0:
        raise ValueError("A variação da quantidade do Bem A não pode ser zero.")
        
    # Retorna o valor absoluto do sacrifício do Bem B por unidade adicional do Bem A
    return abs(delta_b / delta_a)