# import matplotlib.pyplot as plt
# import numpy as np

# # 1. Nova função quadrática: y = 3x² - 12x + 9
# # Deixamos o a=3 (bem fechadinha) e ajustamos b e c para os pontos darem inteiros
# def f(x):
#     return 3 * (x**2) - 12*x + 9

# # Gerar pontos para desenhar a curva fechada
# x = np.linspace(-0.5, 4.5, 400) # Cria 400 números entre -0.5 e 4.5 | O computador não desenha curvas nativamente; ele desenha pequenas retas ligando pontos. Aqui, criamos 400 pontos bem colados uns nos outros. Se você colocar apenas 5 em vez de 400, seu gráfico vai virar um ziguezague cheio de pontas!

# y = f(x)                        # Passa esses 400 números pela sua fórmula matemática

# # 2. Configurar a figura do gráfico
# fig, ax = plt.subplots(figsize=(10, 6))

# # Desenhar a curva da parábola (Linha Verde)
# ax.plot(x, y, color='#5cb878', linewidth=3, label='Parábola (O Gráfico)')

# # 3. NOVOS PONTOS RECALCULADOS (Para não ficar torto!)
# # Novas Raízes (x1=1, x2=3) -> Pontos Laranjas (exatamente onde cruza o X)
# ax.plot([1, 3], [0, 0], 'o', color='#f0ad4e', markersize=12, zorder=5)
# ax.text(0.7, 0.5, '$x_1=1$', fontsize=12, color='#f0ad4e', fontweight='bold')
# ax.text(3.1, 0.5, '$x_2=3$', fontsize=12, color='#f0ad4e', fontweight='bold')

# # Novo Corte no Eixo Y (c=9) -> Ponto Azul Claro
# ax.plot(0, 9, 'o', color='#5bc0de', markersize=12, zorder=5)
# ax.text(0.2, 9, '(0, c=9)', fontsize=12, color='black')

# # Novo Vértice Perfeito (Xv=2, Yv=-3) -> Ponto Vermelho (exatamente na ponta de baixo)
# ax.plot(2, -3, 'o', color='#d9534f', markersize=12, zorder=5)
# ax.text(2.2, -3, '$(X_v=2, Y_v=-3)$', fontsize=12, color='#d9534f', fontweight='bold')

# # 4. Linhas pontilhadas do Vértice alinhadas
# ax.axvline(x=2, color='purple', linestyle=':', linewidth=2)
# ax.axhline(y=-3, xmin=0, xmax=0.5, color='gray', linestyle=':', linewidth=1.5)

# # 5. Estilização dos Eixos (Cruzando no zero)
# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')

# # Setas nos eixos
# ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
# ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# # Legendas e Equação na tela
# ax.text(4.6, 0.5, 'X', fontsize=16, fontweight='bold', color='#1a4a75')
# ax.text(0.2, 14.5, 'Y', fontsize=16, fontweight='bold', color='#1a4a75')
# ax.text(2.8, 12, '$y = 3x^2 - 12x + 9$', fontsize=14, 
#         bbox=dict(facecolor='white', edgecolor='#cbd5e1', boxstyle='round,pad=0.5'))

# # Configurações de limites da tela para enquadrar a nova parábola
# ax.grid(True, linestyle='--', alpha=0.5)
# plt.xlim(-1, 5)
# plt.ylim(-4, 15)

# # Mostrar o gráfico perfeito
# plt.show()

# ----- parabola simples -----

import matplotlib.pyplot as plt
import numpy as np

# 1. A fórmula matemática
def f(x): return x**2 - 4*x + 3

# 2. Criar os valores de X (de -1 até 5) e calcular o Y
x = np.linspace(-1, 5, 200)
y = f(x)

# 3. Mandar desenhar a linha
plt.plot(x, y)
plt.show()