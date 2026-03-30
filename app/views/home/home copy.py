import flet as ft


def home_view(page: ft.Page):
    image_dog = ft.Row(
        # scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                width=200,
                height=200,
                bgcolor=ft.Colors.BLACK,
                shape=ft.BoxShape.CIRCLE,
                image=ft.DecorationImage(
                    src="대추.jpg",
                    fit=ft.BoxFit.COVER,
                    # fit=ft.ImageFit.COVER,
                ),
            )
        ]
    )
    # image_dog.controls[0].width = 100

    # 프로필?
    # profile = ft.Container(
    #     expand=True,
    #     padding=20,
    #     content=ft.Column(
    #         scroll=ft.ScrollMode.AUTO,
    #         controls=[
    #             # profile_card("dog.jpeg", "츄츄(2021.05.25)", "7.3kg"),
    #             image_dog,
    #             # super_long_box([

    #             #     # record_card(
    #             #     #     "3/19",
    #             #     #     "오늘의 기록",
    #             #     #     ["급여량: 43g", "음수량: 100ml", "산책: 30분"]
    #             #     # )

                    
    #             # ]),
    #         ],
    #     ),
    # )

    # 오늘의 기록
    # date_text, title_text, info_list
    # def today_log():
    #     return ft.Row(
    #         alignment=ft.MainAxisAlignment.START,
    #         vertical_alignment=ft.CrossAxisAlignment.CENTER,
    #         spacing=10,
    #         controls=[
    #             mini_box(date_text),
    #             ft.Column(
    #                 spacing=6,
    #                 alignment=ft.MainAxisAlignment.CENTER,
    #                 horizontal_alignment=ft.CrossAxisAlignment.START,
    #                 controls=[
    #                     ft.Row(
    #                         spacing=6,
    #                         controls=[
    #                             ft.Text(f"🔥 오늘의 기록"),
    #                             # ft.Text(
    #                             #     title_text,
    #                             #     size=16,
    #                             #     weight=ft.FontWeight.W_600,
    #                             #     color=ft.Colors.BLACK,
    #                             # ),
    #                         ],
    #                     ),
    #                     ft.Row(
    #                         spacing=6,
    #                         controls=[micro_box(info) for info in info_list],
    #                     ),
    #                 ],
    #             ),
    #         ],
    #     )


    button_style = ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        bgcolor = ft.Colors.BROWN_400,
                        color = ft.Colors.AMBER_100
                    )
    
    status_dog = ft.Column(
        # scroll=ft.ScrollMode.AUTO,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                width=360,
                spacing=8,
                controls=[
                    ft.Container(
                        # content=ft.Text("섭취량"),
                        content=ft.Column([
                        ft.Text("🦴", size=26),
                        ft.Text("섭취량", size=12, weight=ft.FontWeight.W_600, color=ft.Colors.BROWN_700),
                    ], alignment="center", horizontal_alignment="center"),
                        padding=2,
                        # alignment=ft.Alignment.CENTER,
                        bgcolor=ft.Colors.AMBER_200,
                        width=115,
                        height=70,
                        border_radius=10,
                    ),
                    ft.Container(
                        content=ft.Column([
                        ft.Text("💧", size=26),
                        ft.Text("음수량", size=12, weight=ft.FontWeight.W_600, color=ft.Colors.BROWN_700),
                    ], alignment="center", horizontal_alignment="center"),
                        padding=2,
                        # alignment=ft.Alignment.CENTER,
                        bgcolor=ft.Colors.AMBER_200,
                        width=115,
                        height=70,
                        border_radius=10,
                    ),
                    ft.Container(
                        content=ft.Column([
                        ft.Text("사료잔량", size=12, weight=ft.FontWeight.W_600, color=ft.Colors.BROWN_700),
                    ], alignment="center", horizontal_alignment="center"),
                        padding=2,
                        # alignment=ft.Alignment.CENTER,
                        bgcolor=ft.Colors.AMBER_200,
                        width=115,
                        height=70,
                        border_radius=10,
                    ),
                ],
            ),
            # ft.Container(
            #     ft.Button(
            #         "오늘 기록",
            #         style=button_style
            #     ),
            #         # alignment=ft.Alignment.CENTER,
            #         # bgcolor=ft.Colors.AMBER_200,
            #         width=290,
            #         height=50,
            #         border_radius=10,
            #     ),
        ]
    )
    def menu_box(icon, title, on_click=None):
        return ft.Container(
            width=95,
            height=95,
            bgcolor=ft.Colors.YELLOW_500,
            border_radius=16,
            alignment=ft.Alignment(0, 0),
            shadow=ft.BoxShadow(
                blur_radius=8,
                spread_radius=1,
                color=ft.Colors.BLACK12,
            ),
            on_click=on_click,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8,
                controls=[
                    ft.Text(icon, size=28, color=ft.Colors.BLACK),
                    ft.Text(title, size=11, color=ft.Colors.BLACK),
                ],
            ),
        )
    
    log_button = ft.Column(
        spacing=14,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=14,
                controls=[
                    menu_box("🦴", "밥주기", lambda e:print("밥주기")),
                    menu_box("💧", "물주기", lambda e:print("물주기")),
                    menu_box("🦮", "활동기록", lambda e:print("활동기록")),  #🏃
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=14,
                controls=[
                    menu_box("💩", "위생/배변", lambda e:print("위생/배변")),
                    menu_box("🩺", "건강기록", lambda e:print("건강기록")),  #💉💊
                    menu_box("📝", "상태기록", lambda e:print("상태기록")),
                ],
            ),
        ],
    )

    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # 추가
        controls=[
            # 상단
            # row_with_alignment(ft.MainAxisAlignment.SPACE_BETWEEN),

            # 메인 컨테이너
            image_dog,
            # profile,
            status_dog,
            log_button,
        ],
        spacing=15,
    )


# if __name__ == "__main__":
#     import webbrowser, os
#     if os.getenv("FLET_NO_BROWSER"):
#         webbrowser.open = lambda *args, **kwargs: None
#     # ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=34636)
#     ft.run(
#         home_view,
#         assets_dir="assets",
#         view=ft.AppView.WEB_BROWSER,
#         port=34636,
#     )
#     ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=34636)