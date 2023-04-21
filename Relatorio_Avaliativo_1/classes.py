
class Cuidador:
    def __init__(self, id, nome, documento):
        self.id = id
        self.nome = nome
        self.documento = documento
        
class Habitat(Cuidador):
    def __init__(self, id, nome, tipoAmbiente, cuidador):
        self.id = id
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = Cuidador
        
class Animal:
    def __init__(self, id, nome, especie, idade, habitat):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = Habitat