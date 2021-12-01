from random import randint
from random import seed

numero = None
amigos = None
grelha = None
jogadas = None
pontos = None
semente = None

def inicializa_semente(semente_a_usar):

    global semente
    if semente_a_usar == None:
        semente_a_usar = randint(1, 1000)
    seed(semente_a_usar)
    semente = semente_a_usar

def get_numero(linha):
    
    numero = linha[7:-1]
    print('numero ='+str(numero))
    return numero

def get_amigos(linha):
    
    amigos = linha[7:-1]
    print('amigos ='+str(amigos))

    virgulas = 0
    for letra in amigos:
        if letra==',':
            virgulas = virgulas + 1
            
    numero_amigos = virgulas + 1
    if numero_amigos < 2 or numero_amigos > 5:
        print('numero de amigos INVALIDO!!! ('+str(numero_amigos)+')')
        
    return amigos

def le_identificacao():

    global numero
    global amigos
    
    nome_ficheiro = 'identificação.txt'
    modo = 'r'
    ficheiro = open(nome_ficheiro, modo)

    linha1 = ficheiro.readline()
    linha2 = ficheiro.readline()
    ficheiro.close()

    numero = get_numero(linha1)
    amigos = get_amigos(linha2)

def regista_grelha_inicial(g11, g12, g13, g14,
                           g21, g22, g23, g24,
                           g31, g32, g33, g34,
                           g41, g42, g43, g44):

    global grelha
    global jogadas
    global pontos
    
    grelha = [[g11, g12, g13, g14],
              [g21, g22, g23, g24],
              [g31, g32, g33, g34],
              [g41, g42, g43, g44]]
    jogadas = ''
    pontos = None

def regista_jogada(letra):

    global jogadas
    jogadas = jogadas + letra

def regista_pontos(p):

    global pontos
    pontos = p

def regista_ranking():
    import urllib.request
    import json
    mensagem = None
    try:
        request_data = {'numero':  numero,'amigos':  amigos,'jogadas': jogadas,'pontos':  pontos,'semente': semente}
        json_request_data = json.dumps(request_data)
        url ='http://beleza2.ddns.net/api/submit_2048'
        
        req = urllib.request.Request(
            url = url,
            data = bytes(json_request_data.encode('utf-8')),
            method ='POST')
        
        req.add_header('Content-type','application/json; charset=UTF-8')
        
        resp = urllib.request.urlopen(req)
        response_data = json.loads(resp.read().decode('utf-8'))
        resp.close()
        mensagem = response_data['mensagem_cloud']

    except Exception as err:  
        mensagem ='Não foi possível registar a pontuação no ranking.\n'
        mensagem = mensagem + str(err)
        
    return mensagem

def escreve_registo():

    nome_ficheiro = numero + '.' + str(pontos)
    modo = 'w'
    ficheiro = open(nome_ficheiro, modo)
    ficheiro.write('numero=' + numero + '\n')
    ficheiro.write('amigos=' + amigos + '\n')
    ficheiro.write('grelha_inicial=' + str(grelha) + '\n')
    ficheiro.write('jogadas=' + jogadas + '\n')
    ficheiro.write('pontos=' + str(pontos) + '\n')
    ficheiro.write('semente=' + str(semente) + '\n')

    ficheiro.close()
    mensagem_cloud = regista_ranking()

    return mensagem_cloud
