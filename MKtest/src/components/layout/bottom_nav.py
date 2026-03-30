import flet as ft
from main import render_page

def bottom_nav():
    return ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.YELLOW_600,
        inactive_color=ft.Colors.BROWN_200,
        active_color=ft.Colors.BROWN_700,
        # selected_index=current_index,   # 추가
        on_change= lambda e : render_page(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH, label="Log"),
            ft.NavigationBarDestination(
                icon=ft.Icons.FOOD_BANK_ROUNDED,
                selected_icon=ft.Icons.SHOPPING_CART,
                label="Shop",
            ),
            ft.NavigationBarDestination(icon=ft.Icons.MESSENGER_OUTLINE_ROUNDED, label="Contents"),
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON_OUTLINE,
                selected_icon=ft.Icons.PERSON,
                label="MyPage"
            ),
        ],
    ) 