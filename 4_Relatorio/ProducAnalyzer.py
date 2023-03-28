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
    {"$group": {"_id": "$cliente_id"=="B","total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},

])

writeAJson(result,"gasto_cliente_B")