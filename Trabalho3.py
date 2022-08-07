import time as t

def First_fit():
    P = [[0]] #Lista de pacotes com um pacote previamente aberto
    P_aux = []
    inserido = 0
    with open("binpacking-instancias/input/Waescher_TEST0005.txt") as arq: #Ler o arquivo
        for linha in arq.readlines():
            valor = int(linha.strip()) #Pegando os valores de cada linha do arquivo
            P_aux.append(valor)
    arq.close()
    qtd_itens = P_aux.pop(0)
    capacidade = P_aux.pop(0)
    for item in range(qtd_itens): #Para cada item
        inserido = 0
        for pacote in range(len(P)):
            if(inserido == 1): #Caso o item já tenha sido inserido no pacote anterior
                break #Vamos para o próximo item
            elif(P[pacote][0] + P_aux[item] <= capacidade): #Caso o item caiba neste pacote e não tenha sido inserido em nenhum outro pacote
                inserido = 1
                P[pacote][0] += P_aux[item]
                P[pacote].append(P_aux[item]) #Inserimos o item e o marcamos como inserido
            elif(pacote == len(P) - 1): #Caso o item não tenha sido inserido em nenhum pacote e não há mais pacotes para checar
                inserido = 1
                P.append([P_aux[item]])
                P[-1].append(P_aux[item]) #Criamos um novo pacote e inserimos o item nele
    return P

def Next_fit():
    P = [[0]] #Lista de pacotes com um pacote previamente aberto
    P_aux = []
    with open("binpacking-instancias/input/Waescher_TEST0005.txt") as arq: #Ler o arquivo
        for linha in arq.readlines():
            valor = int(linha.strip()) #Pegando os valores de cada linha do arquivo
            P_aux.append(valor)
    arq.close()
    qtd_itens = P_aux.pop(0)
    capacidade = P_aux.pop(0)
    for item in range(qtd_itens): #Para cada item
        if(P[-1][0] + P_aux[item] <= capacidade): #Caso o item caiba no último pacote (ou seja, o pacote mais recentemente aberto)
            P[-1][0] += P_aux[item]
            P[-1].append(P_aux[item]) #Inserimos o item no pacote
        else: #Caso o item não caiba no último pacote aberto
            P.append([P_aux[item]])
            P[-1].append(P_aux[item]) #Abrimos um novo pacote e inserimos o item nele
    return P

def Best_fit():
    P = [[0]] #Lista de pacotes com um pacote previamente aberto
    P_aux = []
    maior_peso = -1
    index = -1
    with open("binpacking-instancias/input/Waescher_TEST0005.txt") as arq: #Ler o arquivo
        for linha in arq.readlines():
            valor = int(linha.strip()) #Pegando os valores de cada linha do arquivo
            P_aux.append(valor)
    arq.close()
    qtd_itens = P_aux.pop(0)
    capacidade = P_aux.pop(0)
    for item in range(qtd_itens): #Para cada item
        maior_peso = -1
        index = -1
        for pacote in range(len(P)):
            if((maior_peso < P[pacote][0]) and (P[pacote][0] + P_aux[item] <= capacidade)): #Caso pacote observado seja o mais pesado de todos os anteriores, e o item atual caiba dentro dele
                maior_peso = P[pacote][0]
                index = pacote #Marcamos o pacote como o melhor pacote
        if(index == -1): #Caso o item não caiba em nenhum pacote
            P.append([P_aux[item]])
            P[-1].append(P_aux[item]) #Abrimos um novo pacote e inserimos o item nele
            continue
        P[index][0] += P_aux[item]
        P[index].append(P_aux[item]) #Caso o item caiba no melhor pacote inserimos o item dentro do pacote
    return P

if __name__ == '__main__':
    print("1 - First-fit\n2 - Next-fit\n3 - Best-fit")
    resposta = input()
    if(resposta == '1'):
        start = t.time()
        resultado = First_fit()
        end = t.time()
        print("Pacotes utilizados: " + str(len(resultado)) + ".")
        print("Tempo transcorrido: " + str(round(start - end, 2)) + " segundos.")
    elif(resposta == '2'):
        start = t.time()
        resultado = Next_fit()
        end = t.time()
        print("Pacotes utilizados: " + str(len(resultado)) + ".")
        print("Tempo transcorrido: " + str(round(start - end, 2)) + " segundos.")
    elif(resposta == '3'):
        start = t.time()
        resultado = Best_fit()
        end = t.time()
        print("Pacotes utilizados: " + str(len(resultado)) + ".")
        print("Tempo transcorrido: " + str(round(start - end, 2)) + " segundos.")
    else:
        print("Número incorreto.")