# Engenharia de software UMC 1º semestre - Software Básico
# Otávio Vinícius e Igor Delfino

from colorama import init, Fore
import os

init(autoreset=True)

linha = "=" * 50
titulo_programa = "CALCULADORA DE HORAS"


def validar_horas(horas: float) -> bool:
    if horas < 0:
        return False
    return True


def validar_valor_hora(valor_hora: float) -> bool:
    if valor_hora <= 0:
        return False
    return True


def validar_percentual(valor: float) -> bool:
    if valor < 0:
        return False
    return True

def validar_cpf(cpf: str) -> bool:
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    return True

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def print_header():
    print("\n" + linha)
    print(titulo_programa.center(50))
    print(linha + "\n")

while True:
    try:
        # Limpando o terminal e imprimindo o cabeçalho
        clear_terminal()
        print_header()

        # Dicionário para armazenar os dados do trabalhador
        dados = {}

        # Identificação do trabalhador
        dados["nome"] = input("Nome do trabalhador: ")
        
        while True:
            cpf = input("CPF: ")
            if validar_cpf(cpf):
                dados["cpf"] = cpf
                break
            else:
                print(f"{Fore.RED}CPF inválido.")

        dados["cargo"] = input("Cargo: ")

        # Limpando o terminal para a próxima etapa
        clear_terminal()
        print_header()

        # Horas normais
        while True:
            try:
                horas_normais = float(input(f"{Fore.BLUE}Horas normais trabalhadas: "))
                if not validar_horas(horas_normais):
                    raise ValueError
                dados["horas_normais"] = horas_normais
                break
            except:
                print(f"{Fore.RED}Valor inválido.")

        # Horas extras
        while True:
            try:
                horas_extras = float(input(f"{Fore.BLUE}Horas extras: "))
                if not validar_horas(horas_extras):
                    raise ValueError
                dados["horas_extras"] = horas_extras
                break
            except:
                print(f"{Fore.RED}Valor inválido.")

        # Valor da hora
        while True:
            try:
                valor_hora = float(input(f"{Fore.BLUE}Valor da hora (R$): "))
                if not validar_valor_hora(valor_hora):
                    raise ValueError
                dados["valor_hora"] = valor_hora
                break
            except:
                print(f"{Fore.RED}Valor inválido.")

        # Percentual de adicional de hora extra
        while True:
            try:
                adicional_hex = float(input(f"{Fore.BLUE}Adicional de hora extra (%): "))
                if not validar_percentual(adicional_hex):
                    raise ValueError
                dados["adicional_hex"] = adicional_hex
                break
            except:
                print(f"{Fore.RED}Valor inválido.")

        # Percentual de desconto
        while True:
            try:
                desconto = float(input(f"{Fore.BLUE}Percentual de descontos (%): "))
                if not validar_percentual(desconto):
                    raise ValueError
                dados["desconto"] = desconto
                break
            except:
                print(f"{Fore.RED}Valor inválido.")

        # ========================
        # CÁLCULOS
        # ========================

        valor_horas_normais = dados["horas_normais"] * dados["valor_hora"]

        valor_hora_extra = dados["valor_hora"] * (1 + dados["adicional_hex"] / 100)

        valor_horas_extras = dados["horas_extras"] * valor_hora_extra

        salario_bruto = valor_horas_normais + valor_horas_extras

        valor_desconto = salario_bruto * (dados["desconto"] / 100)

        salario_liquido = salario_bruto - valor_desconto

        # ========================
        # RECIBO
        # ========================

        print("\n" + linha)
        print("RECIBO DE PAGAMENTO".center(50))
        print(linha)

        print(f"Nome : {dados['nome']}")
        print(f"CPF  : {dados['cpf']}")
        print(f"Cargo: {dados['cargo']}")

        print("\n" + linha)

        print(f"Horas Normais : {dados['horas_normais']}")
        print(f"{Fore.BLUE}Horas Extras  : {dados['horas_extras']}")
        print(f"{Fore.GREEN} Valor Hora    : R$ {dados['valor_hora']:.2f}")
        print(f"{Fore.GREEN} Adicional HEX : {dados['adicional_hex']}%")

        print("\n" + linha)

        print(f"Valor Horas Normais : R$ {valor_horas_normais:.2f}")
        print(f"{Fore.BLUE}Valor Horas Extras  : R$ {valor_horas_extras:.2f}")

        print(f"\n{Fore.GREEN}Salário Bruto : R$ {salario_bruto:.2f}")
        print(f"{Fore.RED}Descontos ({dados['desconto']:.0f}%) : R$ {valor_desconto:.2f}")

        print(f"\n{Fore.GREEN}SALÁRIO LÍQUIDO: R$ {salario_liquido:.2f}")

        print(linha)

        input("\nPressione ENTER para calcular outro recibo...")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Programa encerrado pelo usuário.")
        break