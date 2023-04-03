from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017')
mydb = client['Relatorio_5']
mycollection = mydb['Livros']

class BookModel:
    def _init_(self, database):
        self.mydb = database
        self.collection = database.collection
    
    def create_livro(self, titulo: str, autor: str, ano:int, preco:float):
        try:
            result = self.collection.insert_one({"titulo":titulo, "autor":autor, "ano":ano, "preco":preco})
            book_id = str(result.insert_id)
            print(f"Livro {titulo} criado com id: {book_id}")
            return book_id
        except Exception as error:
            print(f"Um erro ocorreu na criação do livro: {error}")
            return None

    def read_book_by_id (self, book_id:str) -> dict:
        try:
            book = self.collection.find_one({"_id": ObjectId(book_id)})
            if book:
                print(f"Livro encontrado: {book}")
                return book
            else:
                print(f"Nenhum livro encontrado com o id: {book_id}")
                return None
        except Exception as error:
            print(f"Um erro ocorreu durante a leitura do livro : {error}")
            return None

    def update_book(self, book_id:str, titulo: str, autor: str, ano:int, preco:float) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(book_id)},{"$set": {"titulo":titulo, "autor":autor, "ano":ano, "preco":preco}})
            if result.modified_count:
                print(f"Livro {book_id} alterado para {titulo}")
            else:
                print(f"Nenhum livro encontrado com o id {book_id}")
        except Exception as error:
            print(f"Um erro ocorreu durante a alteração do livro : {error}")
            return None

    def delete_book(self, book_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(book_id)})
            if result.deleted_count:
                print(f"Livro com id {book_id} deletado")
            else:
                print(f"Não foi encontrado nenhum livro com esse id {book_id}")
        except Exception as error:
            print(f"Um erro ocorreu durante a exclusão do livro: {error}")
            return None
    



book_model = BookModel(mydb)

# id_livro = create_livro('k',"harry potter e a pedra filosofal","Kennilworthy Whisp",1997,30)
id_livro = book_model.create_livro("harry potter e a pedra filosofal","Kennilworthy Whisp",1997,30)


