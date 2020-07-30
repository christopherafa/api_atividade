from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Albert',idade='34')
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Albert').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Albert').first()
    pessoa.nome = 'Ferreira'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Albert').first()
    pessoa.delete()

if __name__ == '__main__':
    insere_pessoas()
    consulta_pessoas()
    altera_pessoa()
    consulta_pessoas()
