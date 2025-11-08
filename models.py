class Categoria:
    def __init__(self, nome):
        self.nome = nome


class Escola:
    def __init__(self, nome, nome_fantasia, cnpj, endereco, telefone, email, responsavel, cidade, estado):
        self.nome = nome
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.responsavel = responsavel
        self.cidade = cidade
        self.estado = estado


class Atleta:
    def __init__(self, nome, email, idade, altura, peso, data_nascimento, telefone, observacoes,
                 cad_unico, escola_id, categoria_id, categoria_idade):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.observacoes = observacoes
        self.cad_unico = cad_unico
        self.escola_id = escola_id
        self.categoria_id = categoria_id
        self.categoria_idade = categoria_idade


class Podio:
    def __init__(self, atleta_id, colocacao, evento):
        self.atleta_id = atleta_id
        self.colocacao = colocacao
        self.evento = evento
