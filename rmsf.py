import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para ler o arquivo .xvg
def read_xvg(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            if not line.startswith(('#', '@')):  # Ignora comentários e metadados
                data.append(list(map(float, line.split())))
    return np.array(data)

# Lista de arquivos .xvg, excluindo GmDef7
file_paths = [
    'rmsd-GmDef2.xvg',
    'rmsd-GmDef3.xvg',
    'rmsd-GmDef4.xvg',
    'rmsd-GmDef5.xvg',
    'rmsd-GmDef6.xvg',
    'rmsd-GmDef8.xvg',
    'rmsd-GmDef9.xvg',
    'rmsd-GmDef10.xvg',
    'rmsd-GmDef11.xvg',
    'rmsd-GmDef12.xvg',
    'rmsd-GmDef13.xvg',
    'rmsd-GmDef14.xvg',
    'rmsd-GmDef15.xvg',
    'rmsd-GmDef16.xvg',
    'rmsd-GmDef17.xvg',
    'rmsd-GmDef18.xvg',
    'rmsd-GmDef19.xvg',
    'rmsd-GmDef20.xvg',
    'rmsd-GmDef21.xvg',
    'rmsd-GmDef22.xvg',
]

# Carregar os dados
data = [read_xvg(file) for file in file_paths]

# Convertendo para DataFrame para facilitar a manipulação
dfs = [pd.DataFrame(d, columns=['Time', 'RMSD']) for d in data]

# Calcular a Média Móvel (Rolling Average) para todos os datasets
window_size = 50  # Defina o tamanho da janela de suavização
for df in dfs:
    df['Rolling_RMSD'] = df['RMSD'].rolling(window=window_size).mean()

# Calcular limites do eixo y
all_rmsd = np.concatenate([df['RMSD'] for df in dfs])
y_min, y_max = all_rmsd.min(), all_rmsd.max()

# Criar subplots com 4 linhas e 6 colunas para acomodar 21 gráficos
fig, axs = plt.subplots(4, 6, figsize=(30, 20), dpi=300)  # Ajuste o figsize conforme necessário

# Definir o limite x máximo comum a todos os gráficos
x_max = max(df['Time'].max() for df in dfs)

# Definir cores diferentes para cada gráfico bruto (cores mais claras)
colors = [
    '#00FFFF',  # GmDef2
    '#FF6F61',  # GmDef3
    '#6A4C93',  # GmDef4
    '#F0E68C',  # GmDef5
    '#007A8C',  # GmDef6
    '#FFC371',  # GmDef8
    '#F8A3C8',  # GmDef9
    '#3E92CC',  # GmDef10
    '#A3D9A5',  # GmDef11
    '#D9A6C5',  # GmDef12
    '#FFCC29',  # GmDef13
    '#00B65C',  # GmDef14
    '#FFD3B4',  # GmDef15
    '#FFA07A',  # GmDef16
    '#C1C1C1',  # GmDef17
    '#DAF7A6',  # GmDef18
    '#FF9AA2',  # GmDef19
    '#A4C8E1',  # GmDef20
    '#C8E6C9',  # GmDef21
    '#FFB74D'   # GmDef22
]

# Cor cinza escuro para a média
average_color = '#4B4B4B'  # Cinza escuro

# Plotar os gráficos
for i, df in enumerate(dfs):
    # Ajuste do índice para correspondência correta com o GmDef
    actual_gmdef_number = [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22][i]

    ax = axs[i // 6, i % 6]  # Ajuste para grid 4x6
    base_color = colors[i]
    ax.plot(df['Time'], df['RMSD'], label=f'RMSD', color=base_color, alpha=0.5)  # Cor clara
    ax.plot(df['Time'], df['Rolling_RMSD'], label='Mean', color=average_color)  # Cor média
    ax.set_title(f'RMSD with Rolling Mean - GmDef{actual_gmdef_number}')
    ax.set_xlabel('Time (ns)')
    ax.set_ylabel('RMSD (nm)')
    ax.set_xlim([0, x_max])
    ax.set_ylim([y_min, y_max])  # Define a mesma escala para o eixo y
    ax.legend()

# Ajustar o espaçamento horizontal (wspace) e vertical (hspace) para aumentar a separação entre gráficos
plt.subplots_adjust(wspace=0.4, hspace=0.4)

# Salvar o gráfico em alta resolução (300 DPI)
plt.savefig('rmsd_comparison_plot_4.png', dpi=300)

# Exibir os gráficos em alta resolução
plt.show()
