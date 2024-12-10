import pygame as py
import random
import math


#cores

branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (100, 100, 255)
lilas = (220, 208, 255)
vermelho = (255, 105, 97)

window = py.display.set_mode((1000, 700))

py.font.init()

font = py.font.SysFont('Courier New', 50, bold=True)

tabuleiroData = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

jogoData = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
            ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
            ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
            ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
            ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
            ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
            ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
            ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
            ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

esconderNumeros = True
tabuleiroPreenchido = True
clickLastStatus = False
clickX = -1
clickY = -1
num = 0

def tabuleiroHover(window, mousePositionX, mousePositionY):
    quadrado = 66.7
    ajuste = 50
    x = (math.ceil((mousePositionX - ajuste) / quadrado) - 1)
    y = (math.ceil((mousePositionY - ajuste) / quadrado) - 1)
    py.draw.rect(window, preto, (0, 0, 1000, 700))
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        py.draw.rect(window, lilas, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))

def select(window, mouseX, mouseY, clickLastStatus, click, x, y):
    quadrado = 66.7
    ajuste = 50
    if clickLastStatus == True and click == True:
        x = (math.ceil((mouseX - ajuste) / quadrado) - 1)
        y = (math.ceil((mouseY - ajuste) / quadrado) - 1)
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        py.draw.rect(window, lilas, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))
    return x, y

def tabuleiro(window):
    py.draw.rect(window, branco, (50, 50, 600, 600), 6)
    py.draw.rect(window, branco, (50, 250, 600, 200), 6)
    py.draw.rect(window, branco, (250, 50, 200, 600), 6)
    py.draw.rect(window, branco, (50, 117, 600, 67), 2)
    py.draw.rect(window, branco, (50, 317, 600, 67), 2)
    py.draw.rect(window, branco, (50, 517, 600, 67), 2)
    py.draw.rect(window, branco, (117, 50, 67, 600), 2)
    py.draw.rect(window, branco, (317, 50, 67, 600), 2)
    py.draw.rect(window, branco, (517, 50, 67, 600), 2)

def newGame(window):
    py.draw.rect(window, branco, (700, 50, 285, 100))
    palavra = font.render("New Game", True, preto)
    window.blit(palavra, (725, 75))

def linhaEscolhida(tabuleiroData, y):
    linhaSorteada = tabuleiroData[y]
    return linhaSorteada

def colunaEscolhida(tabuleitoData, x):
    colunaSorteada = []
    for n in range(8):
        colunaSorteada.append(tabuleitoData[n][x])
    return colunaSorteada

def quadranteSelecionado(tabuleiroData, x, y):
    quadrante = []
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiroData[0][0], tabuleiroData[0][1], tabuleiroData[0][2],
                          tabuleiroData[1][0], tabuleiroData[1][1], tabuleiroData[1][2],
                          tabuleiroData[2][0], tabuleiroData[2][1], tabuleiroData[2][2]])
    if x >= 3 and x <= 5 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiroData[0][3], tabuleiroData[0][4], tabuleiroData[0][5],
                          tabuleiroData[1][3], tabuleiroData[1][4], tabuleiroData[1][5],
                          tabuleiroData[2][3], tabuleiroData[2][4], tabuleiroData[2][5]])
    if x >= 6 and x <= 8 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiroData[0][6], tabuleiroData[0][7], tabuleiroData[0][8],
                          tabuleiroData[1][6], tabuleiroData[1][7], tabuleiroData[1][8],
                          tabuleiroData[2][6], tabuleiroData[2][7], tabuleiroData[2][8]])
    if x >= 0 and x <= 2 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiroData[3][0], tabuleiroData[3][1], tabuleiroData[3][2],
                          tabuleiroData[4][0], tabuleiroData[4][1], tabuleiroData[4][2],
                          tabuleiroData[5][0], tabuleiroData[5][1], tabuleiroData[5][2]])
    if x >= 3 and x <= 5 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiroData[3][3], tabuleiroData[3][4], tabuleiroData[3][5],
                          tabuleiroData[4][3], tabuleiroData[4][4], tabuleiroData[4][5],
                          tabuleiroData[5][3], tabuleiroData[5][4], tabuleiroData[5][5]])
    if x >= 6 and x <= 8 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiroData[3][6], tabuleiroData[3][7], tabuleiroData[3][8],
                          tabuleiroData[4][6], tabuleiroData[4][7], tabuleiroData[4][8],
                          tabuleiroData[5][6], tabuleiroData[5][7], tabuleiroData[5][8]])
    if x >= 0 and x <= 2 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiroData[6][0], tabuleiroData[6][1], tabuleiroData[6][2],
                          tabuleiroData[7][0], tabuleiroData[7][1], tabuleiroData[7][2],
                          tabuleiroData[8][0], tabuleiroData[8][1], tabuleiroData[8][2]])
    if x >= 3 and x <= 5 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiroData[6][3], tabuleiroData[6][4], tabuleiroData[6][5],
                          tabuleiroData[7][3], tabuleiroData[7][4], tabuleiroData[7][5],
                          tabuleiroData[8][3], tabuleiroData[8][4], tabuleiroData[8][5]])
    if x >= 6 and x <= 8 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiroData[6][6], tabuleiroData[6][7], tabuleiroData[6][8],
                          tabuleiroData[7][6], tabuleiroData[7][7], tabuleiroData[7][8],
                          tabuleiroData[8][6], tabuleiroData[8][7], tabuleiroData[8][8]])
    return quadrante

