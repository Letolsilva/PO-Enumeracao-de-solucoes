import sys
from parser import ler_arquivo_entrada
from solver import calcular_solucoes_basicas, encontrar_solucao_otima

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <arquivo_entrada>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    n, m, c, restricoes = ler_arquivo_entrada(input_file_path)

    A = [linha[:-1] for linha in restricoes]
    b = [linha[-1] for linha in restricoes] 
    restricoes_completas = [A[i] + [b[i]] for i in range(m)]
    
    solucoes_basicas, viaveis, inviaveis = calcular_solucoes_basicas(c, restricoes_completas)
    
    for solucao, z in solucoes_basicas:
        solucao_arredondada = [round(val, 6) for val in solucao]
        z_arredondado = round(z, 6)
        estado = "viável" if all(val >= 0 for val in solucao_arredondada) else "inviável"
        print(f"x = {solucao_arredondada}, z = {z_arredondado} ({estado})")
        

    print(f"Número total de soluções básicas: {len(solucoes_basicas)}")
    print(f"Número de soluções básicas viáveis: {len(viaveis)}")
    print(f"Número de soluções básicas inviáveis: {len(inviaveis)}")


    solucao_otima = encontrar_solucao_otima(viaveis)
    if solucao_otima:
        print("Solução ótima encontrada!")
        print(f"Função objetivo: {round(solucao_otima[1], 6)}")
        print(f"x = {[round(val, 6) for val in solucao_otima[0]]}")
    else:
        print("Nenhuma solução básica viável encontrada!")

if __name__ == "__main__":
    main()