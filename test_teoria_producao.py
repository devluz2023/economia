import pytest
from teoria_producao import TeoriaProducao

def test_produtividade_media():
    # 500 unidades produzidas com 10 trabalhadores = 50 por trabalhador
    pme = TeoriaProducao.calcular_produtividade_media(500, 10)
    assert pme == 50.0

def test_produtividade_media_erro_trabalhador_zero():
    with pytest.raises(ValueError):
        TeoriaProducao.calcular_produtividade_media(500, 0)

def test_produtividade_marginal():
    # Produção sobe de 500 para 580 (delta = 80) com 2 trabalhadores a mais (delta = 2)
    pmg = TeoriaProducao.calcular_produtividade_marginal(80, 2)
    assert pmg == 40.0

def test_custo_oportunidade_fpp():
    # Passando de 100 de B e 0 de A para 80 de B e 10 de A -> |(-20) / 10| = 2.0
    custo = TeoriaProducao.calcular_custo_oportunidade_fpp(100, 80, 0, 10)
    assert custo == 2.0

def test_avaliar_ponto_fpp():
    # Restrição: 2*Qa + 1*Qb = 100
    # Ineficiente
    assert TeoriaProducao.avaliar_ponto_fpp(2, 20, 1, 50, 100) == "Ineficiente (Ociosidade de recursos)"
    # Eficiente
    assert TeoriaProducao.avaliar_ponto_fpp(2, 30, 1, 40, 100) == "Eficiente (Sobre a curva da FPP)"
    # Inatingível
    assert TeoriaProducao.avaliar_ponto_fpp(2, 40, 1, 30, 100) == "Inatingível com os recursos atuais"