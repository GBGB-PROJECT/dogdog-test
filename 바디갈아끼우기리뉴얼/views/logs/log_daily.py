import flet as ft
from components.common.texts import Txt
from components.common.log_tabs import apply_log_tab_change
from components.common.log_data import DAILY_LOG_TAB_DATA
from components.common.three_actions import three_action_buttons
from components.common.layout_tokens import (
    WIDE_CONTENT_WIDTH,
    PAGE_SIDE_PADDING,
    SECTION_GAP,
    LARGE_GAP,
)
from components.common.colors import (
    TEXT_PRIMARY,
    SURFACE_WHITE,
    BORDER_LIGHT,
)


def log_daily_view(page: ft.Page, selected_date):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = SURFACE_WHITE

    selected_top_tab = {"index": 0}
    selected_item = {"key": None}

    top_tabs_area = ft.Container(width=WIDE_CONTENT_WIDTH)
    tab_content = ft.Container(
        width=WIDE_CONTENT_WIDTH,
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

    def daily_header():
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
                        on_click=lambda e: page.open_log_daily_create(selected_date),
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
                daily_header(),
                ft.Container(height=SECTION_GAP),
                top_tabs_area,
                ft.Container(
                    width=WIDE_CONTENT_WIDTH,
                    content=ft.Divider(
                        thickness=1,
                        color=BORDER_LIGHT,
                    ),
                ),
                ft.Container(height=LARGE_GAP + LARGE_GAP - 2),
                tab_content,
                three_action_buttons(bottom_margin=30, vertical_padding=8),
            ],
        ),
    )