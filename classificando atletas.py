print("""\nBem-vindo à Confederação Nacional de Natação!
Para saber em qual categoria o atleta se encaixa, informe abaixo o ano de nascimento.
\033[33mPOR FAVOR APENAS NÚMEROS!\033[m""")

from datetime import date

year = date.today().year
nsc = int(input("\nDigite o ano de nascimento: "))
cat = year - nsc

if 0 <= cat <= 9:  # MIRIM; (0 <=) tirando a possibilidade da data de uma pessoa que não nasceu ainda
    print(f"\nO atleta tem apenas \033[1m{cat} ano(s)\033[m. Sua categoria é a \033[1;36mMIRIM!\033[m\n")
elif 9 < cat <= 14:  # INFANTIL
    print(f"\nO atleta ainda é jovem, apenas \033[1m{cat} ano(s)\033[m. Sua categoria é a \033[1;32mINFANTIL!\033[m\n")
elif 14 < cat <= 19:  # JUNIOR
    print(f"\nO atleta já é um rapaz com \033[1m{cat} ano(s)\033[m. Sua categoria é a \033[1;34mJUNIOR!\033[m\n")
elif 19 < cat <= 25:  # SÊNIOR
    print(f"\nO atleta já é um adulto, tem \033[1m{cat} ano(s)\033[m. Sua categoria é a \033[1;33mSÊNIOR!\033[m\n")
elif 25 < cat <= 130:  # MASTER; até 130 que é a idade máxima segundo estudos suíços
    print(f"\nO atleta é experiente, tem \033[1m{cat} ano(s)\033[m. Sua categoria é a \033[1;35mMASTER!\033[m\n")
else:  # tira a possibilidade de classificar uma pessoa morta
    print("\n\033[31mInforme a data de nascimento de uma pessoa viva.\033[m\n")
