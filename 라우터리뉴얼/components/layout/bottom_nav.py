import flet as ft


def nav_item_rules(icon, label, selected=False, on_click=None):
    return ft.Container(
        expand=True,
        height=74,
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
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
                ft.Text(
                    label,
                    color=ft.Colors.BLACK if selected else ft.Colors.GREY_400,
                    size=10,
                    weight=ft.FontWeight.W_500,
                    text_align=ft.TextAlign.CENTER,
                    max_lines=1,
                    overflow=ft.TextOverflow.ELLIPSIS,
                    no_wrap=True,
                ),
            ],
        ),
    )


def bottom_nav_items(selected_index, on_tab_change):
    tabs = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.CALENDAR_MONTH, "Log"),
        (None, None),  # 👉 FAB 자리
        (ft.Icons.MESSENGER_OUTLINE_ROUNDED, "Contents"),
        (ft.Icons.PERSON_OUTLINE, "MyPage"),
    ]

    controls = []

    for i, (icon, label) in enumerate(tabs):
        # 👉 가운데 FAB 자리
        if icon is None:
            controls.append(ft.Container(width=72))
            continue

        controls.append(
            nav_item_rules(
                icon,
                label,
                selected=(selected_index == i if i < 2 else selected_index == i - 1),
                on_click=lambda e, idx=i if i < 2 else i - 1: on_tab_change(idx)
                if on_tab_change
                else None,
            )
        )

    return controls


def custom_bottom_appbar(selected_index=0, on_tab_change=None):
    return ft.BottomAppBar(
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircularRectangleNotchShape(),
        content=ft.Container(
            height=78,
            padding=ft.padding.symmetric(horizontal=10, vertical=2),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=bottom_nav_items(selected_index, on_tab_change),
            ),
        ),
    )