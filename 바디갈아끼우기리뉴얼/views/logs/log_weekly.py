import flet as ft
from components.common.texts import Txt
from components.common.log_tabs import apply_log_tab_change
from components.common.three_actions import three_action_buttons


def log_weekly_view(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.WHITE

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
            ("all_3", "물 10ml를 마셨습니다", "오전 07:30"),
            ("all_4", "물 10ml를 마셨습니다", "오전 07:30"),
            ("all_5", "사료 35g를 먹었습니다", "오전 07:30"),
            ("all_6", "물 10ml를 마셨습니다", "오전 07:30"),
            ("all_7", "물 10ml를 마셨습니다", "오전 07:30"),
            ("all_8", "물 10ml를 마셨습니다", "오전 07:30"),
            ("all_9", "물 10ml를 마셨습니다", "오전 07:30"),
            ("all_10", "물 10ml를 마셨습니다", "오전 07:30"),
            ("all_11", "물 10ml를 마셨습니다", "오전 07:30"),
            ("all_12", "물 10ml를 마셨습니다", "오전 07:30"),
        ],
        1: [
            ("feed_1", "아침 급여량", "오전 07:30"),
            ("feed_2", "저녁 급여량", "오전 07:30"),
            ("feed_3", "점심 급여량", "오후 12:30"),
            ("feed_4", "간식 급여량", "오후 03:00"),
            ("feed_5", "야식 급여량", "오후 09:00"),
        ],
        2: [
            ("water_1", "오늘 음수량", "오전 07:30"),
            ("water_2", "물 리필 기록", "오전 09:30"),
            ("water_3", "추가 음수", "오후 01:10"),
            ("water_4", "저녁 물 보충", "오후 07:20"),
        ],
        3: [
            ("activity_1", "산책 기록", "오전 07:30"),
            ("activity_2", "놀이 기록", "오후 02:00"),
            ("activity_3", "저녁 산책", "오후 06:20"),
            ("activity_4", "공놀이", "오후 08:10"),
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
                                "2026.04.06~04.13",
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
                ft.Container(height=12),
                top_tabs_area,
                ft.Container(
                    width=350,
                    content=ft.Divider(
                        thickness=1,
                        color=ft.Colors.GREY_300,
                    ),
                ),
                ft.Container(height=30),
                tab_content,
                three_action_buttons(bottom_margin=30, vertical_padding=8),
            ],
        ),
    )