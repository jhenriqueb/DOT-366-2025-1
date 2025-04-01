def pesoIdeal(h, s):
    if s == 1:
        return(72.7 * h) - 58 
    if s == 2:
        return(62.1 * h) - 44.7



while True:
    try:
        sexo = int(input('Digite seu sexo(MASCULINO = 1 FEMININO = 2): '))
        if sexo == 1 or sexo == 2:
            break                    
        else:
            print('Sexo invalido, Digite novamente seu sexo(MASCULINO = 1 FEMININO = 2):')
    except:
        print('Valor inválido, Digite novamente: ')
        

while True:
    try:
        altura = float(input('Digite sua altura(X.XX): '))
        if altura > 1 and  altura < 3:
            break
        else:
            print('Tente novamente. Digite sua altura entre 1 a 3 metros: ')
    except:
       print('Valor inválido, digite novamente: ') 
       
       
resultado = pesoIdeal(altura, sexo)
print(f'Seu peso ideal de acordo com a sua altura é {resultado:.2f}')