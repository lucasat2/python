from datetime import datetime, date

# 1. Mostrar a data e hora atual
agora = datetime.now()
print("Data e hora atual:", agora.strftime("%d/%m/%Y %H:%M:%S"))

# 2. Criar uma data específica (seu aniversário)
aniversario = date(1990, 3, 1)  # Altere para a sua data de nascimento
print("Seu aniversário:", aniversario.strftime("%d/%m/%Y"))

# 3. Calcular quantos dias faltam para o Natal deste ano
hoje = date.today()
natal = date(hoje.year, 12, 25)
if hoje > natal:
    natal = date(hoje.year + 1, 12, 25)

dias_para_natal = (natal - hoje).days
print(f"Faltam {dias_para_natal} dias para o Natal!")
