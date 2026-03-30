import flet as ft

def main(page: ft.Page):
    page.title = "개발개발"

    PRIMARY       = "#2979FF"
    TEXT_DARK     = "#0D1B3E"
    TEXT_GRAY     = "#90A4AE"
    BG_MAIN       = "#F0F4FF"
    BG_CARD       = "#E8EFF9"
    BTN_RECORD    = "#FFFFFF"
    BTN_INPUT     = "#EEF4FF"
    NAV_BG        = "#FFFFFF"

    nav_state = {"selected": "HOME"}

    def shadow(opacity=0.10):
        return ft.BoxShadow(
            spread_radius=0,
            blur_radius=10,
            color=ft.Colors.with_opacity(opacity, PRIMARY),
            offset=ft.Offset(0, 3),
        )

    def snack(msg):
        def handler(e):
            page.snack_bar = ft.SnackBar(ft.Text(msg, color=ft.Colors.WHITE), bgcolor=PRIMARY)
            page.snack_bar.open = True
            page.update()
        return handler

    # 1. 상단 헤더
    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text("똑똑", size=17, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    bgcolor=PRIMARY, 
                    border_radius=10, 
                    padding=ft.Padding(10, 4, 10, 4),
                ),
                ft.Text("🐾dogdog🐾", size=24, weight=ft.FontWeight.BOLD, color=PRIMARY),
                ft.Row(controls=[
                    ft.IconButton(icon=ft.Icons.NOTIFICATIONS_OUTLINED, icon_color=PRIMARY, icon_size=22),
                    ft.IconButton(icon=ft.Icons.SETTINGS_OUTLINED, icon_color=PRIMARY, icon_size=22),
                ], spacing=0),
            ],
            alignment="spaceBetween",
        ),
        padding=ft.Padding(20, 10, 20, 10),
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.with_opacity(0.07, ft.Colors.BLACK), offset=ft.Offset(0, 2)),
    )

# 2. 펫 카드
    AVATAR_RADIUS = 50 
    
    pet_card = ft.Container(
        content=ft.Row([
            ft.Container(
                content=ft.CircleAvatar(
                    content=ft.Container(
                        content=ft.Image(
                            src="대추.jpg",
                            fit="cover", 
                            width=AVATAR_RADIUS * 2,
                            height=AVATAR_RADIUS * 2,
                        ),
                        shape="circle", 
                    ),
                    radius=AVATAR_RADIUS, 
                    bgcolor=ft.Colors.GREY_200,
                ),
                shadow=shadow(0.15), 
                shape="circle",
            ),
            ft.Column([
                ft.Text("흰둥이", size=25, weight=ft.FontWeight.BOLD, color=TEXT_DARK),
                ft.Text("개배고파!", size=18, color=TEXT_GRAY),
            ], spacing=4)
        ], spacing=20), 
        padding=25, 
        margin=ft.Margin(16, 0, 16, 0),
        bgcolor=ft.Colors.WHITE,
        border_radius=25,  
        shadow=shadow(0.08)
    )

    # 기록 섹션
    def section_label(title: str, color: str):
        return ft.Row([
            ft.Container(width=4, height=18, bgcolor=color, border_radius=2),
            ft.Text(title, size=14, weight=ft.FontWeight.BOLD, color=TEXT_DARK),
        ], spacing=8)

    def record_card_btn(label, icon, on_click=None):
        return ft.Container(
            content=ft.Column([
                ft.Text(icon, size=26),
                ft.Text(label, size=12, weight=ft.FontWeight.W_600, color=TEXT_DARK),
            ], alignment="center", horizontal_alignment="center"),
            bgcolor=BTN_RECORD, 
            border_radius=16, 
            padding=16, 
            expand=1, 
            on_click=on_click, 
            shadow=shadow(0.08),
            border=ft.Border(ft.BorderSide(1, "#D6E4FF"), ft.BorderSide(1, "#D6E4FF"), ft.BorderSide(1, "#D6E4FF"), ft.BorderSide(1, "#D6E4FF")),
        )

    record_section = ft.Container(
        content=ft.Column([
            section_label("기록", PRIMARY),
            ft.Container(height=10),
            ft.Row([
                record_card_btn("섭취량", "🦴", snack("섭취량 기록")),
                record_card_btn("음수량", "💧", snack("음수량 기록")),
            ], spacing=10),
            ft.Container(height=10),
            ft.Container(
                content=ft.Row([
                    ft.Row([ft.Text("📋", size=20), ft.Text("기록 요약", size=13, weight=ft.FontWeight.W_600, color=TEXT_DARK)], spacing=8),
                    ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=PRIMARY, size=14),
                ], alignment="spaceBetween"),
                bgcolor=BTN_RECORD, border_radius=16, padding=14, on_click=snack("기록 요약 화면"),
                border=ft.Border(ft.BorderSide(1, "#D6E4FF"), ft.BorderSide(1, "#D6E4FF"), ft.BorderSide(1, "#D6E4FF"), ft.BorderSide(1, "#D6E4FF")),
            ),
        ]),
        bgcolor=BG_CARD, border_radius=20, padding=16, margin=ft.Margin(16, 0, 16, 0)
    )

