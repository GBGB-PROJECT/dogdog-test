import flet as ft
import time
import threading


BG_COLOR = "#FEF3B9"


def main(page: ft.Page):
    page.title = "Splash"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = BG_COLOR

    dog_image = ft.Container(
        content=ft.Image(
            src="dogclay.png",
            width=230,
            fit=ft.BoxFit.CONTAIN,
        ),
        animate_offset=ft.Animation(260, ft.AnimationCurve.EASE_OUT_BACK),
        animate_scale=ft.Animation(260, ft.AnimationCurve.EASE_OUT_BACK),
        offset=ft.Offset(0, 0),
        scale=ft.Scale(1.0),
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
            animate_offset=ft.Animation(260, ft.AnimationCurve.EASE_OUT_BACK),
            animate_scale=ft.Animation(260, ft.AnimationCurve.EASE_OUT_BACK),
            offset=ft.Offset(0, 0),
            scale=ft.Scale(1.0),
        )

    # ✅ 참고 이미지처럼: 왼쪽 Dog를 더 키우고 촘촘하게
    def build_left_word():
        d = animated_letter("d1.png", width=92, left=-6, top=8)
        o = animated_letter("o1.png", width=42, left=48, top=34)
        g = animated_letter("g1.png", width=52, left=78, top=16)

        word = ft.Container(
            width=134,
            height=104,
            content=ft.Stack(
                clip_behavior=ft.ClipBehavior.NONE,
                controls=[d, o, g],
            ),
        )
        return word, [d, o, g]

    # ✅ 참고 이미지처럼: 오른쪽 Dog를 조금 줄이고 왼쪽과 덩어리감 맞춤
    def build_right_word():
        d = animated_letter("d2.png", width=62, left=0, top=10)
        o = animated_letter("o2.png", width=44, left=46, top=28)
        g = animated_letter("g2.png", width=50, left=78, top=18)

        word = ft.Container(
            width=126,
            height=104,
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
        spacing=2,  # ✅ 두 단어 사이 간격 좁힘
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
        controls=[left_word, right_word],
    )

    title_wrap = ft.Container(
        margin=ft.margin.only(top=-2),
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
        group = [dog_image] + letters

        for item in group:
            item.offset = ft.Offset(0, 0.10)
            item.scale = ft.Scale(0.94)
        page.update()
        time.sleep(0.08)

        for item in group:
            item.offset = ft.Offset(0, -0.16)
            item.scale = ft.Scale(1.08)
        page.update()
        time.sleep(0.16)

        for item in group:
            item.offset = ft.Offset(0, 0.04)
            item.scale = ft.Scale(0.98)
        page.update()
        time.sleep(0.10)

        for item in group:
            item.offset = ft.Offset(0, -0.03)
            item.scale = ft.Scale(1.01)
        page.update()
        time.sleep(0.08)

        for item in group:
            item.offset = ft.Offset(0, 0)
            item.scale = ft.Scale(1.0)
        page.update()

        time.sleep(0.4)
        # page.go("/home")

    threading.Thread(target=splash_bounce, daemon=True).start()


ft.run(main)