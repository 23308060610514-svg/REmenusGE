import flet as ft

def DetalleMenuView(page: ft.Page, auth_controller, menu_controller, tipo):
    
    page.bgcolor = ft.Colors.GREY_50
    
    # Configurar según el tipo
    config = {
        "mexicana": {
            "titulo": "Comida Mexicana",
            "color": ft.Colors.RED_600,
            "obtener_platillos": menu_controller.obtener_platillos_mexicanos,
            "tabla": "mexicana"
        },
        "china": {
            "titulo": "Comida China",
            "color": ft.Colors.AMBER_700,
            "obtener_platillos": menu_controller.obtener_platillos_chinos,
            "tabla": "china"
        },
        "mariscos": {
            "titulo": "Mariscos",
            "color": ft.Colors.BLUE_600,
            "obtener_platillos": menu_controller.obtener_platillos_mariscos,
            "tabla": "mariscos"
        }
    }
    
    conf = config.get(tipo, config["mexicana"])
    
    # Obtener platillos
    platillos = conf["obtener_platillos"]()
    
    def volver():
        page.go("/dashboard")
    
    def mostrar_snackbar(mensaje, color=ft.Colors.GREEN_600):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()
    
    # Crear tarjetas de platillos
    tarjetas_platillos = []
    
    if not platillos:
        tarjetas_platillos.append(
            ft.Container(
                content=ft.Text("No hay platillos disponibles", size=16, color=ft.Colors.GREY_600),
                padding=20,
            )
        )
    
    for platillo in platillos:
        tarjeta = ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(
                            ft.Icons.FASTFOOD,
                            size=50,
                            color=conf["color"],
                        ),
                        width=80,
                        alignment=ft.alignment.center,
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                platillo['nombre'],
                                size=18,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                f"Mesa: {platillo['mesa']}",
                                size=12,
                                color=ft.Colors.GREY_600,
                            ),
                            ft.Text(
                                f"${float(platillo['precio']):.2f}",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.GREEN_700,
                            ),
                        ],
                        spacing=5,
                        expand=True,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            width=600,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            padding=15,
            margin=ft.margin.only(bottom=10),
            shadow=ft.BoxShadow(
                blur_radius=5,
                color=ft.Colors.GREY_300,
            ),
        )
        tarjetas_platillos.append(tarjeta)
    
    return ft.View(
        route=f"/menus/{tipo}",
        bgcolor=ft.Colors.GREY_50,
        appbar=ft.AppBar(
            title=ft.Text(
                conf["titulo"],
                size=24,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
            bgcolor=conf["color"],
            center_title=True,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK_ROUNDED,
                icon_color=ft.Colors.WHITE,
                on_click=lambda _: volver(),
                tooltip="Volver",
            ),
            elevation=2,
        ),
        controls=[
            ft.Column(
                [
                    ft.Container(height=20),
                    ft.Row(
                        [
                            ft.Text(
                                "Nuestros Platillos",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLUE_800,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Container(height=20),
                    ft.Column(
                        tarjetas_platillos,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                        scroll=ft.ScrollMode.AUTO,
                    ),
                    ft.Container(height=20),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            )
        ],
    )
