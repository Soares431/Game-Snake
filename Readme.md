
Snake Game em Python utilizando Pygame
---------------------------------------

Este é um jogo clássico da cobrinha, onde o jogador controla uma cobra que cresce ao comer comida. 
O objetivo é evitar que a cobra colida com as bordas ou consigo mesma.

Configurações:
- Tamanho da tela: 600x400 pixels
- Tamanho do quadrado (células): 10x10 pixels
- Velocidade do jogo: 15 quadros por segundo

Estrutura do Código:
1. **Funções**:
   - `gerar_comida()`: Gera uma posição aleatória para a comida.
   - `desenhar_comida(tamanho, pos_comida_x, pos_comida_y)`: Renderiza a comida na tela.
   - `desenha_cobrinha(tamanho, pixels)`: Desenha a cobra com base nas coordenadas armazenadas em `pixels`.
   - `desenha_pontuacao(pontuacao)`: Mostra a pontuação no canto superior esquerdo da tela.
   - `seleciona_velocidade(tecla)`: Define a direção do movimento da cobra com base na tecla pressionada.
   - `roda_jogo()`: Contém o loop principal do jogo e gerencia as interações e atualizações.

2. **Cores**:
   - Preto: Fundo da tela
   - Branco: Corpo da cobra
   - Verde: Comida
   - Vermelho: Pontuação

3. **Lógica do Jogo**:
   - A cobra cresce ao comer a comida.
   - O jogo termina se a cobra colidir com as bordas ou consigo mesma.

Bibliotecas Necessárias:
- `pygame`: Para gráficos e controle de eventos.
- `random`: Para gerar posições aleatórias para a comida.

Como Jogar:
- Use as setas do teclado para mover a cobra.
- O jogo termina se a cobra colidir com as bordas ou com seu próprio corpo.
