import flet as ft
from components.layout.top_bar import top_bar
from views.home.home import home_view
from views.logs.log import log_view
# from shop import shop_view


def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    page.spacing = 0

    current_index = 0

    # ✅ 상단바
    top_bar_area = top_bar()

    # ✅ 본문 영역
    body_area = ft.Container(
        expand=True,
        padding=0,
    )

    # ✅ 추가: 현재 띄운 팝업을 저장할 변수
    popup_ref = None

    # ✅ 추가: 팝업 닫기 함수
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
            expand=True,  # ✅ 화면 전체를 덮는 바깥 컨테이너
            alignment=ft.Alignment(0, 0.7),  # ✅ 여기서 화면 기준 위치 조절
            content=ft.Container(
                width=350,
                height=350,
                bgcolor=ft.Colors.YELLOW_600,
                border_radius=20,
                padding=20,
                content=ft.Column(
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("똑똑 AI가 계산한", size=14, color=ft.Colors.BLACK),
                        ft.Text(
                            "츄츄에게 딱 맞춘 하루 권장량",
                            size=18,
                            weight=ft.FontWeight.W_700,
                            color=ft.Colors.BLACK,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Image(
                            src="밥그릇.png",
                            width=120,
                            height=120,
                            fit=ft.BoxFit.CONTAIN,
                        ),
                        ft.Text("아침 39g, 저녁 39g", color=ft.Colors.BLACK),
                        ft.Text("총 310kcal", color=ft.Colors.BLACK),
                        ft.TextButton("X", on_click=close_popup),
                    ],
                ),
            ),
        )

        page.overlay.append(popup_ref)
        page.update()

    # ✅ 바디 내용 결정
    def get_body(index: int):
        if index == 0:
            return home_view(page)
        elif index == 1:
            return log_view(page)
        elif index == 2:
            return ft.Text("샵 페이지 준비 중")
            # return shop_view(page)
        elif index == 3:
            return ft.Text("콘텐츠 페이지 준비 중")
            # return contents_view(page)
        elif index == 4:
            return ft.Text("마이페이지 준비 중")
            # return mypage_view(page)
        return ft.Text("페이지 준비 중")

    # ✅ 화면 갱신
    def render_page(index: int):
        nonlocal current_index
        current_index = index

        body_area.content = get_body(index)
        bottom_nav.selected_index = index
        page.update()

    # ✅ 하단 네비게이션
    bottom_nav = ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.YELLOW_600,
        inactive_color=ft.Colors.BROWN_200,
        active_color=ft.Colors.BROWN_700,
        on_change=lambda e: render_page(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH, label="Log"),
            ft.NavigationBarDestination(
                icon=ft.Icons.FOOD_BANK_ROUNDED,
                selected_icon=ft.Icons.SHOPPING_CART,
                label="Shop",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.MESSENGER_OUTLINE_ROUNDED,
                label="Contents"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON_OUTLINE,
                selected_icon=ft.Icons.PERSON,
                label="MyPage"
            ),
        ],
    )

    # ✅ 화면 배치
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                top_bar_area,
                body_area,
                bottom_nav,
            ],
        )
    )

    # ✅ 첫 화면 렌더링
    render_page(0)

    # ✅ 시작하자마자 팝업 띄우기
    open_popup()


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