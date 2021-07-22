from Databasewatcher import Database_Watcher

class Poketrader(object):
    def __init__(self):
        self.KARL = Database_Watcher()
        pass

    def my_lists(self,name):
        SQL_suchen = "SELECT * FROM suchen WHERE username = '"+str(name)+"';"
        SQL_anbieten = "SELECT * FROM anbieten WHERE username = '"+str(name)+"';"
        Ergebnis = self.KARL.read_data(SQL_suchen)
        Ergebnis_anbieten = self.KARL.read_data(SQL_anbieten)
        print(Ergebnis, Ergebnis_anbieten)

    def create_search(self,username,pokemon_id,pokemon_name,is_shiny,ort,anzahl):
        sql_for_image = "SELECT * from pokedex WHERE name = '"+str(pokemon_name)+"';"
        SQL_suche_image = self.KARL.read_data(sql_for_image)
        if is_shiny == 1:
            image = SQL_suche_image[0]
            image = image[4]
        else:
            image = SQL_suche_image[0]
            image = image[3]
        enthalten = False
        suche_anzahl = 0
        SQL_suche_sql = "SELECT * FROM suchen WHERE username = '"+str(username)+"';"
        SQL_suche = self.KARL.read_data(SQL_suche_sql)
        for suche in SQL_suche:
            print(suche)
            username_suche = suche[1]
            pokemon_name_suche = suche[3]
            suche_anzahl = suche[6]
            if pokemon_name_suche == pokemon_name:
                enthalten = True
                suche_anzahl = suche_anzahl+anzahl

        if enthalten == False:
            SQL = "Insert into suchen(username, pokemon_id, pokemon_name, is_shiny,ort,anzahl,image) values('"+username+"',"+str(pokemon_id)+",'"+pokemon_name+"','"+str(is_shiny)+"','"+ort+"',"+str(anzahl)+",'"+image+"');"
            self.KARL.write_data(SQL)
        else:
            print("Ist bereits enthalten bitte updaten")
            print("Die neue Anzahl = ",str(suche_anzahl))
            SQL_UPDATE = "UPDATE suchen SET anzahl = "+str(suche_anzahl)+" WHERE username = '"+str(username)+"' and pokemon_name = '"+str(pokemon_name)+"';"
            self.KARL.write_data(SQL_UPDATE)

    def create_offer(self,username,pokemon_id,pokemon_name,is_shiny,ort,anzahl):
        sql_for_image = "SELECT * from pokedex WHERE name = '"+str(pokemon_name)+"';"
        SQL_suche_image = self.KARL.read_data(sql_for_image)
        if is_shiny == 1:
            image = SQL_suche_image[0]
            image = image[4]
        else:
            image = SQL_suche_image[0]
            image = image[3]

        enthalten = False
        suche_anzahl = 0
        SQL_suche_sql = "SELECT * FROM anbieten WHERE username = '"+str(username)+"';"
        SQL_suche = self.KARL.read_data(SQL_suche_sql)
        for suche in SQL_suche:
            print(suche)
            username_suche = suche[1]
            pokemon_name_suche = suche[3]
            suche_anzahl = suche[6]
            if pokemon_name_suche == pokemon_name:
                enthalten = True
                suche_anzahl = suche_anzahl+anzahl
        if enthalten == False:
            SQL = "Insert into anbieten(username, pokemon_id, pokemon_name, is_shiny,ort,anzahl,image) values('"+username+"',"+str(pokemon_id)+",'"+pokemon_name+"','"+str(is_shiny)+"','"+ort+"',"+str(anzahl)+",'"+image+"');"
            self.KARL.write_data(SQL)
        else:
            print("Ist bereits enthalten bitte updaten")
            print("Die neue Anzahl = ",str(suche_anzahl))
            SQL_UPDATE = "UPDATE anbieten SET anzahl = "+str(suche_anzahl)+" WHERE username = '"+str(username)+"' and pokemon_name = '"+str(pokemon_name)+"';"
            self.KARL.write_data(SQL_UPDATE)

    def give_all_pokemon(self):
        SQL_suche_sql = "SELECT * FROM pokedex;"
        SQL_suche = self.KARL.read_data(SQL_suche_sql)
        print(SQL_suche)

    def give_random_searchs_and_offers(self):
        SQL_SEARCH = "SELECT * FROM suchen ORDER BY RAND() LIMIT 10;"
        SQL_OFFERS = "SELECT * FROM anbieten ORDER BY RAND() LIMIT 10;"
        searches = self.KARL.read_data(SQL_SEARCH)
        offers = self.KARL.read_data(SQL_OFFERS)
        Ergebnis = [searches,offers]
        return(Ergebnis)

    def create_user_informations(self,name):
        profilepicture = "https://www.senertec.de/wp-content/uploads/2020/04/blank-profile-picture-973460_1280.png"
        friendcode = "0000 0000 0000 0000"
        actual_place = "something"
        SQL = "Insert into user_data(user_name, profile_picture, friend_code, actual_place) values('"+name+"','"+profilepicture+"','"+friendcode+"','"+actual_place+"');"
        self.KARL.write_data(SQL)

if __name__ == "__main__":
    BOB = Poketrader()
    #BOB.my_lists("Vischie")
    BOB.create_search("Vischie",1,"Partyhut Bisasam",1,"Köthen",1)
    #BOB.create_offer("Vischie",1,"Bisasam",1,"Köthen",1)
    BOB.my_lists("Vischie")
    BOB.give_all_pokemon()
