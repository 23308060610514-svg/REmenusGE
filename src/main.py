import flet as ft
from controllers.UsuariosController import AuthController
from view.LoginView import LoginView
from view.RegisterView import RegisterView  
from view.UsuarioView import UserView

def start(page: ft.Page):
    page.title = "Sistema SIGE"
    # Se recomienda configurar el tema aquí para que sea global
    page.theme_mode = ft.ThemeMode.LIGHT 
    
    auth_ctrl = AuthController()

    def route_change(e):
        # Limpiamos las vistas para manejar una navegación limpia
        page.views.clear()
        
        # Lógica de enrutamiento
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/register": 
            page.views.append(RegisterView(page, auth_ctrl))
        elif page.route == "/perfil":
            page.views.append(UserView(page, auth_ctrl))
        else:
            # Vista por defecto para rutas inexistentes (404)
            page.views.append(
                ft.View(
                    "/404",
                    controls=[
                        ft.AppBar(title=ft.Text("Error"), bgcolor=ft.Colors.RED_ACCENT),
                        ft.Text("Error: Ruta no encontrada", size=30),
                        ft.ElevatedButton("Volver al inicio", on_click=lambda _: page.go("/"))
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

        page.update()
        
    def view_pop(e):
        # Maneja el botón "Atrás" del navegador o del sistema
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
            
    # Asignación de eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Inicialización correcta:
    # page.go dispara el evento route_change automáticamente.
    # Si ya estamos en "/", lo forzamos manualmente una vez.
    if page.route == "/":
        route_change(None)
    else:
        page.go(page.route) # Mantiene la ruta si el usuario refresca en /perfil, por ejemplo.

def main():
    # Es mejor definir el target directamente aquí
    ft.app(target=start)

if __name__ == "__main__":
    main()