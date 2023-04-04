from database import Database
from bookModel import BookModel


# client = MongoClient('mongodb://localhost:27017')
# mydb = client["Relatorio_5"]
# mycollection = mydb["Livros"]

db = Database(database="Relatorio_05", collection="Livros")

bookModel = BookModel(database=db)
x = bookModel.create_livro("harry potter e a pedra filosofal","Kennilworthy Whisp",1997,30)
