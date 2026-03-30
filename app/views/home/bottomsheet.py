import flet as ft

def top_bar(title):
        return ft.Column(
            controls=[
                ft.Container(
                    # padding=ft.padding.only(top=55),
                    # height=100,
                    # width=float("inf"),
                    content=ft.Row(
                        [
                            ft.Text(
                                title,
                                size=20,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Container(
                                alignment=ft.Alignment(1, 0),
                                content=ft.IconButton(icon=ft.Icons.CLOSE_SHARP, 
                                                    icon_color=ft.Colors.GREY_700, 
                                                    icon_size=30, on_click=lambda e: e.page.pop_dialog()),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ),
            ],
        )

# 투데이 로그 기록을 위한 바텀시트
# 바텀시트 도전중.........................
def feeding_bottomSheet():
    bs = ft.BottomSheet(
        open=True,
        scrollable=True,  # 바텀시트 내용만큼 올라옴***
        bgcolor=ft.Colors.WHITE,
        content=
        ft.Container(
            # height=page.window.height * 0.88,   # 핵심
            content=
            ft.Column(
                # scroll=ft.ScrollMode.AUTO,
                # tight=True,
                width=1000,
                controls=
                [
                    top_bar("🦴밥주기"),  # 상단 바
                    ft.Text("오늘 츄츄에게 딱 알맞은 1회 급여량은..", size=16),  # 문구
                    ft.Column
                    (
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=
                        [
                            # 밥그릇 이미지, 급여량
                            ft.Container(
                                alignment=ft.Alignment(0, 0),
                                # shape=ft.BoxShape.CIRCLE,
                                content = ft.Stack(
                                    controls=[
                                        ft.Container(
                                            alignment=ft.Alignment(0, 0),
                                            content=ft.Image(
                                                src="밥그릇.png",
                                                width=200,
                                                height=130
                                            )
                                        ),
                                        ft.Container
                                        (
                                            padding=ft.padding.only(top=45),   # 아래로 내리기
                                            alignment=ft.Alignment(0, 0),
                                            content=ft.Text(
                                                        "40g",
                                                        size=40,
                                                        weight=ft.FontWeight.BOLD,
                                        ))
                                    ]
                                ),
                            ),

                            #상세 내용
                            ft.TextField(  # 급여 중인 사료
                                # value="가장 맛있는 시간 30일, 어덜트 치킨",
                                value="가장 맛있는 시간 30일, 어덜트 치킨",
                                read_only=True,
                                border_radius=9,
                                expand=True,
                                border_color=ft.Colors.GREY_400,
                            ),
                            ft.TextField(  # 급여량
                                value="40g",
                                border_radius=9,
                                expand=True,
                                border_color=ft.Colors.GREY_400,
                            ),
                            ft.TextField(  # 메모
                                hint_text="메모 (선택)",
                                border_radius=9,
                                expand=True,
                                border_color=ft.Colors.GREY_400,
                            ),

                            # 날짜, 시간
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=30,
                                controls=[
                                    ft.Row(
                                        spacing=6,
                                        controls=[
                                            ft.Icon(ft.Icons.CALENDAR_MONTH_OUTLINED, size=18, color=ft.Colors.BLACK54),
                                            ft.Text("2026.03.19", color=ft.Colors.BLACK54),
                                        ],
                                    ),
                                    ft.Row(
                                        spacing=6,
                                        controls=[
                                            ft.Icon(ft.Icons.ACCESS_TIME, size=18, color=ft.Colors.BLACK54),
                                            ft.Text("오전 08:00", color=ft.Colors.BLACK54),
                                        ],
                                    ),
                                ],
                            ),

                            # 저장
                            ft.Container(
                                width=65,
                                height=35,
                                alignment=ft.Alignment(0, 0),
                                # alignment=ft.alignment.center,
                                border_radius=9,
                                bgcolor=ft.Colors.YELLOW_600,
                                content=ft.Text(
                                    "저장",
                                    color=ft.Colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                on_click=lambda e:e.page.pop_dialog()
                    ),])
                ],
                tight=True,
            ),
            padding=10,
    ),
    on_dismiss=lambda e: print("Dismissed!"),
    )
    
    return bs

def water_bottomSheet():
    bs = ft.BottomSheet(
        open=True,
        scrollable=True,  # 바텀시트 내용만큼 올라옴***
        bgcolor=ft.Colors.WHITE,
        content=
        ft.Container(
            # height=page.window.height * 0.88,   # 핵심
            content=
            ft.Column(
                # scroll=ft.ScrollMode.AUTO,
                # tight=True,
                width=1000,
                controls=
                [
                    top_bar("💧물주기"),  # 상단 바
                    # ft.Text("오늘 츄츄에게 딱 알맞은 1회 음수량은..", size=16),  # 문구
                    ft.Column
                    (
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=
                        [
                            ft.TextField(  # 음수량
                                # value="40g",
                                hint_text="물 섭취량(ml)",
                                border_radius=9,
                                expand=True,
                                border_color=ft.Colors.GREY_400,
                            ),
                            ft.TextField(  # 메모
                                hint_text="메모 (선택)",
                                border_radius=9,
                                expand=True,
                                border_color=ft.Colors.GREY_400,
                            ),

                            # 날짜, 시간
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=30,
                                controls=[
                                    ft.Row(
                                        spacing=6,
                                        controls=[
                                            ft.Icon(ft.Icons.CALENDAR_MONTH_OUTLINED, size=18, color=ft.Colors.BLACK54),
                                            ft.Text("2026.03.19", color=ft.Colors.BLACK54),
                                        ],
                                    ),
                                    ft.Row(
                                        spacing=6,
                                        controls=[
                                            ft.Icon(ft.Icons.ACCESS_TIME, size=18, color=ft.Colors.BLACK54),
                                            ft.Text("오전 08:00", color=ft.Colors.BLACK54),
                                        ],
                                    ),
                                ],
                            ),

                            # 저장
                            ft.Container(
                                width=65,
                                height=35,
                                alignment=ft.Alignment(0, 0),
                                # alignment=ft.alignment.center,
                                border_radius=9,
                                bgcolor=ft.Colors.YELLOW_600,
                                content=ft.Text(
                                    "저장",
                                    color=ft.Colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                on_click=lambda e:e.page.pop_dialog()
                    ),])
                ],
                tight=True,
            ),
            padding=10,
            ),
        on_dismiss=lambda e: print("Dismissed!"),
    )
    
    return bs