def preencherQuadrante(tabuleiroData, x2, y2):
    quadrantePreenchido = True
    loop =0
    tryCount = 0
    numero = 1
    while quadrantePreenchido == True:
        x = random.randint(x2, x2 + 2)
        y = random.randint(y2, y2 + 2)
        linhaSorteada = linhaEscolhida(tabuleiroData, y)
        colunaSorteada = colunaEscolhida(tabuleiroData, x)
        quadrante = quadranteSelecionado(tabuleiroData, x, y)
        if tabuleiroData[y][x] == 'n' and numero not in linhaSorteada and numero not in colunaSorteada and numero not in quadrante:
            tabuleiroData[y][x] = numero
            numero += 1
        loop += 1
        if loop == 50:
            tabuleiroData[y2][x2] = 'n'
            tabuleiroData[y2][x2 + 1] = 'n'
            tabuleiroData[y2][x2 + 2] = 'n'
            tabuleiroData[y2 + 1][x2] = 'n'
            tabuleiroData[y2 + 1][x2 + 1] = 'n'
            tabuleiroData[y2 + 1][x2 + 2] = 'n'
            tabuleiroData[y2 + 2][x2] = 'n'
            tabuleiroData[y2 + 2][x2 + 1] = 'n'
            tabuleiroData[y2 + 2][x2 + 2] = 'n'
            loop = 0
            numero = 1
            tryCount += 1
        if tryCount == 10:
            break
        count = 0
        for n in range(9):
            if quadrante[n] != 'n':
                count += 1
        if count == 9:
            quadrantePreenchido = False
    return tabuleiroData

def restartTabuleiroData(tabuleiroData):
    tabuleiroData = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                     ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                     ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                     ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                     ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                     ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                     ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                     ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                     ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]
    return tabuleiroData

def gabarito(tabuleiroData, tabuleiropreencido):
    while tabuleiropreencido == True:
        tabuleiroData = preencherQuadrante(tabuleiroData, 0, 0)
        tabuleiroData = preencherQuadrante(tabuleiroData, 3, 0)
        tabuleiroData = preencherQuadrante(tabuleiroData, 6, 0)
        tabuleiroData = preencherQuadrante(tabuleiroData, 0, 3)
        tabuleiroData = preencherQuadrante(tabuleiroData, 0, 6)
        tabuleiroData = preencherQuadrante(tabuleiroData, 3, 3)
        tabuleiroData = preencherQuadrante(tabuleiroData, 3, 6)
        tabuleiroData = preencherQuadrante(tabuleiroData, 6, 3)
        tabuleiroData = preencherQuadrante(tabuleiroData, 6, 6)
        for nn in range(9):
            for n in range(9):
                if tabuleiroData[nn][n] == 'n':
                    tabuleiroData = restartTabuleiroData(tabuleiroData)
        count = 0
        for nn in range(9):
            for n in range(9):
                if tabuleiroData[nn][n] != 'n':
                    count += 1
        if count == 81:
            tabuleiropreencido = False
    return tabuleiroData, tabuleiropreencido

