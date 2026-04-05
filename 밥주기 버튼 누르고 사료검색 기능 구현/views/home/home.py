import flet as ft
from datetime import datetime
import math
import flet.canvas as cv
from views.home.bottomsheet import select_feeding_bottomSheet, water_bottomSheet

# body
def home_view(page: ft.Page):
    # ─────────────────────────────────────────────
    # ✅ Fold 같은 넓은 화면에서도 본문이 너무 퍼지지 않도록
    # ✅ 아예 고정 폭으로 묶기
    # ─────────────────────────────────────────────
    content_width = 330

    # body 상단 - 강아지 이미지와 목표치
    image_dog = ft.Container(
        width=120,
        height=120,
        bgcolor=ft.Colors.BLACK,
        shape=ft.BoxShape.CIRCLE,
        image=ft.DecorationImage(
            src="대추.jpg",
            fit=ft.BoxFit.COVER,
            # fit=ft.ImageFit.COVER,
        ),
    )

    def goal_status(title, current, total, unit):
        return ft.Column(
            spacing=6,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    title,
                    size=15,
                    color=ft.Colors.GREY_700,
                    weight=ft.FontWeight.W_600,
                ),
                ft.ProgressBar(
                    width=150,
                    height=13,
                    value=current / total,
                    bgcolor=ft.Colors.GREY_300,
                    color=ft.Colors.YELLOW_600,
                    border_radius=10,
                ),
                ft.Text(
                    f"{current}/{total}{unit}",
                    size=15,
                    color=ft.Colors.GREY_500,
                    weight=ft.FontWeight.W_600,
                ),
            ],
        )

    goal_info = ft.Container(
        width=content_width,
        padding=ft.padding.only(left=8, right=8, top=16, bottom=10),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
            controls=[
                image_dog,
                ft.Column(
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        goal_status("🏃목표 활동량", 30, 90, "분"),
                        goal_status("🍚목표 칼로리", 35, 69, "kcal"),
                    ],
                ),
            ],
        ),
    )

    def gauge_chart(percent=40, label="사료 잔여량: 800g"):
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
            width=content_width,
            alignment=ft.Alignment(0, 0),
            content=ft.Container(
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
                            padding=ft.padding.only(top=35),
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
            ),
        )

    # 오늘의 기록
    today_log = ft.Container(
        width=content_width,
        padding=ft.padding.only(left=8, right=8, top=10, bottom=10),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
            controls=[
                ft.Container(
                    width=70,
                    height=70,
                    bgcolor=ft.Colors.YELLOW_600,
                    border_radius=10,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        f'{datetime.now().strftime("%m/%d")}',
                        size=18,
                        weight=ft.FontWeight.W_600,
                        color=ft.Colors.BLACK,
                    ),
                ),
                ft.Column(
                    spacing=6,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Text(
                            "🔥 오늘의 기록",
                            size=18,
                            weight=ft.FontWeight.W_500,
                            color=ft.Colors.BLACK,
                        ),
                        ft.Row(
                            spacing=6,
                            wrap=True,
                            controls=[
                                ft.Text("급여량: 43g", size=12, color=ft.Colors.GREY_800),
                                ft.Text("음수량: 100ml", size=12, color=ft.Colors.GREY_800),
                                ft.Text("산책: 30분", size=12, color=ft.Colors.GREY_800),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    )

    def menu_box(icon, title, on_click=None):
        return ft.Container(
            width=100,
            height=86,
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
                spacing=6,
                controls=[
                    ft.Text(icon, size=26, color=ft.Colors.BLACK),
                    ft.Text(
                        title,
                        size=14,
                        color=ft.Colors.BLACK,
                        weight=ft.FontWeight.W_600,
                    ),
                ],
            ),
        )

    log_button = ft.Container(
        width=content_width,
        padding=ft.padding.only(left=4, right=4, top=6, bottom=8),
        content=ft.Column(
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=8,
                    controls=[
                        menu_box("🦴", "밥주기", lambda e: page.show_dialog(select_feeding_bottomSheet())),
                        menu_box("💧", "물주기", lambda e: page.show_dialog(water_bottomSheet())),
                        menu_box("🦮", "활동기록", lambda e: print("활동기록")),
                    ],
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=8,
                    controls=[
                        menu_box("💩", "위생/배변", lambda e: print("위생/배변")),
                        menu_box("🩺", "건강기록", lambda e: print("건강기록")),
                        menu_box("📝", "상태기록", lambda e: print("상태기록")),
                    ],
                ),
            ],
        ),
    )

    return ft.Container(
        expand=True,
        width=float("inf"),
        alignment=ft.Alignment(0, -1),
        content=ft.Container(
            width=content_width,
            content=ft.Column(
                expand=False,
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    goal_info,
                    gauge_chart(0, "사료 잔여량: ???g"),
                    today_log,
                    log_button,
                    ft.Container(height=16),
                ],
            ),
        ),
    )