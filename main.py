def exibir_menu():
    print("=" * 45)
    print("          CALCULADORA EM PYTHON")
    print("=" * 45)
    print("   1 - Adição")
    print("   2 - Subtração")
    print("   3 - Multiplicação")
    print("   4 - Divisão")
    print("   0 - Sair")
    print()

def calculadora():
    exibir_menu()
    
    while True:
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '0':
            print("Programa encerrado.")
            break
            
        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Primeiro número: "))
                num2 = float(input("Segundo número: "))
                
                # Converte para int se o número for inteiro para ter uma saída limpa (ex: 12 em vez de 12.0)
                num1 = int(num1) if num1.is_integer() else num1
                num2 = int(num2) if num2.is_integer() else num2
                
                print()
                if opcao == '1':
                    res = num1 + num2
                    res = int(res) if isinstance(res, float) and res.is_integer() else res
                    print(f"Resultado: {num1} + {num2} = {res}")
                elif opcao == '2':
                    res = num1 - num2
                    res = int(res) if isinstance(res, float) and res.is_integer() else res
                    print(f"Resultado: {num1} - {num2} = {res}")
                elif opcao == '3':
                    res = num1 * num2
                    res = int(res) if isinstance(res, float) and res.is_integer() else res
                    print(f"Resultado: {num1} * {num2} = {res}")
                elif opcao == '4':
                    if num2 == 0:
                        print("Erro: divisão por zero não é permitida.")
                    else:
                        res = num1 / num2
                        res = int(res) if isinstance(res, float) and res.is_integer() else res
                        print(f"Resultado: {num1} / {num2} = {res}")
            except ValueError:
                print("Erro: Entrada inválida. Digite apenas números.")
        else:
            print("Opção inválida! Tente novamente.")
            
        print()
        continuar = input("Outro cálculo? (s/n): ").strip().lower()
        print()
        
        if continuar != 's':
            print("Programa encerrado.")
            break
        else:
            print("--------- MENU PRINCIPAL ---------")

if __name__ == "__main__":
    calculadora()