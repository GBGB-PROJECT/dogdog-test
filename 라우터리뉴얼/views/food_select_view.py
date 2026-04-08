import flet as ft
from views.home.bottomsheet import food_search_bottomSheet


def food_select_view(page: ft.Page):
    selected_food = {
        "id": None,
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

        if bs not in page.overlay:
            page.overlay.append(bs)

        bs.open = True
        page.update()

    def build_input_field(hint_text):
        return ft.TextField(
            hint_text=hint_text,
            border_radius=9,
            width=float("inf"),
            border_color=ft.Colors.GREY_400,
        )

    def build_action_button(text, bgcolor):
        return ft.Container(
            width=65,
            height=35,
            alignment=ft.Alignment(0, 0),
            border_radius=9,
            bgcolor=bgcolor,
            content=ft.Text(
                text,
                color=ft.Colors.WHITE,
                weight=ft.FontWeight.BOLD,
            ),
        )

    def build_food_selector():
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
                build_food_selector(),
                build_input_field("사료 총 무게(g)"),
                build_input_field("사료 잔여량(g)"),
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
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                    controls=[
                        build_action_button("수정", ft.Colors.YELLOW_600),
                        build_action_button("삭제", ft.Colors.YELLOW_600),
                        build_action_button("저장", ft.Colors.GREY_400),
                    ],
                ),
            ],
        ),
    )