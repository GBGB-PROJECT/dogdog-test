import flet as ft
from components.layout.top_bar import top_bar
from components.layout.bottom_nav import custom_bottom_appbar
from views.home.home import home_view
from views.logs.log import log_view
from views.food_select_view import build_view as food_select_view
# from shop import shop_view


def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    page.spacing = 0

    current_index = 0

        # ✅ 추가
    page.fonts = {
        "Pretendard": "fonts/Pretendard-Regular.otf"
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
        )
    )

    # ─────────────────────────────────────────────
    # 🟦 [추가]
    # 첫 홈 진입 시 팝업 1회만 자동 오픈
    # ─────────────────────────────────────────────
    has_shown_home_popup = False

    # ✅ 상단바
    top_bar_area = top_bar()

    # ✅ 본문 영역
    body_area = ft.Container(
        expand=True,
        padding=0,
    )

    # ✅ 현재 띄운 팝업 참조
    popup_ref = None

    # ✅ 팝업 닫기
    def close_popup(e=None):
        nonlocal popup_ref
        if popup_ref and popup_ref in page.overlay:
            page.overlay.remove(popup_ref)
        popup_ref = None
        page.update()

    # ✅ 추가: 팝업 열기 함수
    def open_popup():
        nonlocal popup_ref

        popup_ref = ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0.95),
            content=ft.Container(
                width=350,
                height=350,
                bgcolor=ft.Colors.YELLOW_600,
                border_radius=20,
                content=ft.Stack(
                    controls=[
                        # ─────────────────────────────────────────────
                        # 🟦 1. bubblebowl (맨 먼저 = 가장 뒤로 감)
                        # ─────────────────────────────────────────────
                        ft.Container(
                            top=8,
                            left=0,
                            right=0,
                            alignment=ft.Alignment(0, -1),
                            content=ft.Image(
                                src="bubblebowl.png",
                                width=220,
                                height=220,
                                fit=ft.BoxFit.CONTAIN,
                            ),
                        ),

                        ft.Container(
                            padding=ft.padding.only(top=65),
                            alignment=ft.Alignment(0, 0),
                            content=ft.Text(
                                "78g",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ),

                        # ─────────────────────────────────────────────
                        # 🟦 2. 제목 (이미지 위에 올라옴)
                        # ─────────────────────────────────────────────
                        ft.Container(
                            top=18,
                            left=0,
                            right=0,
                            content=ft.Column(
                                spacing=2,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        "똑똑 AI가 계산한",
                                        size=14,
                                        color=ft.Colors.BLACK,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        "츄츄에게 딱 맞춘 하루 권장량",
                                        size=18,
                                        weight=ft.FontWeight.W_700,
                                        color=ft.Colors.BLACK,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                            ),
                        ),

                        # ─────────────────────────────────────────────
                        # 🟦 3. 하단 텍스트
                        # ─────────────────────────────────────────────
                        ft.Container(
                            top=230,
                            left=0,
                            right=0,
                            content=ft.Column(
                                spacing=2,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("아침 39g, 저녁 39g", color=ft.Colors.BLACK),
                                    ft.Text("총 310kcal", color=ft.Colors.BLACK),
                                ],
                            ),
                        ),

                        # ─────────────────────────────────────────────
                        # 🟦 4. 닫기 버튼
                        # ─────────────────────────────────────────────
                        ft.Container(
                            bottom=12,
                            left=0,
                            right=0,
                            alignment=ft.Alignment(0, 0),
                            content=ft.IconButton(
                                icon=ft.Icons.CANCEL,
                                icon_color=ft.Colors.RED,
                                icon_size=40,
                                tooltip="닫기",
                                on_click=close_popup,
                            ),
                        ),
                    ]
                ),
            ),
        )

        page.overlay.append(popup_ref)
        page.update()

    # ─────────────────────────────────────────────
    # 🟦 [핵심]
    # food_select 화면 열기
    # - route 이동이 아니라 body_area.content 교체 방식
    # ─────────────────────────────────────────────
    def open_food_select(e=None):
        nonlocal current_index

        current_index = -2
        body_area.content = food_select_view(page)

        # ✅ food_select_view 화면에서만 상단 제목 변경
        top_bar_area.controls = top_bar("사료 등록").controls

        page.bottom_appbar = custom_bottom_appbar(
            selected_index=99,
            on_tab_change=render_page,
        )
        page.update()

    # ─────────────────────────────────────────────
    # 🟨 탭별 본문
    # ─────────────────────────────────────────────
    def get_body(index: int):
        if index == 0:
            return home_view(page)
        elif index == 1:
            return log_view(page)
        elif index == 2:
            return ft.Text("콘텐츠 페이지 준비 중")
        elif index == 3:
            return ft.Text("마이페이지 준비 중")
        return ft.Text("페이지 준비 중")

    # ─────────────────────────────────────────────
    # 🟦 FAB 클릭 시 들어갈 화면
    # ─────────────────────────────────────────────
    def open_shop_from_fab(e=None):
        nonlocal current_index

        current_index = -1
        body_area.content = ft.Text("샵 페이지 준비 중")
        # body_area.content = shop_view(page)

        # ✅ 일반 탭 화면이 아니므로 원래 상단바 복구
        top_bar_area.controls = top_bar().controls

        page.bottom_appbar = custom_bottom_appbar(
            selected_index=99,
            on_tab_change=render_page,
        )
        page.update()

    # ─────────────────────────────────────────────
    # 🟨 메인 탭 렌더링
    # ─────────────────────────────────────────────
    def render_page(index: int):
        nonlocal current_index, has_shown_home_popup
        current_index = index

        body_area.content = get_body(index)

        # ✅ 일반 화면은 다시 원래 츄츄 상단바로 복구
        top_bar_area.controls = top_bar().controls

        page.bottom_appbar = custom_bottom_appbar(
            selected_index=index,
            on_tab_change=render_page,
        )
        page.update()

        # 첫 홈 진입 시 팝업 1회
        if index == 0 and not has_shown_home_popup:
            has_shown_home_popup = True
            open_popup()

    # ─────────────────────────────────────────────
    # 🟦 다른 파일에서 꺼내 쓸 수 있도록 page에 저장
    # ─────────────────────────────────────────────
    page.open_food_select = open_food_select
    page.render_main_tab = render_page

    # ─────────────────────────────────────────────
    # 🟦 가운데 FAB
    # ─────────────────────────────────────────────
    page.floating_action_button = ft.FloatingActionButton(
        content=ft.Container(
            width=60,
            height=60,
            alignment=ft.Alignment(0, 0),
            content=ft.Image(
                src="bowlradius.png",
                fit=ft.BoxFit.CONTAIN,
            ),
        ),
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        elevation=0,
        on_click=open_shop_from_fab,
    )

    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    # 첫 하단 앱바
    page.bottom_appbar = custom_bottom_appbar(
        selected_index=0,
        on_tab_change=render_page,
    )

    # 메인 배치
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

    # 첫 화면
    render_page(0)


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