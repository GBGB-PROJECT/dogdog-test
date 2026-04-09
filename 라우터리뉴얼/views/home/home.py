import flet as ft
from datetime import datetime
from components.common.menu_grid import menu_grid
from views.home.bottomsheet import today_record_bottomSheet


CONTENT_WIDTH = 330


def home_view(page: ft.Page):
    def card_box(content, on_click=None, top=10, bottom=10):
        return ft.Container(
            width=CONTENT_WIDTH,
            padding=ft.padding.only(left=8, right=8, top=top, bottom=bottom),
            content=ft.Container(
                padding=16,
                border_radius=18,
                bgcolor=ft.Colors.WHITE,
                shadow=ft.BoxShadow(
                    blur_radius=15,
                    spread_radius=1,
                    color=ft.Colors.with_opacity(0.10, ft.Colors.BLACK),
                    offset=ft.Offset(0, 5),
                ),
                on_click=on_click,
                content=content,
            ),
        )

    def info_chip(text):
        return ft.Container(
            padding=ft.padding.symmetric(horizontal=10, vertical=6),
            bgcolor="#EEEEEE",
            border_radius=10,
            content=ft.Text(
                text,
                size=12,
                color=ft.Colors.BLACK,
                weight=ft.FontWeight.W_500,
            ),
        )

    def goal_status(title, current, total, unit):
        return ft.Column(
            spacing=6,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Text(
                    title,
                    size=14,
                    color=ft.Colors.GREY_700,
                    weight=ft.FontWeight.W_600,
                ),
                ft.ProgressBar(
                    width=CONTENT_WIDTH - 48,
                    height=10,
                    value=current / total if total else 0,
                    bgcolor=ft.Colors.GREY_300,
                    color=ft.Colors.YELLOW_600,
                    border_radius=10,
                ),
                ft.Text(
                    f"{current}/{total}{unit}",
                    size=13,
                    color=ft.Colors.GREY_500,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        )

    def open_food_remain(e):
        page.go("/food-remain")

    def open_today_record(e):
        page.show_dialog(today_record_bottomSheet())

    def food_remain_info(current_g="???g", total_kg="???kg", days_left="??", progress=0):
        return ft.Column(
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Text(
                    "급여 중인 사료 잔여량",
                    size=17,
                    color=ft.Colors.BLACK,
                    weight=ft.FontWeight.W_600,
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            f"{current_g} / {total_kg}",
                            size=14,
                            color=ft.Colors.BLACK,
                            weight=ft.FontWeight.W_600,
                        ),
                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=10, vertical=4),
                            bgcolor=ft.Colors.GREY_200,
                            border_radius=8,
                            content=ft.Text(
                                f"{days_left}일치 남음",
                                size=12,
                                color=ft.Colors.BLACK,
                                weight=ft.FontWeight.W_500,
                            ),
                        ),
                    ],
                ),
                ft.ProgressBar(
                    width=CONTENT_WIDTH - 48,
                    height=10,
                    value=progress,
                    bgcolor=ft.Colors.GREY_300,
                    color=ft.Colors.YELLOW_600,
                    border_radius=10,
                ),
                ft.Text(
                    "예상 소진일",
                    size=12,
                    color=ft.Colors.GREY_600,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        )

    def food_remain_card():
        return card_box(
            content=food_remain_info("???g", "???kg", "??", 0),
            on_click=open_food_remain,
            top=6,
            bottom=10,
        )

    def today_record_card():
        return card_box(
            on_click=open_today_record,
            top=12,
            bottom=10,
            content=ft.Column(
                spacing=14,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "오늘의 기록",
                                size=18,
                                weight=ft.FontWeight.W_600,
                                color=ft.Colors.BLACK,
                            ),
                            ft.Text(
                                datetime.now().strftime("%Y.%m.%d"),
                                size=14,
                                color=ft.Colors.GREY_600,
                                weight=ft.FontWeight.W_500,
                            ),
                        ],
                    ),
                    ft.Row(
                        spacing=8,
                        wrap=True,
                        controls=[
                            info_chip("급여량: 0g"),
                            info_chip("음수량: 0ml"),
                            info_chip("산책: 0분"),
                        ],
                    ),
                    ft.Column(
                        spacing=12,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            goal_status("목표 활동량", 0, 90, "분"),
                            goal_status("목표 칼로리", 0, 310, "kcal"),
                        ],
                    ),
                ],
            ),
        )

    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        alignment=ft.Alignment(0, -1),
        content=ft.Container(
            width=CONTENT_WIDTH,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    today_record_card(),
                    food_remain_card(),
                    menu_grid(page, content_width=CONTENT_WIDTH, top=6, bottom=8),
                    ft.Container(height=16),
                ],
            ),
        ),
    )