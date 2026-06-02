import flet as ft

def CarritoView(page: ft.Page, auth_controller):
    
    page.bgcolor = ft.Colors.GREY_50
    page.title = "REmenus - Carrito"
    
    # Inicializar carrito en user_data si no existe
    if page.user_data is None:
        page.user_data = {}
    if 'carrito' not in page.user_data:
        page.user_data['carrito'] = []
    
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
    
    def eliminar_del_carrito(index):
        platillo = page.user_data['carrito'].pop(index)
        mostrar_snackbar(f"✗ {platillo['nombre']} eliminado del carrito", ft.Colors.RED_600)
        page.go("/carrito")  # Recargar la vista
    
    def vaciar_carrito(e):
        page.user_data['carrito'].clear()
        mostrar_snackbar("Carrito vaciado correctamente", ft.Colors.ORANGE_600)
        page.go("/carrito")
    
    def realizar_pedido(e):
        if not page.user_data['carrito']:
            mostrar_snackbar("El carrito está vacío", ft.Colors.RED_600)
            return
        
        total = sum(float(item['precio']) for item in page.user_data['carrito'])
        mostrar_snackbar(f"✓ Pedido realizado por ${total:.2f}. ¡Gracias por tu compra!", ft.Colors.GREEN_600)
        page.user_data['carrito'].clear()
        page.go("/dashboard")
    
    # Crear lista de items del carrito
    items_carrito = []
    total = 0
    carrito = page.user_data['carrito']  # Referencia local
    
    for i, item in enumerate(carrito):
        subtotal = float(item['precio'])
        total += subtotal
        
        tarjeta = ft.Container(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.FASTFOOD, size=40, color=ft.Colors.BLUE_600),
                    ft.Column(
                        [
                            ft.Text(item['nombre'], size=18, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Mesa: {item['mesa']}", size=12, color=ft.Colors.GREY_600),
                            ft.Text(f"${subtotal:.2f}", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                        ],
                        spacing=5,
                        expand=True,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        icon_color=ft.Colors.RED_600,
                        icon_size=30,
                        on_click=lambda e, idx=i: eliminar_del_carrito(idx),
                        tooltip="Eliminar",
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            padding=15,
            margin=ft.margin.only(bottom=10),
            shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.GREY_300),
        )
        items_carrito.append(tarjeta)
    
    # Si el carrito está vacío
    if not items_carrito:
        items_carrito.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.SHOPPING_CART, size=80, color=ft.Colors.GREY_400),
                        ft.Text("Tu carrito está vacío", size=20, color=ft.Colors.GREY_600),
                        ft.Text("Agrega platillos desde el Dashboard", size=14, color=ft.Colors.GREY_500),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                ),
                padding=50,
                bgcolor=ft.Colors.WHITE,
                border_radius=15,
            )
        )
    
    # Botones
    btn_volver = ft.IconButton(
        icon=ft.Icons.ARROW_BACK,
        icon_color=ft.Colors.WHITE,
        on_click=lambda _: volver(),
        tooltip="Volver",
    )
    
    btn_vaciar = ft.ElevatedButton(
        "VACIAR CARRITO",
        icon=ft.Icons.DELETE_SWEEP,
        on_click=vaciar_carrito,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.RED_600,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    
    btn_comprar = ft.ElevatedButton(
        "REALIZAR PEDIDO",
        icon=ft.Icons.SHOPPING_CART_CHECKOUT,
        on_click=realizar_pedido,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_600,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    
    return ft.View(
        route="/carrito",
        bgcolor=ft.Colors.GREY_50,
        appbar=ft.AppBar(
            title=ft.Text("REmenus - Mi Carrito", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True,
            leading=btn_volver,
            elevation=4,
        ),
        controls=[
            ft.Column(
                [
                    ft.Container(height=10),
                    
                    # Resumen del carrito
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Text(f"📦 Items: {len(carrito)}", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(f"💰 Total: ${total:.2f}", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        padding=15,
                        bgcolor=ft.Colors.BLUE_50,
                        border_radius=15,
                        margin=ft.margin.only(bottom=10),
                    ),
                    
                    # Lista de items
                    ft.Column(items_carrito, scroll=ft.ScrollMode.AUTO, spacing=10, expand=True),
                    
                    # Botones de acción
                    ft.Row(
                        [btn_vaciar, btn_comprar],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    
                    ft.Container(height=20),
                ],
                expand=True,
            )
        ],
    )