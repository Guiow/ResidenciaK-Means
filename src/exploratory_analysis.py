import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns


#Carregamento dos dados de treino, cada valor delimitado por espaço e eles nao possuem rotulos
data = pd.read_csv('data/X_train.txt', sep='\\s+', header=None)

def main():
    #initial_analysis()
    #visualizeData2D()
    visualizeData3D()
    #visualizeDistribution()

def initial_analysis():
    # Adicionar o head do dataset ao resumo
    head_dataset = "Primeiras 5 linhas do dataset:\n" + data.head().iloc[:, :5].to_string(index=False)  # Apenas 5 primeiras colunas

    num_linhas, num_colunas = data.shape
    resumo_dataset = f"""De acordo com o note do README os dados já estão normalizados.\n
        Total de linhas: {num_linhas}\n
        Total de colunas: {num_colunas}\n
        Tipo dos dados: float64\n"""

    # Salvar o resumo do dataset e o head em um arquivo .txt
    with open('docs/metrics/resumo_dataset.txt', 'w') as file:
        file.write(head_dataset)
        file.write("\n\n")
        file.write(resumo_dataset)

def visualizeData2D():
    #Reduzindo a dimensionalidade para 2, para ser plotado num grafico 2D
    X_pca_2d = applyPCA(2)

    #Visualizando os dados em 2D
    plt.figure(figsize=(10, 6))
    plt.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], alpha=0.6, c='blue', edgecolor='k', s=30)
    plt.title("Projeção dos Dados X_train em 2D após PCA", fontsize=14)
    plt.xlabel("Componente Principal 1", fontsize=12)
    plt.ylabel("Componente Principal 2", fontsize=12)
    plt.grid(True)
    plt.savefig("docs/graphs/visualizacao_dados_2d")

def applyPCA(n_components):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(data)

def visualizeData3D():
    #Reduzindo a dimensionalidade para 2, para ser plotado num grafico 3D
    X_pca_3d = applyPCA(3)

    #Visualizando os dados em 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(
        X_pca_3d[:, 0], 
        X_pca_3d[:, 1], 
        X_pca_3d[:, 2],
        alpha=0.6, c='blue', edgecolor='k', s=30
    )
    ax.set_title("Projeção 3D dos Dados X_train após PCA", fontsize=14)

    #CP = Componente Principal
    ax.set_xlabel("CP 1", fontsize=12)
    ax.set_ylabel("CP 2", fontsize=12)
    ax.set_zlabel("CP 3", fontsize=12)
    ax.view_init(elev=8, azim=115) 
    fig.savefig('docs/graphs/visualizacao_dados_3d.png', dpi=300)  # Salva a imagem em alta resolução

def visualizeDistribution():
    #Resume o conjunto dos dados em 12 valores
    X_pca = applyPCA(12)
    pca_df = pd.DataFrame(data=X_pca, columns=[f'PC{i+1}' for i in range(12)])

    # Visualizando as distribuições com histogramas das 12 primeiras componentes principais
    plt.figure(figsize=(18, 10))
    for i, col in enumerate(pca_df.columns):# Iterando sobre as 12 colunas de componentes principais
        plt.subplot(3, 4, i+1)
        sns.histplot(pca_df[col], kde=True, bins=30)
        plt.title(f'Distribuição da {col}')
        plt.xlabel('Valor')
        plt.ylabel('Frequência')

    plt.tight_layout()
    plt.savefig('docs/graphs/distribuicao_resumida')

if __name__ == "__main__":
    main()