from database import Database
from familyDatabase import FamilyDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.230.72.148:7687", "neo4j", "equation-propulsion-size")
# db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
mydb = FamilyDatabase(db)

# EXIBINDO TODOS
print(f'Pessoas do banco {mydb.get_nome()}')


# EXIBINDO PAI_DO
print(f'Pai do: {mydb.get_pai()}')

# EXIBINDO MAE_DO
print(f'Mae do: {mydb.get_mae()}')

# EXIBINDO QUEM TA VIVO
print(f'Pessoas vivas/mortas: {mydb.get_vivo()}')

# Fechando a conexão
db.close()