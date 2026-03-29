import flet as ft


def red_custom_appbar(title="중앙 텍스트"):
    right_icons = ft.Row(
        spacing=8,
        controls=[
            ft.Icon(ft.Icons.SEARCH, color=ft.Colors.WHITE),
            ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.WHITE),
        ],
    )

    return ft.Container(
        height=60,
        bgcolor=ft.Colors.RED,
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(width=56),
                ft.Text(
                    title,
                    size=20,
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    width=56,
                    content=right_icons,
                    alignment=ft.Alignment(1, 0),
                ),
            ],
        ),
    )


def nav_item(icon, label, on_click=None):
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
                ft.Icon(icon, color=ft.Colors.WHITE, size=24),
                ft.Text(
                    label,
                    color=ft.Colors.WHITE,
                    size=12,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        ),
    )


def Red_custom_bottom_appbar(on_tab_change=None):
    items = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.EDIT_NOTE, "Log"),
        (ft.Icons.MENU_BOOK, "Contents"),
        (ft.Icons.PERSON, "MyPage"),
    ]

    return ft.BottomAppBar(
        bgcolor=ft.Colors.RED,
        shape=ft.CircularRectangleNotchShape(),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                nav_item(
                    icon,
                    label,
                    on_click=(lambda e, idx=i: on_tab_change(idx) if on_tab_change else None),
                )
                for i, (icon, label) in enumerate(items)
            ],
        ),
    )


def color_change_box(label, selected=False, on_click=None):
    return ft.Container(
        width=350,
        height=100,

        # ✅ 추가: 선택되면 배경을 노란색으로 변경
        # ✅ 기능: "있다" 또는 "없다" 클릭 시 해당 박스가 강조됨
        bgcolor=ft.Colors.YELLOW if selected else ft.Colors.WHITE,

        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=10,
        on_click=on_click,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Row(
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            ft.Icons.RADIO_BUTTON_CHECKED
                            if selected
                            else ft.Icons.RADIO_BUTTON_UNCHECKED,
                            color=ft.Colors.BLACK,
                            size=20,
                        ),
                        ft.Text(
                            label,
                            size=14,
                            weight=ft.FontWeight.W_500,
                            color=ft.Colors.BLACK,
                        ),
                    ],
                )
            ],
        ),
    )


def white_large_box(
    line1,
    line3,
    line4,
    line5,
    line6,
    bgcolor=ft.Colors.WHITE,
    border_color=ft.Colors.GREY_300,
    on_click=None,
):
    return ft.Container(
        width=330,
        bgcolor=bgcolor,
        border_radius=16,
        border=ft.border.all(1, border_color),
        padding=ft.padding.symmetric(horizontal=16, vertical=16),
        on_click=on_click,
        content=ft.Column(
            spacing=12,
            tight=True,  # ✅ 내용 높이만큼만 자연스럽게 박스 크기 잡기
            controls=[
                ft.Text(
                    line1,
                    size=14,
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.BLACK,
                ),

                # ✅ 추가: 4자 택일용 라디오 그룹
                # ✅ 기능: 단어1~단어4 중 하나만 가로로 선택 가능하게 만듦
                ft.RadioGroup(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=14,
                        controls=[
                            ft.Radio(value="1주",
                                     label="1주",
                                     label_style=ft.TextStyle(  # ✅ 추가: 라벨 글자 진하게
                            color=ft.Colors.BLACK,  # ✅ 추가
                            weight=ft.FontWeight.W_500,  # ✅ 추가
                            size=14,  # ✅ 추가
                        ),
                        ),
                            ft.Radio(value="2주", 
                                     label="2주",
                                     label_style=ft.TextStyle(  # ✅ 추가: 라벨 글자 진하게
                            color=ft.Colors.BLACK,  # ✅ 추가
                            weight=ft.FontWeight.W_500,  # ✅ 추가
                            size=14,  # ✅ 추가
                        ),
                        ),
                            ft.Radio(value="3주", 
                                     label="3주",
                                     label_style=ft.TextStyle(  # ✅ 추가: 라벨 글자 진하게
                            color=ft.Colors.BLACK,  # ✅ 추가
                            weight=ft.FontWeight.W_500,  # ✅ 추가
                            size=14,  # ✅ 추가
                        ),
                        ),
                            ft.Radio(value="4주", 
                                     label="4주",
                                     label_style=ft.TextStyle(  # ✅ 추가: 라벨 글자 진하게
                            color=ft.Colors.BLACK,  # ✅ 추가
                            weight=ft.FontWeight.W_500,  # ✅ 추가
                            size=14,  # ✅ 추가
                        ),),
                        ],
                    )
                ),

                ft.Text(
                    line3,
                    size=13,
                    color=ft.Colors.BLACK,
                ),
                ft.Text(
                    line4,
                    size=13,
                    color=ft.Colors.BLACK,
                ),
                ft.Text(
                    line5,
                    size=13,
                    color=ft.Colors.BLACK,
                ),
                ft.Text(
                    line6,
                    size=13,
                    color=ft.Colors.BLACK,
                ),
            ],
        ),
    )


