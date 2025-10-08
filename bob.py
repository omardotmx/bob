def escrever_texto(quantidade, texto):
    for _ in range(quantidade):
        print(texto)

while True:
    escolha = input("Digite 1 para BOB ESPONJA, 2 para GARY, 3 para LULA MOLUSCO, ou 0 para sair: ")

    if escolha == '0':
        print("Encerrando o programa. Adeus!")
        break
    elif escolha == '1':
        escrever_texto(10, "BOB ESPONJA")
    elif escolha == '2':
        escrever_texto(20, "GARY")
    elif escolha == '3':
        escrever_texto(1, "LULA MOLUSCO")
    else:
        print("Escolha inválida. Tente novamente.")
