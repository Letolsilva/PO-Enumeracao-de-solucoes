# Projeto de Enumeração de Soluções Básicas em Programação Linear

Este projeto tem como objetivo enumerar todas as soluções básicas (viáveis e inviáveis) de um problema de programação linear de minimização. O programa lê um arquivo de entrada que especifica o problema e utiliza um parser para interpretar os dados, seguido de um solver que calcula as soluções.

## Estrutura do Projeto

- `src/main.py`: Ponto de entrada da aplicação.
- `src/parser.py`: Funções para ler e interpretar o arquivo de entrada.
- `src/solver.py`: Lógica para calcular todas as soluções básicas.
- `src/types/index.py`: Definições de tipos e classes para estruturas de dados.
- `requirements.txt`: Dependências do projeto.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências listadas em `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```
3. Execute o programa passando o caminho do arquivo de entrada como argumento:
   ```
   python src/main.py caminho/do/arquivo.txt
   ```

## Exemplo de Uso

Considere um arquivo de entrada com a seguinte estrutura:

```
5 3
-1 -2 0 0 0
1 1 1 0 0 4
1 0 0 1 0 2
0 1 0 0 1 3
```

Ao executar o programa, ele irá processar o arquivo e apresentar todas as soluções básicas, indicando se são viáveis ou inviáveis, além de identificar a solução ótima.
