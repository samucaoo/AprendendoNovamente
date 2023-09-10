class Churrasco:
    def  __init__(self, pessoas :int, dia :str):
        self.pessoas = pessoas
        self.dia = dia

    def calcularTotalCarne(self, pessoas):
        self.pessoas = pessoas
        totalcarne = pessoas * 400
        print(f"O dia do evento será {self.dia}")
        print(f"A quantidade de carne para {pessoas} pessoas é de {totalcarne} Gramas")
        print("Teste do commit no github")
        print("Aqui foi o vini que fez")
        print("Aqui foi o vini que fez dnv para testar")



