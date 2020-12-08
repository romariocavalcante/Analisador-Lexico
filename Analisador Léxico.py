import json

token = []
identificacao = []
tamanho = []
posicao = []
tokens = []
tabela_s = []
cont_ind = 0

def carregaArq():
    arq = open('codigo.txt', 'r')
    dados =arq.read()
    arq.close()
    return dados
            
def salvar(dado):
    js= json.dumps(dado)
    fp = open('saida.json', 'w')
    fp.write(js)
    fp.close() 

dados = carregaArq()
dados= dados.split(' ')
ultimo=dados[len(dados) -1]
dados.remove(dados[len(dados) -1])
dados.append(ultimo[:len(ultimo) -1])
dados.append(ultimo[len(ultimo) -1])

def isOperador(dado):
    operador = ['<','=','+']
    return dado in operador

def isReservada(dado):
    reservado = ['while','do']
    return dado in reservado
  
def isTerminador(dados):
    if (dados[len(dados)-1] == ';'):
        return True

def isIdentificador(dado):
    identificador = ['i','j']
    return dado in identificador

def Posicao(dado, ocorrencia):
    dados = carregaArq()
    encontrou=0
    posicao=dados.index(dado)
    while ocorrencia>1:
        dados[posicao]='o'
        posicao=dados.index(dado)
        ocorrencia -=1
    return '(0,'+str(posicao)+')'
            

tokens = []
indice= []
simbol= []
cont= 0

for i in dados:
    elementos={}
    ocoReservada=0

    if isReservada(i):
        ocoReservada+=1
        elementos.update({'token':i})
        elementos.update({'identificacao':'palavra reservada'})
        elementos.update({'tamanho':len(i)})
        elementos.update({'posicao':Posicao(i,ocoReservada)})
        tokens.append(elementos)  

    elif isIdentificador(i):
        if i not in simbol:
            cont+=1
            indice.append(cont)
            simbol.append(i)

        if i in simbol:
            elementos.update({'token':i})
            elementos.update({'identificacao':['identificador',simbol.index(i)+1]})
            elementos.update({'tamanho':len(i)})
            elementos.update({'posicao':Posicao(i,ocoReservada)})
        tokens.append(elementos)

    elif isOperador(i):
        elementos.update({'token':i})
        elementos.update({'identificacao':'operador'})
        elementos.update({'tamanho':len(i)})
        elementos.update({'posicao':Posicao(i,ocoReservada)})
        tokens.append(elementos)


    elif i.isdigit():
        if i not in simbol:
            cont+=1
            indice.append(cont)
            simbol.append(i)

        if i in simbol:
            elementos.update({'token':i})
            elementos.update({'identificacao':['constante',simbol.index(i)+1]})
            elementos.update({'tamanho':len(i)})
            elementos.update({'posicao':Posicao(i,ocoReservada)})
        tokens.append(elementos)

salvar(tokens)
simbolos = {}
simbolos.update({"indices":indice,"simbolos":simbol})