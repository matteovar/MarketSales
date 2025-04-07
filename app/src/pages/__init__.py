from .Desempenho_por_Categoria import show_hello
from .Visao_Geral import show_dashboard
from .Impacto_de_Promoções import show_dic

# Dicionário com todas as páginas disponíveis
pages = {
    "Visao Geral": show_dashboard,
    "Desempenho_por_Categoria.py": show_hello,
    "Impacto de Promoções": show_dic,
}
