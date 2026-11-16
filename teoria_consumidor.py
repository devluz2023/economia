class TeoriaConsumidor:

    @staticmethod
    def calcular_tms_cobb_douglas(utilidade_x: float, utilidade_y: float) -> float:
        """Calcula a Taxa Marginal de Substituição (TMS) dados as utilidades marginais dos bens X e Y."""
        if utilidade_y == 0:
            raise ValueError("A utilidade marginal do bem Y não pode ser zero.")
        return utilidade_x / utilidade_y

    @staticmethod
    def calcular_equilibrio_cobb_douglas(renda: float, px: float, py: float, alpha: float = 0.5, beta: float = 0.5) -> tuple:
        """
        Calcula o equilíbrio do consumidor para uma função de utilidade Cobb-Douglas típica: U(X,Y) = X^alpha * Y^beta.
        Garante que todo o orçamento é gasto nas proporções ótimas.
        """
        if px <= 0 or py <= 0 or renda <= 0:
            raise ValueError("Preços e renda devem ser maiores que zero.")
        
        # Proporções de gasto para Cobb-Douglas: X = (alpha / (alpha + beta)) * (Renda / Px)
        soma_expoentes = alpha + beta
        qtd_x = (alpha / soma_expoentes) * (renda / px)
        qtd_y = (beta / soma_expoentes) * (renda / py)
        
        return round(qtd_x, 4), round(qtd_y, 4)

    @staticmethod
    def calcular_efeitos_slutsky(x1: float, xh: float, x2: float) -> dict:
        """
        Calcula o Efeito Preço total decomposto em Efeito Substituição e Efeito Renda.
        - x1: Quantidade inicial consumida
        - xh: Quantidade no ponto intermediário (Compensação de Hicks / utilidade constante)
        - x2: Quantidade final consumida após a variação de preço
        """
        efeito_substituição = xh - x1
        efeito_renda = x2 - xh
        efeito_preco_total = x2 - x1
        
        # Validação da identidade fundamental: EP = ES + ER
        if round(efeito_preco_total, 5) != round(efeito_substituição + efeito_renda, 5):
            raise ValueError("A soma de ES e ER deve ser igual ao Efeito Preço total.")
            
        return {
            "efeito_substituição": efeito_substituição,
            "efeito_renda": efeito_renda,
            "efeito_preco_total": efeito_preco_total
        }

    @staticmethod
    def calcular_elasticidade_preco_demanda(q_inicial: float, q_final: float, p_inicial: float, p_final: float) -> float:
        """Calcula a elasticidade-preço da demanda (ε) com base nas variações de preço e quantidade."""
        delta_q = q_final - q_inicial
        delta_p = p_final - p_inicial
        
        if delta_p == 0:
            raise ValueError("A variação do preço não pode ser zero.")
        if q_inicial == 0 or p_inicial == 0:
            raise ValueError("Quantidade inicial e preço inicial devem ser maiores que zero.")
            
        elasticidade = (delta_q / delta_p) * (p_inicial / q_inicial)
        return round(elasticidade, 4)