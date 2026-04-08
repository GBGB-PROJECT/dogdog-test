import flet as ft

def custom_appbar(title="중앙 텍스트"):
    right_icons = ft.Row(
        spacing=8,
        controls=[
            ft.Icon(ft.Icons.SEARCH, color=ft.Colors.BLACK),
            ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.BLACK),
        ],
    )

    return ft.Container(
        height=60,
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(width=56),  # 왼쪽 빈자리
                ft.Text(
                    title,
                    size=20,
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.BLACK,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    width=56,   # 오른쪽 아이콘 자리와 비슷하게 맞춤
                    content=right_icons,
                    alignment=ft.Alignment(1, 0),
                ),
            ],
        ),
    )
def invisible_middle_box(image_src):
    return ft.Container(
        width=200,   # 👉 크게 키움 (원하는 값으로 조절)
        height=200,
        bgcolor=ft.Colors.TRANSPARENT,  # 👉 완전 투명
        border=None,  # 👉 테두리 없음
        border_radius=20,  # 👉 둥글게 (선택)
        alignment=ft.Alignment(0, 0),
        content=ft.Image(
            src=image_src,
            fit=ft.BoxFit.COVER,  # 👉 꽉 채우기
        ),
    )

def nav_item(icon, label, selected=False, on_click=None):
    return ft.Container(
        expand=True,
        height=70,
        on_click=on_click,
        alignment=ft.Alignment(0, 0),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
            controls=[
                ft.Icon(
                    icon,
                    color=ft.Colors.BLACK,
                    size=24,
                ),
                ft.Text(
                    label,
                    color=ft.Colors.BLACK,
                    size=12,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        ),
    )


# ✅ 수정: custom_navbar를 BottomAppBar용 내용으로 바꿈
def custom_bottom_appbar(selected_index=0, on_tab_change=None):
    items = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.EDIT_NOTE, "Log"),
        (ft.Icons.MENU_BOOK, "Contents"),
        (ft.Icons.PERSON, "MyPage"),
    ]

    return ft.BottomAppBar(
        bgcolor=ft.Colors.YELLOW,
        shape=ft.CircularRectangleNotchShape(),  # ✅ 가운데 홈(파인 부분) 생성
        content=ft.Row(
            spacing=8,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                nav_item(
                    icon,
                    label,
                    selected=(i == selected_index),
                    on_click=(lambda e, idx=i: on_tab_change(idx) if on_tab_change else None),
                )
                for i, (icon, label) in enumerate(items)
            ],
        ),
    )

