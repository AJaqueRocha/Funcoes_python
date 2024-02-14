# Função soma 3 argumentos
def tres_argumentos(num1, num2, num3):
    soma = num1 + num2 + num3
    return soma

resultado = tres_argumentos(1, 2, 3)
print(f'A soma dos três argumentos é {resultado}')


# Função fornece o reverso de um número
def numero_reverso(num):
    reverso = str(num)[::-1]
    return int(reverso)

num = 527
resultado = numero_reverso(num)
print(f'O reverso do número 527 é {resultado}')


# Pergunta converter temperatura
def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def converte_temperatura():
    opcao = input("Digite 'Celsius' se deseja converter a temperatura para Celsius ou digite 'Fahrenheit' se deseja converter a temperatura para fahrenheit: ")

    if opcao == "Celsius":
        celsius = float(input("Qual é a temperatura em graus Celsius? "))
        fahrenheit = celsius_fahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é {fahrenheit}")

    elif opcao == "Fahrenheit":
        fahrenheit = float(input("Qual é a temperatura Fahrenheit? "))
        celsius = fahrenheit_celsius(fahrenheit)
        print(f"A temperatura em Celsius é {celsius}")

    else:
        print("Opção inválida. Digite 'Celsius' se deseja converter a temperatura para Celsius ou digite 'Fahrenheit' se deseja converter a temperatura para fahrenheit.")
        return converte_temperatura()

converte_temperatura()


# Ler quanto dinheiro o usuário tem na carteira
dic_convert = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suiço": 0.42,
    "Euro": 5.36,
    "Libra esterlina": 6.21
}

valor_reais = float(input("Qual valor você possui em sua carteira (em Reais)? "))

for moeda, taxa in dic_convert.items():
    valor_moeda = valor_reais / taxa
    print(f"Com R$ {valor_reais:.2f} você pode comprar {valor_moeda:.2f} de {moeda}.")


# Contando vogais
def contar_vogais(frase):
    vogais = 'aeiouAEIOU'
    total_vogais = 0
    for letra in frase:
        if letra in vogais:
            total_vogais += 1
    return total_vogais

frase = input("Digite uma frase: ")
resultado = contar_vogais(frase)
print("O total de vogais na frase informada é", resultado)


# Jogo da forca
import random

palavras = ["jogo", "programacao", "desenvolvedora", "resiliencia", "python"]

def jogo_forca():
    palavra_secreta = random.choice(palavras)
    espacos = ["_"] * len(palavra_secreta)
    tentativas = 6
    letras_erradas = []
    dica = False
    
    while tentativas > 0:
        print("Palavra secreta:", " ".join(espacos))
        print("Tentativas restantes:", tentativas)
        print("Letras erradas:", ", ".join(letras_erradas))
        
        if tentativas == 3 and not dica:
            resposta = input("Quer uma dica? (sim/não): ")
            if resposta.lower() == "sim":
                dica = True
                print("Dica: A palavra tem", len(palavra_secreta), "letras.")
        
        letra = input("Digite uma letra: ")
        
        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    espacos[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1
        
        if "_" not in espacos:
            print("Parabéns! Você adivinhou a palavra secreta:", palavra_secreta)
            break
    
    if tentativas == 0:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)

jogo_forca()