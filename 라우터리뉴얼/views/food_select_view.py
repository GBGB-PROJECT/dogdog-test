import flet as ft
from views.home.bottomsheet import food_search_bottomSheet
from components.common.three_actions import three_action_buttons


def food_select_view(page: ft.Page):
    selected_food = {
        "name": "등록할 사료를 검색하세요",
    }

    selected_food_text = ft.Text(
        selected_food["name"],
        color=ft.Colors.GREY_600,
        size=14,
        overflow=ft.TextOverflow.ELLIPSIS,
    )

    def handle_food_selected(food_id, food_name):
        selected_food["id"] = food_id
        selected_food["name"] = food_name
        selected_food_text.value = food_name
        selected_food_text.color = ft.Colors.BLACK
        page.update()

    def open_food_search_sheet(e):
        bs = food_search_bottomSheet(
            page=page,
            on_food_selected=handle_food_selected,
        )
        page.show_dialog(bs)

    def food_info_input_field(hint_text):
        return ft.TextField(
            hint_text=hint_text,
            border_radius=9,
            width=float("inf"), # 👈  없으면 상자 길이 짧아짐 
            border_color=ft.Colors.GREY_400,
        )

    # def build_action_button(text, bgcolor):
    #     return ft.Container(
    #         width=65,
    #         height=35,
    #         alignment=ft.Alignment(0, 0),
    #         border_radius=9,
    #         bgcolor=bgcolor,
    #         content=ft.Text(
    #             text,
    #             color=ft.Colors.WHITE,
    #             weight=ft.FontWeight.BOLD,
    #         ),
    #     )

    def food_selector_box():
        return ft.Container(
            width=float("inf"),
            height=56,
            padding=ft.padding.symmetric(horizontal=12),
            alignment=ft.Alignment(-1, 0),
            border_radius=9,
            border=ft.border.all(1, ft.Colors.GREY_400),
            content=selected_food_text,
            on_click=open_food_search_sheet,
        )

    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.START,
            spacing=12,
            controls=[
                food_selector_box(),
                food_info_input_field("사료 총 무게(g)"),
                food_info_input_field("사료 잔여량(g)"),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            ft.Icons.CALENDAR_MONTH_OUTLINED,
                            size=18,
                            color=ft.Colors.BLACK54,
                        ),
                        ft.Text("2026.03.19", color=ft.Colors.BLACK54),
                    ],
                ),
                three_action_buttons(bottom_margin=30, vertical_padding=8),
            ],
        ),
    )