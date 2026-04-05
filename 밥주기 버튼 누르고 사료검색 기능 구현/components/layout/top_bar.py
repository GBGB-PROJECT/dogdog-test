import flet as ft


def dog_list(dog):
    return ft.MenuItemButton(
        width=200,
        content=ft.Text(
            dog,
            size=15,
            color=ft.Colors.BLACK,
            weight=ft.FontWeight.W_500,
        ),
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DEFAULT: ft.Colors.WHITE,
                ft.ControlState.HOVERED: ft.Colors.GREY_100,
            },
            color={
                ft.ControlState.DEFAULT: ft.Colors.BLACK,
                ft.ControlState.HOVERED: ft.Colors.BLACK,
            },
            elevation=0,
            shadow_color=ft.Colors.TRANSPARENT,
            padding=ft.padding.symmetric(horizontal=12, vertical=14),
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )


# 메뉴바
dog_menubar = ft.Row(
    [
        ft.MenuBar(
            expand=True,
            style=ft.MenuStyle(
                alignment=ft.Alignment(0, 0),
                bgcolor=ft.Colors.TRANSPARENT,
                elevation=0,
                shadow_color=ft.Colors.TRANSPARENT,
                mouse_cursor={
                    ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                    ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                },
            ),
            controls=[
                ft.SubmenuButton(
                    menu_style=ft.MenuStyle(
                        bgcolor=ft.Colors.WHITE,
                        shadow_color=ft.Colors.with_opacity(0.10, ft.Colors.BLACK),
                        elevation=6,
                    ),
                    width=200,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "츄츄(4년 9개월,♀)",
                                size=16,
                                color=ft.Colors.GREY_700,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Icon(
                                ft.Icons.KEYBOARD_ARROW_DOWN,
                                size=25,
                                color=ft.Colors.GREY_700,
                            ),
                        ],
                    ),
                    controls=[
                        dog_list("츄츄(4년 9개월,♀)"),
                        dog_list("츄츄(4년 9개월,♀)"),
                        dog_list("츄츄(4년 9개월,♀)"),
                    ],
                ),
            ],
        )
    ]
)


# 상단
# ✅ 기본 화면: 기존 구조 그대로 유지
# ✅ food_select 같은 특정 화면만 title_text로 중앙 제목 표시
def top_bar(title_text=None):
    # ─────────────────────────────────────────────
    # ✅ title_text가 없으면 기존 츄츄 메뉴바 그대로
    # ─────────────────────────────────────────────
    if not title_text:
        return ft.Column(
            controls=[
                ft.Container(
                    padding=ft.padding.only(top=55, left=20, right=20),
                    height=100,
                    width=float("inf"),
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment(0, -1),
                        end=ft.Alignment(0, 1),
                        colors=[ft.Colors.YELLOW_600, ft.Colors.WHITE],
                    ),
                    alignment=ft.Alignment(0, 0),
                    content=ft.Container(
                        width=330,
                        content=ft.Row(
                            [
                                ft.Container(
                                    width=40,
                                    height=40,
                                ),
                                ft.Container(
                                    expand=True,
                                    alignment=ft.Alignment(0, 0),
                                    content=dog_menubar,
                                ),
                                ft.Container(
                                    width=40,
                                    height=40,
                                    alignment=ft.Alignment(1, 0),
                                    content=ft.IconButton(
                                        icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                                        icon_color=ft.Colors.GREY_700,
                                        icon_size=28,
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                ),
            ],
        )

    # ─────────────────────────────────────────────
    # ✅ title_text가 있으면 그 화면만 중앙 제목 표시
    # ─────────────────────────────────────────────
    return ft.Column(
        controls=[
            ft.Container(
                padding=ft.padding.only(top=55, left=20, right=20),
                height=100,
                width=float("inf"),
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(0, -1),
                    end=ft.Alignment(0, 1),
                    colors=[ft.Colors.YELLOW_600, ft.Colors.WHITE],
                ),
                alignment=ft.Alignment(0, 0),
                content=ft.Container(
                    width=330,
                    content=ft.Stack(
                        controls=[
                            ft.Row(
                                [
                                    ft.Container(
                                        width=40,
                                        height=40,
                                    ),
                                    ft.Container(expand=True),
                                    ft.Container(
                                        width=40,
                                        height=40,
                                        alignment=ft.Alignment(1, 0),
                                        content=ft.IconButton(
                                            icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                                            icon_color=ft.Colors.GREY_700,
                                            icon_size=28,
                                        ),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Container(
                                alignment=ft.Alignment(0, 0),
                                content=ft.Text(
                                    title_text,
                                    size=18,
                                    color=ft.Colors.GREY_700,
                                    weight=ft.FontWeight.W_600,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ),
                        ]
                    ),
                ),
            ),
        ],
    )