def esconder(tabuleiroData, jogoData, esconderNumeros):
    if esconderNumeros == True:
        for n in range(40):
            sorteado = True
            while sorteado == True:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if jogoData[y][x] == 'n':
                    jogoData[y][x] = tabuleiroData[y][x]
                    sorteado = False
        esconderNumeros = False
    return jogoData, esconderNumeros

def escrever(window, jogoData):
    quadrado = 66.7
    ajuste = 67
    for nn in range(9):
        for n in range(9):
            if jogoData[nn][n] != 'n':
                palavra = font.render(str(jogoData[nn][n]), True, branco)
                window.blit(palavra, (ajuste + n * quadrado, ajuste - 5 + nn * quadrado))
                if jogoData[nn][n] == 'X':
                    palavra = font.render(str(jogoData[nn][n]), True, vermelho)
                    window.blit(palavra, (ajuste + n * quadrado, ajuste - 5 + nn * quadrado))

def digitar(numero):
    try:
        numero = int(numero[1])
    except:
        numero = int(numero)
    return numero

def numCheq(tabuleiroData, jogodata, clickX, clickY, num):
    x = clickX
    y = clickY
    ajuste = 50
    quadrado = 66.7
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiroData[y][x] == num and jogoData[y][x] == 'n' and num != 0:
        jogodata[y][x] = num
        num = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiroData[y][x] == num and jogoData[y][x] == num and num != 0:
        pass
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiroData[y][x] != num and jogoData[y][x] == 'n' and num != 0:
        jogodata[y][x] = 'X'
        num = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiroData[y][x] == num and jogoData[y][x] == 'X' and num != 0:
        jogodata[y][x] = num
        num = 0
    return jogodata, num

def botaoNewgame(mouseX, mouseY, clickLastStatus, click, tabuleiroPreenchido, esconderNumeros, tabuleiroData, jogoData):
    x = mouseX
    y = mouseY
    if x >= 700 and x <= 950 and y >= 50 and y <= 150 and clickLastStatus == False and click == True:
        tabuleiroPreenchido = True
        esconderNumeros = True
        tabuleiroData = restartTabuleiroData(tabuleiroData)
        jogoData = restartTabuleiroData(jogoData)
    return tabuleiroPreenchido, esconderNumeros, tabuleiroData, jogoData

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()
        if event.type == py.KEYDOWN:
            num = py.key.name(event.key)
            if event.key == py.K_ESCAPE:
                py.quit()
                quit()

    mouse = py.mouse.get_pos()
    mouseX = mouse[0]
    mouseY = mouse[1]

    click = py.mouse.get_pressed()

    tabuleiroHover(window, mouseX, mouseY)
    clickX, clickY = select(window, mouseX, mouseY, clickLastStatus, click[0], clickX, clickY)
    tabuleiro(window)
    newGame(window)
    tabuleiroData, tabuleiroPreenchido = gabarito(tabuleiroData, tabuleiroPreenchido)
    jogoData, esconderNumeros = esconder(tabuleiroData, jogoData, esconderNumeros)
    escrever(window, jogoData)
    num = digitar(num)
    jogoData, num = numCheq(tabuleiroData, jogoData, clickX, clickY, num)
    tabuleiroPreenchido, esconderNumeros, tabuleiroData, jogoData = botaoNewgame(mouseX, mouseY, clickLastStatus,
                                        click[0], tabuleiroPreenchido, esconderNumeros, tabuleiroData, jogoData)

    if click[0] == True:
        clickLastStatus = True
    else:
        clickLastStatus = False

    py.display.update()

