from models.MenuModel import MenuModel

class MenuController:
    def __init__(self):
        self.menu_model = MenuModel()
    
    def obtener_platillos_mexicanos(self):
        """Obtiene todos los platillos mexicanos"""
        return self.menu_model.obtener_platillos_mexicanos()
    
    def obtener_platillos_chinos(self):
        """Obtiene todos los platillos chinos"""
        return self.menu_model.obtener_platillos_chinos()
    
    def obtener_platillos_mariscos(self):
        """Obtiene todos los platillos de mariscos"""
        return self.menu_model.obtener_platillos_mariscos()
    
    def agregar_platillo_mexicano(self, id_usuario, menu, precio, mesa):
        return self.menu_model.agregar_platillo_mexicano(id_usuario, menu, precio, mesa)
    
    def agregar_platillo_chino(self, id_usuario, menu, precio, mesa):
        return self.menu_model.agregar_platillo_chino(id_usuario, menu, precio, mesa)
    
    def agregar_platillo_marisco(self, id_usuario, menu, precio, mesa):
        return self.menu_model.agregar_platillo_marisco(id_usuario, menu, precio, mesa)
    
    def eliminar_platillo_mexicano(self, id_platillo):
        return self.menu_model.eliminar_platillo_mexicano(id_platillo)
    
    def eliminar_platillo_chino(self, id_platillo):
        return self.menu_model.eliminar_platillo_chino(id_platillo)
    
    def eliminar_platillo_marisco(self, id_platillo):
        return self.menu_model.eliminar_platillo_marisco(id_platillo)
