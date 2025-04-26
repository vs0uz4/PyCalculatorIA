def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida"
    return x / y

def clear_screen():
    print("\n" * 50)  # Simula limpeza da tela

def show_menu():
    print("=" * 50)
    print("CALCULADORA SIMPLES".center(50))
    print("=" * 50)
    print("\nOPERAÇÕES DISPONÍVEIS:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("q - Sair")
    print("=" * 50)

def calculator():
    while True:
        clear_screen()
        show_menu()
        
        try:
            # Escolha da operação
            choice = input("\nDigite o número da operação desejada: ").lower()
            
            if choice == 'q':
                print("\nObrigado por usar a calculadora!")
                break
                
            if choice not in ['1', '2', '3', '4']:
                input("\nOpção inválida! Pressione Enter para tentar novamente...")
                continue
                
            # Entrada dos números
            print("\nDigite os números para a operação:")
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))
            
            # Execução da operação escolhida
            if choice == '1':
                print(f"\nResultado: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"\nResultado: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"\nResultado: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"\nResultado: {num1} / {num2} = {result}")
            
            input("\nPressione Enter para continuar...")
                
        except ValueError:
            input("\nErro: Por favor, digite números válidos. Pressione Enter para continuar...")
        except Exception as e:
            input(f"\nOcorreu um erro: {e}\nPressione Enter para continuar...")

if __name__ == "__main__":
    calculator() 