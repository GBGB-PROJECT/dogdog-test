import datetime
import calendar
import flet as ft


def main(page: ft.Page):
    # =========================
    # 1. page 기본 설정
    # =========================
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = ft.Colors.WHITE
    page.appbar = None

    # =========================
    # 2. 달력 화면 상태값
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
        page.update()

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
            on_click=lambda e, d=day: select_day(d),  # ☑️ 날짜 칸을 누르면 그 날짜를 선택하게 함
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
        cal = calendar.Calendar(firstweekday=6)  # ☑️ firstweekday=6 은 일요일부터 시작하게 만드는 설정
        month_days = cal.monthdayscalendar(current_year, current_month)

        cell_width = 40
        calendar_width = cell_width * 7
        weekday_names = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

        weekday_row = ft.Row(  # ☑️  SUN MON TUE WED ...
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
            ft.Row(  # ☑️ Row 안에 날짜칸(day_cell)을 7개 넣음
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
            border=ft.border.all(1, ft.Colors.GREY_300),
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
                                month_title(current_year, current_month),  # ☑️ 예: March 2026
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
                    weekday_row,  # ☑️  SUN MON TUE WED ...
                    ft.Column(
                        tight=True,
                        spacing=8,
                        controls=week_rows,  # ☑️ 날짜칸(day_cell) 7개
                    ),
                ],
            ),
        )

    # =========================
    # 8. 달력 초기 렌더링
    # =========================
    build_calendar()  # ☑️ 이게 없으면 화면에 달력이 안뜸

    # =========================
    # 10. page 본문 연결
    # =========================
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                expand=True,
                alignment=ft.Alignment(0, 0),
                content=calendar_container,  # ☑️ 이거 없어도 달력 안나옴
            ),
        )
    )


if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )