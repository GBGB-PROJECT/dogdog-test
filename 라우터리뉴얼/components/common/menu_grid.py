import flet as ft
from components.common.menu_box import menu_box
from views.home.bottomsheet import select_feeding_bottomSheet, water_bottomSheet


def menu_grid(page: ft.Page, content_width=330, top=6, bottom=8):
    
    # 🔴◆ 추가: 현재 열려 있는 dialog가 있으면 먼저 닫고 새로 여는 공통 함수
    def reopen_dialog(new_dialog):
        try:
            page.pop_dialog()
        except Exception:
            pass

        # 🔴◆ 추가: 새 dialog 열기
        page.show_dialog(new_dialog)

    def prevent_double_feeding_dialog(e):
        reopen_dialog(select_feeding_bottomSheet())

    def prevent_double_water_dialog(e):
        reopen_dialog(water_bottomSheet())

    menu_rows = [
        [
            menu_box(
                "dogbowl.png",
                "밥주기",
                # ☑️ 원인: 클릭할 때마다 새 BottomSheet를 즉시 생성해서 show_dialog()
                # lambda e: page.show_dialog(select_feeding_bottomSheet()),
                prevent_double_feeding_dialog, 
            ),
            menu_box(
                "waterdrop.png",
                "물주기",
                # ☑️ 원인 후보: 이것도 같은 구조라 중복 오픈 가능
                # lambda e: page.show_dialog(water_bottomSheet()),
                prevent_double_water_dialog, 
            ),
            menu_box("dogwalking.png", "활동기록"),
        ],
        [
            menu_box("poop.png", "위생/배변"),
            menu_box("injection.png", "건강기록"),
            menu_box("note.png", "상태기록"),
        ],
    ]

    return ft.Container( # 🔴◆ 이게 없으니 홈 화면이 죽고 회색으로 변함
        width=content_width,
        padding=ft.padding.only(left=4, right=4, top=top, bottom=bottom),
        content=ft.Column(
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=8,
                    controls=row_controls, # 🔴◆ 이게 없으니 홈에서 메뉴 그리드가 사라짐 
                )
                for row_controls in menu_rows # 🔴◆ 이게 없으니 홈에서 메뉴 그리드가 사라짐 
            ],
        ),
    )