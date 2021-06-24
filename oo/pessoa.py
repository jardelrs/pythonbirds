class Pessoa:
    def __init__(self, nome=None, idade=38):
        self.idade = idade
        self.nome = nome
    def cumprimento(self):
        return f'Olá mundo {id(p)}'

if __name__ == '__main__':
    p = Pessoa('Pedro')
    print(Pessoa.cumprimento(p))
    print(id(p))
    print(p.nome)
    print(p.cumprimento())
    p.nome = 'Jardel'
    print(p.nome)
    print(p.idade)
