continuar = True

while continuar:
    
    numero = int(input('Qual Tabuada? '))
    
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")
    
    continuar = input('Deseja continuar? (s/n)')
    continuar = True if continuar == 's' else False