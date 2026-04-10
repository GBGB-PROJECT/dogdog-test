import flet as ft
import time
import threading


BG_COLOR = "#FEF3B9"


def main(page: ft.Page):
    page.title = "Splash"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = BG_COLOR

    dog_image = ft.Image(
        src="dogclay.png",
        width=230,
        fit=ft.BoxFit.CONTAIN,
    )

    def animated_letter(src, width, left, top):
        return ft.Container(
            left=left,
            top=top,
            content=ft.Image(
                src=src,
                width=width,
                fit=ft.BoxFit.CONTAIN,
            ),
            animate_offset=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK),
            animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK),
            offset=ft.Offset(0, 0),
            scale=ft.Scale(1.0),
        )

    # ✅ LEFT 재조정
    def build_left_word():
        d = animated_letter("d1.png", width=80, left=0, top=14)
        o = animated_letter("o1.png", width=42, left=60, top=36)
        g = animated_letter("g1.png", width=50, left=98, top=20)

        word = ft.Container(
            width=154,
            height=112,
            content=ft.Stack(
                clip_behavior=ft.ClipBehavior.NONE,
                controls=[d, o, g],
            ),
        )
        return word, [d, o, g]

    # ✅ RIGHT 기준
    def build_right_word():
        d = animated_letter("d2.png", width=66, left=0, top=14)
        o = animated_letter("o2.png", width=54, left=44, top=30)
        g = animated_letter("g2.png", width=54, left=86, top=18)

        word = ft.Container(
            width=142,
            height=112,
            content=ft.Stack(
                clip_behavior=ft.ClipBehavior.NONE,
                controls=[d, o, g],
            ),
        )
        return word, [d, o, g]

    left_word, left_letters = build_left_word()
    right_word, right_letters = build_right_word()
    letters = left_letters + right_letters

    title_logo = ft.Row(
        spacing=4,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
        controls=[left_word, right_word],
    )

    title_wrap = ft.Container(
        margin=ft.margin.only(top=-4),
        content=title_logo,
    )

    splash_content = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
        controls=[
            dog_image,
            title_wrap,
        ],
    )

    splash_view = ft.Container(
        expand=True,
        bgcolor=BG_COLOR,
        alignment=ft.Alignment(0, 0),
        content=splash_content,
    )

    page.add(splash_view)
    page.update()

    def splash_bounce():
        group = letters

        for l in group:
            l.offset = ft.Offset(0, 0.15)
            l.scale = ft.Scale(0.90)
        page.update()
        time.sleep(0.1)

        for l in group:
            l.offset = ft.Offset(0, -0.28)
            l.scale = ft.Scale(1.18)
        page.update()
        time.sleep(0.2)

        for l in group:
            l.offset = ft.Offset(0, 0.08)
            l.scale = ft.Scale(0.94)
        page.update()
        time.sleep(0.14)

        for l in group:
            l.offset = ft.Offset(0, -0.10)
            l.scale = ft.Scale(1.05)
        page.update()
        time.sleep(0.12)

        for l in group:
            l.offset = ft.Offset(0, 0)
            l.scale = ft.Scale(1.0)
        page.update()

        time.sleep(0.45)
        # page.go("/home")

    threading.Thread(target=splash_bounce, daemon=True).start()


ft.run(main)