import cv2
import numpy as np

# 1. Carregar a imagem em escala de cinza
img = cv2.imread('odair.png', 0)

# --- Verificação de Erro ---
# Se a imagem não for encontrada, img será None. Isso evita o erro `!_src.empty()`.
if img is None:
    print("Erro: Não foi possível encontrar o arquivo 'odair.png'.")
    print("Verifique se o arquivo de imagem está na mesma pasta que o script 'Imagem.py'.")
else:
    # 2. Detectar as bordas com o algoritmo Canny
    # O primeiro limiar (100) deve ser menor que o segundo (200).
    bordas = cv2.Canny(img, 100, 200)

    # 3. Criar uma imagem preta (toda com zeros) com as mesmas dimensões
    # e 3 canais de cor (BGR) para desenhar as bordas coloridas.
    bordas_coloridas = np.zeros((bordas.shape[0], bordas.shape[1], 3), dtype=np.uint8)

    # 4. Mudar a cor das bordas para verde de forma eficiente
    # Onde a imagem 'bordas' for branca (valor 255), definimos a cor para verde [0, 255, 0] (BGR).
    # Isso usa a matriz 'bordas' como uma máscara.
    bordas_coloridas[bordas == 255] = [0, 255, 0]

    cv2.imshow('Bordas Verdes', bordas_coloridas)
    cv2.waitKey(0)
    cv2.destroyAllWindows() # Boa prática para fechar todas as janelas ao final.