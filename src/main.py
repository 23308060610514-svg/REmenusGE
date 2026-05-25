import flet as ft
from controllers.UsuariosController import AuthController
from controllers.MenuController import MenuController
from view.LoginView import LoginView
from view.RegisterView import RegisterView  
from view.UsuarioView import UserView
from view.RecoverView import RecoverView
from view.MenuView import MenuView
from view.DetalleMenuView import DetalleMenuView

def start(page: ft.Page):
    page.title = "REmenus - Sistema de Menús"
    page.theme_mode = ft.ThemeMode.LIGHT 
    page.bgcolor = ft.Colors.GREY_50
    page.window_width = 1200
    page.window_height = 800
    page.window_resizable = True
    
    auth_ctrl = AuthController()
    menu_ctrl = MenuController()

    def route_change(e):
        page.views.clear()
        
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
            
        elif page.route == "/register": 
            page.views.append(RegisterView(page, auth_ctrl))
            
        elif page.route == "/recover":
            page.views.append(RecoverView(page, auth_ctrl))
            
        elif page.route == "/dashboard":
            if page.user_data:
                page.views.append(MenuView(page, auth_ctrl, menu_ctrl))
            else:
                page.go("/")
                
        elif page.route.startswith("/menus/"):
            tipo = page.route.split("/")[-1]  # mexicana, china o mariscos
            if page.user_data:
                page.views.append(DetalleMenuView(page, auth_ctrl, menu_ctrl, tipo))
            else:
                page.go("/")
            
        elif page.route == "/perfil":
            if page.user_data:
                page.views.append(UserView(page, auth_ctrl))
            else:
                page.go("/")
                
        else:
            page.views.append(
                ft.View(
                    "/404",
                    controls=[
                        ft.AppBar(title=ft.Text("Error 404"), bgcolor=ft.Colors.RED_700),
                        ft.Column([
                            ft.Icon(ft.Icons.ERROR_OUTLINE, size=100, color=ft.Colors.RED_700),
                            ft.Text("Página no encontrada", size=32, weight="bold"),
                            ft.Text(f"La ruta '{page.route}' no existe", size=16),
                            ft.Container(height=30),
                            ft.ElevatedButton(
                                "Ir al inicio", 
                                on_click=lambda _: page.go("/"),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE)
                            ),
                        ], alignment=ft.MainAxisAlignment.CENTER, 
                           horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                           expand=True)
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        page.update()
        
    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            page.window_close()
            
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")

def main():
    ft.app(target=start)

if __name__ == "__main__":
    main()
