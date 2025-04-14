def inserir_letras_alfabeto():
    alfabeto = []
    print("Digite 10 letras do alfabeto:")
    for i in range(10):
        while True:
            try:
                letra = input(f"Digite a {i+1}ª letra: ").strip().upper()

                if len(letra) != 1:
                    print("Erro! Digite apenas uma letra.")
                    continue

                if not letra.isalpha():
                    print("Erro! Digite apenas letras do alfabeto.")
                    continue

                alfabeto.append(letra)
                break

            except Exception:
                print("Erro! Digite apenas letras do alfabeto.")
    return alfabeto

def contar_letra(alfabeto, letra_busca):
    contador = 0
    for letra in alfabeto:
        if letra == letra_busca:
            contador += 1
    return contador

alfabeto = inserir_letras_alfabeto()
contador_A = contar_letra(alfabeto, 'A')

print("\nLista de letras digitadas:", alfabeto)
print(f"A letra 'A' aparece {contador_A} vezes na lista.")