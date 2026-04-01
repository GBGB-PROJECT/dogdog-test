import flet as ft


# ─────────────────────────────────────────────
# 🟨 수정 1: alignment=ft.Alignment.center 오류 수정
# 이유:
# - ft.Alignment.center 는 존재하지 않음
# - 정가운데 정렬은 ft.Alignment(0, 0) 으로 써야 함
# ─────────────────────────────────────────────
def arrow_back(on_click=None):
    return ft.Container(
        width=40,
        height=40,
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        content=ft.Icon(
            ft.Icons.ARROW_BACK,
            size=22,
            color=ft.Colors.BLACK,
        ),
    )


def about_dog():
    return ft.Column(
        spacing=0,
        controls=[
            ft.Text(
                "About your Dog",
                weight=ft.FontWeight.W_500,
                color=ft.Colors.BLACK,
                size=30,
            ),
            ft.Text(
                "반려동물의 기본 정보를 입력하세요",
                weight=ft.FontWeight.W_500,
                color=ft.Colors.BLACK,
                size=15,
            ),
        ],
    )


def long_box(
    text,
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    border_color=ft.Colors.GREY_300,
    on_click=None,
    icon=None,
):
    controls = []

    if icon:
        controls.append(ft.Icon(icon, size=18, color=text_color))

    controls.append(
        ft.Text(
            text,
            size=14,
            weight=ft.FontWeight.W_500,
            color=text_color,
        )
    )

    return ft.Container(
        width=350,
        height=50,
        bgcolor=bgcolor,
        border=ft.Border.all(1, border_color),
        border_radius=10,
        padding=10,
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
            controls=controls,
        ),
    )


def bottom_continue_button(on_click=None):
    return ft.Container(
        alignment=ft.Alignment(0, 0),
        content=long_box(
            "Continue",
            bgcolor=ft.Colors.YELLOW,
            text_color=ft.Colors.BLACK,
            on_click=on_click,
        ),
    )


def input_box(label=None, hint_text=None):
    return ft.TextField(
        width=350,
        height=50,
        border_radius=10,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_400,
        hint_text=hint_text,
        label=label,
    )