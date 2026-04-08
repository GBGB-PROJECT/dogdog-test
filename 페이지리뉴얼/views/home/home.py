import flet as ft
from datetime import datetime
from components.common.menu_box import menu_box
from views.home.bottomsheet import (
    select_feeding_bottomSheet,
    water_bottomSheet,
    today_record_bottomSheet,
)


# body
def home_view(page: ft.Page):
    content_width = 330

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
                    width=content_width - 48,
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

    def handle_open_food_remain(e):
        page.open_food_remain()

    def remain_info_box(current_g="???g", total_kg="???kg", days_left="??", progress=0):
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
                            # alignment=ft.Alignment(0, 0),
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
                    width=content_width - 48,
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

    def remain_card(current_g="???g", total_kg="???kg", days_left="??", progress=0):
        return ft.Container(
            width=content_width,
            padding=ft.padding.only(left=8, right=8, top=6, bottom=10),
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
                on_click=handle_open_food_remain,
                content=remain_info_box(
                    current_g=current_g,
                    total_kg=total_kg,
                    days_left=days_left,
                    progress=progress,
                ),
            ),
        )

    today_summary_card = ft.Container(
        width=content_width,
        padding=ft.padding.only(left=8, right=8, top=12, bottom=10),
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
            on_click=lambda e: page.show_dialog(today_record_bottomSheet()),

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
        ),
    )

    log_button = ft.Container(
        width=content_width,
        padding=ft.padding.only(left=4, right=4, top=6, bottom=8),
        content=ft.Column(
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=8,
                    controls=[
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
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=8,
                    controls=[
                        menu_box("poop.png", "위생/배변"),
                        menu_box("injection.png", "건강기록"),
                        menu_box("note.png", "상태기록"),
                    ],
                ),
            ],
        ),
    )

    return ft.Container(
        expand=True,
        # width=float("inf"),
        bgcolor=ft.Colors.WHITE,
        alignment=ft.Alignment(0, -1),
        content=ft.Container(
            width=content_width,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    today_summary_card,
                    remain_card("???g", "???kg", "??", 0),
                    log_button,
                    ft.Container(height=16),
                ],
            ),
        ),
    )