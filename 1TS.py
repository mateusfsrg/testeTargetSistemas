
def fibonacci(n):
    a,b = 0,1

    if n==0 or n==1:
        return True

    while b<n:
        a,b = b, a + b

    return b==n

numero = int(input('Qual número devo verificar?'))

if fibonacci(numero):
    print(f'O número {numero} pertence à sequência de Fibonacci.')
else:
    print(f'o número {numero} NÃO pertence à sequência de Fibonacci.')

