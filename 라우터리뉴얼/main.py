import flet as ft
from urllib.parse import parse_qs, urlparse
from datetime import datetime
from components.layout.top_bar import top_bar
from components.layout.bottom_nav import custom_bottom_appbar
from views.home.home import home_view
from views.logs.log import log_view
from views.logs.log_daily import log_daily_view
from views.logs.log_daily_create import log_daily_create_view
from views.logs.log_weekly import log_weekly_view
from views.food_select_view import food_select_view
from views.food_remain_view import food_remain_view
from views.mypage.mypage_view import mypage_view
# from shop import shop_view
import flet.canvas as cv


def main(page: ft.Page):
    BODY_WHITE = "#FFFFFF"

    page.bgcolor = BODY_WHITE
    page.padding = 0
    page.spacing = 0

    page.fonts = {"Pretendard": "fonts/Pretendard-Regular.otf"}

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

    top_bar_area = top_bar()
    body_area = ft.Container(
        expand=True,
        padding=0,
        bgcolor=BODY_WHITE,
    )

    popup_ref = None

    def close_popup(e=None):
        nonlocal popup_ref
        if popup_ref and popup_ref in page.overlay:
            page.overlay.remove(popup_ref)
        popup_ref = None
        page.update()

    def open_popup():
        nonlocal popup_ref

        popup_ref = ft.Container(
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

        page.overlay.append(popup_ref)
        page.update()

    # ✅ 라우터: 하단 탭 index -> 실제 route 문자열 매핑
    # ✅ bottom nav에서 숫자 index만 넘겨도 page.go() 할 수 있게 연결
    route_map = {
        0: "/",
        1: "/log",
        2: "/contents",
        3: "/mypage",
    }

    # ✅ 라우터: query string 안의 date 값을 꺼내서 날짜 화면에 전달
    # ✅ 예: /log/daily?date=2026-04-08
    def parse_selected_date(route: str):
        parsed = urlparse(route)
        params = parse_qs(parsed.query)
        date_value = params.get("date", [None])[0]

        if not date_value:
            return datetime.today().date()

        try:
            return datetime.fromisoformat(date_value).date()
        except ValueError:
            return datetime.today().date()

    # ✅ 라우터: 하단 탭 클릭 시 index를 route 문자열로 바꿔서 이동
    def render_page(index: int):
        page.go(route_map.get(index, "/"))

    # ✅ 라우터: route마다 필요한 화면 설정만 딕셔너리로 반환
    # ✅ body / top bar / bottom nav index를 한 군데서 관리
    # ✅ render_route 안의 긴 if/elif를 줄이기 위한 핵심 함수
    def build_route_config(path: str, route: str):
        selected_date = parse_selected_date(route)

        route_config = {
            "/": {
                "body": home_view(page),
                "top": top_bar(),
                "bottom_index": 0,
            },
            "/log": {
                "body": log_view(page),
                "top": top_bar("Log", back_route="/"),
                "bottom_index": 1,
            },
            "/contents": {
                "body": ft.Text("콘텐츠 페이지 준비 중"),
                "top": top_bar("Contents", back_route="/"),
                "bottom_index": 2,
            },
            "/mypage": {
                "body": mypage_view(page),
                "top": top_bar("My Page", back_route="/"),
                "bottom_index": 3,
            },
            "/food-select": {
                "body": food_select_view(page),
                "top": top_bar("사료 등록", back_route="/food-remain"),
                "bottom_index": 99,
            },
            "/food-remain": {
                "body": food_remain_view(page),
                "top": top_bar("급여중인 제품", back_route="/mypage"),
                "bottom_index": 3,
            },
            "/log/daily": {
                "body": log_daily_view(page, selected_date),
                "top": top_bar("Log", back_route="/log"),
                "bottom_index": 1,
            },
            "/log/daily/create": {
                "body": log_daily_create_view(page, selected_date),
                "top": top_bar(
                    "Log",
                    back_route=f"/log/daily?date={selected_date.isoformat()}",
                ),
                "bottom_index": 1,
            },
            "/log/weekly": {
                "body": log_weekly_view(page),
                "top": top_bar("Log", back_route="/log"),
                "bottom_index": 1,
            },
            "/shop": {
                "body": ft.Text("샵 페이지 준비 중"),
                "top": top_bar(),
                "bottom_index": 99,
            },
        }

        return route_config.get(path)

    # ✅ 라우터: route 설정값을 실제 화면(top/body/bottom)에 반영
    # ✅ route별 공통 처리 코드를 여기서 한 번만 작성
    def apply_route_config(config: dict):
        body_area.content = config["body"]
        top_bar_area.controls = config["top"].controls
        page.bottom_appbar = custom_bottom_appbar(
            selected_index=config["bottom_index"],
            on_tab_change=render_page,
        )

    # ✅ 라우터: 현재 route 문자열을 읽고
    # ✅ 해당 route 설정을 가져와 화면에 적용
    # ✅ 없는 route면 홈("/")으로 보냄
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

        # ✅ 홈 첫 진입 시에만 팝업 1회 실행
        if path == "/" and not has_shown_home_popup:
            has_shown_home_popup = True
            open_popup()

    # ✅ 라우터: page.go()로 route가 바뀌면 자동으로 render_route 실행
    def on_route_change(e):
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

    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[top_bar_area, body_area],
        )
    )

    # ✅ 라우터: 앱 첫 실행 시 현재 route 기준으로 첫 화면 렌더링
    render_route(page.route or "/")


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