import numeroromano  # Importa o módulo numeroromano

if __name__ == "__main__":
    # Solicita um número romano ao usuário
    numero_romano = input("Digite um número romano: ").strip().upper()
    try:
        resultado = numeroromano.converte(numero_romano)
        print(f"O número romano {numero_romano} é equivalente a {resultado} em números inteiros.")
    except ValueError as e:
        print(f"Erro: {e}")
