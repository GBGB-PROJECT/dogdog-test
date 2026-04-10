import os
import webbrowser
from datetime import datetime

import flet as ft

import components as dogdog
import views as catcat
from components.common.texts import Txt, TxtBold


BODY_WHITE = "#FFFFFF"


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
            # shape=ft.RoundedRectangleBorder(radius=20), # ☑️
            content=ft.Container(
                width=350,
                height=500,
                bgcolor="#FEF3B9",
                border_radius=20,
                # padding=0, # ☑️
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
    page.padding = 0
    page.spacing = 0

    page.fonts = {
        "Pretendard": "fonts/Pretendard-Regular.otf",
        "PretendardBold": "fonts/Pretendard-ExtraBold.otf",
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

    # ============================================================
    # ✅ 현재 화면 상태
    # ============================================================
    view_history = []
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

    def make_view_config(top, body, bottom_index):
        return {
            "top": top,
            "body": body,
            "bottom_index": bottom_index,
        }

    def log_top_bar():
        return dogdog.top_bar("Log", on_back=open_back)

    # ============================================================
    # ✅ 화면 설정 사전
    # - 화면 추가는 여기만 수정하면 됨
    # ============================================================
    def build_view_config(name: str, data=None):
        target_date = data or datetime.today().date()

        view_map = {
            "home": lambda: make_view_config(
                dogdog.top_bar(),
                catcat.home_view(page),
                0,
            ),
            "log": lambda: make_view_config(
                log_top_bar(),
                catcat.log_view(page),
                1,
            ),
            "contents": lambda: make_view_config(
                dogdog.top_bar("Contents", on_back=open_back),
                Txt("콘텐츠 페이지 준비 중"),
                2,
            ),
            "mypage": lambda: make_view_config(
                dogdog.top_bar("My Page", on_back=open_back),
                catcat.mypage_view(page),
                3,
            ),
            "food_remain": lambda: make_view_config(
                dogdog.top_bar("급여중인 제품", on_back=open_back),
                catcat.food_remain_view(page),
                3,
            ),
            "food_select": lambda: make_view_config(
                dogdog.top_bar("사료 등록", on_back=open_back),
                catcat.food_select_view(page),
                99,
            ),
            "log_daily": lambda: make_view_config(
                log_top_bar(),
                catcat.log_daily_view(page, target_date),
                1,
            ),
            "log_daily_create": lambda: make_view_config(
                log_top_bar(),
                catcat.log_daily_create_view(page, target_date),
                1,
            ),
            "log_weekly": lambda: make_view_config(
                log_top_bar(),
                catcat.log_weekly_view(page),
                1,
            ),
            "shop": lambda: make_view_config(
                dogdog.top_bar(on_back=open_back),
                Txt("샵 페이지 준비 중"),
                99,
            ),
        }

        if name not in view_map:
            raise ValueError(f"알 수 없는 화면 이름: {name}")

        return view_map[name]()

    # ============================================================
    # ✅ 실제 화면 반영
    # ============================================================
    def apply_view_config(name: str, data=None):
        nonlocal has_shown_home_popup

        config = build_view_config(name, data)

        current_view["name"] = name
        current_view["data"] = data

        top_bar_area.controls = config["top"].controls
        body_area.content = config["body"]
        page.bottom_appbar = dogdog.custom_bottom_navbar(
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

        tab_map = {
            0: "home",
            1: "log",
            2: "contents",
            3: "mypage",
        }

        open_view(tab_map.get(index, "home"), record_history=False)

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

    simple_open_views = {
        "open_home": "home",
        "open_log": "log",
        "open_contents": "contents",
        "open_mypage": "mypage",
        "open_food_remain": "food_remain",
        "open_food_select": "food_select",
        "open_log_weekly": "log_weekly",
        "open_shop": "shop",
    }

    for attr_name, view_name in simple_open_views.items():
        setattr(page, attr_name, lambda e=None, name=view_name: open_view(name))

    def open_log_daily_wrapper(target_date=None):
        open_view("log_daily", data=target_date)

    def open_log_daily_create_wrapper(target_date=None):
        open_view("log_daily_create", data=target_date)

    page.open_log_daily = open_log_daily_wrapper
    page.open_log_daily_create = open_log_daily_create_wrapper

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