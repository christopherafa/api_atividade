from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Ferreira',idade='36')
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Christopher').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ferreira').first()
    pessoa.nome = 'Albert'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Albert').first()
    pessoa.delete()

def insere_usuario(login,senha):
    usuario = Usuarios(login=login,senha=senha)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    #insere_usuario('christopher','123')
    #insere_usuario('albert','456')
    consulta_usuarios()
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()
