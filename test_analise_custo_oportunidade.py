import pandas as pd
import pytest
from analise_custo_oportunidade import consultar_sgs, calcular_custo_oportunidade_real,calcular_custo_oportunidade_fpp

def test_consultar_sgs_formato_e_tipo():
    """Garante que a função do BACEN retorna um DataFrame estruturado corretamente."""
    # Série 432 = Selic Meta
    df = consultar_sgs(432, '01/01/2024')
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'valor' in df.columns
    assert pd.api.types.is_datetime64_any_dtype(df.index)
    assert pd.api.types.is_numeric_dtype(df['valor'])

def test_consultar_sgs_serie_invalida():
    """Garante que o sistema lida corretamente com códigos de série inexistentes."""
    with pytest.raises(Exception):
        consultar_sgs(99999999, '01/01/2024')

def test_calcular_custo_oportunidade_real_integridade():
    """Verifica se o cálculo do custo de oportunidade real gera as colunas e dados esperados."""
    df_resultado = calcular_custo_oportunidade_real('01/01/2024')
    
    assert isinstance(df_resultado, pd.DataFrame)
    assert 'selic_aa' in df_resultado.columns
    assert 'ipca_m' in df_resultado.columns
    assert 'juro_real_aproximado' in df_resultado.columns
    assert len(df_resultado) > 0
    # O custo real não deve conter valores nulos no resultado final processado
    assert df_resultado['juro_real_aproximado'].isnull().sum() == 0


def test_calcular_custo_oportunidade_fpp():
    """Valida o cálculo do custo de oportunidade na FPP (sacrifício do Bem B por unidade de A)."""
    # Exemplo: Se passamos de 100 unidades de B e 0 de A para 80 unidades de B e 10 de A:
    # Delta B = 80 - 100 = -20
    # Delta A = 10 - 0 = 10
    # Custo de Oportunidade = |-20 / 10| = 2 unidades de B por cada unidade de A.
    
    custo = calcular_custo_oportunidade_fpp(qtd_b_inicial=100, qtd_b_final=80, 
                                          qtd_a_inicial=0, qtd_a_final=10)
    
    assert custo == 2.0

def test_calcular_custo_oportunidade_fpp_divisao_por_zero():
    """Garante que a função lida com divisões por zero se o Bem A não variar."""
    import pytest
    with pytest.raises(ValueError):
        calcular_custo_oportunidade_fpp(100, 80, 10, 10)