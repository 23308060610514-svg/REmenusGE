from .databaseModel import Database  # ← CORRECTO

class MenuModel:
    def __init__(self):
        self.db = Database()
    
    def obtener_platillos_mexicanos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT ID_comidaMex as id, Menu as nombre, PrecioMex as precio, MezaNum1 as mesa FROM restaurantemex")
        platillos = cursor.fetchall()
        conn.close()
        return platillos
    
    def obtener_platillos_chinos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT ID_comidaChin as id, Menu as nombre, PrecioChin as precio, MezaNum2 as mesa FROM restaurantechin")
        platillos = cursor.fetchall()
        conn.close()
        return platillos
    
    def obtener_platillos_mariscos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT ID_comidaMar as id, Menu as nombre, PrecioMari as precio, MezaNum3 as mesa FROM restaurantemaris")
        platillos = cursor.fetchall()
        conn.close()
        return platillos