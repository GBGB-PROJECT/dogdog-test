import asyncio
import flet as ft
from components.common.banner import banner
from components.common.texts import Txt


def white_long_box(
    text,
    left_icon=None,
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    on_click=None,
    show_left_icon=True,
    show_chevron=True,
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
        width=330,
        height=64,
        bgcolor=bgcolor,
        border_radius=16,
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
        spacing=14,
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

    menu_items = [
        ("내 정보", ft.Icons.PERSON_OUTLINE),
        ("마이 쇼핑", ft.Icons.STOREFRONT_OUTLINED),
        ("공지사항", ft.Icons.NOTIFICATIONS_NONE),
        ("문의하기", ft.Icons.HELP_OUTLINE),
    ]

    menu_controls = []
    for text, icon in menu_items:
        menu_controls.append(
            white_long_box(
                text,
                left_icon=icon,
            )
        )
        menu_controls.append(ft.Container(height=6))

    banner_area.controls = build_banners()

    return ft.Container(
        expand=True,
        width=float("inf"),
        alignment=ft.Alignment(0, -1),
        padding=ft.padding.only(left=10, right=10, top=12, bottom=12),
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            controls=[
                ft.Container(height=18),

                banner_area,
                ft.Container(height=14),

                *menu_controls,

                white_long_box(
                    "로그아웃",
                    text_color=ft.Colors.GREY_300,
                    show_left_icon=False,
                    show_chevron=False,
                ),

                ft.Container(height=20),
            ],
        ),
    )