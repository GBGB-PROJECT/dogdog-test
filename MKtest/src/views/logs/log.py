import flet as ft
from datetime import datetime
import math
import flet.canvas as cv


def log_view(page: ft.Page):
    image_dog = ft.Row(
        # scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                width=150,
                height=150,
                bgcolor=ft.Colors.BLACK,
                shape=ft.BoxShape.CIRCLE,
                image=ft.DecorationImage(
                    src="대추.jpg",
                    fit=ft.BoxFit.COVER,
                    # fit=ft.ImageFit.COVER,
                ),
            )
        ]
    )

    def goal_status(title, current, total, unit):
        return ft.Column(
                spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(title, size=15),
                    ft.Container(
                        # width=300,
                        content=
                            ft.ProgressBar(
                                width=200, 
                                height=13,
                                value=current/total,
                                bgcolor=ft.Colors.GREY_300,
                                color=ft.Colors.YELLOW_600,
                                border_radius=10,
                            )
                    ),
                    ft.Text(f"{current}/{total}{unit}", size=15),
                ],
            )

    goal_info = ft.Container(
    padding=20,
    content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.Container(
                    content=image_dog),
                ft.Column(
                    spacing=6,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=
                        [
                            goal_status("🏃목표 활동량", 30, 90, "분"),
                            goal_status("🍚목표 칼로리", 35, 69, "kcal"),
                        ],
                ),
            ]
        ),
    )


    def gauge_chart(percent=40, label="사료 잔여량: 800g"):
        # percent: 0 ~ 100
        value_angle = 180 * (percent / 100)

        width = 220
        height = 130
        stroke_w = 18
        radius = 80
        cx = width / 2
        cy = 105

        # 시작 각도: 180도(왼쪽)부터 0도(오른쪽)까지 반원
        start_angle = math.pi
        sweep_bg = math.pi
        sweep_value = math.pi * (percent / 100)

        return ft.Container(
            width=width,
            height=height,
            content=ft.Stack(
                controls=[
                    cv.Canvas(
                        width=width,
                        height=height,
                        shapes=[
                            # 배경 반원
                            cv.Arc(
                                x=cx - radius,
                                y=cy - radius,
                                width=radius * 2,
                                height=radius * 2,
                                start_angle=start_angle,
                                sweep_angle=sweep_bg,
                                paint=ft.Paint(
                                    style=ft.PaintingStyle.STROKE,
                                    stroke_width=stroke_w,
                                    color=ft.Colors.GREY_300,
                                    stroke_cap=ft.StrokeCap.ROUND,
                                ),
                            ),
                            # 진행 반원
                            cv.Arc(
                                x=cx - radius,
                                y=cy - radius,
                                width=radius * 2,
                                height=radius * 2,
                                start_angle=start_angle,
                                sweep_angle=sweep_value,
                                paint=ft.Paint(
                                    style=ft.PaintingStyle.STROKE,
                                    stroke_width=stroke_w,
                                    color=ft.Colors.YELLOW_600,
                                    stroke_cap=ft.StrokeCap.ROUND,
                                ),
                            ),
                        ],
                    ),
                    ft.Container(
                        width=width,
                        height=height,
                        padding=ft.padding.only(top=35),   # 아래로 내리기
                        alignment=ft.Alignment(0, 0),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                            controls=[
                                ft.Text(
                                    f"{percent}%",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLUE_GREY_900,
                                ),
                                ft.Text(
                                    label,
                                    size=15,
                                    color=ft.Colors.BLUE_GREY_400,
                                ),
                            ],
                        ),
                    ),
                ]
            ),
        )

    # 오늘의 기록
    today_log = ft.Container(
        margin=20,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            controls=
            [
            ft.Container(
                width=70,
                height=75,
                bgcolor=ft.Colors.YELLOW_600,
                border_radius=10,
                alignment=ft.Alignment(0, 0),  # ✅ 여기 수정
                content=ft.Text(
                    f'{datetime.now().strftime("%m/%d")}',
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.BLACK,
                ),
            ),ft.Column(
                spacing=6,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.Row(
                        spacing=6,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "🔥 오늘의 기록",
                                size=20,
                                weight=ft.FontWeight.W_500,
                                color=ft.Colors.BLACK,
                            ),
                        ],
                    ),
                    ft.Row(
                        spacing=6,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            # micro_box(info) for info in info_list
                            ft.Text(f"급여량: 43g ", size=13),
                            ft.Text(f"음수량: 100ml ", size=13),
                            ft.Text(f"산책: 30분" , size=13),
                        ],
                    ),
                ],
            ),
            ]
        )
    )


    button_style = ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        bgcolor = ft.Colors.BROWN_400,
                        color = ft.Colors.AMBER_100
                    )

    # 바텀시트 도전중.........................
    def example():
        bs = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    [
                        ft.Text("This is sheet's content!"),
                        ft.Button(
                            "Close bottom sheet", on_click=lambda e: e.page.pop_dialog()
                        ),
                    ],
                    tight=True,
                ),
                padding=10,
            ),
            open=False,
            on_dismiss=lambda e: print("Dismissed!"),
        )

        return ft.Button("Display bottom sheet", on_click=lambda e: e.page.show_dialog(bs))

    def menu_box(icon, title, on_click=None):
        return ft.Container(
            width=110,
            height=95,
            bgcolor=ft.Colors.YELLOW_600,
            border_radius=16,
            alignment=ft.Alignment(0, 0),
            shadow=ft.BoxShadow(
                blur_radius=8,
                spread_radius=1,
                color=ft.Colors.BLACK12,
            ),
            on_click=on_click,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8,
                controls=[
                    ft.Text(icon, size=28, color=ft.Colors.BLACK),
                    ft.Text(title, size=15, color=ft.Colors.BLACK),
                ],
            ),
        )
    
    log_button = ft.Column(
        spacing=14,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=14,
                controls=[
                    menu_box("🦴", "밥주기", lambda e:example()),
                    menu_box("💧", "물주기", lambda e:print("물주기")),
                    menu_box("🦮", "활동기록", lambda e:print("활동기록")),  #🏃
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=14,
                controls=[
                    menu_box("💩", "위생/배변", lambda e:print("위생/배변")),
                    menu_box("🩺", "건강기록", lambda e:print("건강기록")),  #💉💊
                    menu_box("📝", "상태기록", lambda e:print("상태기록")),
                ],
            ),
        ],
    )

    

    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # 추가
        controls=[
            # 상단
            # row_with_alignment(ft.MainAxisAlignment.SPACE_BETWEEN),

            # 메인 컨테이너
            # 요약화면
            #image_dog,
            goal_info,
            # profile,
            gauge_chart(70, "사료 잔여량: 800g"),
            today_log,
        ],
        spacing=0,
    )




# if __name__ == "__main__":
#     import webbrowser, os
#     if os.getenv("FLET_NO_BROWSER"):
#         webbrowser.open = lambda *args, **kwargs: None
#     # ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=34636)
#     ft.run(
#         home_view,
#         assets_dir="assets",
#         view=ft.AppView.WEB_BROWSER,
#         port=34636,
#     )
#     ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=34636)