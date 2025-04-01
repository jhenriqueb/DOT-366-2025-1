def poligonos():
    
    while True:
        try:
            nl = int(input('Digite a quantidade de lados da figura(TRIANGULO(3) QUADRADO(4) PENTAGONO(5)): '))
            if nl  >= 3 and nl <= 5:
                break
            else:
                print('Tente novamente')
        except:
            print('Valor inválido, digite novamente: ') 
            
    while True:
        try:
            nl = float(input('Digite em cm o lado do poligono: '))
            break
        except:
            print('Valor inválido, digite novamente: ') 
            