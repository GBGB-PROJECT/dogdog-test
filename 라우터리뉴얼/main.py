import os
import webbrowser
from datetime import datetime
from urllib.parse import parse_qs, urlparse

import flet as ft

import components as dogdog
import views as catcat


BODY_WHITE = "#FFFFFF"

TAB_ROUTE_MAP = {
    0: "/",
    1: "/log",
    2: "/contents",
    3: "/mypage",
}


class Popup:
    def __init__(self, page: ft.Page):
        self.page = page
        self.day_recommendation = self.day_recommendation_dialog()

    def day_recommendation_dialog(self) -> ft.AlertDialog:
        return ft.AlertDialog(
            modal=True, # 👉 팝업 뜨면 뒤 화면 클릭 못하게 막음
            bgcolor=ft.Colors.TRANSPARENT, 
            inset_padding=10, # ☑️ 범인
            # content_padding=0, # ☑️
            # shape=ft.RoundedRectangleBorder(radius=20), # ☑️
            content=ft.Container(
                width=350,
                height=500,
                bgcolor="#FEF3B9",
                border_radius=20,
                # padding=0, # ☑️ 
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER, # 👉 없으면 위에 붙음
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER, # 👉 없으면 왼쪽으로 몰림
                    spacing=0, # 👉 없으면 텍스트 두줄 간격이 너무 벌어짐 
                    controls=[
                        ft.Text(
                            "똑똑 AI가 계산한",
                            size=14,
                            weight=ft.FontWeight.W_600,
                            color=ft.Colors.BLACK,
                        ),
                        ft.Container(height=8),
                        ft.Text(
                            "츄츄에게 딱 맞춘 하루 권장량",
                            size=24,
                            weight=ft.FontWeight.W_700,
                            color=ft.Colors.BLACK,
                        ),
                        ft.Container(height=18),
                        ft.Stack(
                            width=150, # 👉 없으면 말풍선이 왼쪽으로 이동
                            height=85, # 👉 말풍선 크기 확대 
                            controls=[
                                ft.Image(
                                    src="numberballon.png",
                                    width=150,
                                    height=85,
                                    fit=ft.BoxFit.CONTAIN,
                                ),
                                ft.Container(
                                    alignment=ft.Alignment(0, 0),
                                    content=ft.Text(
                                        "78g",
                                        size=32,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.BLACK,
                                    ),
                                ),
                            ],
                        ),
                        ft.Image(
                            src="dogbowl.png",
                            width=165,
                            height=165,
                            fit=ft.BoxFit.CONTAIN,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.CANCEL,
                            icon_color="#C62828",
                            icon_size=42,
                            tooltip="닫기",
                            on_click=self.close,
                        ),
                    ],
                ),
            ),
            open=False,
        )

    def open(self):
        self.day_recommendation.open = True
        self.page.show_dialog(self.day_recommendation)

    def close(self, e=None):
        self.day_recommendation.open = False
        self.page.pop_dialog()


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
    popup = Popup(page)

    top_bar_area = dogdog.top_bar()
    body_area = ft.Container(
        expand=True,
        padding=0,
        bgcolor=BODY_WHITE,
    )

    def open_popup():
        popup.open()

    # ============================================================
    # ✅ route query에 있는 date 값을 날짜로 변환
    # 예: /log/daily?date=2026-04-09
    # ============================================================
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

    # ============================================================
    # ✅ 하단 탭 클릭 시 index를 실제 route로 바꿔 이동
    # ============================================================
    def go_tab(index: int):
        page.go(TAB_ROUTE_MAP.get(index, "/"))

    # ============================================================
    # ✅ 화면 구성값 묶기
    # ============================================================
    def route_config(top, body, bottom_index):
        return {
            "top": top,
            "body": body,
            "bottom_index": bottom_index,
        }

    # ============================================================
    # ✅ 현재 path에 맞는 화면 설정 준비
    # ✅ route에 date가 있으면 같이 꺼내서 daily 화면에 전달
    # ============================================================
    def build_route_config(path: str, route: str):
        selected_date = parse_selected_date(route)

        routes = {
            "/": route_config(
                top=dogdog.top_bar(),
                body=catcat.home_view(page),
                bottom_index=0,
            ),
            "/log": route_config(
                top=dogdog.top_bar("Log", back_route="/"),
                body=catcat.log_view(page),
                bottom_index=1,
            ),
            "/contents": route_config(
                top=dogdog.top_bar("Contents", back_route="/"),
                body=ft.Text("콘텐츠 페이지 준비 중"),
                bottom_index=2,
            ),
            "/mypage": route_config(
                top=dogdog.top_bar("My Page", back_route="/"),
                body=catcat.mypage_view(page),
                bottom_index=3,
            ),
            "/food-select": route_config(
                top=dogdog.top_bar("사료 등록", back_route="/food-remain"),
                body=catcat.food_select_view(page),
                bottom_index=99,
            ),
            "/food-remain": route_config(
                top=dogdog.top_bar("급여중인 제품", back_route="/mypage"),
                body=catcat.food_remain_view(page),
                bottom_index=3,
            ),
            "/log/daily": route_config(
                top=dogdog.top_bar("Log", back_route="/log"),
                body=catcat.log_daily_view(page, selected_date),
                bottom_index=1,
            ),
            "/log/daily/create": route_config(
                top=dogdog.top_bar(
                    "Log",
                    back_route=f"/log/daily?date={selected_date.isoformat()}",
                ),
                body=catcat.log_daily_create_view(page, selected_date),
                bottom_index=1,
            ),
            "/log/weekly": route_config(
                top=dogdog.top_bar("Log", back_route="/log"),
                body=catcat.log_weekly_view(page),
                bottom_index=1,
            ),
            "/shop": route_config(
                top=dogdog.top_bar(),
                body=ft.Text("샵 페이지 준비 중"),
                bottom_index=99,
            ),
        }

        return routes.get(path)

    # ============================================================
    # ✅ route 설정값을 실제 화면에 반영
    # ============================================================
    def apply_route_config(config: dict):
        top_bar_area.controls = config["top"].controls
        body_area.content = config["body"]
        page.bottom_appbar = dogdog.custom_bottom_navbar(
            selected_index=config["bottom_index"],
            on_tab_change=go_tab,
        )

    # ============================================================
    # ✅ 현재 route를 읽어서 해당 화면으로 렌더링
    # ✅ 없는 route면 홈("/")으로 이동
    # ============================================================
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

    # ============================================================
    # ✅ page.go()로 route가 바뀌면 render_route 실행
    # ============================================================
    def on_route_change(e):
        render_route(e.route)

    page.on_route_change = on_route_change

    # ============================================================
    # ✅ 중앙 FAB 설정
    # ============================================================
    page.floating_action_button = ft.FloatingActionButton(
        content=ft.Image(
            src="skeleton.png",
            fit=ft.BoxFit.COVER,
        ),
        bgcolor=ft.Colors.TRANSPARENT,
        shape=ft.CircleBorder(),
        # 1. 기본 그림자 
        elevation=0,
        
        # 2. 상태별 그림자(Elevation) 모두 제거
        hover_elevation=0,      # 마우스 올렸을 때 튀어나오는 그림자
        highlight_elevation=0,  # 클릭했을 때 생기는 그림자
        focus_elevation=0,      # 포커스 되었을 때 그림자
        
        # 3. 클릭/오버 시 생기는 어두운 오버레이(리플) 투명하게 만들기
        splash_color=ft.Colors.TRANSPARENT,  # 클릭 시 퍼지는 물결 효과색
        hover_color=ft.Colors.TRANSPARENT,   # 마우스 올렸을 때 덮이는 색상
        focus_color=ft.Colors.TRANSPARENT,   # 탭/포커스 시 덮이는 색상
        on_click=lambda e: page.go("/shop"),
    )

    page.floating_action_button_location = (
        ft.FloatingActionButtonLocation.CENTER_DOCKED
    )

    # ============================================================
    # ✅ 기본 레이아웃 등록
    # ============================================================
    main_page = ft.Column(
        expand=True,
        spacing=0,
        controls=[
            top_bar_area,
            body_area,
        ],
    )

    page.add(main_page)

    # ============================================================
    # ✅ 최초 route 렌더링
    # ============================================================
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