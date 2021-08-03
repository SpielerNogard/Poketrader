import sqlite3 as sl
con = sl.connect('Poketrader.db', check_same_thread=False)
class Poketrader(object):
    def __init__(self):
        pass

    def read_data_from_table(self,SQL):
        Ergebnis = []
        with con:
            data = con.execute(SQL)
            for row in data:
                print(row)
                Ergebnis.append(row)
        return(Ergebnis)

    def insert_data_to_table(self,sql,data):
        sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
        data = [
            (1, 'Alice', 21),
            (2, 'Bob', 22),
            (3, 'Chris', 23)
        ]
        with con:
            con.executemany(sql, data)

    def my_lists(self,name):
        SQL_suchen = "SELECT * FROM suchen WHERE username = '"+str(name)+"';"
        SQL_anbieten = "SELECT * FROM anbieten WHERE username = '"+str(name)+"';"
        Suchen = self.read_data_from_table(SQL_suchen)
        Angebote = self.read_data_from_table(SQL_anbieten)
        print(Suchen, Angebote)

    def create_search(self,username,pokemon_id,pokemon_name,is_shiny,ort,anzahl):
        image = ""
        sql_for_image = "SELECT * from pokedex WHERE name = '"+str(pokemon_name)+"';"
        Ergebnis = self.read_data_from_table(sql_for_image)
        if is_shiny == 1:
            image = Ergebnis[0]
            image = image[4]
        else:
            image = Ergebnis[0]
            image = image[3]
        enthalten = False
        suche_anzahl = 0
        SQL_suche_sql = "SELECT * FROM suchen WHERE username = '"+str(username)+"';"
        Ergebnis = self.read_data_from_table(SQL_suche_sql)
        print(Ergebnis)
        for suche in Ergebnis:
            print(suche)
            username_suche = suche[1]
            pokemon_name_suche = suche[3]
            suche_anzahl = suche[6]
            if pokemon_name_suche == pokemon_name:
                enthalten = True
                suche_anzahl = suche_anzahl+anzahl

        if enthalten == False:
            SQL = "Insert into suchen(username, pokemon_id, pokemon_name, is_shiny,ort,anzahl,image) values('"+username+"',"+str(pokemon_id)+",'"+pokemon_name+"','"+str(is_shiny)+"','"+ort+"',"+str(anzahl)+",'"+image+"');"
            SQL2 = "Insert into suchen(username,pokemonid,pokemonname,isshiny,ort,anzahl,image) values(?,?,?,?,?,?,?);"
            data = [username,pokemon_id,pokemon_name,is_shiny,ort,anzahl,image]
            self.insert_data_to_table(SQL2,data)
        else:
            print("Ist bereits enthalten bitte updaten")
            print("Die neue Anzahl = ",str(suche_anzahl))
            SQL_UPDATE = "UPDATE suchen SET anzahl = "+str(suche_anzahl)+" WHERE username = '"+str(username)+"' and pokemonname = '"+str(pokemon_name)+"';"
            con.execute(SQL_UPDATE)
            con.commit()
        

    def create_offer(self,username,pokemon_id,pokemon_name,is_shiny,ort,anzahl):
        image = ""
        sql_for_image = "SELECT * from pokedex WHERE name = '"+str(pokemon_name)+"';"
        Ergebnis = self.read_data_from_table(sql_for_image)
        if is_shiny == 1:
            image = Ergebnis[0]
            image = image[4]
        else:
            image = Ergebnis[0]
            image = image[3]
        enthalten = False
        suche_anzahl = 0
        SQL_suche_sql = "SELECT * FROM anbieten WHERE username = '"+str(username)+"';"
        Ergebnis = self.read_data_from_table(SQL_suche_sql)
        print(Ergebnis)
        for suche in Ergebnis:
            print(suche)
            username_suche = suche[1]
            pokemon_name_suche = suche[3]
            suche_anzahl = suche[6]
            if pokemon_name_suche == pokemon_name:
                enthalten = True
                suche_anzahl = suche_anzahl+anzahl

        if enthalten == False:
            SQL = "Insert into anbieten(username, pokemon_id, pokemon_name, is_shiny,ort,anzahl,image) values('"+username+"',"+str(pokemon_id)+",'"+pokemon_name+"','"+str(is_shiny)+"','"+ort+"',"+str(anzahl)+",'"+image+"');"
            SQL2 = "Insert into anbieten(username,pokemonid,pokemonname,isshiny,ort,anzahl,image) values(?,?,?,?,?,?,?);"
            data = [username,pokemon_id,pokemon_name,is_shiny,ort,anzahl,image]
            self.insert_data_to_table(SQL2,data)
        else:
            print("Ist bereits enthalten bitte updaten")
            print("Die neue Anzahl = ",str(suche_anzahl))
            SQL_UPDATE = "UPDATE anbieten SET anzahl = "+str(suche_anzahl)+" WHERE username = '"+str(username)+"' and pokemonname = '"+str(pokemon_name)+"';"
            con.execute(SQL_UPDATE)
            con.commit()

    def give_all_pokemon(self):
        sql_for_image = "SELECT * from pokedex;"
        Ergebnis = self.read_data_from_table(sql_for_image)
        print(Ergebnis)

    def give_random_searchs_and_offers(self):
        SQL_SEARCH = "SELECT * FROM suchen ORDER BY RANDOM() LIMIT 10;"
        SQL_OFFERS = "SELECT * FROM anbieten ORDER BY RANDOM() LIMIT 10;"
        searches = self.read_data_from_table(SQL_SEARCH)
        offers = self.read_data_from_table(SQL_OFFERS)
        Ergebnis = [searches,offers]
        return(Ergebnis)

    def create_user_informations(self,name):
        profilepicture = "https://www.senertec.de/wp-content/uploads/2020/04/blank-profile-picture-973460_1280.png"
        friendcode = "0000 0000 0000 0000"
        actual_place = "something"
        SQL2 = "Insert into UserData(username, profilepicture, friendcode, actualplace) values(?,?,?,?);"
        data = [name,profilepicture,friendcode,actual_place]
        self.insert_data_to_table(SQL2,data)

    def find_the_user(self,name):
        SQL = "SELECT * FROM UserData WHERE username = '"+str(name)+"';"
        offers = self.read_data_from_table(SQL)
        this_user = offers[0]
        return(this_user)
    
    def update_user(self,name, code, bild, ort):
        SQL_UPDATE = "UPDATE UserData SET profilepicture = '"+str(bild)+"', friendcode='"+str(code)+"',actualplace='"+str(ort)+"' WHERE username = '"+str(name)+"';"
        con.execute(SQL_UPDATE)
        con.commit()
        SQL_update_anbieten = "UPDATE anbieten SET ort = '"+str(ort)+"' WHERE username = '"+str(name)+"';"
        con.execute(SQL_update_anbieten)
        con.commit()
        SQL_update_anbieten = "UPDATE suchen SET ort = '"+str(ort)+"' WHERE username = '"+str(name)+"';"
        con.execute(SQL_update_anbieten)
        con.commit()

if __name__ == "__main__":
    BOB = Poketrader()
    BOB.my_lists("Vischie")
    #BOB.create_search("Vischie",1,"Partyhut Bisasam",1,"Köthen",1)
    #BOB.create_offer("Vischie",1,"Bisasam",1,"Köthen",1)
    #BOB.my_lists("Vischie")
    #BOB.give_all_pokemon()
    BOB.give_all_pokemon()
