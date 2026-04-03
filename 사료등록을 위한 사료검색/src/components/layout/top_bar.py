import flet as ft

def dog_list(dog):
    return ft.MenuItemButton(
        width=200,
        content=ft.Text(dog, size=15),
        style=ft.ButtonStyle(
            elevation=0,  # 그림자 제거
            shadow_color=ft.Colors.TRANSPARENT,  # 그림자 완전 제거
        ),
        # on_click=handle_menu_item_click,
    )

# 메뉴바
dog_menubar = ft.Row(
    [
        ft.MenuBar(
            expand=True,
            style=ft.MenuStyle(
                alignment=ft.Alignment.CENTER,
                bgcolor=ft.Colors.TRANSPARENT,  # 메뉴바 투명
                elevation=0,  # 그림자 제거
                shadow_color=ft.Colors.TRANSPARENT,  # 그림자 완전 제거
                mouse_cursor={
                    ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                    ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                },
            ),
            controls=[
                ft.SubmenuButton(
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
                    padding=ft.padding.only(top=55),
                    height=100,
                    width=float("inf"),
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment(0, -1),
                        end=ft.Alignment(0, 1),
                        colors=[ft.Colors.YELLOW_600, ft.Colors.WHITE],
                    ),
                    content=ft.Row(
                        [
                            ft.Container(
                                width=50,
                                height=50,
                            ),
                            ft.Container(
                                content=dog_menubar,
                            ),
                            ft.Container(
                                alignment=ft.Alignment(1, 0),
                                content=ft.IconButton(
                                    icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                                    icon_color=ft.Colors.GREY_700,
                                    icon_size=30,
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
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
                padding=ft.padding.only(top=55),
                height=100,
                width=float("inf"),
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(0, -1),
                    end=ft.Alignment(0, 1),
                    colors=[ft.Colors.YELLOW_600, ft.Colors.WHITE],
                ),
                content=ft.Stack(
                    controls=[
                        # 왼쪽/오른쪽 자리 유지
                        ft.Row(
                            [
                                ft.Container(
                                    width=50,
                                    height=50,
                                ),
                                ft.Container(expand=True),
                                ft.Container(
                                    width=50,
                                    height=50,
                                    alignment=ft.Alignment(1, 0),
                                    content=ft.IconButton(
                                        icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                                        icon_color=ft.Colors.GREY_700,
                                        icon_size=30,
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        # 제목만 진짜 가운데
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
        ],
    )