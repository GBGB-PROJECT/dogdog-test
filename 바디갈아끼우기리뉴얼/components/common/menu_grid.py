import flet as ft
from components.common.menu_box import menu_box


def menu_grid(
    page: ft.Page,
    content_width=330,
    top=6,
    bottom=8,
    on_feeding_click=None,
    on_water_click=None,
    on_activity_click=None,
    on_hygiene_click=None,
    on_health_click=None,
    on_note_click=None,
):
    menu_rows = [
        [
            menu_box(
                "dogbowl.png",
                "밥주기",
                on_feeding_click,
            ),
            menu_box(
                "waterdrop.png",
                "물주기",
                on_water_click,
            ),
            menu_box(
                "dogwalking.png",
                "활동기록",
                on_activity_click,
            ),
        ],
        [
            menu_box(
                "poop.png",
                "위생/배변",
                on_hygiene_click,
            ),
            menu_box(
                "injection.png",
                "건강기록",
                on_health_click,
            ),
            menu_box(
                "note.png",
                "상태기록",
                on_note_click,
            ),
        ],
    ]

    return ft.Container(  # 🔴◆ 이게 없으니 홈 화면이 죽고 회색으로 변함
        width=content_width,
        padding=ft.padding.only(left=4, right=4, top=top, bottom=bottom),
        content=ft.Column(
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=8,
                    controls=row_controls,  # 🔴◆ 이게 없으니 홈에서 메뉴 그리드가 사라짐
                )
                for row_controls in menu_rows  # 🔴◆ 이게 없으니 홈에서 메뉴 그리드가 사라짐
            ],
        ),
    )