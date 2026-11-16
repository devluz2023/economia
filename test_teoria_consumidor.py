import pytest
from teoria_consumidor import TeoriaConsumidor

def test_calcular_tms():
    # UMgX = 10, UMgY = 5 -> TMS = 2.0
    tms = TeoriaConsumidor.calcular_tms_cobb_douglas(10.0, 5.0)
    assert tms == 2.0

def test_calcular_equilibrio_cobb_douglas():
    # Renda = 1000, Px = 10, Py = 20, preferencias simétricas (alpha=0.5, beta=0.5)
    # X otimo = 0.5 * (1000 / 10) = 50
    # Y otimo = 0.5 * (1000 / 20) = 25
    qx, qy = TeoriaConsumidor.calcular_equilibrio_cobb_douglas(renda=1000, px=10, py=20)
    assert qx == 50.0
    assert qy == 25.0

def test_calcular_efeitos_slutsky():
    # X1 = 100, XH = 90 (queda de consumo por substituição), X2 = 70 (queda total após efeito renda)
    # ES = 90 - 100 = -10
    # ER = 70 - 90 = -20
    # EP = 70 - 100 = -30
    efeitos = TeoriaConsumidor.calcular_efeitos_slutsky(100, 90, 70)
    assert efeitos["efeito_substituição"] == -10.0
    assert efeitos["efeito_renda"] == -20.0
    assert efeitos["efeito_preco_total"] == -30.0

def test_calcular_elasticidade_preco_demanda():
    # Preço sobe de 10 para 12 (delta_p = 2), Quantidade cai de 100 para 80 (delta_q = -20)
    # ε = (-20 / 2) * (10 / 100) = -10 * 0.1 = -1.0
    varepsilon = TeoriaConsumidor.calcular_elasticidade_preco_demanda(100, 80, 10, 12)
    assert varepsilon == -1.0