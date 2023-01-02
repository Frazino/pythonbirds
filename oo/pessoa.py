class Pessoa:
    def __init__(self, nome=None, idade=33):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá! {id(self)}'

if __name__== '__main__':
    p= Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Roger'
    print(p.nome)
    print(p.idade)