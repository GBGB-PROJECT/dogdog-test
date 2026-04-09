import flet as ft
from components.common.menu_box import menu_box
from views.home.bottomsheet import select_feeding_bottomSheet, water_bottomSheet


def menu_grid(page: ft.Page, content_width=330, top=6, bottom=8):
    menu_rows = [
        [
            menu_box(
                "dogbowl.png",
                "밥주기",
                lambda e: page.show_dialog(select_feeding_bottomSheet()),
            ),
            menu_box(
                "waterdrop.png",
                "물주기",
                lambda e: page.show_dialog(water_bottomSheet()),
            ),
            menu_box("dogwalking.png", "활동기록"),
        ],
        [
            menu_box("poop.png", "위생/배변"),
            menu_box("injection.png", "건강기록"),
            menu_box("note.png", "상태기록"),
        ],
    ]

    return ft.Container(
        width=content_width,
        padding=ft.padding.only(left=4, right=4, top=top, bottom=bottom),
        content=ft.Column(
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=8,
                    controls=row_controls,
                )
                for row_controls in menu_rows
            ],
        ),
    )