import os
import webbrowser

import flet as ft

import components as dogdog
import views as catcat


BODY_WHITE = "#FFFFFF"


class Popup:
    def __init__(self, page: ft.Page):
        self.page = page
        self.home_recommendation = self._build_home_recommendation_dialog()

    def _build_home_recommendation_dialog(self) -> ft.AlertDialog:
        return ft.AlertDialog(
            modal=True,
            bgcolor=ft.Colors.TRANSPARENT,
            inset_padding=10,
            content_padding=0,
            shape=ft.RoundedRectangleBorder(radius=20),
            content=ft.Container(
                width=350,
                height=500,
                bgcolor="#FEF3B9",
                border_radius=20,
                padding=0,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
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
                            width=150,
                            height=85,
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
                                        size=28,
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
        self.home_recommendation.open = True
        self.page.show_dialog(self.home_recommendation)

    def close(self, e=None):
        self.home_recommendation.open = False
        self.page.pop_dialog()


def main(page: ft.Page):
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

    def apply_layout(body, top_bar, bottom_index):
        body_area.content = body
        top_bar_area.controls = top_bar.controls
        page.bottom_appbar = dogdog.custom_bottom_navbar(
            selected_index=bottom_index,
            on_tab_change=render_page,
        )
        page.update()

    def open_popup():
        popup.open()

    def render_page(index: int):
        nonlocal has_shown_home_popup

        if index == 0:
            apply_layout(
                body=catcat.home_view(page),
                top_bar=dogdog.top_bar(),
                bottom_index=0,
            )
            if not has_shown_home_popup:
                has_shown_home_popup = True
                open_popup()
            return

        if index == 1:
            apply_layout(
                body=catcat.log_view(page),
                top_bar=dogdog.top_bar("Log"),
                bottom_index=1,
            )
            return

        if index == 2:
            apply_layout(
                body=ft.Text("콘텐츠 페이지 준비 중"),
                top_bar=dogdog.top_bar("Contents"),
                bottom_index=2,
            )
            return

        if index == 3:
            apply_layout(
                body=catcat.mypage_view(page),
                top_bar=dogdog.top_bar("My Page"),
                bottom_index=3,
            )
            return

    def open_food_select(e=None):
        apply_layout(
            body=catcat.food_select_view(page),
            top_bar=dogdog.top_bar("사료 등록"),
            bottom_index=99,
        )

    def open_food_remain(e=None):
        apply_layout(
            body=catcat.food_remain_view(page),
            top_bar=dogdog.top_bar("급여중인 제품"),
            bottom_index=3,
        )

    def open_log_daily(target_date):
        apply_layout(
            body=catcat.log_daily_view(page, target_date),
            top_bar=dogdog.top_bar("Log"),
            bottom_index=1,
        )

    def open_log_daily_create(target_date):
        apply_layout(
            body=catcat.log_daily_create_view(page, target_date),
            top_bar=dogdog.top_bar("Log"),
            bottom_index=1,
        )

    def open_log_weekly():
        apply_layout(
            body=catcat.log_weekly_view(page),
            top_bar=dogdog.top_bar("Log"),
            bottom_index=1,
        )

    def open_shop_from_fab(e=None):
        apply_layout(
            body=ft.Text("샵 페이지 준비 중"),
            top_bar=dogdog.top_bar(),
            bottom_index=99,
        )

    page.open_food_select = open_food_select
    page.open_food_remain = open_food_remain
    page.open_log_daily = open_log_daily
    page.open_log_daily_create = open_log_daily_create
    page.open_log_weekly = open_log_weekly
    page.render_main_tab = render_page

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
        on_click=open_shop_from_fab,
    )

    page.floating_action_button_location = (
        ft.FloatingActionButtonLocation.CENTER_DOCKED
    )

    main_page = ft.Column(
        expand=True,
        spacing=0,
        controls=[
            top_bar_area,
            body_area,
        ],
    )

    page.add(main_page)
    render_page(0)


if __name__ == "__main__":
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )
