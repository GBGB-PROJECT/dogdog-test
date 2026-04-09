import flet as ft


def banner(
    text="",
    image_src=None,
    selected=False,
    on_click=None,
):
    box_bgcolor = "#FEF3B9" if selected else ft.Colors.WHITE
    arrow_bgcolor = ft.Colors.WHITE if selected else "#FEF3B9"

    arrow_circle = ft.Container(
        width=40,
        height=40,
        bgcolor=arrow_bgcolor,
        border_radius=20,
        alignment=ft.Alignment(0, 0),
        content=ft.Icon(
            ft.Icons.ARROW_FORWARD,
            color=ft.Colors.BLACK,
            size=22,
        ),
    )

    left_slot = ft.Container(
        width=50,
        height=50,
        alignment=ft.Alignment(0, 0),
        content=(
            ft.Container(
                width=50,
                height=50,
                border_radius=25,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=ft.Image(
                    src=image_src,
                    width=50,
                    height=50,
                    fit=ft.BoxFit.COVER,
                ),
            )
            if image_src
            else None
        ),
    )

    center_slot = ft.Container(
        expand=True,
        alignment=ft.Alignment(0, 0),
        content=ft.Text(
            text,
            size=18,
            weight=ft.FontWeight.W_600,
            color=ft.Colors.BLACK,
            text_align=ft.TextAlign.CENTER,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
        ),
    )

    right_slot = ft.Container(
        width=50,
        height=50,
        alignment=ft.Alignment(0, 0),
        content=arrow_circle,
    )

    return ft.Container(
        width=330,
        height=72,
        bgcolor=box_bgcolor,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=16,
        padding=ft.padding.symmetric(horizontal=14),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                left_slot,
                center_slot,
                right_slot,
            ],
        ),
    )