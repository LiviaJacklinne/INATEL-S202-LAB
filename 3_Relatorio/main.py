from database import Database
from WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

''' Pesquisa 1 - Pokemons com  90<= ATTACK >= 100 (OK) '''
# pokemon_atk = db.collection.find({"base.Attack": {"$lte": 100} and {"$gte":90}})
# writeAJson(pokemon_atk, "pesquisa1_ATK_pokemon")

''' Pesquisa 2 - Pokemons que começam com a letra P (OK) '''
# pokemon_letter_P = db.collection.find({"name.english":{"$regex":"^P"}})
# writeAJson(pokemon_letter_P,"pesquisa2_Pokemom_com_P")

''' Pesquisa 3 - Pokemons de fogo (OK) '''
# fire_pokemons = db.collection.find({"type":"Fire"})
# writeAJson(fire_pokemons,"pesquisa3_Pokemon_de_Fogo")

''' Pesquisa 4 - Busca o pokemon com velocidade igual a 150'''
# speed_pokemon = db.collection.find({"base.Speed":150})
# writeAJson(speed_pokemon,"pesquisa4_Pokemom_Speed_150")


''' Pesquisa 5 -  '''
pokemons_water_or_poison = db.collection.find({"$or": [{"type":"Water"},{"type":"Poison"}]})
writeAJson(pokemons_water_or_poison,"pesquisa5_Pokemons_water_or_poison")