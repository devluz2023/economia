import pytest
from teoria_producao_custos import TeoriaProducaoCustos

def test_calcular_custos():
    # CF = 200, CV = 300, Q = 50
    # CT = 500, CFMe = 4.0, CVMe = 6.0, CMe = 10.0
    res = TeoriaProducaoCustos.calcular_custos_totais_e_medios(200.0, 300.0, 50.0)
    assert res["custo_total"] == 500.0
    assert res["custo_fixo_medio"] == 4.0
    assert res["custo_variavel_medio"] == 6.0
    assert res["custo_total_medio"] == 10.0

def test_verificar_retornos_escala():
    assert TeoriaProducaoCustos.verificar_retornos_escala_cobb_douglas(0.6, 0.4) == "Retornos Constantes de Escala"
    assert TeoriaProducaoCustos.verificar_retornos_escala_cobb_douglas(0.7, 0.5) == "Retornos Crescentes de Escala"
    assert TeoriaProducaoCustos.verificar_retornos_escala_cobb_douglas(0.3, 0.4) == "Retornos Decrescentes de Escala"

def test_calcular_demanda_mercado():
    # Consumidor 1: Q1 = 10 - P
    # Consumidor 2: Q2 = 15 - 2P
    # Para P = 3 -> Q1 = 7, Q2 = 9 -> Mercado = 16
    f1 = lambda p: 10 - p
    f2 = lambda p: 15 - (2 * p)
    
    mercado = TeoriaProducaoCustos.calcular_demanda_mercado([f1, f2], preco=3.0)
    assert mercado == 16.0

def test_equilibrio_longo_prazo_firma():
    # PMg_L = 20, PMg_K = 10 -> Razão = 2.0
    # w = 100, r = 50 -> Razão = 2.0
    assert TeoriaProducaoCustos.equilibrio_longo_prazo_firma(20.0, 10.0, 100.0, 50.0) is True