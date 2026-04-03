import flet as ft
import datetime
import calendar
import flet_charts as fch
import math
import flet.canvas as cv


def banner(
    text="",
    # sub_text="",
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

    left_controls.append(
        ft.Column(
            spacing=2,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    text,
                    size=18,
                    weight=ft.FontWeight.W_600,
                    color=text_color,
                ),
                # ft.Text(
                #     sub_text,
                #     size=12,
                #     color=ft.Colors.GREY_700,
                # ),
            ],
        )
    )

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


def change_tab(index):
    print("선택된 탭:", index)


def log_view(page: ft.Page):
    # =========================
    # 1. page 기본 설정
    # =========================
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = ft.Colors.TRANSPARENT
    page.appbar = None

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

    # =========================
    # 3. 달력 화면 상태값
    # =========================
    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    selected_date = today

    calendar_container = ft.Container()

    # =========================
    # 4. 달력 관련 내부 함수
    # =========================
    def month_title(year, month):  # ☑️ strftime("%B %Y") → "March 2026"
        return datetime.date(year, month, 1).strftime("%B %Y")

    def select_day(day):
        nonlocal selected_date  # ☑️ selected_date 값을 수정하겠다는 선언
        selected_date = datetime.date(current_year, current_month, day)
        build_calendar()
        page.update()  # ✅ 선택 날짜 눌렀을 때 바로 반영

    def prev_month(e):
        nonlocal current_year, current_month
        if current_month == 1:
            current_month = 12
            current_year -= 1
        else:
            current_month -= 1
        build_calendar()
        page.update()

    def next_month(e):
        nonlocal current_year, current_month
        if current_month == 12:
            current_month = 1
            current_year += 1
        else:
            current_month += 1
        build_calendar()
        page.update()

    def day_cell(day):
        if day == 0:  # ☑️ 달력에서 빈칸 칸 처리
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
            on_click=lambda e, d=day: select_day(d),  # ☑️ 날짜 칸 클릭
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

    def build_calendar():  # ☑️ 달력 데이터 생성기
        cal = calendar.Calendar(firstweekday=6)  # ☑️ 일요일 시작
        month_days = cal.monthdayscalendar(current_year, current_month)

        cell_width = 40
        calendar_width = cell_width * 7
        weekday_names = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

        weekday_row = ft.Row(
            width=calendar_width,
            spacing=0,
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
                spacing=0,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[day_cell(day) for day in week],
            )
            for week in month_days
        ]

        header = ft.Container(
            width=calendar_width,
            height=32,
            content=ft.Stack(
                controls=[
                    # ✅ 제목은 진짜 가운데
                    ft.Container(
                        width=calendar_width,
                        height=32,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Text(
                            month_title(current_year, current_month),
                            size=17,
                            weight=ft.FontWeight.W_500,
                            color=ft.Colors.BLACK,
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ),
                    # ✅ 화살표는 오른쪽 고정
                    ft.Container(
                        width=calendar_width,
                        height=32,
                        alignment=ft.Alignment(1, 0),
                        content=ft.Row(
                            spacing=0,
                            tight=True,
                            alignment=ft.MainAxisAlignment.END,
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
                    ),
                ],
            ),
        )

        calendar_container.content = ft.Container(
            width=350,
            bgcolor=ft.Colors.WHITE,
            border_radius=30,
            padding=ft.padding.only(left=20, right=20, top=18, bottom=18),
            content=ft.Column(
                tight=True,
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    header,
                    weekday_row,
                    ft.Column(
                        tight=True,
                        spacing=8,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=week_rows,
                    ),
                ],
            ),
        )

    # =========================
    # 5. 차트 관련 내부 상태값 / 데이터
    # =========================
    selected_metric = "급여량"
    chart_container = ft.Container()
    metric_selector_container = ft.Container()

    chart_data_map = {
        "급여량": [
            ("Mon", 2.8),
            ("Tue", 3.0),
            ("Wed", 3.4),
            ("Thu", 3.1),
            ("Fri", 3.6),
            ("Sat", 3.8),
            ("Sun", 3.3),
        ],
        "음수량": [],
        "몸무게": [
            ("Mon", 2.2),
            ("Tue", 2.3),
            ("Wed", 4.2),
            ("Thu", 2.0),
            ("Fri", 5.0),
            ("Sat", 6.2),
            ("Sun", 3.9),
        ],
    }

    # =========================
    # 6. 차트 관련 함수
    # =========================
    def get_current_chart_data():
        return chart_data_map[selected_metric]

    def refresh_chart():
        chart_container.content = build_line_chart()

    def refresh_metric_selector():
        metric_selector_container.content = ft.Row(
            spacing=14,
            controls=[
                metric_label("급여량"),
                metric_label("음수량"),
                metric_label("몸무게"),
            ],
        )

    def change_metric(metric):
        nonlocal selected_metric
        selected_metric = metric
        refresh_metric_selector()
        refresh_chart()
        page.update()

    def metric_label(text):
        is_selected = selected_metric == text

        return ft.Container(
            on_click=lambda e, metric=text: change_metric(metric),
            ink=True,
            border_radius=8,
            padding=ft.padding.symmetric(horizontal=6, vertical=4),
            content=ft.Text(
                f"• {text}",
                size=14,
                color=ft.Colors.BLACK if is_selected else ft.Colors.GREY_600,
                weight=ft.FontWeight.W_600,
            ),
        )

    def build_line_chart():
        chart_data = get_current_chart_data()

        if not chart_data:
            return ft.Container(
                width=310,
                height=280,
                alignment=ft.Alignment(0, 0),
                content=ft.Text(
                    "기록이 없습니다.",
                    color=ft.Colors.BLACK,
                    size=16,
                    weight=ft.FontWeight.W_500,
                ),
            )

        normal_points = []
        highlight_points = []
        bottom_labels = []

        for i, (day_text, value) in enumerate(chart_data):
            normal_points.append(fch.LineChartDataPoint(i, value))

            bottom_labels.append(
                fch.ChartAxisLabel(
                    value=i,
                    label=ft.Text(
                        day_text,
                        size=14,
                        color=ft.Colors.GREY_700,
                        weight=ft.FontWeight.W_500,
                    ),
                )
            )

        sorted_points = sorted(
            enumerate(chart_data),
            key=lambda item: item[1][1],
            reverse=True,
        )[:1]

        highlight_indexes = [idx for idx, _ in sorted_points]

        for i, (_, value) in enumerate(chart_data):
            if i in highlight_indexes:
                highlight_points.append(fch.LineChartDataPoint(i, value))

        return fch.LineChart(
            data_series=[
                fch.LineChartData(
                    points=normal_points,
                    stroke_width=3,
                    color="#8A8A8A",
                    curved=True,
                    rounded_stroke_cap=True,
                ),
                fch.LineChartData(
                    points=highlight_points,
                    stroke_width=0,
                    point=True,
                    color="#F2D21B",
                ),
            ],
            min_x=0,
            max_x=len(chart_data) - 1,
            min_y=0,
            max_y=8,
            width=310,
            height=280,
            interactive=True,
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

    # =========================
    # 7. 첫 차트 / 버튼 생성
    # =========================
    refresh_metric_selector()
    refresh_chart()

    # =========================
    # 8. 달력 초기 렌더링
    # =========================
    build_calendar()

    # =========================
    # 9. 레이아웃 섹션
    # =========================
    detail_title_section = ft.Text(
        "일주일 상세 기록",
        size=16,
        weight=ft.FontWeight.W_500,
        color=ft.Colors.BLACK,
    )

    detail_banner_section = banner(
        image_src="dog.jpeg",
        text="2026.03.12~2026.03.19",
        bgcolor=ft.Colors.YELLOW_600,
    )

    stats_card_section = ft.Container(
        width=350,
        bgcolor="#F7F7F7",
        border=ft.border.all(1, "#D0D0D0"),
        border_radius=20,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    height=74,
                    bgcolor=ft.Colors.YELLOW_600,
                    padding=ft.padding.only(left=14, right=14, top=14, bottom=10),
                    content=ft.Stack(
                        controls=[
                            ft.Container(
                                alignment=ft.Alignment(0, -1),
                                content=ft.Text(
                                    "츄츄 기록 통계",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK,
                                ),
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    padding=ft.padding.all(14),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    metric_selector_container,
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
                            chart_container,
                        ],
                    ),
                ),
            ],
        ),
    )

    summary_micro_box_section = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            micro_box("일 평균 000kcal   |   목표 000kcal   |   달성 0회"),
        ],
    )

    # ✅ 제일 중요한 수정
    # ✅ 달력 / 제목 / 배너 / 카드 / 요약박스를 전부 같은 width=350 본문 컬럼 하나에 넣음
    # ✅ 이전처럼 calendar_container 와 body_section 를 바깥 Column에 따로 두지 않음
    # ✅ 그래서 전체가 같은 중앙축으로 정렬됨
    main_content = ft.Container(
        width=350,
        content=ft.Column(
            spacing=14,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                calendar_container,
                detail_title_section,
                detail_banner_section,
                stats_card_section,
                summary_micro_box_section,
            ],
        ),
    )

    # =========================
    # 10. 최종 반환
    # =========================
    return ft.Container(
        expand=True,
        width=float("inf"),  # ✅ 화면 전체 폭을 먼저 잡아주고
        alignment=ft.Alignment(0, -1),  # ✅ 그 안에서 본문을 진짜 중앙 정렬
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            controls=[
                main_content,
            ],
        ),
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