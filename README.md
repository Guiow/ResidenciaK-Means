# ResidenciaK-Means

Este repositório contém o projeto *ResidenciaK-Means*, desenvolvido para realizar análise de agrupamento no conjunto de dados "Human Activity Recognition Using Smartphones". O projeto utiliza o algoritmo K-Means para identificar padrões e agrupar dados obtidos por sensores de smartphones em diferentes atividades humanas.

---

## Estrutura do Repositório

```plaintext
ResidenciaK-Means/
├── data/
│   └── X_train.txt
├── docs/
│   ├── graphs/
│   │   ├── visualizacao_dados_2d.png
│   │   ├── visualizacao_dados_3d.png
│   │   ├── distribuicao_resumida.png
│   │   ├── clusters2Dk=2.png
│   │   ├── clusters2Dk=3.png
│   │   ├── clusters2Dk=4.png
│   │   ├── clusters3Dk=2.png
│   │   └── clusters3Dk=3.png
│   └── metrics/
│       └── resumo_dataset.txt
├── src/
│   ├── k_means.py
│   ├── generate_report.py
│   └── exploratory_analysis.py
└── README.md
```

---

## Explicação de Cada Parte

### **`data/`**
- Contém o conjunto de dados necessário para a análise.
  - **`X_train.txt`**: Arquivo principal do dataset usado no projeto, contendo dados de sensores de smartphones.

### **`docs/`**
- **`graphs/`**: Armazena as visualizações geradas durante a análise.
  - **`visualizacao_dados_2d.png`**: Gráfico em 2D da projeção dos dados usando PCA.
  - **`visualizacao_dados_3d.png`**: Visualização tridimensional dos dados após PCA.
  - **`distribuicao_resumida.png`**: Histograma dos 12 principais componentes após PCA.
  - **`clusters2Dk=2.png`**, **`clusters2Dk=3.png`**, **`clusters2Dk=4.png`**: Visualização dos clusters gerados em 2D.
  - **`clusters3Dk=2.png`**, **`clusters3Dk=3.png`**: Visualização dos clusters em 3D.

- **`metrics/`**:
  - **`resumo_dataset.txt`**: Resumo inicial do conjunto de dados, detalhando suas características principais, como número de linhas, colunas e tipos de dados.

### **`src/`**
- Contém os scripts principais do projeto:
  
  1. **`k_means.py`**:
     - Implementa o algoritmo K-Means para diferentes valores de K.
     - Calcula métricas como o *Silhouette Score* e visualiza os clusters gerados.
  
  2. **`generate_report.py`**:
     - Gera o relatório final em PDF utilizando a biblioteca `ReportLab`.
     - Inclui introdução, metodologia, resultados, discussões, conclusão e trabalhos futuros.
     
  3. **`exploratory_analysis.py`**:
     - Realiza análise exploratória inicial dos dados.
     - Executa a projeção dos dados em 2D e 3D usando PCA.
     - Gera visualizações gráficas e histogramas dos componentes principais.

---

## Dependências

Certifique-se de instalar as bibliotecas Python necessárias:

```bash
pip install numpy pandas matplotlib scikit-learn reportlab
```

---

## Como Executar

1. **Pré-requisitos**:
   - Certifique-se de que o arquivo `X_train.txt` está localizado na pasta `data/`.

2. **Análise Exploratória**:
   ```bash
   python src/exploratory_analysis.py
   ```

   - Este script gera visualizações em 2D e 3D e cria histogramas dos componentes principais na pasta `docs/graphs/`.

3. **Clustering com K-Means**:
   ```bash
   python src/k_means.py
   ```

   - Gera clusters para diferentes valores de K e salva os resultados gráficos.

4. **Gerar Relatório**:
   ```bash
   python src/generate_report.py
   ```

   - Produz um relatório em PDF na pasta `docs/` com os resultados e análises.

---

## Conclusão e Trabalhos Futuros

### Conclusão:
O projeto demonstrou a viabilidade de utilizar o algoritmo K-Means para agrupar atividades humanas com base em dados de sensores. O uso de PCA foi crucial para simplificar a interpretação dos dados, e métricas como o *Silhouette Score* validaram os agrupamentos obtidos.

### Trabalhos Futuros:
- Experimentar outros algoritmos de clustering, como DBSCAN ou Hierarchical Clustering.
- Incorporar métodos avançados de validação para avaliar os resultados.
- Estender a análise para incluir variáveis categóricas ou externas ao dataset original.

---

## Referências
- Human Activity Recognition Using Smartphones Dataset, UCI Machine Learning Repository: <https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones>.
- Documentação do *ReportLab*: <https://www.reportlab.com/docs/>.
- Documentação do Scikit-Learn: <https://scikit-learn.org/stable/>.

## Autores
#### Guilherme Oliveira
#### Matheus Queiroz