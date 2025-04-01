def somarMedia(n1, n2):
    if 6  < (n1+n2) / 2:
        return 'PARABÉNS'
    else:
        return 'REPROVADO' 




while True:
    try:
        nota1 = float(input('Digite a 1° nota: '))        
        nota2 = float(input('Digite a 2° nota: '))    
        break
    except ValueError:
        print('Erro!!!, Digite novamente')
        
        
        
resultado = somarMedia(nota1, nota2)
print(resultado)

        