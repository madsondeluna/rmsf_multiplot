# RMSF Comparison Plot

Este repositório contém um script Python para comparar a evolução da RMSF (Root Mean Square Fluctuation) de múltiplos arquivos `.xvg` gerados a partir de simulações de dinâmica molecular. O código lê e processa os dados, e gera gráficos para visualização das flutuações nos resíduos das simulações.

## Funcionalidades

- **Leitura de arquivos `.xvg`**: O código lê arquivos de dados RMSF, ignorando comentários e metadados, e extrai as colunas de resíduos (AA) e RMSF (nm).
- **Visualização**: Plota gráficos para cada arquivo de dados com a RMSF ao longo dos resíduos (AA) e usa cores distintas para cada gráfico.
- **Salvar gráficos**: O gráfico final é salvo em alta resolução (300 DPI) no formato PNG.
- **Limitação do eixo x**: O eixo x é ajustado com limites específicos dependendo do arquivo, com uma diferença para os casos dos arquivos 14 e 16.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- `pandas`
- `numpy`
- `matplotlib`

Você pode instalá-las utilizando o `pip`:

```bash
pip install pandas numpy matplotlib

## Aviso

Os arquivos `.xvg` disponíveis neste repositório são meramente ilustrativos.
