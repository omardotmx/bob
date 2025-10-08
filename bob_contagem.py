def escrever_texto(quantidade, texto):
    for _ in range(quantidade):
        print(texto)

while True:
    escolha = input("Digite 1 para BOB ESPONJA, 2 para GARY, 3 para LULA MOLUSCO, ou 0 para sair: ")

    if escolha == '0':
        print("Encerrando o programa. Adeus!")
        break
    elif escolha in ['1', '2', '3']:
        try:
            n = int(input("Digite o número de repetições (N): "))
            if n <= 0:
                print("Por favor, insira um número positivo.")
                continue
            if escolha == '1':
                escrever_texto(n, "BOB ESPONJA")
            elif escolha == '2':
                escrever_texto(n, "GARY")
            elif escolha == '3':
                escrever_texto(n, "LULA MOLUSCO")
        except ValueError:
            print("Por favor, insira um número válido.")
    else:
        print("Escolha inválida. Tente novamente.")
