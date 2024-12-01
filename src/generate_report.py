from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

# Criando o arquivo PDF
pdf_file = "docs/relatorio_projeto.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Criando o estilo do relatório
styles = getSampleStyleSheet()

# Definindo o conteúdo do relatório
content = []

# Título do relatório
title = Paragraph("Relatório do Projeto de Análise de Atividades Humanas", styles['Title'])
content.append(title)
content.append(Spacer(1, 12))

# Subtítulo e introdução
subtitle = Paragraph("Introdução", styles['Heading2'])
content.append(subtitle)
content.append(Spacer(1, 6))

# Corpo do texto
body_text = """
O projeto visa desenvolver um modelo de clustering para a análise de um conjunto de dados de atividades humanas coletados com sensores de smartphones. O dataset "Human Activity Recognition Using Smartphones", disponível no repositório da UCI Machine Learning, contém medições de 561 variáveis extraídas de acelerômetros e giroscópios de 30 voluntários em atividades cotidianas como caminhar, subir escadas e ficar em pé. Este estudo busca identificar padrões de comportamento e agrupar as atividades usando o algoritmo de K-means, destacando a importância da escolha do número de clusters, a normalização dos dados e a análise dos resultados.

O uso do K-means é justificado por sua capacidade de segmentar grandes volumes de dados de forma eficiente e permitir a exploração visual e quantitativa dos clusters formados. A aplicação de técnicas como PCA para redução de dimensionalidade facilita a visualização e a interpretação dos grupos, enquanto a avaliação de métricas como o silhouette score e a inércia proporciona uma análise crítica da qualidade dos agrupamentos.
"""
content.append(Paragraph(body_text, styles['BodyText']))

#Caminho para o arquivo de resumo
summary_file = 'docs/metrics/resumo_dataset.txt'
normal_style = styles['Normal']
title_style = styles['Title']
heading_style = styles['Heading2']

# Título do relatório
title = Paragraph("Metodologia", styles['Title'])
content.append(title)
content.append(Spacer(1, 12))

# 1. Análise Inicial do Dataset
subtitle = Paragraph("1. Análise Inicial do Dataset", styles['Heading2'])
content.append(subtitle)
content.append(Spacer(1, 6))

body_text = (
    "A análise inicial do dataset revelou que os dados possuem o tipo float64, o que é comum para medições de sensores de alta precisão. "
    "O dataset contém um total de 7352 linhas e 561 colunas, representando um grande número de observações e variáveis. Importante destacar que, "
    "conforme descrito no README do dataset, os dados já estavam normalizados desde o início, o que assegura que todas as variáveis contribuam de forma equilibrada para as análises subsequentes."
)
content.append(Paragraph(body_text, styles['BodyText']))
content.append(Spacer(1, 12))

# 2. Visualização 2D dos Dados
subtitle = Paragraph("2. Visualização 2D dos Dados", styles['Heading2'])
content.append(subtitle)
content.append(Spacer(1, 6))

body_text = (
    "A visualização em 2D foi realizada para examinar a distribuição dos dados em um espaço bidimensional. "
    "A projeção dos dados após a aplicação da técnica de PCA revelou dois conjuntos distintos, evidenciando a separação de grupos dentro do dataset. "
    "Essa visualização fornece uma visão clara da estrutura dos dados, permitindo a identificação de possíveis agrupamentos e padrões que poderão ser explorados pelo algoritmo K-means."
)
content.append(Paragraph(body_text, styles['BodyText']))
content.append(Spacer(1, 12))
content.append(Image("docs/graphs/visualizacao_dados_2d.png", width=400, height=300))

# 3. Visualização 3D dos Dados
subtitle = Paragraph("3. Visualização 3D dos Dados", styles['Heading2'])
content.append(subtitle)
content.append(Spacer(1, 6))

body_text = (
    "A análise em 3D, também baseada na técnica de PCA, foi usada para examinar os dados em três dimensões, revelando três agrupamentos claros. "
    "Essa projeção tridimensional proporciona uma melhor compreensão da separação dos grupos e da distribuição dos dados, mostrando que há uma estrutura que justifica a aplicação do algoritmo K-means para identificação de clusters. "
    "A visualização em 3D ajuda a perceber a complexidade dos dados e a interpretar as relações entre as variáveis de forma mais detalhada."
)
content.append(Paragraph(body_text, styles['BodyText']))
content.append(Spacer(1, 12))
content.append(Image("docs/graphs/visualizacao_dados_3d.png", width=400, height=300))

# 4. Redução de Dimensionalidade com PCA e Distribuição dos Componentes
subtitle = Paragraph("4. Redução de Dimensionalidade com PCA e Distribuição dos Componentes", styles['Heading2'])
content.append(subtitle)
content.append(Spacer(1, 6))

body_text = (
    "A técnica de PCA foi aplicada para reduzir a dimensionalidade dos dados para 12 componentes principais. "
    "Essa redução tornou a visualização e a interpretação dos dados mais gerenciáveis e revelou insights interessantes. "
    "Para cada uma das 12 componentes principais, foi gerado um histograma para examinar a distribuição dos dados."
)
content.append(Paragraph(body_text, styles['BodyText']))
content.append(Spacer(1, 12))

content.append(Image("docs/graphs/distribuicao_resumida.png", width=400, height=300))

body_text = (
    "Os histogramas mostraram que, entre os 12 componentes, pelo menos 9 seguem uma distribuição normal, indicando uma simetria nos dados que pode facilitar a modelagem. "
    "No entanto, 3 componentes apresentaram distribuições mais irregulares, sugerindo que esses componentes podem ter características diferentes ou serem mais influenciados por ruído nos dados. "
    "Essas observações são cruciais para a análise de clusters e podem impactar a interpretação e a eficácia do algoritmo K-means na identificação de agrupamentos."
)
content.append(Paragraph(body_text, styles['BodyText']))

# Construindo o PDF
document.build(content)

print(f"Relatório criado com sucesso: {pdf_file}")


