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

    # 빈 자리 생성
    # 상단바가 들어갈 자리 - 추후
    # top_bar_area = ft.Container()
    top_bar_area = top_bar()

    # 본문이 들어갈 자리
    body_area = ft.Container(
        expand=True,
        padding=0,
    )

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

    def render_page(index: int):
        nonlocal current_index
        current_index = index

        # top_bar_area.content = get_top_bar(index)
        body_area.content = get_body(index)

        bottom_nav.selected_index = index
        # bottom_nav.bgcolor = get_nav_bgcolor(index)

        page.update()

    bottom_nav = ft.CupertinoNavigationBar(
            bgcolor=ft.Colors.YELLOW_600,
            inactive_color=ft.Colors.BROWN_200,
            active_color=ft.Colors.BROWN_700,
            # selected_index=current_index,   # 추가
            on_change= lambda e : render_page(e.control.selected_index),
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH, label="Log"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.FOOD_BANK_ROUNDED,
                    selected_icon=ft.Icons.SHOPPING_CART,
                    label="Shop",
                ),
                ft.NavigationBarDestination(icon=ft.Icons.MESSENGER_OUTLINE_ROUNDED, label="Contents"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.PERSON_OUTLINE,
                    selected_icon=ft.Icons.PERSON,
                    label="MyPage"
                ),
            ],
        ) 

    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                top_bar_area,  # 상단바
                body_area,  # 바디
                bottom_nav,  # 하단바
            ],
        )
    )

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