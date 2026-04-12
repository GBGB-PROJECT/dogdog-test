import asyncio
import flet as ft
from components.common.banner import banner
from components.common.texts import Txt
from components.common.layout_tokens import (
    CONTENT_WIDTH,
    CARD_RADIUS,
    OUTER_PAGE_PADDING,
    LARGE_GAP,
    MEDIUM_GAP,
)
from components.common.colors import (
    TEXT_PRIMARY,
    SURFACE_WHITE,
    BORDER_LIGHT,
)


MENU_ITEMS = [
    ("내 정보", ft.Icons.PERSON_OUTLINE),
    ("마이 쇼핑", ft.Icons.STOREFRONT_OUTLINED),
    ("공지사항", ft.Icons.NOTIFICATIONS_NONE),
    ("문의하기", ft.Icons.HELP_OUTLINE),
]


def white_long_box(
    text,
    left_icon=None,
    bgcolor=SURFACE_WHITE,
    text_color=TEXT_PRIMARY,
    on_click=None,
    show_left_icon=True,
    show_chevron=True,
    show_border=True, # 👉 추가: 테두리 표시 여부 제어
):
    left_controls = []

    if show_left_icon:
        left_controls.append(
            ft.Icon(left_icon, color=text_color, size=20)
        )

    left_controls.append(
        Txt(
            text,
            size=14,
            weight=ft.FontWeight.W_500,
            color=text_color,
        )
    )

    return ft.Container(
        width=CONTENT_WIDTH,
        height=64,
        bgcolor=bgcolor,
        border=ft.border.all(1, BORDER_LIGHT) if show_border else None, # 👉 추가: 조건부 border
        border_radius=CARD_RADIUS,
        padding=ft.padding.symmetric(horizontal=16),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    spacing=10,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=left_controls,
                ),
                ft.Icon(
                    ft.Icons.CHEVRON_RIGHT,
                    color=text_color,
                    size=22,
                ) if show_chevron else ft.Container(width=22),
            ],
        ),
    )


def mypage_view(page: ft.Page):
    selected_banner = {"index": None}
    banner_area = ft.Column(
        spacing=MEDIUM_GAP,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    def change_selected_banner(index):
        selected_banner["index"] = index
        banner_area.controls = build_banners()
        page.update()

    def select_banner(index):
        def handler(e):
            change_selected_banner(index)
        return handler

    async def select_and_open_food_remain(e):
        change_selected_banner(1)
        await asyncio.sleep(0.3)
        page.open_food_remain()

    def build_banners():
        return [
            banner(
                image_src="대추.jpg",
                text="내 반려동물 정보",
                selected=(selected_banner["index"] == 0),
                on_click=select_banner(0),
            ),
            banner(
                text="급여중인 제품 보러가기",
                selected=(selected_banner["index"] == 1),
                on_click=select_and_open_food_remain,
            ),
        ]

    def build_menu_controls():
        controls = []

        for text, icon in MENU_ITEMS:
            controls.append(
                white_long_box(
                    text,
                    left_icon=icon,
                    show_border=False,  # 👉 추가: 메뉴 전부 테두리 제거
                )
            )
            controls.append(ft.Container(height=6))

        return controls

    banner_area.controls = build_banners()

    return ft.Container(
        expand=True,
        width=float("inf"),
        alignment=ft.Alignment(0, -1),
        padding=ft.padding.only(
            left=10,
            right=10,
            top=OUTER_PAGE_PADDING,
            bottom=OUTER_PAGE_PADDING,
        ),
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            controls=[
                ft.Container(height=LARGE_GAP + 2),
                banner_area,
                ft.Container(height=14),
                *build_menu_controls(),
                white_long_box(
                    "로그아웃",
                    text_color=ft.Colors.GREY_300,
                    show_left_icon=False,
                    show_chevron=False,
                    show_border=False, # 👉 추가: 로그아웃은 테두리 제거
                ),
                ft.Container(height=20),
            ],
        ),
    )