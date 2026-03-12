# Engenharia de software UMC 1º semestre - Software Básico
# Otávio Vinícius e Igor Delfino
from colorama import init, Fore, Back;
import os;

# Reseta as formatações de cores no terminal de volta ao padrão automaticamete
init(autoreset=True)

linha = "=" * 50;
titulo_programa = "CALCULADORA DE HORAS";

def validar_horas(horas: int) -> bool:
    '''
    Recebe o valor em horas e verifica se é um valor acima de zero e inteiro.

    Args:
        horas (int): Horas a serem validadas
    
    Returns:
        valid (bool): Se o valor é válido 
    '''

    if (horas <= 0 or type(horas) != int):
        return False
    return True

def validar_valor_hora(valor_hora: float) -> bool:
    '''
    Recebe o valor em reais de cada hora e verifica se é um valor positivo e inteiro.

    Args:
        valor_hora (float): Horas a serem validadas
    
    Returns:
        valid (bool): Se o valor é válido 
    '''

    if (valor_hora <= 0 or type(valor_hora) != float):
        return False
    return True

def clear_terminal():
    os.system("cls");

while True:
    # Cabeçalho da aplicação
    print("\n\n" + linha);
    print(titulo_programa);
    print(linha + "\n\n");

    dados = {}

    # Coleta de dados de horas
    while True:
        horas_totais = input(f"{Fore.BLUE} Insira a quantidade de horas \n");
        if (validar_horas(horas_totais) == False):
            print(f"{Fore.RED} Por favor, insira uma quantidade válida de horas. \n\n");
            continue
        else:
            dados["horas_totais"] = float(horas_totais)
            break;

    # Coleta de dados de horas extras
    while True:
        horas_extras = input(f"{Fore.BLUE} Insira a quantidade de horas extras \n");
        if (validar_horas(horas_totais) == False):
            print(f"{Fore.RED} Por favor, insira uma quantidade válida de horas. \n\n");
            continue
        else:
            dados["horas_extras"] = float(horas_extras)
            break;

    # Coleta de dados de horas extras
    while True:
        horas_extras = input(f"{Fore.BLUE} Insira a quantidade de horas extras \n");
        if (validar_horas(horas_totais) == False):
            print(f"{Fore.RED} Por favor, insira uma quantidade válida de horas. \n\n");
            continue
        else:
            dados["horas_extras"] = float(horas_extras)
            break;

