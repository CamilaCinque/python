# import matplotlib.pyplot as plt
# import numpy as np

# print("calculadora de parábola!")

# a = float(input("insira o valor de a:"))
# b = float(input("insira o valor de b:"))
# c = float(input("insira o valor de c:"))

# delta = (b ** 2) - (4 * a * c)

# # Cálculo do Vértice (ponto de virada)
# xv = -b / (2 * a)
# yv = -delta / (4 * a)

# # 3. Gerando o intervalo do gráfico baseado no Vértice
# # Isso faz o gráfico ficar sempre centralizado na curva, não importa os números digitados
# x = np.linspace(xv - 5, xv + 5, 400)
# y = a * (x**2) + b * x + c

# # 4. Configurando a tela do gráfico
# plt.figure(figsize=(8, 6))
# plt.plot(x, y, color="blue", linewidth=2, label="Parábola (Curva)")

# # Desenhando o Vértice (Ponto Vermelho)
# plt.scatter(xv, yv, color="red", s=100, zorder=5, label=f"Vértice ({xv:.1f}, {yv:.1f})")

# # Desenhando onde a curva corta o eixo Y (Ponto Roxo)
# plt.scatter(0, c, color="purple", s=100, zorder=5, label=f"Corta Y em {c:.1f}")

# # 5. Regra de Bhaskara para desenhar as Raízes (Eixo X)
# if delta >= 0:
#     # Se o delta for positivo ou zero, existem raízes reais
#     x1 = (-b + np.sqrt(delta)) / (2 * a)
#     x2 = (-b - np.sqrt(delta)) / (2 * a)
#     plt.scatter([x1, x2], [0, 0], color="green", s=100, zorder=5, label="Raízes (Eixo X)")
#     print(f"\n-> Raízes encontradas: x1 = {x1:.2f} e x2 = {x2:.2f}")
# else:
#     # Se o delta for negativo, a parábola flutua e não toca o eixo X
#     print("\n-> Esta equação não possui raízes reais (não corta o eixo X).")

# # 6. Detalhes visuais para o gráfico ficar bonito
# plt.axhline(0, color="black", linewidth=1, linestyle="--") # Linha do horizonte (X)
# plt.axvline(0, color="black", linewidth=1, linestyle="--") # Linha vertical (Y)
# plt.grid(True, linestyle=":")
# plt.title(f"Gráfico de y = {a}x² + ({b})x + ({c})", fontsize=12, fontweight="bold")
# plt.legend() # Mostra a legenda com as cores dos pontos

# print(f"-> Vértice calculado: ({xv:.2f}, {yv:.2f})")
# print("\nExibindo o gráfico na tela...")
# plt.show()