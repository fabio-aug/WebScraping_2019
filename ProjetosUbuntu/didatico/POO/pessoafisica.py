from didático.POO.pessoa import PC

class pf(PC):
    def __init__(self, cpf, nome, idade):
        self.cpf = cpf
        PC.__init__(self, nome, idade)

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf
