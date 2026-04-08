import flet as ft
from datetime import datetime
from components.common.menu_box import menu_box
from views.home.bottomsheet import (
    select_feeding_bottomSheet,
    water_bottomSheet,
    today_record_bottomSheet,
)


CONTENT_WIDTH = 330


def home_view(page: ft.Page):
    # ============================================================
    # ✅ 공통 작은 UI
    # ============================================================
    def card_shell(content, on_click=None, top=10, bottom=10):
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

    # ============================================================
    # ✅ 이동 / 이벤트
    # ============================================================
    def open_food_remain(e):
        page.go("/food-remain")

    def open_today_record(e):
        page.show_dialog(today_record_bottomSheet())

    # ============================================================
    # ✅ 사료 잔여량 카드
    # ============================================================
    def build_remain_info(current_g="???g", total_kg="???kg", days_left="??", progress=0):
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

    def build_remain_card():
        return card_shell(
            content=build_remain_info("???g", "???kg", "??", 0),
            on_click=open_food_remain,
            top=6,
            bottom=10,
        )

    # ============================================================
    # ✅ 오늘의 기록 카드
    # ============================================================
    def build_today_summary_card():
        return card_shell(
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

    # ============================================================
    # ✅ 기록 버튼 영역
    # ============================================================
    def build_log_button_grid():
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
            width=CONTENT_WIDTH,
            padding=ft.padding.only(left=4, right=4, top=6, bottom=8),
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

    # ============================================================
    # ✅ 최종 화면
    # ============================================================
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
                    build_today_summary_card(),
                    build_remain_card(),
                    build_log_button_grid(),
                    ft.Container(height=16),
                ],
            ),
        ),
    )