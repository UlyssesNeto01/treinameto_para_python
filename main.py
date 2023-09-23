# pergunte ao usuario o seu nome e a sua idade e a sua cidade e se ele colocar qualquer coisa que não seja a letras do alfabeto
# em seu nome ou na cidade, deve retona erro e que ele coloque da forma certa e isso também vale para idade só vale numeros
# validos para idade, as inicias do nome deve esta em maiusculo mesmo que o usuario coloque em minusculo tanto para nome quanto
# para o nome da cidade, deve colocar em maiuculo. e mostre uma mensagem com as informações dele e coloque as informações para ele ver
# se ele não gostar ou errou, mostre uma alternativa no final onde ele vai dizer se esta tudo ok se estiver ele diz sim e se não





while True:
    n = input("Coloque seu nome completo: ")
    nome = n.replace(" ", "")
    if nome.isalpha():
        nomeTitle = n.title()

        while True:
            c = input("Coloque o nome de sua cidade: ")
            cidade = c.replace(" ", "")
            if cidade.isalpha():
                cidade_separada = c.split()
                cidade_list = []

                for CidadeNova in cidade_separada:
                    CidadeReformada = CidadeNova.capitalize()
                    cidade_list.append(CidadeReformada)

                Nome_cidade = " ".join(cidade_list)

                while True:
                    try:
                        i = int(input("Coloque sua idade: "))
                        print(f"O seu nome é: {nomeTitle}\nO nome da sua cidade: {Nome_cidade}\nSua idade é: {i}")

                        Yes = int(input(
                            "Seus dados estão certos? Digite 1 para certo e 0 para errado e alterar seus dados: "))
                        if Yes == 1:
                            break  # Saia do loop interno se os dados estiverem corretos
                        elif Yes == 0:
                            break  # Saia do loop interno se o usuário desejar alterar os dados
                        else:
                            print("Coloque os valores 1 ou 0")
                    except ValueError:
                        print("Você digitou errado o dígito, coloque um número válido")

                # Se o usuário escolher alterar os dados, volte ao início da pergunta do nome
                if Yes == 0:
                    break

                # Se os dados estiverem corretos, saia do loop interno
                if Yes == 1:
                    break

            else:
                print("Nome da cidade errado, só letras do alfabeto")

        # Se o usuário escolher alterar os dados, volte ao início da pergunta do nome
        if Yes == 0:
            continue

        # Se os dados estiverem corretos, saia do loop externo
        if Yes == 1:
            break

    else:
        print("Nome errado, coloque só letras do alfabeto")

print("teste deu certo")
print("novo teste")