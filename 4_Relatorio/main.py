from database import Database
from save_json import writeAJson

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

# Questão 1
# result1 = db.collection.aggregate([
    ## Separa o array de produtos
#     {"$unwind": "$produtos"},
#     {"$group": {"_id":"$cliente_id", "total":{"$sum": {"$multiply": ["$produtos.quantidade","$produtos.preco"]}}}},
    ## Encontra um item especifico
#     {"$match":{"_id":"B"}}
# ])
# writeAJson(result1, "Total_cliente_B")

# Questão 2
# result2 = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
    ## Ordena em ordem crescente
#     {"$sort": {"total": 1}},
    ## limita a uma exibição
#     {"$limit": 1}
# ])
# writeAJson(result2, "Produto_menos_vendido")

# Questão 3
# result3 = db.collection.aggregate([
#     {"$unwind":"$produtos"},
#     {"$group": {"_id":"$cliente_id", "gasto":{"$sum":{"$multiply": ["$produtos.quantidade","$produtos.preco"]}}}},
#     {"$sort": {"gasto": 1}},
#     {"$limit":1}
# ])
# writeAJson(result3, "Cliente_menos_gastou")

# Questão 4
result4 = db.collection.aggregate([
    {"$unwind":"$produtos"},
    {"$group":{"_id":"$produtos.nome","total":{"$sum": "$produtos.quantidade"}}},
    {"$match":{"total":{"$gt":2}}}
])
writeAJson(result4, "Mais_2_vendas")