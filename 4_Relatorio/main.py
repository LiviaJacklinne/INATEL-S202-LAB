from database import Database
from save_json import writeAJson

# instanciando conexão com o banco de dados
db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

# o result vai retornar a média do valor que foi gasto na loja por todos os clientes
result = db.collection.aggregate([
    # unwind, separa os dados para fazermos a agregação
    # mutiply, está multiplicando os produtos pelo preço
    # sum, vai fazer a soma com o resultados da multiplicação e salvar em total

    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id","total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    # avg, faz a média da soma
    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
])

# vamos criar um json com nome "media", e salvar o que tem no resul
writeAJson(result, "media")

result2 = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
    # sort, é responsavel por ordenar os dados
    {"$sort": {"total": -1}},
    # limitamos o nosso "print" a uma unica informação
    {"$limit": 1}
])

# vamos criar um json com nome "mais_vendido", e salvar o que tem no resul
writeAJson(result2, "mais_vendido")

result3= db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": {"cliente": "$cliente_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
])

# vamos criar um json com nome "maior_consumidor", e salvar o que tem no resul
writeAJson(result3, "maior_consumidor")