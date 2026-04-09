import flet as ft


def white_long_box3(
    text,
    time_text="오전 07:30",
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    time_color=ft.Colors.BLACK,
    on_click=None,
):
    return ft.Container(
        width=350,
        height=70,
        bgcolor=bgcolor,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=16,
        padding=ft.padding.symmetric(horizontal=16),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(text, size=14, weight=ft.FontWeight.W_500, color=text_color),
                ft.Text(time_text, size=14, weight=ft.FontWeight.W_600, color=time_color),
            ],
        ),
    )


def mid_box(text):
    return ft.Container(
        width=72,
        height=40,
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        bgcolor=ft.Colors.YELLOW_600,
        border_radius=10,
        content=ft.Text(
            text,
            size=13,
            weight=ft.FontWeight.W_600,
            color=ft.Colors.BLACK,
        ),
    )


def mid_box2(text):
    return ft.Container(
        width=72,
        height=40,
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        bgcolor=ft.Colors.GREY_100,
        border_radius=10,
        content=ft.Text(
            text,
            size=13,
            weight=ft.FontWeight.W_600,
            color=ft.Colors.BLACK,
        ),
    )