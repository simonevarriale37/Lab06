from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        # inizializzo connection
        connection = None
        try:
            # faccio la connessione al database
            connection = get_connection()
            # creo un cursore
            cursor = connection.cursor()
            # seleziono tutti gli attributi della tabella automobile
            query = "SELECT * FROM automobile"
            # eseguo la query
            cursor.execute(query)
            # salvo i risultati della query
            result = cursor.fetchall()
            if not result:
                return None
            automobili = []
            for riga in result:
                codice = riga[0]
                marca = riga[1]
                modello = riga[2]
                anno = riga[3]
                posti = riga[4]
                disponibile = bool(riga[5])
                auto = Automobile(codice, marca, modello, anno, posti, disponibile)
                automobili.append(auto)
            return automobili
        except Exception as e:
            print(e)
            return None
        # chiudo connessione e cursore
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()



    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # controllo se il modello è vuoto
        if not modello:
            return None
        # inizializzo la connessione
        connection = None
        try:
            connection = get_connection()
            cursor = connection.cursor()
            # seleziono dalla tabello le auto con il modello inserito
            query = "SELECT * FROM automobile WHERE modello LIKE %s"
            cursor.execute(query, (f"%{modello}%",))
            result = cursor.fetchall()
            if not result:
                return None
            automobili = []
            for riga in result:
                codice = riga[0]
                marca = riga[1]
                modello = riga[2]
                anno = riga[3]
                posti = riga[4]
                disponibile = bool(riga[5])
                auto = Automobile(codice, marca, modello, anno, posti, disponibile)
                automobili.append(auto)
            return automobili
        except Exception as e:
            print(e)
            return None
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

