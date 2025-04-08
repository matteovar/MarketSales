from .Performance_by_Category import show_hello
from .General_Informations import show_dashboard
from .Impact_of_Promotions import show_dic
from .Costumer_Profile import show_cli

# Dicionário com todas as páginas disponíveis
pages = {
    "General Informations": show_dashboard,
    "Performance_by_Category.py": show_hello,
    "Impact of Promotions": show_dic,
    "Costumer_Profile.py": show_cli
}
