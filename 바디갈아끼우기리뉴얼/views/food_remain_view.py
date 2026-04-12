import flet as ft
from components.common.texts import Txt
from components.common.layout_tokens import (
    CONTENT_WIDTH,
    CARD_RADIUS,
    SECTION_GAP,
    PAGE_SIDE_PADDING,
    LARGE_GAP,
)
from components.common.colors import (
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    SURFACE_WHITE,
    BORDER_LIGHT,
)


TAB_LABELS = ["전체", "사료", "간식", "영양제"]


def food_remain_view(page: ft.Page):
    selected_top_tab = {"index": 0}
    top_tabs_area = ft.Container(width=CONTENT_WIDTH)
    tab_content = ft.Container(width=CONTENT_WIDTH, expand=True)

    def open_food_select(e):
        page.open_food_select()

    def food_remain_info2():
        return ft.Column(
            spacing=10,
            controls=[
                ft.Row(
                    controls=[
                        Txt(
                            "???g / ???kg",
                            size=14,
                            color=TEXT_PRIMARY,
                            weight=ft.FontWeight.W_600,
                        ),
                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=10, vertical=4),
                            bgcolor=ft.Colors.GREY_200,
                            border_radius=8,
                            alignment=ft.Alignment(0, 0),
                            content=Txt(
                                "??일치 남음",
                                size=12,
                                color=TEXT_PRIMARY,
                                weight=ft.FontWeight.W_500,
                            ),
                        ),
                    ],
                ),
                ft.ProgressBar(
                    width=298,
                    height=10,
                    value=0,
                    bgcolor=BORDER_LIGHT,
                    color=BORDER_LIGHT,
                    border_radius=10,
                ),
                Txt(
                    "예상 소진일",
                    size=12,
                    color=TEXT_SECONDARY,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        )

    def food_image_card():
        return ft.Container(
            width=CONTENT_WIDTH,
            height=330,
            border_radius=CARD_RADIUS,
            border=ft.border.all(1, BORDER_LIGHT),
            bgcolor=SURFACE_WHITE,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        height=220,
                        alignment=ft.Alignment(0, 0),
                        content=Txt(
                            "등록된 제품이 없습니다",
                            size=16,
                            color=TEXT_SECONDARY,
                            weight=ft.FontWeight.W_500,
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ),
                    ft.Divider(height=1, thickness=1, color=BORDER_LIGHT),
                    ft.Container(
                        expand=True,
                        padding=ft.padding.symmetric(horizontal=16, vertical=12),  # 👈 이게 없으면 왼쪽으로 쏠림
                        content=food_remain_info2(),
                    ),
                ],
            ),
        )

    def build_tab_content():
        return ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=SECTION_GAP,
            controls=[food_image_card()],
        )

    def top_tab_button(label, index):
        is_selected = selected_top_tab["index"] == index

        return ft.Container(
            on_click=lambda e, idx=index: change_top_tab(idx),
            content=ft.Column(
                spacing=6,
                alignment=ft.MainAxisAlignment.END, # 👈 없으면 글자가 섞임
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, # 👈 없으면 탭 밑줄이 어긋남
                controls=[
                    Txt(
                        label,
                        size=15,
                        color=TEXT_PRIMARY if is_selected else ft.Colors.GREY,
                        weight=ft.FontWeight.W_700 if is_selected else ft.FontWeight.W_500,
                    ),
                    ft.Container(
                        height=3,
                        width=42,
                        bgcolor=TEXT_PRIMARY if is_selected else ft.Colors.TRANSPARENT,
                        border_radius=10,
                    ),
                ],
            ),
        )

    def food_register_button():
        return ft.Container(
            height=30,
            padding=ft.padding.symmetric(horizontal=10),
            border_radius=8,
            bgcolor=ft.Colors.GREY_200,
            alignment=ft.Alignment(0, 0),
            on_click=open_food_select,
            content=ft.Row(
                spacing=4,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    Txt(
                        "사료 등록",
                        size=12,
                        color=TEXT_PRIMARY,
                        weight=ft.FontWeight.W_500,
                    ),
                    ft.Icon(
                        ft.Icons.EDIT,
                        size=13,
                        color=TEXT_PRIMARY,
                    ),
                ],
            ),
        )

    def build_top_tabs():
        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    spacing=10,
                    controls=[
                        top_tab_button(label, i)
                        for i, label in enumerate(TAB_LABELS)
                    ],
                ),
                food_register_button(),
            ],
        )

    def change_top_tab(index):
        selected_top_tab["index"] = index
        tab_content.content = build_tab_content()
        top_tabs_area.content = build_top_tabs()
        page.update()

    top_tabs_area.content = build_top_tabs()
    change_top_tab(0)

    return ft.Container(
        expand=True,
        bgcolor=SURFACE_WHITE,
        alignment=ft.Alignment(0, -1),
        content=ft.Container(
            width=CONTENT_WIDTH,
            padding=ft.padding.only(top=PAGE_SIDE_PADDING, bottom=PAGE_SIDE_PADDING),
            content=ft.Column(
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    top_tabs_area,
                    ft.Container(
                        width=CONTENT_WIDTH,
                        margin=ft.Margin.only(top=6, bottom=LARGE_GAP),
                        content=ft.Divider(thickness=1, color=BORDER_LIGHT),
                    ),
                    tab_content,
                ],
            ),
        ),
    )