import time
def bob(quantidade, texto):
   
    for i in range(1, quantidade + 1):
        
        print(f"{texto} {i}")
        
        
while True:
    
    escolha = input("Digite 1 para BOB ESPONJA, 2 para GARY, 3 para LULA MOLUSCO, ou 0 para sair: ")

    if escolha == '0':
        print("Encerrando o programa. Adeus!")
        break
    elif escolha in ['1', '2', '3']:
        try:
            n = int(input("Digite o número de repetições (N): "))
            if n <= 0:
                print("Por favor, insira um número positivo de 1 a 1000000.")
                continue
            if n >= 1000000000000000000000000:
                print("números muito grandes podem travar o computador")
                continue
            start = time.time()
            if escolha == '1':
                bob(n, "BOB ESPONJA")
                print('{} segundos'.format(time.time() - start))
            elif escolha == '2':
                bob(n, "GARY")
                print('{} segundos'.format(time.time() - start))
            elif escolha == '3':
                bob(n, "LULA MOLUSCO")
                print('{} segundos'.format(time.time() - start))
                
        except ValueError:
            print("Por favor, insira um número válido.")
        except MemoryError:
            print("memória insuficiente")
    else:
        print("Escolha inválida. Tente novamente.")


