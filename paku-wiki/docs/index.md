# Paku-Paku

Bem vindo a documentação do **Paku-Paku**. Nessa página você vai conhecer mais sobre o jogo, seus elementos e como jogar.

## Sobre o jogo
O Paku-Paku é um jogo inspirado no Pac-Man. O jogador assume o controle do Paku e o guia pelo labirinto em busca das bolinhas pra alimentar o faminto Paku. Mas guiar o Paku não é uma tarefa tão simples, o labirinto é um lugar perigoso e cheio de fantasmas que o perseguem, a única esperança do Paku é escapar dos fantasmas ou conseguir alcançar uma super bolinha que lhe da poderes que o tornam capaz de comer os fantasmas, mas isso não resolve o problema pois os fantasmas sempre voltam.

O **objetivo** do jogo é que o Paku consiga comer o maior número de bolinhas possíveis sem ser capturado pelos fantasmas. Ao comer as bolinhas especiais (maiores) o Paku consegue poderes por 15 segundos, e fica forte o suficiente para comer os fantasmas, sabendo disso os fantasmas começam a fugir do Paku.

## Elementos do Paku-Paku

### Paku

<center>
<img src="https://i.imgur.com/p0h1DyT.png"></img>
</center>

O **Paku** é o personagem principal do jogo. O jogador pode mover o Paku para todas as direções desejadas, desde que não haja uma parede na direção.

O Paku pode ser morto pelos Fantasmas caso seja capturado. Porém ao comer uma super bolinha o Paku ganha poderes, e enquanto os poderes durarem (15 segundos) ele não pode ser morto pelos fantasmas, pelo contrário, ele pode comer eles e ganhar um bônus de 100 pontos. Quando os poderes do Paku começam a se enfraquecer (nos últimos 5 segundos) os fantasmas começam a piscar voltando pra sua forma original.


### Blinky

<center>
<img src="https://i.imgur.com/Ta8Q1C8.png"></img>
</center>

O Blinky é um fantasma muito inteligente, ele usa um algoritmo de Dijkstra para perseguir o Paku.

Sempre que o Paku ganha poderes, ele usa o mesmo algoritmo para tentar fugir.

### Inky

<center>
<img src="https://i.imgur.com/QQioYop.png"></img>
</center>

O Inky é um fantasma que gosta de trabalhar em equipe, ele tenta se unir a outro fantasma para emboscar Paku.

Sempre que o Paku ganha poderes, ele tenta fugir correndo para longe de todos os fantasmas pois acha que ficará mais seguro assim.
### Pinky 


<center>
<img src="https://i.imgur.com/vyciGvi.png"></img>
</center>

O Pinky é um fantasma estrategista, ele tenta estar sempre um passo a frente de Paku para surpreende-lo.

Sempre que o Paku ganha poderes, ele tenta fugir correndo pro lado contrário de onde Paku estiver.

### Clyde

<center>
<img src="https://i.imgur.com/5MtDjms.png"></img>
</center>

O Clyde é um fantasma atrapalhado e medroso, sempre que é preciso perseguir o Paku ele fica sem saber o que fazer, pois tem medo de se aproximar e morrer.

Sempre que o Paku ganha poderes ele tenta fugir correndo desesperado de medo pelo labirinto.

### Bordy

<center>
<img src="https://i.imgur.com/fwnpvc6.png"></img>
</center>

O Bordy é um fantasma muito inteligente, ele usa um algoritmo de Bellman-Ford para perseguir o Paku.

Sempre que o Paku ganha poderes, ele usa o mesmo algoritmo para tentar fugir.

### Bolinhas

<center>
<img src="https://i.imgur.com/TEW2Ssu.png"></img>
</center>

As bolinhas são capturadas sempre que o Paku passa por elas e geram pontos para o jogador.

Existem dois tipos de bolinhas no jogo:  

- **Bolinhas comuns**: valem apenas 10 pontos.
- **Super bolinas**: São maiores que as bolinhas comuns e valem 50 pontos e dão ao Paku poder suficiente para comer os fantasmas durante 15 segundos.
### Tela de Menu

![](https://i.imgur.com/3nTtWZt.png)

- **RECORDES:** Ao ser clicado, direciona o jogador para a tela de recordes.
- **AJUSTES:** Ao ser clicado, direciona o jogador para a tela de ajustes.
- **JOGAR:** Ao ser clicado, inicia um jogo, com os ajustes que estejam selecionados.

### Tela de Ajustes

![](https://i.imgur.com/FPYvtrM.png)

Na tela de ajustes o jogador pode selecionar as configurações desejadas por ele para a partida.

#### Rotas
- **Mostrar Dijkstra:** Ao ser clicado configura o jogo para mostrar a rota calculada (usando o algoritmo de Dijkstra) pelo fantasma Blinky até o player. *Um dos fantasmas deve ser o Blinky para o botão ser ativado no jogo*

- **Mostrar Bellman-Ford:** Ao ser clicado, configura o jogo para mostrar a rota calculada (usando o algoritmo de Bellman-Ford) pelo fantasma Bordy até o player. *Um dos fantasmas deve ser o Bordy para o botão ser ativado no jogo*

#### Labirinto
- **Espelhar Labirinto:** Ao ser clicado, configura o labirinto gerado para ser do tipo espelhado, dessa forma o algoritmo de geração do labirinto irá gerar apenas metade e o resto será espelhado, simétrico no eixo Y.

- **Kruskal:** Ao ser clicado, configura o labirinto para ser gerado a partir da MST do algoritmo ambicioso de Kruskal. **É o algoritmo utilizado como padrão do jogo, caso nenhum seja selecionado**

- **Prim:** Ao ser clicado, configura o labirinto para ser gerado a partir da MST do algoritmo ambicioso de Prim. 

#### Fantasmas
O Paku-Paku tem sempre 4 fantasmas que o perseguem durante o jogo e você pode selecionar quem são esses fantasmas. Ao clicar no botão o fantasma será trocado por outro, é possível escolher qualquer um entre todos os 5 fantasmas, inclusive fantasmas iguais.

## Como usar
### Instalação 
**Linguagem**: Python<br>
**Framework**: --- <br>

**Pré-requisitos** para rodar o Paku-Paku 2:  
- Instale o [Python](https://www.python.org/downloads/) (versão 3.8.5)  
- Instale o [Pyxel](https://github.com/kitao/pyxel/blob/master/README.pt.md) (versão 1.4.3)

### Instalar e Executar (Sistema baseado em Debian)

    $ pip3 install pyxel 
    $ git clone https://github.com/projeto-de-algoritmos/Final_Paku-2.git
    $ cd Final_Paku-2/paku
    $ python3 game.py

<!--### Executar via release-->

## Como jogar

Para jogar o Paku-Paku é bem simples, basta clicar no botão jogar da Tela de Menu (caso deseje clique no botão ajustes primeiro e faça as configurações desejadas). Ao clicar no botão o labirinto será gerado, após a geração do labirinto o Paku começara a se mover, para redireciona-lô basta pressionar as setinhas do teclado ou as teclas w-a-s-d. Tente sobreviver a perseguição dos fantasmas enquanto alimenta o Paku para conseguir a vitória.

### GIF demonstrativa

![](https://i.imgur.com/1guR11m.gif)