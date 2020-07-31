from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

'''
USUARIOS = {
    'christopher':'123',
    'albert':'456'
}


@auth.verify_password
def verificacao(login,senha):
    if not (login,senha):
        return False
    return USUARIOS.get(login) == senha
'''
@auth.verify_password
def verificacao(login,senha):
    if not (login,senha):
        return False
    return Usuarios.query.filter_by(login=login,senha=senha).first()


class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id':pessoa.id
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Pessoa nao encontrada'
            }
        return response

    def put(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

    def delete(self,nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            pessoa.delete()
            return {'status':'sucesso','mensagem ':'Pessoa {} excluida com sucesso'.format(nome)}
        except AttributeError:
            return {'status':'error','mensagem':'Pessoa nao encontrada'}

class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all() #cuidado! pega tudo
        response = [{'id':p.id,'nome':p.nome,'idade':p.idade}for p in pessoas]
        return response
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'],idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':a.id,'nome':a.nome,'pessoa':a.pessoa.nome} for a in atividades]
        return response
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'],pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome':atividade.nome,
            'id': atividade.id
        }
        return response

api.add_resource(Pessoa,'/pessoa/<string:nome>/')
api.add_resource(ListaPessoas,'/pessoa/')
api.add_resource(ListaAtividades,'/atividades/')

if __name__ == '__main__':
    app.run(debug=True)
