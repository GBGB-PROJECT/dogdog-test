import flet as ft


def main(page: ft.Page):
    page.title = "Splash"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Container(
            expand=True, # ☑️ 이게 없으면 그라데이션이 가로만 적용됨 
            width=float("inf"), # ☑️ 이게 없으면 그라데이션이 세로만 적용됨

            # 🟩 수정: gradient 제거하고 단색 배경으로 변경
            bgcolor=ft.Colors.YELLOW,

            content=ft.Column(
                expand = True,
                alignment=ft.MainAxisAlignment.CENTER, # ☑️ 이게 없으면 로고가 천장에 붙음
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, # ☑️ 이게 없으면 로고가 왼쪽에 붙음
                controls=[
                    ft.Image(
                        src="ddoglogo.png",
                        width=150,
                        height=150,
                    ),
                ],
            ),
        )
    )

ft.run(main)

if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.app(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )