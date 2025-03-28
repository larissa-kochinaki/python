horario = []
def programa():
    num = input("Digite as horas")
    recebido = num.split(':')
    horasec = int(recebido[0])*3600
    minsec = int(recebido[1])*60
    sec = int(recebido[2])
    total = horasec + minsec+ sec
    print(f'{total}')
programa()