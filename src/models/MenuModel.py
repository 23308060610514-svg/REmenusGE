from .databaseModel import Database

class MenuModel:
    def __init__(self):
        self.db = Database()
    
    def obtener_platillos_mexicanos(self):
        """Obtiene todos los platillos de comida mexicana"""
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT ID_comidaMex as id, Menu as nombre, PrecioMex as precio, MezaNum1 as mesa FROM restaurantemex")
        platillos = cursor.fetchall()
        conn.close()
        return platillos
    
    def obtener_platillos_chinos(self):
        """Obtiene todos los platillos de comida china"""
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT ID_comidaChin as id, Menu as nombre, PrecioChin as precio, MezaNum2 as mesa FROM restaurantechin")
        platillos = cursor.fetchall()
        conn.close()
        return platillos
    
    def obtener_platillos_mariscos(self):
        """Obtiene todos los platillos de mariscos"""
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT ID_comidaMar as id, Menu as nombre, PrecioMari as precio, MezaNum3 as mesa FROM restaurantemaris")
        platillos = cursor.fetchall()
        conn.close()
        return platillos
    
    def agregar_platillo_mexicano(self, id_usuario, menu, precio, mesa):
        """Agrega un nuevo platillo mexicano"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO restaurantemex (ID_usuario, Menu, PrecioMex, MezaNum1) VALUES (%s, %s, %s, %s)",
                (id_usuario, menu, precio, mesa)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
    
    def agregar_platillo_chino(self, id_usuario, menu, precio, mesa):
        """Agrega un nuevo platillo chino"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO restaurantechin (ID_usuario, Menu, PrecioChin, MezaNum2) VALUES (%s, %s, %s, %s)",
                (id_usuario, menu, precio, mesa)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
    
    def agregar_platillo_marisco(self, id_usuario, menu, precio, mesa):
        """Agrega un nuevo platillo de mariscos"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO restaurantemaris (ID_usuario, Menu, PrecioMari, MezaNum3) VALUES (%s, %s, %s, %s)",
                (id_usuario, menu, precio, mesa)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
    
    def eliminar_platillo_mexicano(self, id_platillo):
        """Elimina un platillo mexicano"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM restaurantemex WHERE ID_comidaMex = %s", (id_platillo,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
    
    def eliminar_platillo_chino(self, id_platillo):
        """Elimina un platillo chino"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM restaurantechin WHERE ID_comidaChin = %s", (id_platillo,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
    
    def eliminar_platillo_marisco(self, id_platillo):
        """Elimina un platillo de mariscos"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM restaurantemaris WHERE ID_comidaMar = %s", (id_platillo,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