def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.TRANSPARENT
    page.appbar = None

    def change_tab(index):
        print("선택된 탭:", index)

    # ✅ 추가: Pagelet 생성
    pagelet = ft.Pagelet(
        expand=True,
        content=ft.Container(),  # ✅ 필수
        bgcolor=ft.Colors.YELLOW,  # ✅ 이게 있으니까 검은 음영이 사라짐 
        )


    pagelet.floating_action_button = ft.FloatingActionButton(
        content=ft.Container(
            width=60,   # 👉 버튼 안 영역 키움
            height=60,
            alignment=ft.Alignment(0, 0),
            content=ft.Image(
                src="bowlradius.png",
                fit=ft.BoxFit.CONTAIN,  # 👉 비율 유지
            ),
        ),
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        elevation=0,
        on_click=lambda e: print("가운데 버튼 클릭"),
    )


    # ✅ 추가: FAB 위치를 하단 중앙에 도킹
    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    # ✅ 추가: 하단바를 BottomAppBar로 연결
    pagelet.bottom_appbar = custom_bottom_appbar(
        selected_index=0,
        on_tab_change=change_tab,
    )


    def menu_box(image_src):
        return ft.Container(
            width=95,
            height=95,
            padding=0,
            margin=0,
            content=ft.Image(
                src=image_src,
                fit=ft.BoxFit.COVER,  # 꽉 채우기
            ),
        )
    def super_long_box(controls=None):
            return ft.Container(
                width=350,
                height=100,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=10,
                padding=10,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,  # 왼쪽 정렬
                    controls=controls or [],  # 👉 리스트로 받기
                ),
            )
        
    def mini_box(text):
        return ft.Container(
            width=70,
            height=60,
            bgcolor=ft.Colors.YELLOW,
            border_radius=10,
            alignment=ft.Alignment(0, 0),  # ✅ 여기 수정
            content=ft.Text(
                text,
                size=18,
                weight=ft.FontWeight.W_700,
                color=ft.Colors.BLACK,
            ),
        )
        
    def micro_box(text):
        return ft.Container(
            padding=ft.Padding.symmetric(horizontal=8, vertical=4),
            bgcolor=ft.Colors.GREY_200,
            border_radius=6,
            content=ft.Text(
                text,
                size=10,
                color=ft.Colors.BLACK,
            ),
        )
    
    def record_card(date_text, title_text, info_list):
        return ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            controls=[
                mini_box(date_text),

                ft.Column(
                    spacing=6,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Row(
                            spacing=6,
                            controls=[
                                ft.Text("🔥"),
                                ft.Text(
                                    title_text,
                                    size=16,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.Colors.BLACK,
                                ),
                            ],
                        ),
                        ft.Row(
                            spacing=6,
                            controls=[micro_box(info) for info in info_list],
                        ),
                    ],
                ),
            ],
        )
    
        
    menu_grid1 = ft.Column(
      spacing=14,
      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      controls=[
          ft.Row(
              alignment=ft.MainAxisAlignment.CENTER,
              spacing=14,
              controls=[
                  menu_box("raw.png"),
                  menu_box("raw.png"),
                  menu_box("raw.png"),
              ],
          ),
      ],
  )
    
    menu_grid2 = ft.Column(
      spacing=14,
      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      controls=[
          ft.Row(
              alignment=ft.MainAxisAlignment.CENTER,
              spacing=14,
              controls=[
                  menu_box("raw.png"),
                  menu_box("raw.png"),
                  menu_box("raw.png"),
              ],
          ),
          ft.Row(
              alignment=ft.MainAxisAlignment.CENTER,
              spacing=14,
              controls=[
                  menu_box("raw.png"),
                  menu_box("raw.png"),
                  menu_box("raw.png"),
              ],
          ),
      ],
  )
    
    dropdown = ft.Dropdown(
        label="sort",
        width=320,
        border=ft.InputBorder.NONE,
        content_padding=10,
        options=[
            ft.dropdown.Option("사과"),
            ft.dropdown.Option("바나나"),
            ft.dropdown.Option("포도"),
        ],
    )

    # ✅ 기존 본문은 content로 유지
    pagelet.content = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, 1),
            end=ft.Alignment(0, -1),
            colors=[
                ft.Colors.WHITE,
                ft.Colors.WHITE,
                ft.Colors.YELLOW,
            ],
        ),
        content=ft.SafeArea(
            expand=True,
            content=ft.Column(
                expand=True,
                spacing=0,
                controls=[
                    custom_appbar("개밥개밥푸드"),
                    ft.Container(
                        expand=True,
                        padding=20,
                        content=ft.Column(
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                ft.Text("🔥오늘 츄츄에게 딱 알맞은 급여량은", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
                                ft.Container(
                                    height=100,
                                    bgcolor=ft.Colors.WHITE,
                                    alignment=ft.Alignment(0, 0),  # 👈 중앙 정렬
                                    content=invisible_middle_box("scale.jpg"),
                                ),                               
                                super_long_box([
                                            record_card(
                                                "3/19",
                                                "급여중인 사료 잔여량",
                                                ["잔여량: 800g", "예상 소진일: 3월 28일"]
                                            )
                                        ]),
                                ft.Text("추천사료", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
                                menu_grid1,
                                ft.Divider(),
                                ft.Text("전체 상품", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
                                ft.Container(
                                    width=350,
                                    height=60,
                                    border=ft.border.all(1, ft.Colors.GREY_300),
                                    border_radius=10,
                                    padding=ft.padding.symmetric(horizontal=10),
                                    alignment=ft.Alignment(0, 0),
                                    content=dropdown,
                                ),
                                menu_grid2,
                            ],
                        ),
                    ),
                ],
            ),
        ),
    )

    page.add(pagelet)


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