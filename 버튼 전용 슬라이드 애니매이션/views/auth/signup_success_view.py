import flet as ft


def build_view(page: ft.Page):
    return ft.Container(
        expand=True,
        width=float("inf"),
        bgcolor=ft.Colors.YELLOW,
        alignment=ft.Alignment(0, 0),
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(
                    src="checkone.png",
                    width=150,
                    height=150,
                ),
                ft.Text(
                    "회원 가입이 완료되었습니다.",
                    weight=ft.FontWeight.W_800,
                    color=ft.Colors.BLACK,
                    size=20,
                ),
            ],
        ),
    )