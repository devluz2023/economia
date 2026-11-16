class TeoriaProducaoCustos:

    @staticmethod
    def calcular_custos_totais_e_medios(custo_fixo: float, custo_variavel: float, quantidade: float) -> dict:
        """Calcula custos totais, custos médios e custos marginais parciais."""
        if quantidade <= 0:
            raise ValueError("A quantidade produzida deve ser maior que zero.")
            
        ct = custo_fixo + custo_variavel
        cfme = custo_fixo / quantidade
        cvme = custo_variavel / quantidade
        cme = ct / quantidade
        
        return {
            "custo_total": ct,
            "custo_fixo_medio": round(cfme, 4),
            "custo_variavel_medio": round(cvme, 4),
            "custo_total_medio": round(cme, 4)
        }

    @staticmethod
    def verificar_retornos_escala_cobb_douglas(alpha: float, beta: float) -> str:
        """Verifica os retornos de escala de uma função Cobb-Douglas através da soma dos expoentes (alpha + beta)."""
        soma = alpha + beta
        if abs(soma - 1.0) < 1e-5:
            return "Retornos Constantes de Escala"
        elif soma > 1.0:
            return "Retornos Crescentes de Escala"
        else:
            return "Retornos Decrescentes de Escala"

    @staticmethod
    def calcular_demanda_mercado(demandas_individuais: list, preco: float) -> float:
        """
        Calcula a demanda de mercado somando horizontalmente as quantidades 
        calculadas por funções de demanda individuais para um dado preço.
        Cada item na lista 'demandas_individuais' deve ser uma função lambda ou callable f(p).
        """
        quantidade_total = sum(funcao_demanda(preco) for funcao_demanda in demandas_individuais)
        return round(quantidade_total, 4)

    @staticmethod
    def equilibrio_longo_prazo_firma(pmg_l: float, pmg_k: float, salario_w: float, aluguel_r: float) -> bool:
        """
        Verifica a condição de equilíbrio da firma no longo prazo (tangência entre isoquanta e isocusto):
        PMg_L / PMg_K == w / r
        """
        if pmg_k == 0 or aluguel_r == 0:
            raise ValueError("Produtividade marginal do capital e aluguel do capital não podem ser zero.")
            
        razao_produtividades = pmg_l / pmg_k
        razao_custos = salario_w / aluguel_r
        
        return round(razao_produtividades, 4) == round(razao_custos, 4)