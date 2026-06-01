from models.MenuModel import MenuModel 

class MenuController:
    def __init__(self):
        self.menu_model = MenuModel()
    
    def obtener_platillos_mexicanos(self):
        return self.menu_model.obtener_platillos_mexicanos()
    
    def obtener_platillos_chinos(self):
        return self.menu_model.obtener_platillos_chinos()
    
    def obtener_platillos_mariscos(self):
        return self.menu_model.obtener_platillos_mariscos()