def red_long_box(
    text,
    bgcolor=ft.Colors.RED,
    text_color=ft.Colors.WHITE,
    border_color=ft.Colors.GREY_300,
    on_click=None,
    icon=None,
):
    controls = []

    if icon:
        controls.append(ft.Icon(icon, size=18, color=text_color))

    controls.append(
        ft.Text(
            text,
            size=14,
            weight=ft.FontWeight.W_500,
            color=text_color,
        )
    )

    return ft.Container(
        width=350,
        height=50,
        bgcolor=bgcolor,
        border=ft.Border.all(1, border_color),
        border_radius=10,
        padding=10,
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
            controls=controls,
        ),
    )


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.WHITE
    page.appbar = None

    # ✅ 추가: 현재 있다/없다 중 어떤 항목이 선택되었는지 저장하는 변수
    # ✅ 기능: "있다" 선택 시 화이트 박스를 보여주고, "없다" 선택 시 숨김 처리
    selected_option = None

    # ✅ 추가: 본문 전체를 다시 그려 넣을 컬럼
    # ✅ 기능: 선택 상태가 바뀔 때 controls를 다시 구성하기 쉽게 해줌
    body_column = ft.Column(
        expand=True,
        spacing=0,
        scroll=ft.ScrollMode.AUTO,  # ✅ 내용 길어지면 스크롤 가능
    )

    # 🟦 추가: 하단 고정 버튼 영역
    # 🟦 기능: 본문 스크롤과 분리해서 네비바 바로 위에 버튼을 항상 고정
    fixed_bottom_button = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=ft.padding.only(left=16, right=16, top=10, bottom=10),
        content=ft.Container(
            content=red_long_box(
                text="똑똑 배송 시작하기",
            ),
            alignment=ft.Alignment(0, 0),
        ),
    )

    def change_tab(index):
        print("선택된 탭:", index)

    # ✅ 추가: 있다/없다 선택 상태를 바꾸는 함수
    # ✅ 기능: 박스를 눌렀을 때 selected_option 값을 바꾸고 화면을 새로 그림
    def select_option(value):
        nonlocal selected_option
        selected_option = value
        rebuild_body()

    # ✅ 추가: 현재 선택 상태에 따라 본문 UI를 다시 구성하는 함수
    # ✅ 기능: "있다" 선택 시 첫 번째 박스 아래에 white_large_box를 보이게 함
    def rebuild_body():
        body_column.controls = [
            red_custom_appbar("개밥개밥푸드"),
            ft.Container(margin=ft.margin.symmetric(vertical=10)),
            ft.Container(
                content=ft.Text("똑똑 배송 시작하기"),
                alignment=ft.Alignment(0, 0),
            ),
            ft.Divider(),

            # ✅ 첫 번째 color_change_box
            ft.Container(
                content=color_change_box(
                    label="새로운 똑똑 배송 시작하기",
                    selected=(selected_option == "새로운 똑똑 배송 시작하기"),
                    on_click=lambda e: select_option("새로운 똑똑 배송 시작하기"),
                ),
                alignment=ft.Alignment(0, 0),
            ),

            # ✅ 추가: "새로운 똑똑 배송 시작하기" 선택 시 첫 번째 박스 바로 아래에 상세 박스 표시
            # ✅ 기능: visible=True일 때만 화이트 라지 박스가 화면에 나타남
            ft.Container(
                content=white_large_box(
                    line1="첫구매 배송주기",
                    line3="똑똑 배송으로 주문하신 제품의 급여 시작일 등록시 똑똑 AI가 급여량과 잔여량을 계산하여 실제 사료 소진일에 맞춰 똑똑 배송 설정한 제품을 자동 결제 및 배송합니다",
                    line4="급여시작일 미등록시 선택하신 첫구매 배송주기에 맞춰 자동 결제 및 배송됩니다.",
                    line5="구독 중인 똑똑 배송 제품은 자동 결제, 배송되기 7,3일 전 알려드립니다.",
                    line6="🚨 마이페이지 내 똑똑 배송 미루기 와 똑똑 배송 일정 당기기를 할 수 있습니다",
                ),
                alignment=ft.Alignment(0, 0),
                margin=ft.margin.symmetric(vertical=10),
                visible=(selected_option == "새로운 똑똑 배송 시작하기"),
            ),

            # ✅ 두 번째 color_change_box : 없다
            ft.Container(
                content=color_change_box(
                    label="나의 똑똑 배송에 추가하기",
                    selected=(selected_option == "나의 똑똑 배송에 추가하기"),
                    on_click=lambda e: select_option("나의 똑똑 배송에 추가하기"),
                ),
                alignment=ft.Alignment(0, 0),
            ),

            # 🟦 추가: 본문 마지막 여백
            # 🟦 기능: 마지막 컨텐츠가 고정 버튼에 가려지지 않도록 아래 공간 확보
            ft.Container(height=20),
        ]
        page.update()

    pagelet = ft.Pagelet(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        content=ft.Container(),
    )

    pagelet.floating_action_button = ft.FloatingActionButton(
        content=ft.Image(
            src="bowlradius_red.png",
            width=40,
            height=40,
            fit=ft.BoxFit.COVER,
        ),
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        elevation=0,
        on_click=lambda e: print("가운데 버튼 클릭"),
    )

    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    pagelet.bottom_appbar = Red_custom_bottom_appbar(on_tab_change=change_tab)

    # 🟦 수정: pagelet.content에 body_column만 넣지 않고
    # 🟦 기능: "스크롤 본문" + "하단 고정 버튼" 구조로 분리
    pagelet.content = ft.Column(
        expand=True,
        spacing=0,
        controls=[
            ft.Container(
                expand=True,
                content=body_column,
            ),
            fixed_bottom_button,
        ],
    )

    # ✅ 추가: 앱 시작 시 처음 화면을 한 번 그려주는 호출
    # ✅ 기능: 아무것도 선택되지 않은 초기 상태 UI를 먼저 화면에 표시
    rebuild_body()

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