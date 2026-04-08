import flet as ft


def nav_item(icon, label, selected=False, on_click=None):
    return ft.Container(
        expand=True,
        height=74,
        on_click=on_click,
        alignment=ft.Alignment(0, 0),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=3,
            controls=[
                ft.Icon(
                    icon,
                    color=ft.Colors.BLACK if selected else ft.Colors.GREY_400,
                    size=22,
                ),
                ft.Container(
                    width=64,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        label,
                        color=ft.Colors.BLACK if selected else ft.Colors.GREY_400,
                        size=10,
                        weight=ft.FontWeight.W_500,
                        text_align=ft.TextAlign.CENTER,
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS,
                        no_wrap=True,
                    ),
                ),
            ],
        ),
    )

def custom_bottom_appbar(selected_index=0, on_tab_change=None):
    return ft.BottomAppBar(
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircularRectangleNotchShape(),
        content=ft.Container(
            height=78,
            alignment=ft.Alignment(0, 0),
            padding=ft.padding.only(left=10, right=10, top=2, bottom=2),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        expand=True,
                        content=nav_item(
                            ft.Icons.HOME,
                            "Home",
                            selected=(selected_index == 0),
                            on_click=lambda e: on_tab_change(0) if on_tab_change else None,
                        ),
                    ),
                    ft.Container(
                        expand=True,
                        content=nav_item(
                            ft.Icons.CALENDAR_MONTH,
                            "Log",
                            selected=(selected_index == 1),
                            on_click=lambda e: on_tab_change(1) if on_tab_change else None,
                        ),
                    ),

                    # ─────────────────────────────────────────────
                    # 🟦 가운데 FAB 자리 확보
                    # ─────────────────────────────────────────────
                    ft.Container(width=72),

                    ft.Container(
                        expand=True,
                        content=nav_item(
                            ft.Icons.MESSENGER_OUTLINE_ROUNDED,
                            "Contents",
                            selected=(selected_index == 2),
                            on_click=lambda e: on_tab_change(2) if on_tab_change else None,
                        ),
                    ),
                    ft.Container(
                        expand=True,
                        content=nav_item(
                            ft.Icons.PERSON_OUTLINE,
                            "MyPage",
                            selected=(selected_index == 3),
                            on_click=lambda e: on_tab_change(3) if on_tab_change else None,
                        ),
                    ),
                ],
            ),
        ),
    )
