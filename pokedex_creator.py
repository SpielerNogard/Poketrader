from Databasewatcher import Database_Watcher

BOB = Database_Watcher()



def insert_to_dex(pokemon_id,name,pic1,pic2):
    SQL = "Insert into pokedex(pokemon_id, name, picture, shiny_picture) values("+str(pokemon_id)+",'"+name+"','"+pic1+"','"+pic2+"');"
    BOB.write_data(SQL)


for a in range(100):
    pokemon_id = input("Pokemon_id: ")
    name = input("Pokemon Name: ")
    pic1 = input("Normales Bild: ")
    pic2 = input("Shiny Bild: ")
    insert_to_dex(pokemon_id,name,pic1,pic2)