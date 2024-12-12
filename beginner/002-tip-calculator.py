'''
If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
Write your code below this line 👇
'''

msg_greeting = """
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
🤑🤑🤑 Bem vindo ao calculador de gorjetas! 🤑🤑🤑

Use o ponto (.) para separar os centavos. (Exemplo: 150.55)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

"""

msg_ask_total = "Qual o total da conta?💸💰 R$\n"
msg_ask_n_people = "Quantas pessoas vão dividir a conta?👨‍👩‍👧‍👦\n"
msg_ask_tip = "Qual a porcentagem de gorjeta você quer dar?🤔\n"

def tip_calculator():
    print(msg_greeting)
    total = float(input(msg_ask_total))
    n_people = int(input(msg_ask_n_people))
    tip = int(input(msg_ask_tip))
    total_with_tip = total * (1 + tip/100)
    each_person_pays = "{:.2f}".format(round(total_with_tip / n_people, 2))
    print(f"Cada pessoa deve pagar R${each_person_pays}")

if __name__ == "__main__":
    tip_calculator()