# 입력 섹션
    def input_btn(label, icon):
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Text(icon, size=22), 
                    width=44, height=44, 
                    bgcolor=ft.Colors.WHITE, 
                    border_radius=22, 
                    alignment=ft.Alignment(0, 0), 
                    shadow=shadow(0.08)
                ),
                ft.Text(
                    label, 
                    size=12, 
                    weight=ft.FontWeight.BOLD, 
                    color=ft.Colors.BLACK87    
                )
            ], horizontal_alignment="center", spacing=8),
            
            bgcolor=ft.Colors.WHITE, 
            border_radius=16, 
            padding=15, 
            expand=1, 
            on_click=snack(f"{label} 입력"),
            border=ft.Border(
                ft.BorderSide(1.5, "#D0E0FF"),
                ft.BorderSide(1.5, "#D0E0FF"), 
                ft.BorderSide(1.5, "#D0E0FF"), 
                ft.BorderSide(1.5, "#D0E0FF")
            ),
        )
    input_grid = ft.Column([
        ft.Row([input_btn(label, icon) for label, icon in [("밥주기", "🍚"), ("물주기", "🚰"), ("약먹기", "💊")]], spacing=10),
        ft.Row([input_btn(label, icon) for label, icon in [("대소변", "🚽"), ("체중", "⚖️"), ("관찰", "🔍")]], spacing=10),
    ], spacing=10)

    input_section = ft.Container(
        content=ft.Column([
            section_label("데일리", PRIMARY), 
            ft.Container(height=10), 
            input_grid
        ]),
        padding=ft.Padding(16, 0, 16, 0)
    )
    def build_nav():
        items = [("HOME", ft.Icons.HOME_OUTLINED, ft.Icons.HOME), ("LOG", ft.Icons.ARTICLE_OUTLINED, ft.Icons.ARTICLE), ("AI", ft.Icons.SMART_TOY_OUTLINED, ft.Icons.SMART_TOY), ("My", ft.Icons.PERSON_OUTLINED, ft.Icons.PERSON)]
        def on_tap(label):
            nav_state["selected"] = label
            main_layout.controls[2] = build_nav()
            page.update()
        nav_buttons = []
        for label, icon_off, icon_on in items:
            is_sel = nav_state["selected"] == label
            nav_buttons.append(ft.GestureDetector(content=ft.Column([ft.Icon(icon_on if is_sel else icon_off, color=PRIMARY if is_sel else TEXT_GRAY, size=24), ft.Text(label, size=10, color=PRIMARY if is_sel else TEXT_GRAY, weight="bold")], horizontal_alignment="center", spacing=2), on_tap=lambda e, lbl=label: on_tap(lbl), expand=1))
        
        shop_fab = ft.Container(
            content=ft.Column([ft.Text("🛒", size=18), ft.Text("Shop", size=9, color="white", weight="bold")], alignment="center", horizontal_alignment="center", spacing=0),
            width=56, height=56, bgcolor=PRIMARY, border_radius=28, shadow=shadow(0.3), on_click=snack("Shop 이동"), offset=ft.Offset(0, -0.3)
        )
        nav_buttons.insert(2, ft.Container(content=shop_fab, expand=1, alignment=ft.Alignment(0, 0)))
        return ft.Container(content=ft.Row(nav_buttons, alignment="spaceAround", vertical_alignment="center"), bgcolor=NAV_BG, height=80, padding=ft.Padding(0, 0, 0, 15), shadow=ft.BoxShadow(blur_radius=10, color="#10000000", offset=ft.Offset(0, -2)))

    # 전체 조립
    body = ft.Column(controls=[ft.Container(height=20), pet_card, ft.Container(height=25), record_section, ft.Container(height=25), input_section, ft.Container(height=30)], scroll="auto", expand=True)
    main_layout = ft.Column(controls=[header, ft.Container(content=body, expand=True, bgcolor=BG_MAIN), build_nav()], spacing=0, expand=True)
    page.add(main_layout)

if __name__ == "__main__":
    import webbrowser, os
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None
    ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=34636)