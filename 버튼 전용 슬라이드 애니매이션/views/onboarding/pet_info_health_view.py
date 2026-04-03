import flet as ft
from components.common.common_components import about_dog, input_box
from components.layout.common_layout import build_screen_body


def build_view(page: ft.Page):
    allergy_value = None
    disease_value = None

    def on_allergy_change(e):
        nonlocal allergy_value
        allergy_value = e.control.value
        page.update()

    def on_disease_change(e):
        nonlocal disease_value
        disease_value = e.control.value
        page.update()

    body_controls = [
        ft.Container(margin=ft.Margin.only(top=50), content=about_dog()),
        ft.Text("알레르기", weight=ft.FontWeight.W_500),
        ft.Container(
            width=350,
            padding=12,
            content=ft.RadioGroup(
                value=allergy_value,
                on_change=on_allergy_change,
                content=ft.Row(
                    spacing=20,
                    controls=[
                        ft.Radio(value="yes", label="있다"),
                        ft.Radio(value="no", label="없다"),
                    ],
                ),
            ),
        ),
        input_box(label="반려동물의 알레르기를 적어주세요"),
        ft.Text("질병", weight=ft.FontWeight.W_500),
        ft.Container(
            width=350,
            padding=12,
            content=ft.RadioGroup(
                value=disease_value,
                on_change=on_disease_change,
                content=ft.Row(
                    spacing=20,
                    controls=[
                        ft.Radio(value="yes", label="있다"),
                        ft.Radio(value="no", label="없다"),
                    ],
                ),
            ),
        ),
        input_box(label="반려동물의 질병을 적어주세요"),
    ]

    # ─────────────────────────────────────────────
    # 🟦 체크: 본문만 반환
    # ─────────────────────────────────────────────
    return build_screen_body(body_controls)