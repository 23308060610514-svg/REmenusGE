import flet as ft
from controllers.UsuariosController import AuthController
from view.LoginView import LoginView
from view.RegisterView import RegisterView  
from view.UsuarioView import UserView
from view.RecoverView import RecoverView

def start(page: ft.Page):
    page.title = "Sistema REMenus"
    page.theme_mode = ft.ThemeMode.LIGHT 
    page.bgcolor = ft.Colors.GREY_50
    page.window_width = 1000
    page.window_height = 700
    page.window_resizable = True
    
    auth_ctrl = AuthController()

    def route_change(e):
        print(f"📍 Ruta: {page.route}")
    
    # Crear la vista según la ruta
        if page.route == "/":
            view = LoginView(page, auth_ctrl)
        elif page.route == "/register": 
            view = RegisterView(page, auth_ctrl)
        elif page.route == "/recover":
            view = RecoverView(page, auth_ctrl)
        elif page.route == "/perfil":
            view = UserView(page, auth_ctrl)
        else:
        # ✅ CORREGIDO - Versión más simple
            view = ft.View(
                "/404",
                ft.AppBar(title=ft.Text("Error"), bgcolor=ft.Colors.RED_ACCENT),
                ft.Column(
                    [
                        ft.Text("Error: Ruta no encontrada", size=30),
                        ft.Text(f"La ruta '{page.route}' no existe", size=16),
                        ft.ElevatedButton("Volver al inicio", on_click=lambda _: page.go("/"))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                ),
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
    
    # Asignar la vista
        page.views.clear()
        page.views.append(view)
        page.update()
    
    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    # Forzar la primera carga
    page.route = "/"
    route_change(None)  # Llamada manual

def main():
    ft.app(target=start)

if __name__ == "__main__":
    main()

