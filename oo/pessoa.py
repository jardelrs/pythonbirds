class Pessoa:
    def cumprimento(self):
        return f'Olá mundo {id(p)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimento(p))
    print(id(p))
    print(p.cumprimento())
