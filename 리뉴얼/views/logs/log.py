import asyncio
import flet as ft
import datetime
import calendar
import flet_charts as fch
from components.common.banner import banner

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
    page.bgcolor = ft.Colors.WHITE   # ✅ 수정
    page.appbar = None

    content_width = 330

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
        page.update()
    
    def handle_day_click(day):
        tapped_date = datetime.date(current_year, current_month, day)

        if selected_date == tapped_date: # 👈 2번 눌러야 log_daily.py로 이동 
            page.open_log_daily(tapped_date)
        else:
            select_day(day)

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
        if day == 0:
            return ft.Container(
                width=36,
                height=36,
            )

        is_selected = (
            selected_date.year == current_year
            and selected_date.month == current_month
            and selected_date.day == day
        )

        return ft.Container(
            width=36,
            height=36,
            alignment=ft.Alignment(0, 0),
            on_click=lambda e, d=day: handle_day_click(d),
            content=ft.Container(
                width=28,
                height=28,
                border_radius=14,
                bgcolor="#FEF3B9" if is_selected else None,
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

        cell_width = 36
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
                        size=10,
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
                                    style=ft.ButtonStyle(padding=4),
                                    on_click=prev_month,
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.CHEVRON_RIGHT,
                                    icon_size=18,
                                    icon_color=ft.Colors.GREY_700,
                                    style=ft.ButtonStyle(padding=4),
                                    on_click=next_month,
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )

        calendar_container.content = ft.Container(
            width=content_width,
            bgcolor=ft.Colors.WHITE,
            border_radius=24,
            padding=ft.padding.only(left=14, right=14, top=18, bottom=18),
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

    banner_boxes = []

    def set_selected_banner(index):
        for i, box in enumerate(banner_boxes):
            if i == index:
                box.bgcolor = "#FEF3B9"
                box.arrow_circle.bgcolor = ft.Colors.WHITE
            else:
                box.bgcolor = ft.Colors.WHITE
                box.arrow_circle.bgcolor = "#FEF3B9"
        page.update()

    def select_banner(index):
        async def handler(e):
            set_selected_banner(index)
            await asyncio.sleep(0.3)
            page.open_log_weekly()
        return handler

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

    def get_current_chart_data():
        return chart_data_map[selected_metric]

    def refresh_chart():
        chart_container.content = build_line_chart()

    def refresh_metric_selector():
        metric_selector_container.content = ft.Row(
            spacing=10,
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
            padding=ft.padding.symmetric(horizontal=4, vertical=4),
            content=ft.Text(
                f"• {text}",
                size=13,
                color=ft.Colors.BLACK if is_selected else ft.Colors.GREY_600,
                weight=ft.FontWeight.W_600,
            ),
        )

    def build_line_chart():
        chart_data = get_current_chart_data()

        if not chart_data:
            return ft.Container(
                width=290,
                height=240,
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
                        size=13,
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
                    color="#FEF3B9",
                ),
            ],
            min_x=0,
            max_x=len(chart_data) - 1,
            min_y=0,
            max_y=8,
            width=290,
            height=240,
            interactive=True,
            border=ft.border.all(0, ft.Colors.TRANSPARENT),
            left_axis=fch.ChartAxis(
                labels=[],
                label_size=0,
            ),
            bottom_axis=fch.ChartAxis(
                labels=bottom_labels,
                label_size=36,
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

    refresh_metric_selector()
    refresh_chart()
    build_calendar()

    detail_title_section = ft.Text(
        "일주일 상세 기록",
        size=16,
        weight=ft.FontWeight.W_500,
        color=ft.Colors.BLACK,
    )

    detail_banner_section = banner(
        image_src="대추.jpg",
        text="2026.04.06~2026.04.13",
        on_click=select_banner(0),
    )

    banner_boxes.extend([detail_banner_section])

    stats_card_section = ft.Container(
        width=content_width,
        bgcolor="#F7F7F7",
        border=ft.border.all(1, "#D0D0D0"),
        border_radius=20,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    height=48,
                    bgcolor="#FEF3B9",
                    border_radius=ft.border_radius.only(top_left=18, top_right=18),  # 👈 테두리 뭉개짐 수정
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,  # 👈 테두리 뭉개짐 수정
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
                                        width=90,
                                        height=34,
                                        border=ft.border.all(1, "#CFCFCF"),
                                        border_radius=12,
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Text(
                                            "Last 7 Days",
                                            size=11,
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

    main_content = ft.Container(
        width=content_width,
        content=ft.Column(
            spacing=14,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                calendar_container,
                detail_title_section,
                detail_banner_section,
                stats_card_section,
                summary_micro_box_section,
                ft.Container(height=12),
            ],
        ),
    )

    return ft.Container(
        expand=True,
        width=float("inf"),
        alignment=ft.Alignment(0, -1),
        padding=ft.padding.only(left=10, right=10, top=12, bottom=12),
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                main_content,
            ],
        ),
    )