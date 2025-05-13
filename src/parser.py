def ler_arquivo_entrada(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    n, m = map(int, linhas[0].strip().split())
    coeficientes_objetivo = list(map(float, linhas[1].strip().split()))
    
    restricoes = []
    for i in range(2, 2 + m):
        restricao = list(map(float, linhas[i].strip().split()))
        restricoes.append(restricao)
    
    return n, m, coeficientes_objetivo, restricoes

