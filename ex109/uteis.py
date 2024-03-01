def aumentar(num):
    return(num+1)
def diminuir(num):
    return(num-1)
def dobro(num):
    return(num*2)
def metade(num):
    return(num/2)
def linha():
    print('*-' * 25)
def moeda(num, show=True):
    if show:
        return(f'R${num:.2f}')
    else:
        return(num)