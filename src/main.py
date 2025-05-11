from parser import ler_arquivo_entrada
from solver import calcular_solucoes_basicas, encontrar_solucao_otima

def main():
    input_file_path = 'entrada.txt' 

    n, m, c, restricoes = ler_arquivo_entrada(input_file_path)

    A = [linha[:-1] for linha in restricoes] # coeficientes das variáveis
    b = [linha[-1] for linha in restricoes] # termos independentes
    restricoes_completas = [A[i] + [b[i]] for i in range(m)]
    
    solucoes_basicas, viaveis, inviaveis = calcular_solucoes_basicas(c, restricoes_completas)
    
    for solucao, z in solucoes_basicas:
        estado = "viável" if all(val >= 0 for val in solucao) else "inviável"
        print(f"x = {solucao}, z = {z} ({estado})")
    

    print(f"Número total de soluções básicas: {len(solucoes_basicas)}")
    print(f"Número de soluções básicas viáveis: {len(viaveis)}")
    print(f"Número de soluções básicas inviáveis: {len(inviaveis)}")


    solucao_otima = encontrar_solucao_otima(viaveis)
    if solucao_otima:
        print("Solução ótima encontrada!")
        print(f"Função objetivo: {solucao_otima[1]}")
        print(f"x = {solucao_otima[0]}")
    else:
        print("Nenhuma solução básica viável encontrada!")

if __name__ == "__main__":
    main()