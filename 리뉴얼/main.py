import flet as ft
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

    # current_index = 0

    # ✅ 폰트
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
    padding=ft.padding.only(
        left=20,
        right=20,
        top=24,
        bottom=16,
    ),
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

    def open_food_select(e=None):
        

        body_area.content = food_select_view(page) 

        top_bar_area.controls = top_bar("사료 등록").controls 

        page.bottom_appbar = custom_bottom_appbar( 
            selected_index=99,
            on_tab_change=render_page,
        )
        page.update()

    def open_food_remain(e=None):

        body_area.content = food_remain_view(page)

        top_bar_area.controls = top_bar("급여중인 제품").controls

        page.bottom_appbar = custom_bottom_appbar(
            selected_index=3,
            on_tab_change=render_page,
        )
        page.update()

    def open_log_daily(target_date):

        body_area.content = log_daily_view(page, target_date)

        top_bar_area.controls = top_bar("Log", back_index=1).controls

        page.bottom_appbar = custom_bottom_appbar(
            selected_index=1,
            on_tab_change=render_page,
        )
        page.update()

    def open_log_daily_create(target_date):

        body_area.content = log_daily_create_view(page, target_date)

        top_bar_area.controls = top_bar("Log", back_index=1).controls

        page.bottom_appbar = custom_bottom_appbar(
            selected_index=1,
            on_tab_change=render_page,
        )
        page.update()

    def open_log_weekly():

        body_area.content = log_weekly_view(page)

        top_bar_area.controls = top_bar("Log", back_index=1).controls

        page.bottom_appbar = custom_bottom_appbar(
            selected_index=1,
            on_tab_change=render_page,
        )
        page.update()

    def get_body(index: int):
        if index == 0:
            return home_view(page)
        elif index == 1:
            return log_view(page)
        elif index == 2:
            return ft.Text("콘텐츠 페이지 준비 중")
        elif index == 3:
            return mypage_view(page)
        
    def open_shop_from_fab(e=None):

        body_area.content = ft.Text("샵 페이지 준비 중")

        top_bar_area.controls = top_bar().controls

        page.bottom_appbar = custom_bottom_appbar(
            selected_index=99,
            on_tab_change=render_page,
        )
        page.update()

    def render_page(index: int):
        nonlocal has_shown_home_popup

        body_area.content = get_body(index)

        if index == 1:
            top_bar_area.controls = top_bar("Log").controls
        elif index == 2:
            top_bar_area.controls = top_bar("Contents").controls
        elif index == 3:
            top_bar_area.controls = top_bar("My Page").controls
        else:
            top_bar_area.controls = top_bar().controls

        page.bottom_appbar = custom_bottom_appbar(
            selected_index=index,
            on_tab_change=render_page,
        )
        page.update()

        if index == 0 and not has_shown_home_popup:
            has_shown_home_popup = True 
            open_popup()

    page.open_food_select = open_food_select
    page.open_food_remain = open_food_remain
    page.open_log_daily = open_log_daily
    page.open_log_daily_create = open_log_daily_create
    page.open_log_weekly = open_log_weekly
    page.render_main_tab = render_page

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
        on_click=open_shop_from_fab, 
    )

    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

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