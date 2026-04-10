import flet as ft
from components.common.texts import Txt


def menu_box(image_src, title, on_click=None):
    return ft.Container(
        width=100,
        height=86,
        bgcolor=ft.Colors.WHITE,
        border_radius=16,
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        shadow=ft.BoxShadow(
            blur_radius=15,
            spread_radius=0,
            color=ft.Colors.with_opacity(0.08, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        ),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
            controls=[
                ft.Image(src=image_src, width=38, height=38),
                Txt(
                    title,
                    size=14,
                    weight=ft.FontWeight.W_600,
                ),
            ],
        ),
    )