import flet as ft
from components.common.texts import Txt
from components.common.log_tabs import apply_log_tab_change
from components.common.log_data import DAILY_LOG_TAB_DATA
from components.common.three_actions import three_action_buttons
from components.common.menu_grid import menu_grid
from components.common.dialog_utils import reopen_dialog
from views.home.bottomsheet import select_feeding_bottomSheet, water_bottomSheet
from components.common.layout_tokens import (
    CONTENT_WIDTH,
    WIDE_CONTENT_WIDTH,
    PAGE_SIDE_PADDING,
    SECTION_GAP,
    SMALL_GAP,
)
from components.common.colors import (
    TEXT_PRIMARY,
    SURFACE_WHITE,
    BORDER_LIGHT,
)


def log_daily_create_view(page: ft.Page, selected_date):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = SURFACE_WHITE

    content_width = CONTENT_WIDTH

    selected_top_tab = {"index": 0}
    selected_item = {"key": None}

    top_tabs_area = ft.Container(width=WIDE_CONTENT_WIDTH)
    tab_content = ft.Container(
        width=WIDE_CONTENT_WIDTH,
        expand=True,
    )

    item_controls = {}

    def open_feeding_sheet(e):
        reopen_dialog(page, select_feeding_bottomSheet())

    def open_water_sheet(e):
        reopen_dialog(page, water_bottomSheet())

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

    def create_header():
        return ft.Container(
            width=WIDE_CONTENT_WIDTH,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    Txt(
                        selected_date.strftime("%Y.%m.%d"),
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=TEXT_PRIMARY,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        icon_size=26,
                        icon_color=TEXT_PRIMARY,
                    ),
                ],
            ),
        )

    return ft.Container(
        expand=True,
        alignment=ft.Alignment(0, -1),
        padding=ft.padding.only(
            top=PAGE_SIDE_PADDING,
            left=PAGE_SIDE_PADDING,
            right=PAGE_SIDE_PADDING,
            bottom=0,
        ),
        content=ft.Column(
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                create_header(),
                ft.Container(height=SMALL_GAP),
                menu_grid(
                    page,
                    content_width=content_width,
                    top=2,
                    bottom=4,
                    on_feeding_click=open_feeding_sheet,
                    on_water_click=open_water_sheet,
                ),
                ft.Container(height=SMALL_GAP),
                top_tabs_area,
                ft.Container(
                    width=WIDE_CONTENT_WIDTH,
                    content=ft.Divider(
                        thickness=1,
                        color=BORDER_LIGHT,
                    ),
                ),
                ft.Container(height=SECTION_GAP),
                tab_content,
                three_action_buttons(bottom_margin=12, vertical_padding=6),
            ],
        ),
    )