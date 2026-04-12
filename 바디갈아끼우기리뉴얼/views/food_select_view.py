import flet as ft
from components.common.texts import Txt
from components.common.three_actions import three_action_buttons
from components.common.colors import (
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    SURFACE_WHITE,
    BORDER_MEDIUM,
)
from views.home.bottomsheet import food_search_bottomSheet
from views.home.bottomsheet_props import sheet_text_field


def food_select_view(page: ft.Page):
    selected_food = {
        "id": None,
        "name": "등록할 사료를 검색하세요",
    }

    selected_food_text = Txt(
        selected_food["name"],
        color=TEXT_SECONDARY,
        size=14,
        overflow=ft.TextOverflow.ELLIPSIS,
    )

    def handle_food_selected(food_id, food_name):
        selected_food["id"] = food_id
        selected_food["name"] = food_name
        selected_food_text.value = food_name
        selected_food_text.color = TEXT_PRIMARY
        page.update()

    def open_food_search_sheet(e):
        bs = food_search_bottomSheet(
            page=page,
            on_food_selected=handle_food_selected,
        )
        page.show_dialog(bs)

    def food_selector_box():
        return ft.Container(
            width=float("inf"),  # ☑️ 체크: 이게 있어야 검색 상자가 부모 너비만큼 길게 늘어남
            height=56,
            padding=ft.padding.symmetric(horizontal=12),
            alignment=ft.Alignment(-1, 0),
            border_radius=9,
            border=ft.border.all(1, BORDER_MEDIUM),
            content=selected_food_text,
            on_click=open_food_search_sheet,
        )

    def registered_date_row():
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Icon(
                    ft.Icons.CALENDAR_MONTH_OUTLINED,
                    size=18,
                    color=ft.Colors.BLACK54,
                ),
                Txt("2026.03.19", color=ft.Colors.BLACK54),
            ],
        )

    return ft.Container(
        expand=True,
        bgcolor=SURFACE_WHITE,
        padding=20,  # ☑️ 체크: 바깥 여백만 주고 전체 화면 너비를 그대로 쓰게 해야 입력칸이 길게 보임
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.START,
            spacing=12,
            controls=[
                food_selector_box(),
                sheet_text_field(hint_text="사료 총 무게(g)"),  # ☑️ 체크: TextField는 기본적으로 부모 폭을 따라감
                sheet_text_field(hint_text="사료 잔여량(g)"),   # ☑️ 체크: 그래서 부모를 좁게 만들지만 않으면 길게 유지됨
                registered_date_row(),
                three_action_buttons(bottom_margin=30, vertical_padding=8),
            ],
        ),
    )