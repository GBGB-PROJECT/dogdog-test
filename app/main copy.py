import asyncio
import flet as ft
from home import home_view
from log import log_view
# from shop import shop_view
def handle_menu_item_click(e):
        print(f"{e.control.content.value}.on_click")

def dog_list(dog):
    return ft.MenuItemButton(
        width=200,
        content=ft.Text(dog, size=15),
        style=ft.ButtonStyle(
            elevation=0,  # 그림자 제거
            shadow_color=ft.Colors.TRANSPARENT,  # 그림자 완전 제거
        ),
        on_click=handle_menu_item_click,
    )

# 메뉴바
dog_menubar = ft.Row(
        [
            ft.MenuBar(
                expand=True,
                style=ft.MenuStyle(
                    alignment=ft.Alignment.CENTER,
                    bgcolor=ft.Colors.TRANSPARENT, # 메뉴바 투명
                    elevation=0,  # 그림자 제거
                    shadow_color=ft.Colors.TRANSPARENT,  # 그림자 완전 제거
                    mouse_cursor={
                        ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                        ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                    },
                ),
                controls=[
                    ft.SubmenuButton(
                        width=200,
                        content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=
                                    [
                                        ft.Text("츄츄(4년 9개월,♀)", size=16, color=ft.Colors.GREY_700, weight=ft.FontWeight.W_600,),
                                        ft.Icon(ft.Icons.KEYBOARD_ARROW_DOWN, size=25, color=ft.Colors.GREY_700),
                                    ]
                                ),
                        controls=[
                            dog_list("츄츄(4년 9개월,♀)"),
                            dog_list("츄츄(4년 9개월,♀)"),
                            dog_list("츄츄(4년 9개월,♀)"),
                        ],
                    ),
                ],
            )
        ]
    )

# 상단
def top_bar(align: ft.MainAxisAlignment, center):
    return ft.Column(
        controls=[
            ft.Container(
                padding=ft.padding.only(top=55),
                height=100,
                width=float("inf"),
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(0, -1),
                    end=ft.Alignment(0, 1),
                    colors=[ft.Colors.YELLOW_600,ft.Colors.WHITE],
                ),
                content=ft.Row(
                    [
                        ft.Container(
                            width=50,
                            height=50,
                        ),
                        ft.Container(
                            content = center,
                            # on_click=lambda e:print("")
                            ),
                        
                        ft.Container(
                            alignment=ft.Alignment(1, 0),
                            content=ft.IconButton(icon=ft.Icons.NOTIFICATIONS_OUTLINED, icon_color=ft.Colors.GREY_700, icon_size=30),
                            # ft.IconButton(icon=ft.Icons.SETTINGS_OUTLINED, icon_color=ft.Colors.BROWN_300, icon_size=25),
                        ),
                    ],
                    alignment=align,
                ),
            ),
        ],
    )


def main(page: ft.Page):
    page.padding = 0

    def get_nav_index():
        if page.route == "/":
            return 0
        elif page.route == "/log":
            return 1
        elif page.route == "/shop":
            return 2
        elif page.route == "/contents":
            return 3
        elif page.route == "/mypage":
            return 4
        return 0

    def change_page(event):
        print(event)
        idx = event.control.selected_index

        if idx == 0:
            asyncio.create_task(page.push_route("/"))
        elif idx == 1:
            asyncio.create_task(page.push_route("/log"))
        elif idx == 2:
            asyncio.create_task(page.push_route("/shop"))
        elif idx == 3:
            asyncio.create_task(page.push_route("/contents"))
        elif idx == 4:
            asyncio.create_task(page.push_route("/mypage"))

    def bottom_nav():
        return ft.CupertinoNavigationBar(
            bgcolor=ft.Colors.YELLOW_600,
            inactive_color=ft.Colors.BROWN_200,
            active_color=ft.Colors.BROWN_700,
            selected_index=get_nav_index(),   # 추가
            on_change= lambda e : change_page(e),
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

    def get_body():
        if page.route == "/":
            return home_view(page)

        elif page.route == "/log":
            return log_view(page)

        # elif page.route == "/shop":
        #     page.views.append(shop_view(page))
        
        else:
            return ft.Text('페이지 준비 중')

    def route_change(e):
        if page.route == "/":
            content = dog_menubar
        elif page.route == "/log":
            content = ft.Text("Log", size=18)
        # elif page.route == "/shop":
        #     content = "개밥개밥푸드🦴"
        # elif page.route == "/contents":
        #     content = "Contents"
        # elif page.route == "/mypage":
        #     content = "MyPage"
        else:
            content = dog_menubar

        print('1')
        page.views.clear()

        body = get_body()

        page.views.append(
            ft.View(
                route=page.route,
                # appbar=top_bar(ft.MainAxisAlignment.SPACE_BETWEEN, content),
                bgcolor=ft.Colors.WHITE,
                navigation_bar=bottom_nav(),
                controls = [
                    top_bar(ft.MainAxisAlignment.SPACE_BETWEEN, content),
                    ft.Container(
                        expand=True,
                        content=body,
                        # padding=ft.padding.only(top=0, bottom=10),
                    ),
                    # bottom_nav(),
                ],
            )
        )

        page.update()

    page.on_route_change = route_change #페이지 이동 감지 시 실행
    # asyncio.create_task(page.push_route("/"))

    page.route = "/"
    route_change(None)

if __name__ == "__main__":
    import webbrowser, os
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None
    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )