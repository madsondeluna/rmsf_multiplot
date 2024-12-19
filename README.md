# RMSD Comparison with Rolling Mean

Este repositório contém um script Python para comparar a evolução do RMSD (Root Mean Square Deviation) de múltiplos arquivos `.xvg` gerados a partir de simulações de dinâmica molecular. O código lê e processa os dados, calcula a média móvel (Rolling Mean) e gera gráficos para visualização dos resultados.

## Funcionalidades

- **Leitura de arquivos `.xvg`**: O código lê os arquivos de dados, ignorando comentários e metadados, e extrai as colunas de tempo e RMSD.
- **Média Móvel**: Calcula a média móvel para suavizar as flutuações do RMSD ao longo do tempo.
- **Visualização**: Plota gráficos para cada arquivo de dados, com o RMSD e a média móvel sobrepostos, utilizando cores diferentes para cada gráfico. Os gráficos são dispostos em uma grade de 4 linhas e 6 colunas.
- **Salvamento de Gráficos**: O gráfico final é salvo em alta resolução (300 DPI) no formato PNG.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- `pandas`
- `numpy`
- `matplotlib`

Você pode instalá-las utilizando o `pip`:

```bash
pip install pandas numpy matplotlib
