import os
import webbrowser
from datetime import datetime
from urllib.parse import parse_qs, urlparse

import flet as ft
import flet.canvas as cv

from components.layout.bottom_nav import custom_bottom_appbar
from components.layout.top_bar import top_bar
from views.food_remain_view import food_remain_view
from views.food_select_view import food_select_view
from views.home.home import home_view
from views.logs.log import log_view
from views.logs.log_daily import log_daily_view
from views.logs.log_daily_create import log_daily_create_view
from views.logs.log_weekly import log_weekly_view
from views.mypage.mypage_view import mypage_view


BODY_WHITE = "#FFFFFF"

TAB_ROUTE_MAP = {
    0: "/",
    1: "/log",
    2: "/contents",
    3: "/mypage",
}


def main(page: ft.Page):
    # ============================================================
    # ✅ 페이지 기본 설정
    # ============================================================
    page.bgcolor = BODY_WHITE
    page.padding = 0
    page.spacing = 0

    page.fonts = {
        "Pretendard": "fonts/Pretendard-Regular.otf",
    }

    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(
        font_family="Pretendard",
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLACK,
            on_primary=ft.Colors.WHITE,
            surface=ft.Colors.WHITE,
            on_surface=ft.Colors.BLACK,
            on_surface_variant=ft.Colors.BLACK,
        ),
    )

    has_shown_home_popup = False
    popup_ref = None

    top_bar_area = top_bar()
    body_area = ft.Container(
        expand=True,
        padding=0,
        bgcolor=BODY_WHITE,
    )

    def build_home_popup():
        return ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0.55),
            content=ft.Container(
                width=350,
                height=500,
                bgcolor="#FEF3B9",
                border_radius=20,
                content=ft.Container(
                    padding=ft.padding.only(left=20, right=20, top=24, bottom=16),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            ft.Text(
                                "똑똑 AI가 계산한",
                                size=14,
                                weight=ft.FontWeight.W_600,
                                color=ft.Colors.BLACK,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(height=8),
                            ft.Text(
                                "츄츄에게 딱 맞춘 하루 권장량",
                                size=24,
                                weight=ft.FontWeight.W_700,
                                color=ft.Colors.BLACK,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(height=18),
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=0,
                                controls=[
                                    ft.Container(
                                        width=150,
                                        height=85,
                                        bgcolor=ft.Colors.WHITE,
                                        border_radius=42,
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Text(
                                            "78g",
                                            size=28,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.BLACK,
                                        ),
                                    ),
                                    ft.Container(
                                        width=24,
                                        height=12,
                                        content=cv.Canvas(
                                            shapes=[
                                                cv.Path(
                                                    [
                                                        cv.Path.MoveTo(0, 0),
                                                        cv.Path.LineTo(24, 0),
                                                        cv.Path.LineTo(12, 12),
                                                        cv.Path.Close(),
                                                    ],
                                                    paint=ft.Paint(
                                                        color=ft.Colors.WHITE,
                                                        style=ft.PaintingStyle.FILL,
                                                    ),
                                                )
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            ft.Container(height=20),
                            ft.Image(
                                src="dogbowl.png",
                                width=165,
                                height=165,
                                fit=ft.BoxFit.CONTAIN,
                            ),
                            ft.Container(height=8),
                            ft.IconButton(
                                icon=ft.Icons.CANCEL,
                                icon_color="#C62828",
                                icon_size=42,
                                tooltip="닫기",
                                on_click=close_popup,
                            ),
                        ],
                    ),
                ),
            ),
        )

    def close_popup(e=None):
        nonlocal popup_ref

        if popup_ref and popup_ref in page.overlay:
            page.overlay.remove(popup_ref)

        popup_ref = None
        page.update()

    def open_popup():
        nonlocal popup_ref

        popup_ref = build_home_popup()
        page.overlay.append(popup_ref)
        page.update()


    def parse_selected_date(route: str): # ✅ route query에 있는 date 값을 날짜로 변환
        parsed = urlparse(route)
        params = parse_qs(parsed.query)
        date_value = params.get("date", [None])[0]

        if not date_value:
            return datetime.today().date()

        try:
            return datetime.fromisoformat(date_value).date()
        except ValueError:
            return datetime.today().date()

    def go_tab(index: int): # ✅ 하단 탭 클릭 시 index를 실제 route로 바꿔 이동
        page.go(TAB_ROUTE_MAP.get(index, "/"))

    def route_config(top, body, bottom_index): # ✅ 화면 구성
        return {
            "top": top,
            "body": body,
            "bottom_index": bottom_index,
        }

    # ✅ 현재 path에 맞는 화면 설정을 준비
    # ✅ route에 date가 있으면 같이 꺼내서 daily 화면에 전달
    def build_route_config(path: str, route: str):
        selected_date = parse_selected_date(route)

        routes = {
            "/": route_config(
                body=home_view(page),
                top=top_bar(),
                bottom_index=0,
            ),
            "/log": route_config(
                body=log_view(page),
                top=top_bar("Log", back_route="/"),
                bottom_index=1,
            ),
            "/contents": route_config(
                body=ft.Text("콘텐츠 페이지 준비 중"),
                top=top_bar("Contents", back_route="/"),
                bottom_index=2,
            ),
            "/mypage": route_config(
                body=mypage_view(page),
                top=top_bar("My Page", back_route="/"),
                bottom_index=3,
            ),
            "/food-select": route_config(
                body=food_select_view(page),
                top=top_bar("사료 등록", back_route="/food-remain"),
                bottom_index=99,
            ),
            "/food-remain": route_config(
                body=food_remain_view(page),
                top=top_bar("급여중인 제품", back_route="/mypage"),
                bottom_index=3,
            ),
            "/log/daily": route_config(
                body=log_daily_view(page, selected_date),
                top=top_bar("Log", back_route="/log"),
                bottom_index=1,
            ),
            "/log/daily/create": route_config(
                body=log_daily_create_view(page, selected_date),
                top=top_bar(
                    "Log",
                    back_route=f"/log/daily?date={selected_date.isoformat()}",
                ),
                bottom_index=1,
            ),
            "/log/weekly": route_config(
                body=log_weekly_view(page),
                top=top_bar("Log", back_route="/log"),
                bottom_index=1,
            ),
            "/shop": route_config(
                body=ft.Text("샵 페이지 준비 중"),
                top=top_bar(),
                bottom_index=99,
            ),
        }

        return routes.get(path)

    def apply_route_config(config: dict): # ✅ route 설정값을 실제 화면에 반영
        top_bar_area.controls = config["top"].controls
        body_area.content = config["body"]
        page.bottom_appbar = custom_bottom_appbar(
            selected_index=config["bottom_index"],
            on_tab_change=go_tab,
        )

    # ✅ 현재 route를 읽어서 해당 화면으로 렌더링
    # ✅ 없는 route면 홈("/")으로 이동
    def render_route(route: str):
        nonlocal has_shown_home_popup

        parsed = urlparse(route)
        path = parsed.path or "/"

        config = build_route_config(path, route)

        if config is None:
            page.go("/")
            return

        apply_route_config(config)
        page.update()

        if path == "/" and not has_shown_home_popup:
            has_shown_home_popup = True
            open_popup()

    def on_route_change(e): # ✅ page.go()로 route가 바뀌면 render_route 실행
        render_route(e.route)

    page.on_route_change = on_route_change

    page.floating_action_button = ft.FloatingActionButton(
        content=ft.Container(
            alignment=ft.Alignment(0, 0),
            content=ft.Image(
                src="skeleton.png",
                width=70,
                height=70,
                fit=ft.BoxFit.COVER,
            ),
        ),
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        width=72,
        height=72,
        elevation=0,
        on_click=lambda e: page.go("/shop"),
    )

    page.floating_action_button_location = (
        ft.FloatingActionButtonLocation.CENTER_DOCKED
    )

    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                top_bar_area,
                body_area,
            ],
        )
    )

    render_route(page.route or "/")


if __name__ == "__main__":
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )