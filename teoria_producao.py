class TeoriaProducao:
    
    @staticmethod
    def calcular_produtividade_media(quantidade_total: float, fator_trabalho: float) -> float:
        """Calcula a Produtividade Média do Trabalho (PMe_L)."""
        if fator_trabalho <= 0:
            raise ValueError("A quantidade de fator de trabalho deve ser maior que zero.")
        return quantidade_total / fator_trabalho

    @staticmethod
    def calcular_produtividade_marginal(delta_quantidade: float, delta_trabalho: float) -> float:
        """Calcula a Produtividade Marginal do Trabalho (PMg_L)."""
        if delta_trabalho == 0:
            raise ValueError("A variação do fator de trabalho não pode ser zero.")
        return delta_quantidade / delta_trabalho

    @staticmethod
    def calcular_custo_oportunidade_fpp(qtd_b_inicial: float, qtd_b_final: float, 
                                        qtd_a_inicial: float, qtd_a_final: float) -> float:
        """Calcula o custo de oportunidade (Taxa Marginal de Transformação - TMT) ao longo da FPP."""
        delta_b = qtd_b_final - qtd_b_inicial
        delta_a = qtd_a_final - qtd_a_inicial
        
        if delta_a == 0:
            raise ValueError("A variação da quantidade do Bem A não pode ser zero.")
            
        return abs(delta_b / delta_a)

    @staticmethod
    def avaliar_ponto_fpp(coef_a: float, qa: float, coef_b: float, qb: float, recursos_totais: float) -> str:
        """
        Avalia se um ponto de produção (Qa, Qb) é eficiente, ineficiente ou inatingível 
        dada a restrição linear de recursos: coef_a * Qa + coef_b * Qb = Recursos Totais.
        """
        gasto_total = (coef_a * qa) + (coef_b * qb)
        
        if round(gasto_total, 5) < round(recursos_totais, 5):
            return "Ineficiente (Ociosidade de recursos)"
        elif round(gasto_total, 5) == round(recursos_totais, 5):
            return "Eficiente (Sobre a curva da FPP)"
        else:
            return "Inatingível com os recursos atuais"