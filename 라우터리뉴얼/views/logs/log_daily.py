import flet as ft
from components.common.log_tabs import build_log_top_tabs, build_selectable_log_box
from components.common.three_actions import three_action_buttons


def log_daily_view(page: ft.Page, selected_date):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.WHITE

    selected_top_tab = {"index": 0}

    tab_content = ft.Container(
        width=350,
        expand=True,
    )

    selected_item = {"key": None}

    top_tabs_area = ft.Container(width=350)

    item_controls = {}

    def select_item(item_key):
        selected_item["key"] = item_key

        for key, control in item_controls.items():
            control.bgcolor = (
                ft.Colors.GREY_200 if key == selected_item["key"] else ft.Colors.WHITE
            )

        tab_content.update()

    def selectable_box(item_key, text, time_text):
        box = build_selectable_log_box(
            item_key=item_key,
            text=text,
            time_text=time_text,
            selected_key=selected_item["key"],
            on_select=select_item,
        )
        item_controls[item_key] = box
        return box

    def refresh_top_tabs():
        top_tabs_area.content = build_log_top_tabs(
            selected_index=selected_top_tab["index"],
            on_tab_change=change_top_tab,
        )

    def change_top_tab(index):
        selected_top_tab["index"] = index

        item_controls.clear()
        selected_item["key"] = None

        if index == 0:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    selectable_box("all_1", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_2", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_3", "사료 35g를 먹었습니다", "오전 07:30"),
                    selectable_box("all_4", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_5", "물 10ml를 마셨습니다", "오전 07:30"),
                ],
            )

        elif index == 1:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    selectable_box("feed_1", "아침 급여량", "오전 07:30"),
                    selectable_box("feed_2", "점심 급여량", "오후 12:30"),
                    selectable_box("feed_3", "저녁 급여량", "오후 07:00"),
                ],
            )

        elif index == 2:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    selectable_box("water_1", "오늘 음수량", "오전 07:30"),
                    selectable_box("water_2", "물 리필 기록", "오전 09:30"),
                    selectable_box("water_3", "추가 음수", "오후 01:10"),
                ],
            )

        elif index == 3:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    selectable_box("activity_1", "산책 기록", "오전 07:30"),
                    selectable_box("activity_2", "놀이 기록", "오후 02:00"),
                    selectable_box("activity_3", "저녁 산책", "오후 06:20"),
                ],
            )

        refresh_top_tabs()
        page.update()

    refresh_top_tabs()
    change_top_tab(0)

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
                            ft.Text(
                                selected_date.strftime("%Y.%m.%d"),
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.ADD,
                                icon_size=26,
                                icon_color=ft.Colors.BLACK,
                                on_click=lambda e: page.go(
                                    f"/log/daily/create?date={selected_date.isoformat()}"
                                ),
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