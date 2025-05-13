def calcular_solucoes_basicas(coeficientes, restricoes):
    from itertools import combinations
    import numpy as np

    n = len(coeficientes)
    m = len(restricoes)

    solucoes_basicas = []
    viaveis = []
    inviaveis = []

    for indices in combinations(range(n), m):
        A = np.array([[restricoes[i][j] for j in indices] for i in range(m)])
        b = np.array([restricoes[i][-1] for i in range(m)])
        
        try:
            x = np.linalg.solve(A, b)
            solucao = [0] * n
            
            for i, idx in enumerate(indices):
                solucao[idx] = x[i]
            
            z = sum(coeficientes[i] * solucao[i] for i in range(n))
            solucoes_basicas.append((solucao, z))

            if all(val >= 0 for val in solucao):
                viaveis.append((solucao, z))
            else:
                inviaveis.append((solucao, z))

        except np.linalg.LinAlgError:
            continue

    return solucoes_basicas, viaveis, inviaveis

def encontrar_solucao_otima(viaveis):
    if not viaveis:
        return None
    return min(viaveis, key=lambda x: x[1])
