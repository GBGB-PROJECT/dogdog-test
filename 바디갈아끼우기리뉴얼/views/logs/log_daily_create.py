import flet as ft
from components.common.texts import Txt
from components.common.log_tabs import apply_log_tab_change
from components.common.log_data import DAILY_LOG_TAB_DATA
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

    apply_log_tab_change(
        0,
        selected_top_tab,
        selected_item,
        item_controls,
        tab_content,
        top_tabs_area,
        DAILY_LOG_TAB_DATA,
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