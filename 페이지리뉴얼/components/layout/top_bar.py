import flet as ft

TOP_VANILLA = "#FEF3B9"
BODY_WHITE = "#FFFFFF"


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


dog_menubar = ft.Column(
    spacing=2,
    horizontal_alignment=ft.CrossAxisAlignment.START,
    controls=[
        ft.Row(
            spacing=8,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=50,
                    height=50,
                    border_radius=25, 
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,  
                    content=ft.Image(
                        src="dogclay.png",
                        width=50,
                        height=50,
                        fit=ft.BoxFit.COVER,  
                    ),
                ),
                ft.Row(
                    controls=[
                        ft.MenuBar(
                            expand=True,
                            style=ft.MenuStyle(
                                alignment=ft.Alignment(-1, 0),
                                bgcolor=ft.Colors.TRANSPARENT,
                                elevation=0,
                                shadow_color=ft.Colors.TRANSPARENT,
                            ),
                            controls=[
                                ft.SubmenuButton(
                                    menu_style=ft.MenuStyle(
                                        bgcolor=ft.Colors.WHITE,
                                        shadow_color=ft.Colors.with_opacity(0.10, ft.Colors.BLACK),
                                        elevation=6,
                                    ),
                                    width=220,
                                    content=ft.Column(
                                        spacing=2,
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                        controls=[
                                            ft.Row(
                                                spacing=2,
                                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
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
                                            ft.Container(
                                                padding=ft.padding.only(left=0),
                                                content=ft.Text(
                                                    "(4년 9개월,♀)",
                                                    size=11,
                                                    color=ft.Colors.GREY_600,
                                                    weight=ft.FontWeight.W_500,
                                                ),
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
                ),
            ],
        ),
    ],
)


def top_shell(content):
    return ft.Container(
        width=float("inf"),
        height=105,
        bgcolor=TOP_VANILLA,
        border_radius=ft.border_radius.only(
            bottom_left=34,
            bottom_right=34,
        ),
        padding=ft.padding.only(top=52, left=20, right=20, bottom=14),
        content=ft.Container(
            width=330,
            alignment=ft.Alignment(0, 0),
            content=content,
        ),
    )


def top_bar(title_text=None, back_index=0): 
    
    if not title_text:
        return ft.Column(
            spacing=0,
            controls=[
                top_shell(
                    ft.Row(
                        [
                            ft.Container(width=0, height=40),
                            ft.Container(
                                expand=True,
                                alignment=ft.Alignment(-1, 0),
                                content=dog_menubar,
                            ),
                            ft.Container(
                                width=40,
                                height=40,
                                alignment=ft.Alignment(1, 0),
                                content=ft.IconButton(
                                    icon=ft.Icons.NOTIFICATIONS_NONE_ROUNDED,
                                    icon_color=ft.Colors.GREY_700,
                                    icon_size=28,
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                )
            ],
        )

    return ft.Column(
        spacing=0,
        controls=[
            top_shell(
                ft.Stack(
                    controls=[
                        ft.Row(
                            [
                                ft.Container(
                                    width=40,
                                    height=40,
                                    alignment=ft.Alignment(-1, 0),
                                    content=ft.IconButton(
                                        icon=ft.Icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                        icon_color=ft.Colors.GREY_700,
                                        icon_size=24,
                            

                                        
                                        on_click=lambda e: e.page.render_main_tab(back_index),
                                    ),
                                ),
                                ft.Container(expand=True),
                                ft.Container(
                                    width=40,
                                    height=40,
                                    alignment=ft.Alignment(1, 0),
                                    content=ft.IconButton(
                                        icon=ft.Icons.NOTIFICATIONS_NONE_ROUNDED,
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
                )
            )
        ],
    )