import datetime
import calendar
import flet as ft
import flet_charts as fch


def custom_appbar(title="중앙 텍스트"):
    right_icons = ft.Row(
        spacing=8,
        controls=[
            ft.Icon(ft.Icons.SEARCH, color=ft.Colors.BLACK),
            ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.BLACK),
        ],
    )

    return ft.Container(
        height=60,
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(width=56),  # 왼쪽 빈자리
                ft.Text(
                    title,
                    size=20,
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.BLACK,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    width=56,
                    content=right_icons,
                    alignment=ft.Alignment(1, 0),
                ),
            ],
        ),
    )


def nav_item(icon, label, selected=False, on_click=None):
    return ft.Container(
        expand=True,
        height=70,
        on_click=on_click,
        alignment=ft.Alignment(0, 0),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
            controls=[
                ft.Icon(
                    icon,
                    color=ft.Colors.BLACK,
                    size=24,
                ),
                ft.Text(
                    label,
                    color=ft.Colors.BLACK,
                    size=12,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        ),
    )


def custom_bottom_appbar(selected_index=0, on_tab_change=None):
    items = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.EDIT_NOTE, "Log"),
        (ft.Icons.MENU_BOOK, "Contents"),
        (ft.Icons.PERSON, "MyPage"),
    ]

    return ft.BottomAppBar(
        bgcolor=ft.Colors.YELLOW,
        shape=ft.CircularRectangleNotchShape(),
        content=ft.Row(
            spacing=8,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                nav_item(
                    icon,
                    label,
                    selected=(i == selected_index),
                    on_click=(lambda e, idx=i: on_tab_change(idx) if on_tab_change else None),
                )
                for i, (icon, label) in enumerate(items)
            ],
        ),
    )


def banner(
    text="",
    sub_text="",  # 👉 추가
    image_src=None,
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    arrow_bgcolor=ft.Colors.WHITE,
    on_click=None,
):
    left_controls = []

    if image_src:
        left_controls.append(
            ft.Container(
                width=50,
                height=50,
                border_radius=25,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=ft.Image(
                    src=image_src,
                    width=50,
                    height=50,
                    fit=ft.BoxFit.COVER,
                ),
            )
        )

    # 👉 여기 핵심 수정
    left_controls.append(
        ft.Column(
            spacing=2,  # 👉 위아래 간격
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    text,
                    size=18,
                    weight=ft.FontWeight.W_600,
                    color=text_color,
                ),
                ft.Text(
                    sub_text,  # 👉 추가 텍스트
                    size=12,
                    color=ft.Colors.GREY_700,
                ),
            ],
        )
    )

    # 배너 배경이 흰색이면 화살표 동그라미는 노란색
    arrow_bg = ft.Colors.YELLOW if bgcolor == ft.Colors.WHITE else ft.Colors.WHITE

    return ft.Container(
        width=350,
        height=72,
        bgcolor=bgcolor,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=16,
        padding=ft.Padding(left=14, top=0, right=14, bottom=0),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=left_controls,
                ),
                ft.Container(
                    width=40,
                    height=40,
                    bgcolor=arrow_bg,
                    border_radius=20,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Icon(
                        ft.Icons.ARROW_FORWARD,
                        color=ft.Colors.BLACK,
                    ),
                ),
            ],
        ),
    )


def micro_box(text):
    return ft.Container(
        padding=ft.padding.symmetric(horizontal=8, vertical=4),
        bgcolor=ft.Colors.GREY_200,
        border_radius=6,
        content=ft.Text(
            text,
            size=10,
            color=ft.Colors.BLACK,
        ),
    )


