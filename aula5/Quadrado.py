"""
Quadrado
    lado: int
    cor: str

"""
class Quadrado:

    def __init__(self, lado, cor):
        self.lado = lado
        self.cor = cor
        
    
    def area(self) -> int:
        #area = self.lado * self.lado
        area = self.lado * self.lado
        return area
    
    
    
    def perimetro(self):
        pass
    
    
    def mudar_cor(self):
        pass
    
