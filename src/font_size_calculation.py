import math
class FontSizeCalculation:
    def __init__(self):
        pass

    def calcular_tamanho_fonte(self, texto):
  
        num_caracteres = len(texto)
        a = 563.2256986592307
        b = 0.5354202812578108
        tamanho_fonte = a / (num_caracteres ** b )
        
        return math.floor(tamanho_fonte)  # Arredondar para baixo para evitar cortes