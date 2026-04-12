import os
import webbrowser
from datetime import datetime

import flet as ft

import components as components
import views as views
from components.common.texts import Txt, TxtBold
from views.view_registry import build_view_config

BODY_WHITE = "#FFFFFF"

MAIN_TAB_VIEW_MAP = {
    0: "home",
    1: "log",
    2: "contents",
    3: "mypage",
}

SIMPLE_OPEN_VIEWS = {
    "open_home": "home",
    "open_log": "log",
    "open_contents": "contents",
    "open_mypage": "mypage",
    "open_food_remain": "food_remain",
    "open_food_select": "food_select",
    "open_log_weekly": "log_weekly",
    "open_shop": "shop",
}


class Popup:
    def __init__(self, page: ft.Page):
        self.page = page
        self.day_recommendation = self.day_recommendation_dialog()

    def day_recommendation_dialog(self) -> ft.AlertDialog:
        return ft.AlertDialog(
            modal=True,  # 👉 팝업 뜨면 뒤 화면 클릭 못하게 막음
            bgcolor=ft.Colors.TRANSPARENT,
            inset_padding=10,  # ☑️ 범인
            content_padding=0,  # ☑️ 범인 2
            content=ft.Container(
                width=350,
                height=500,
                bgcolor="#FEF3B9",
                border_radius=20,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,  # 👉 없으면 위에 붙음
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # 👉 없으면 왼쪽으로 몰림
                    spacing=0,  # 👉 없으면 텍스트 두줄 간격이 너무 벌어짐
                    controls=[
                        Txt(
                            "똑똑 AI가 계산한",
                            size=14,
                            weight=ft.FontWeight.W_600,
                            color=ft.Colors.BLACK,
                        ),
                        ft.Container(height=8),
                        TxtBold(
                            "츄츄에게 딱 맞춘 하루 권장량",
                            size=24,
                            color=ft.Colors.BLACK,
                        ),
                        ft.Container(height=18),
                        ft.Stack(
                            width=170,  # ⬅️ 없으면 말풍선이 왼쪽으로 이동
                            height=90,  # ⬅️ 말풍선 크기 확대
                            alignment=ft.Alignment(0, 0),  # ⬅️ 추가 (Stack 기준 고정)
                            controls=[
                                ft.Image(
                                    src="numberballon.png",
                                    width=170,  # ⬅️
                                    height=90,  # ⬅️ 핵심
                                    fit=ft.BoxFit.CONTAIN,
                                ),
                                ft.Container(
                                    expand=True,  # ⬅️ 추가 (이게 핵심)
                                    alignment=ft.Alignment(0, -0.17),  # ⬅️ 수정
                                    content=TxtBold(
                                        "78g",
                                        size=45,  # ⬅️
                                        color=ft.Colors.BLACK,
                                    ),
                                ),
                            ],
                        ),
                        ft.Container(
                            margin=ft.margin.only(top=-28),  # ⬅️ 밥그릇과 말풍선 간격
                            content=ft.Image(
                                src="dogbowl.png",
                                width=210,
                                height=210,
                                fit=ft.BoxFit.CONTAIN,
                            ),
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
    page.padding = 0  # ⬅️ 이게 없으니 화면 주변부에 회색 테두리 형성
    # page.spacing = 0

    page.fonts = {
        "Pretendard": "fonts/Pretendard-Regular.otf",
        "PretendardBold": "fonts/Pretendard-ExtraBold.otf",
    }

    page.theme_mode = ft.ThemeMode.LIGHT  # ⬅️ 이게 없으면 모바일 화면이 검게 나옴
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

    top_bar_area = components.top_bar()
    body_area = ft.Container(
        expand=True,  # ⬅️ 이게 없으니 바텀시트 제외한 스크롤바 전멸
        # padding=0,
        # bgcolor=BODY_WHITE,
    )

    # ============================================================
    # ✅ 현재 화면 상태
    # ============================================================
    view_history = []  # ⬅️ 이게 없으면 버튼 눌러도 화면 전환 불가
    current_view = {"name": None, "data": None}

    def open_popup():
        popup.open()

    # ============================================================
    # ✅ 현재 화면 저장
    # ============================================================
    def save_current_view():
        if current_view["name"] is None:
            return

        view_history.append(
            {
                "name": current_view["name"],
                "data": current_view["data"],
            }
        )

    # ============================================================
    # ✅ 실제 화면 반영
    # ============================================================
    def apply_view_config(name: str, data=None):
        nonlocal has_shown_home_popup

        config = build_view_config(page, open_back, name, data)

        current_view["name"] = name
        current_view["data"] = data

        top_bar_area.controls = config["top"].controls
        body_area.content = config["body"]
        page.bottom_appbar = components.custom_bottom_navbar(
            selected_index=config["bottom_index"],
            on_tab_change=open_main_tab,
        )
        page.update()

        if name == "home" and not has_shown_home_popup:
            has_shown_home_popup = True
            open_popup()

    # ============================================================
    # ✅ 유일한 화면 전환 함수
    # ============================================================
    def open_view(name: str, data=None, record_history=True):
        if record_history:
            save_current_view()

        apply_view_config(name, data)

    # ============================================================
    # ✅ 메인 탭 이동
    # ============================================================
    def open_main_tab(index: int):
        view_history.clear()
        open_view(MAIN_TAB_VIEW_MAP.get(index, "home"), record_history=False)

    # ============================================================
    # ✅ 뒤로가기
    # ============================================================
    def open_back(e=None):
        if not view_history:
            open_view("home", record_history=False)
            return

        previous = view_history.pop()
        open_view(
            previous["name"],
            data=previous["data"],
            record_history=False,
        )

    # ============================================================
    # ✅ 기존 뷰 파일 호환용 page.open_xxx 래퍼
    # - 뷰 파일 수정량 최소화
    # ============================================================
    page.open_view = open_view
    page.open_back = open_back

    for attr_name, view_name in SIMPLE_OPEN_VIEWS.items():  # ⬅️ 이게 없으면 버튼 눌러도 화면 전환 불가
        setattr(page, attr_name, lambda e=None, name=view_name: open_view(name))

    def open_log_daily(target_date=None):
        open_view("log_daily", data=target_date)

    def open_log_daily_create(target_date=None):
        open_view("log_daily_create", data=target_date)

    page.open_log_daily = open_log_daily
    page.open_log_daily_create = open_log_daily_create

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
        elevation=0,
        hover_elevation=0,
        highlight_elevation=0,
        focus_elevation=0,
        splash_color=ft.Colors.TRANSPARENT,
        hover_color=ft.Colors.TRANSPARENT,
        focus_color=ft.Colors.TRANSPARENT,
        on_click=lambda e: open_view("shop"),
    )

    page.floating_action_button_margin = ft.margin.only(bottom=2)
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
    # ✅ 최초 화면 렌더링
    # ============================================================
    open_view("home", record_history=False)


if __name__ == "__main__":
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )