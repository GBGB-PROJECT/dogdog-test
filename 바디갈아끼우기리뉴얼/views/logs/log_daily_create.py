import flet as ft
from components.common.texts import Txt
from components.common.log_tabs import apply_log_tab_change
from components.common.three_actions import three_action_buttons
from components.common.menu_grid import menu_grid


def log_daily_create_view(page: ft.Page, selected_date):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.WHITE

    content_width = 330

    selected_top_tab = {"index": 0}
    selected_item = {"key": None}

    top_tabs_area = ft.Container(width=350)
    tab_content = ft.Container(
        width=350,
        expand=True,
    )

    item_controls = {}

    tab_data_map = {
        0: [
            ("all_1", "물 10ml를 마셨습니다", "오전 07:30"),
            ("all_2", "물 10ml를 마셨습니다", "오전 07:30"),
            ("all_3", "사료 35g를 먹었습니다", "오전 07:30"),
            ("all_4", "물 10ml를 마셨습니다", "오전 07:30"),
            ("all_5", "물 10ml를 마셨습니다", "오전 07:30"),
        ],
        1: [
            ("feed_1", "아침 급여량", "오전 07:30"),
            ("feed_2", "점심 급여량", "오후 12:30"),
            ("feed_3", "저녁 급여량", "오후 07:00"),
        ],
        2: [
            ("water_1", "오늘 음수량", "오전 07:30"),
            ("water_2", "물 리필 기록", "오전 09:30"),
            ("water_3", "추가 음수", "오후 01:10"),
        ],
        3: [
            ("activity_1", "산책 기록", "오전 07:30"),
            ("activity_2", "놀이 기록", "오후 02:00"),
            ("activity_3", "저녁 산책", "오후 06:20"),
        ],
    }

    apply_log_tab_change(
        0,
        selected_top_tab,
        selected_item,
        item_controls,
        tab_content,
        top_tabs_area,
        tab_data_map,
        page,
    )

    return ft.Container(
        expand=True,
        alignment=ft.Alignment(0, -1),
        padding=ft.padding.only(top=20, left=20, right=20, bottom=0),
        content=ft.Column(
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=350,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            Txt(
                                selected_date.strftime("%Y.%m.%d"),
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.ADD,
                                icon_size=26,
                                icon_color=ft.Colors.BLACK,
                            ),
                        ],
                    ),
                ),
                ft.Container(height=8),
                menu_grid(page, content_width=content_width, top=2, bottom=4),
                ft.Container(height=8),
                top_tabs_area,
                ft.Container(
                    width=350,
                    content=ft.Divider(
                        thickness=1,
                        color=ft.Colors.GREY_300,
                    ),
                ),
                ft.Container(height=12),
                tab_content,
                three_action_buttons(bottom_margin=12, vertical_padding=6),
            ],
        ),
    )