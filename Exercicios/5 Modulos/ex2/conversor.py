def celsius_para_fahrenheit(celsius):
    """Converte temperatura de Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """Converte temperatura de Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    print("Conversor de Temperaturas")
    escolha = input("Digite 'C' para converter de Celsius para Fahrenheit ou 'F' para converter de Fahrenheit para Celsius: ").strip().upper()
    
    if escolha == 'C':
        temp_celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{temp_celsius}°C equivale a {celsius_para_fahrenheit(temp_celsius):.2f}°F")
    elif escolha == 'F':
        temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{temp_fahrenheit}°F equivale a {fahrenheit_para_celsius(temp_fahrenheit):.2f}°C")
    else:
        print("Opção inválida!")