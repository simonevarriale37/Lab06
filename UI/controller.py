import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # Creo la funzione per mostrare l'elenco di auto
    def mostra_automobili(self, e):
        try:
            # prendo dal model l'elenco delle auto e la salvo in lista_auto
            lista_auto = self._model.get_automobili()
            # pulisco la lista delle auto
            self._view.lista_auto.controls.clear()
            # controllo se la lista è vuota
            if lista_auto is None or len(lista_auto) == 0:
                self._view.lista_auto.controls.append(ft.Text("Nessuna automobile trovata"))
            else:
                for auto in lista_auto:
                    testo = ft.Text(str(auto))
                    self._view.lista_auto.controls.append(testo)
            self._view.update()
        except Exception as e:
            self._view.lista_auto.controls.clear()
            self._view.lista_auto.controls.append(ft.Text(f"Errore {e}"))
            self._view.update()
    # Creo la funzione per cercare un modello di auto
    def cerca_automobili(self, e):
        # prendo l'input inserito dall'utente e lo salvo in modello
        modello = self._view.input_modello_auto.value.strip()
        # pulisco la lista per eventuali risultati già stampati in precedenza
        self._view.lista_auto.controls.clear()
        if modello == "":
            self._view.show_alert("Inserisci un nuovo modello")
            return
        # mostro le auto del modello inserito, se non li trovo stampo "nessun modello trovato"
        try:
            lista_trovate = self._model.cerca_automobili_per_modello(modello)
            if lista_trovate is None or len(lista_trovate) == 0:
                self._view.lista_auto_ricerca.controls.append(ft.Text("Nessun modello trovato"))
            else:
                for auto in lista_trovate:
                    testo = ft.Text(str(auto))
                    self._view.lista_auto_ricerca.controls.append(testo)
            self._view.update()
        except Exception as e:
            self._view.lista_auto_ricerca.controls.append(ft.Text(f"Errore {e}"))
            self._view.update()