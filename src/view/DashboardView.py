import flet as ft
from models.MenuModel import MenuModel

def DashboardView(page: ft.Page, auth_controller):
    
    page.bgcolor = ft.Colors.GREY_50
    page.title = "REmenus - Dashboard"
    
    # Inicializar carrito en user_data si no existe
    if page.user_data is None:
        page.user_data = {}
    if 'carrito' not in page.user_data:
        page.user_data['carrito'] = []
    
    # Crear el modelo directamente
    menu_model = MenuModel()
    
    # Obtener nombre del usuario
    nombre_usuario = page.user_data.get('nombre', 'Usuario') if page.user_data else "Usuario"
    
    def mostrar_snackbar(mensaje, color=ft.Colors.GREEN_600):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()
    
    def cerrar_sesion(e):
        page.user_data = None
        page.go("/")
        mostrar_snackbar("Sesión cerrada correctamente", ft.Colors.BLUE_600)
    
    def ir_a_perfil(e):
        page.go("/perfil")
    
    def ir_al_carrito(e):
        page.go("/carrito")
    
    def agregar_al_carrito(platillo):
        # Agregar al carrito en user_data
        page.user_data['carrito'].append(platillo)
        total_items = len(page.user_data['carrito'])
        total_precio = sum(float(item['precio']) for item in page.user_data['carrito'])
        mostrar_snackbar(f"✓ {platillo['nombre']} agregado al carrito (Total: {total_items} items - ${total_precio:.2f})", ft.Colors.GREEN_600)
        
        # Actualizar el contador del botón del carrito
        btn_carrito.content = ft.Text(f"🛒 {total_items}", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        page.update()
    
    # Obtener platillos de cada categoría
    platillos_mexicanos = menu_model.obtener_platillos_mexicanos()
    platillos_chinos = menu_model.obtener_platillos_chinos()
    platillos_mariscos = menu_model.obtener_platillos_mariscos()
    
    # ========== FUNCIÓN PARA CREAR TARJETA DE PLATILLO ==========
    def crear_tarjeta_platillo(platillo, color):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(ft.Icons.FASTFOOD, size=40, color=color),
                        width=60,
                    ),
                    ft.Column(
                        [
                            ft.Text(platillo['nombre'], size=18, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Mesa: {platillo['mesa']}", size=12, color=ft.Colors.GREY_600),
                            ft.Text(f"${float(platillo['precio']):.2f}", size=16, 
                                    weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                        ],
                        spacing=5,
                        expand=True,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.ADD_SHOPPING_CART,
                        icon_color=color,
                        icon_size=30,
                        on_click=lambda e, p=platillo: agregar_al_carrito(p),
                        tooltip="Agregar al carrito",
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            width=500,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            padding=15,
            margin=ft.margin.only(bottom=10),
            shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.GREY_300),
        )
    
    # ========== CREAR SECCIONES DE CATEGORÍAS ==========
    
    # Sección Comida Mexicana
    tarjetas_mexicanas = []
    for platillo in platillos_mexicanos:
        tarjetas_mexicanas.append(crear_tarjeta_platillo(platillo, ft.Colors.RED_600))
    
    seccion_mexicana = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [ft.Text("🌮", size=30), ft.Text("Comida Mexicana", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_600)],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(color=ft.Colors.RED_600, thickness=2),
                ft.Container(height=10),
                ft.Column(tarjetas_mexicanas if tarjetas_mexicanas else [ft.Text("No hay platillos disponibles")], spacing=10),
            ],
            spacing=0,
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        padding=20,
        margin=ft.margin.only(bottom=20),
    )
    
    # Sección Comida China
    tarjetas_chinas = []
    for platillo in platillos_chinos:
        tarjetas_chinas.append(crear_tarjeta_platillo(platillo, ft.Colors.AMBER_700))
    
    seccion_china = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [ft.Text("🥡", size=30), ft.Text("Comida China", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.AMBER_700)],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(color=ft.Colors.AMBER_700, thickness=2),
                ft.Container(height=10),
                ft.Column(tarjetas_chinas if tarjetas_chinas else [ft.Text("No hay platillos disponibles")], spacing=10),
            ],
            spacing=0,
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        padding=20,
        margin=ft.margin.only(bottom=20),
    )
    
    # Sección Mariscos
    tarjetas_mariscos = []
    for platillo in platillos_mariscos:
        tarjetas_mariscos.append(crear_tarjeta_platillo(platillo, ft.Colors.BLUE_600))
    
    seccion_mariscos = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [ft.Text("🦐", size=30), ft.Text("Mariscos", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_600)],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(color=ft.Colors.BLUE_600, thickness=2),
                ft.Container(height=10),
                ft.Column(tarjetas_mariscos if tarjetas_mariscos else [ft.Text("No hay platillos disponibles")], spacing=10),
            ],
            spacing=0,
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        padding=20,
        margin=ft.margin.only(bottom=20),
    )
    
    # Botón del carrito con contador
    total_items = len(page.user_data['carrito'])
    btn_carrito = ft.Container(
        content=ft.Text(f"🛒 {total_items}", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
        bgcolor=ft.Colors.GREEN_600,
        border_radius=20,
        padding=10,
        on_click=ir_al_carrito,
    )
    
    btn_perfil = ft.IconButton(
        icon=ft.Icons.PERSON_ROUNDED,
        icon_color=ft.Colors.WHITE,
        on_click=ir_a_perfil,
        tooltip="Mi Perfil",
    )
    
    btn_cerrar = ft.IconButton(
        icon=ft.Icons.LOGOUT_ROUNDED,
        icon_color=ft.Colors.WHITE,
        on_click=cerrar_sesion,
        tooltip="Cerrar Sesión",
    )
    
    # ========== VISTA PRINCIPAL CON SCROLL ==========
    return ft.View(
        route="/dashboard",
        bgcolor=ft.Colors.GREY_50,
        appbar=ft.AppBar(
            title=ft.Text("REmenus - Dashboard", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True,
            actions=[btn_perfil, btn_carrito, btn_cerrar],
            elevation=4,
        ),
        controls=[
            ft.ListView(
                [
                    # Tarjeta de bienvenida
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(f"¡Bienvenido, {nombre_usuario}!", 
                                        size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                                ft.Text("Explora nuestros deliciosos platillos", 
                                        size=16, color=ft.Colors.GREY_600),
                            ],
                            spacing=5,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,
                        bgcolor=ft.Colors.BLUE_50,
                        border_radius=15,
                        margin=ft.margin.only(bottom=20),
                    ),
                    
                    # Sección Comida Mexicana
                    seccion_mexicana,
                    
                    # Sección Comida China
                    seccion_china,
                    
                    # Sección Mariscos
                    seccion_mariscos,
                    
                    # Pie de página
                    ft.Container(
                        content=ft.Text("© 2024 REMenus - Todos los derechos reservados", 
                                       size=12, color=ft.Colors.GREY_500),
                        padding=20,
                    ),
                ],
                spacing=0,
                height=page.window_height,
                auto_scroll=False,
            ),
        ],
    )