def log_view(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = ft.Colors.TRANSPARENT
    page.appbar = None

    def change_tab(index):
        print("선택된 탭:", index)

    pagelet = ft.Pagelet(
        expand=True,
        content=ft.Container(),
        bgcolor=ft.Colors.YELLOW,
    )
    pagelet.floating_action_button = ft.FloatingActionButton(
        content=ft.Container(
            width=60,   # 👉 버튼 안 영역 키움
            height=60,
            alignment=ft.Alignment(0, 0),
            content=ft.Image(
                src="bowlradius.png",
                fit=ft.BoxFit.CONTAIN,  # 👉 비율 유지
            ),
        ),
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        elevation=0,
        on_click=lambda e: print("가운데 버튼 클릭"),
    )

    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    pagelet.bottom_appbar = custom_bottom_appbar(
        selected_index=0,
        on_tab_change=change_tab,
    )

    dropdown = ft.Dropdown(
        label="츄츄",
        width=320,
        border=ft.InputBorder.NONE,
        content_padding=10,
        options=[
            ft.dropdown.Option("사과"),
            ft.dropdown.Option("바나나"),
            ft.dropdown.Option("포도"),
        ],
    )

    # =========================================================
    # [수정 1] 체중 라인차트 데이터 변경
    # 기존: 날짜 5개
    # 변경: 예시 이미지처럼 요일 7개
    # =========================================================
    weight_data = [
        ("Mon", 2.2),
        ("Tue", 2.3),
        ("Wed", 4.2),
        ("Thu", 2.0),
        ("Fri", 5.0),
        ("Sat", 6.2),
        ("Sun", 3.9),
    ]

    # =========================================================
    # [수정 2] build_weight_chart() 완전 수정
    # - 회색 곡선
    # - 왼쪽 숫자 숨김
    # - 가로선만 표시
    # - 아래 요일만 표시
    # =========================================================
    def build_weight_chart():
        if not weight_data:
            return ft.Text("기록이 없습니다.", color=ft.Colors.BLACK)

        normal_points = []
        highlight_points = []
        bottom_labels = []

        for i, (day_text, weight) in enumerate(weight_data):
            normal_points.append(fch.LineChartDataPoint(i, weight))

            # 강조 (Thu=3, Sat=5)
            if i in [3, 5]:
                highlight_points.append(fch.LineChartDataPoint(i, weight))

            bottom_labels.append(
                fch.ChartAxisLabel(
                    value=i,
                    label=ft.Text(
                        day_text,
                        size=15,
                        color="#7A7A7A",
                        weight=ft.FontWeight.W_500,
                    ),
                )
            )

        return fch.LineChart(
            data_series=[
                # 기본 회색 라인
                fch.LineChartData(
                    points=normal_points,
                    stroke_width=3,
                    color="#8A8A8A",
                    curved=True,
                    rounded_stroke_cap=True,
                ),

                # 노란 점만 따로 그리기 (핵심)
                fch.LineChartData(
                    points=highlight_points,
                    stroke_width=0,
                    color="#F2D21B",
                ),
            ],
            min_x=0,
            max_x=len(weight_data) - 1,
            min_y=0,
            max_y=8,
            width=310,
            height=280,
            interactive=False,
            border=ft.border.all(0, ft.Colors.TRANSPARENT),

            left_axis=fch.ChartAxis(
                labels=[],
                label_size=0,
            ),

            bottom_axis=fch.ChartAxis(
                labels=bottom_labels,
                label_size=40,
            ),

            horizontal_grid_lines=fch.ChartGridLines(
                interval=1.5,
                color="#D9D9D9",
                width=1,
            ),

            vertical_grid_lines=fch.ChartGridLines(
                interval=1,
                color=ft.Colors.TRANSPARENT,
                width=0,
            ),
        )

    # -------------------------
    # 인라인 달력 상태
    # -------------------------
    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    selected_date = today

    calendar_container = ft.Container()

    def month_title(year, month):
        return datetime.date(year, month, 1).strftime("%B %Y")

    def select_day(day):
        nonlocal selected_date
        selected_date = datetime.date(current_year, current_month, day)
        build_calendar()

    def prev_month(e):
        nonlocal current_year, current_month
        if current_month == 1:
            current_month = 12
            current_year -= 1
        else:
            current_month -= 1
        build_calendar()

    def next_month(e):
        nonlocal current_year, current_month
        if current_month == 12:
            current_month = 1
            current_year += 1
        else:
            current_month += 1
        build_calendar()

    def day_cell(day):
        if day == 0:
            return ft.Container(
                width=40,
                height=40,
            )

        is_selected = (
            selected_date.year == current_year
            and selected_date.month == current_month
            and selected_date.day == day
        )

        return ft.Container(
            width=40,
            height=40,
            alignment=ft.Alignment(0, 0),
            on_click=lambda e, d=day: select_day(d),
            content=ft.Container(
                width=28,
                height=28,
                border_radius=14,
                bgcolor=ft.Colors.YELLOW if is_selected else None,
                alignment=ft.Alignment(0, 0),
                content=ft.Text(
                    str(day),
                    size=14,
                    color=ft.Colors.BLACK,
                    weight=ft.FontWeight.W_500,
                ),
            ),
        )

    def build_calendar():
        cal = calendar.Calendar(firstweekday=6)
        month_days = cal.monthdayscalendar(current_year, current_month)

        cell_width = 40
        calendar_width = cell_width * 7
        weekday_names = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

        weekday_row = ft.Row(
            width=calendar_width,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Container(
                    width=cell_width,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        name,
                        size=11,
                        color=ft.Colors.GREY_500,
                    ),
                )
                for name in weekday_names
            ],
        )

        week_rows = [
            ft.Row(
                width=calendar_width,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[day_cell(day) for day in week],
            )
            for week in month_days
        ]

        calendar_container.content = ft.Container(
            width=350,
            bgcolor=ft.Colors.WHITE,
            border_radius=30,
            padding=ft.padding.only(left=20, right=20, top=18, bottom=18),
            content=ft.Column(
                tight=True,
                spacing=10,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                month_title(current_year, current_month),
                                size=17,
                                weight=ft.FontWeight.W_500,
                                color=ft.Colors.BLACK,
                            ),
                            ft.Row(
                                spacing=0,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.CHEVRON_LEFT,
                                        icon_size=18,
                                        icon_color=ft.Colors.GREY_700,
                                        style=ft.ButtonStyle(
                                            padding=4,
                                        ),
                                        on_click=prev_month,
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.CHEVRON_RIGHT,
                                        icon_size=18,
                                        icon_color=ft.Colors.GREY_700,
                                        style=ft.ButtonStyle(
                                            padding=4,
                                        ),
                                        on_click=next_month,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    weekday_row,
                    ft.Column(
                        tight=True,
                        spacing=8,
                        controls=week_rows,
                    ),
                ],
            ),
        )

        page.update()

    # 처음 화면에 달력 1회 생성
    build_calendar()

    pagelet.content = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, 1),
            end=ft.Alignment(0, -1),
            colors=[
                ft.Colors.WHITE,
                ft.Colors.WHITE,
                ft.Colors.YELLOW,
            ],
        ),
        content=ft.SafeArea(
            expand=True,
            content=ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    custom_appbar("LOG"),
                    ft.Container(height=12),

                    ft.Container(
                        width=350,
                        height=60,
                        bgcolor=ft.Colors.WHITE,
                        border=ft.border.all(1, ft.Colors.GREY_300),
                        border_radius=10,
                        padding=ft.padding.symmetric(horizontal=10),
                        alignment=ft.Alignment(0, 0),
                        content=dropdown,
                    ),

                    ft.Container(height=2),
                    calendar_container,
                    ft.Container(
                        width=350,
                        content=ft.Divider(
                            thickness=1,
                            color=ft.Colors.GREY_300,
                        ),
                    ),
                    ft.Text(
                        "일주일 상세 기록",
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.BLACK,
                    ),
                    banner(image_src="dog.jpeg", text="2026.03.12~2026.03.19", sub_text="산책 기록 요약", bgcolor=ft.Colors.YELLOW),

                    ft.Container(height=12),

                    # =========================================================
                    # [수정 3] 기존 "체중 변화" 카드 부분을 통째로 교체
                    # - 상단 노란 헤더 추가
                    # - 내부에 Stack 사용
                    # - 차트 위에 노란 점 2개 추가
                    # =========================================================
                    ft.Container(
                        width=350,
                        bgcolor="#F7F7F7",
                        border=ft.border.all(1, "#D0D0D0"),
                        border_radius=20,
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                # 상단 노란 헤더
                                ft.Container(
                                    height=74,
                                    bgcolor=ft.Colors.YELLOW,
                                    padding=ft.padding.only(left=14, right=14, top=14, bottom=10),
                                    content=ft.Stack(
                                        controls=[
                                            ft.Container(
                                                alignment=ft.Alignment(0, -1),
                                                content=ft.Text(
                                                    "우리 아이 기록 통계",
                                                    size=16,
                                                    weight=ft.FontWeight.BOLD,
                                                    color=ft.Colors.BLACK,
                                                ),
                                            ),
                                        ],
                                    ),
                                ),

                                # 카드 본문
                                ft.Container(
                                    padding=ft.padding.all(14),
                                    content=ft.Column(
                                        spacing=12,
                                        controls=[
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Row(
                                                        spacing=14,
                                                        controls=[
                                                            ft.Text(
                                                                "• 급여량",
                                                                size=13,
                                                                color="#777777",
                                                                weight=ft.FontWeight.W_600,
                                                            ),
                                                            ft.Text(
                                                                "• 음수량",
                                                                size=13,
                                                                color="#777777",
                                                                weight=ft.FontWeight.W_600,
                                                            ),
                                                            ft.Text(
                                                                "• 몸무게",
                                                                size=13,
                                                                color="#777777",
                                                                weight=ft.FontWeight.W_600,
                                                            ),
                                                        ],
                                                    ),
                                                    ft.Container(
                                                        width=95,
                                                        height=38,
                                                        border=ft.border.all(1, "#CFCFCF"),
                                                        border_radius=12,
                                                        alignment=ft.Alignment(0, 0),
                                                        content=ft.Text(
                                                            "Last 7 Days",
                                                            size=12,
                                                            color=ft.Colors.BLACK,
                                                            weight=ft.FontWeight.W_500,
                                                        ),
                                                    ),
                                                ],
                                            ),

                                            # 차트만 카드 안에 둠
                                            ft.Container(
                                                width=320,
                                                height=330,
                                                alignment=ft.Alignment(0, 0),
                                                content=build_weight_chart(),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),

                    # ✅ micro_box는 카드 바깥으로 뺌
                    ft.Container(height=8),

                    ft.Container(
                        width=350,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                micro_box("일 평균 000kcal   |   목표 000kcal   |   달성 0회"),
                            ],
                        ),
                    ),

                    ft.Container(height=16),
                ],
            ),
        ),
    )

    return pagelet


if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.run(
        log_view,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )