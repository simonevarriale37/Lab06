import flet as ft
import mysql.connector
from model.model import Autonoleggio
from UI.view import View
from UI.controller import Controller

'''
DA ESEGUIRE
'''

def main(page: ft.Page):
    my_model = Autonoleggio("Polito Rent", "Alessandro Visconti")
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()


ft.app(target=main)
