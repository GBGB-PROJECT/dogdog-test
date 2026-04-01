import flet as ft
from components.common.common_components import about_dog
from components.layout.common_layout import build_screen
from components.navigation import go_next, go_back

def invisible_checkbox(text):
    return ft.Container(
        width=350,
        height=50,
        padding=10,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Checkbox(),
                ft.Text(text, weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            ],
        ),
    )


def invisible_radio(text, value):
    return ft.Container(
        width=350,
        height=50,
        padding=10,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Radio(value=value),
                ft.Text(text, weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            ],
        ),
    )


def radio_time_group():
    return ft.RadioGroup(
        content=ft.Column(
            spacing=0,
            controls=[
                invisible_radio("하루 30분", "30min"),
                invisible_radio("하루 30분 이상", "30min_plus"),
                invisible_radio("하루 1시간 이상", "1hour_plus"),
            ],
        ),
    )


def build_view(page: ft.Page):
    body_controls = [
        ft.Container(margin=ft.margin.only(top=50), content=about_dog()),
        ft.Text("급여 시간", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
        invisible_checkbox("아침"),
        invisible_checkbox("점심"),
        invisible_checkbox("저녁"),
        ft.Text("산책 시간", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
        radio_time_group(),
    ]

    return build_screen(
        page=page,
        body_controls=body_controls,
        on_back=lambda e: go_back(page),
        on_continue=lambda e: go_next(page),
    )