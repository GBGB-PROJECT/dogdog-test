import flet as ft


def red_custom_appbar(title="중앙 텍스트"):
    right_icons = ft.Row(
        spacing=8,
        controls=[
            ft.Icon(ft.Icons.SEARCH, color=ft.Colors.WHITE),         # ✅ 아이콘 흰색
            ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.WHITE),  # ✅ 아이콘 흰색
        ],
    )

    return ft.Container(
        height=60,
        bgcolor=ft.Colors.RED,  # ✅ 배경 빨간색
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
                    color=ft.Colors.WHITE,  # ✅ 텍스트 흰색
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
                    color=ft.Colors.WHITE,
                    size=24,
                ),
                ft.Text(
                    label,
                    color=ft.Colors.WHITE,
                    size=12,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        ),
    )


# ✅ 수정: custom_navbar를 BottomAppBar용 내용으로 바꿈
def Red_custom_bottom_appbar(selected_index=0, on_tab_change=None):
    items = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.EDIT_NOTE, "Log"),
        (ft.Icons.MENU_BOOK, "Contents"),
        (ft.Icons.PERSON, "MyPage"),
    ]

    return ft.BottomAppBar(
        bgcolor=ft.Colors.RED,
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
        bgcolor=ft.Colors.WHITE,  # ✅ 이게 있으니까 검은 음영이 사라짐
    )

    pagelet.floating_action_button = ft.FloatingActionButton(
        content=ft.Container(
            width=60,   # 👉 버튼 안 영역 키움
            height=60,
            alignment=ft.Alignment(0, 0),
            content=ft.Image(
                src="bowlradius_red.png",
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
    pagelet.bottom_appbar = Red_custom_bottom_appbar(
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

    # ✅ 추천사료 한 칸(이미지 1개)을 만드는 전용 박스
    # ✅ 화살표를 눌렀을 때 바뀌는 최종 대상은 이 박스들 안에 들어가는 이미지들임
    # ✅ image_src 값이 current_recommend_index에 따라 달라지면서 화면 이미지가 바뀜
    def recommend_menu_box(image_src):
        return ft.Container(
            width=72,   # ✅ 수정: 추천사료 전용 박스 크기를 줄여서 모바일 폭에서도 안 넘치게 함
            height=72,  # ✅ 수정: 95 -> 72로 줄여서 좌우 화살표까지 함께 들어가게 함
            padding=0,
            margin=0,
            content=ft.Image(
                src=image_src,
                fit=ft.BoxFit.CONTAIN,  # ✅ 수정: COVER 대신 CONTAIN으로 해서 이미지가 잘리지 않게 함
            ),
        )

    # ✅ 현재 페이지(index)에 해당하는 추천사료 3개를 한 줄로 만드는 함수
    # ✅ build_recommend_menu(0)이면 recommended_pages의 0번 묶음 이미지를 보여줌
    # ✅ build_recommend_menu(1)이면 다음 묶음 이미지 3개로 갈아끼워진 Row를 새로 만들어줌
    # ✅ 즉, 화살표 클릭 시 recommend_content.content 안에 다시 넣어지는 핵심 UI 생성 함수
    def build_recommend_menu(index):
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=6,  # ✅ 수정: 추천사료 사이 간격을 14 -> 6으로 줄여서 모바일에서 덜 밀리게 함
            controls=[
                recommend_menu_box(image_src) for image_src in recommended_pages[index]  # ✅ 수정: 추천사료는 전용 작은 박스 사용
            ],
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
            bgcolor=ft.Colors.RED,
            border_radius=10,
            alignment=ft.Alignment(0, 0),  # ✅ 여기 수정
            content=ft.Text(
                text,
                size=18,
                weight=ft.FontWeight.W_700,
                color=ft.Colors.WHITE,
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

    # ✅ 추천사료 페이지 데이터
    # ✅ 바깥 리스트 = 페이지 묶음
    # ✅ 안쪽 리스트 = 한 페이지에서 보여줄 이미지 3개
    # ✅ 예: current_recommend_index가 0이면 첫 번째 3개, 1이면 두 번째 3개가 선택됨
    recommended_pages = [
        ["raw.png", "raw.png", "raw.png"],      # ✅ 첫 번째 3개
        ["시저.png", "시저.png", "시저.png"],   # ✅ 두 번째 3개
        ["시저2.png", "시저2.png", "시저2.png"],  # ✅ 세 번째 3개
    ]

    # ✅ 현재 몇 번째 추천사료 페이지를 보여주는지 저장하는 상태값
    # ✅ 왼쪽/오른쪽 화살표를 누를 때 이 값이 줄거나 늘어남
    # ✅ 이 값이 바뀌어야 어떤 이미지 묶음을 보여줄지 결정할 수 있음
    current_recommend_index = 0

    # ✅ 추천사료 표시 영역 자체
    # ✅ 처음에는 current_recommend_index = 0 이므로 첫 번째 추천사료 묶음이 들어감
    # ✅ 화살표 클릭 후에는 이 Container의 content를 새 Row로 교체해서 화면을 바꿈
    recommend_content = ft.Container(
        content=build_recommend_menu(current_recommend_index)
    )

    # ✅ 왼쪽 화살표 클릭 함수
    # ✅ 현재 페이지가 0보다 크면 한 칸 이전 페이지로 이동
    # ✅ current_recommend_index를 1 감소시킨 뒤
    # ✅ recommend_content.content를 새 추천사료 Row로 교체
    # ✅ 마지막으로 page.update()로 실제 화면에 변경사항 반영
    def show_prev_recommend(e):
        nonlocal current_recommend_index
        if current_recommend_index > 0:
            current_recommend_index -= 1
            recommend_content.content = build_recommend_menu(current_recommend_index)
            page.update()

    # ✅ 오른쪽 화살표 클릭 함수
    # ✅ 현재 페이지가 마지막 페이지보다 앞에 있으면 한 칸 다음 페이지로 이동
    # ✅ current_recommend_index를 1 증가시킨 뒤
    # ✅ recommend_content.content를 새 추천사료 Row로 교체
    # ✅ 마지막으로 page.update()로 실제 화면에 변경사항 반영
    def show_next_recommend(e):
        nonlocal current_recommend_index
        if current_recommend_index < len(recommended_pages) - 1:
            current_recommend_index += 1
            recommend_content.content = build_recommend_menu(current_recommend_index)
            page.update()

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
        content=ft.SafeArea(
            expand=True,
            content=ft.Column(
                expand=True,
                spacing=0,
                controls=[
                    red_custom_appbar("개밥개밥푸드"),
                    ft.Container(
                        expand=True,
                        padding=20,
                        content=ft.Column(
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                ft.Text(
                                    "츄츄에게 딱 맞춘 하루 권장량",
                                    weight=ft.FontWeight.W_500,
                                    color=ft.Colors.BLACK,
                                ),
                                ft.Container(
                                    height=100,
                                    bgcolor=ft.Colors.WHITE,
                                    alignment=ft.Alignment(0, 0),  # 👈 중앙 정렬
                                    content=invisible_middle_box("bowl_red.png"),
                                ),
                                super_long_box([
                                    record_card(
                                        "3/19",
                                        "급여중인 사료 잔여량",
                                        ["잔여량: 800g", "예상 소진일: 3월 28일"]
                                    )
                                ]),
                                ft.Text(
                                    "추천사료",
                                    weight=ft.FontWeight.W_500,
                                    color=ft.Colors.BLACK,
                                ),
                                ft.Container(
                                    width=350,  # ✅ 수정: 추천사료 전체 영역 폭을 한 번 감싸서 좌우 정렬이 쏠리지 않게 함
                                    alignment=ft.Alignment(0, 0),
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=0,  # ✅ 수정: 화살표/가운데 영역 사이 불필요한 간격 제거
                                        controls=[
                                            ft.Container(
                                                width=36,  # ✅ 수정: 왼쪽 화살표 자리를 고정폭으로 확보해서 위치가 흔들리지 않게 함
                                                alignment=ft.Alignment(0, 0),
                                                content=ft.IconButton(
                                                    icon=ft.Icons.CHEVRON_LEFT,
                                                    icon_color=ft.Colors.RED,
                                                    on_click=show_prev_recommend,  # ✅ 왼쪽 화살표를 누르면 이전 추천사료 페이지로 이동
                                                ),
                                            ),
                                            ft.Container(
                                                expand=True,  # ✅ 수정: 기존 width=300 제거, 남는 공간을 유동적으로 써서 모바일에서도 안 잘리게 함
                                                alignment=ft.Alignment(0, 0),
                                                content=recommend_content,  # ✅ 실제로 추천사료 이미지들이 들어가 있는 중앙 표시 영역
                                            ),
                                            ft.Container(
                                                width=36,  # ✅ 수정: 오른쪽 화살표 자리도 따로 확보해서 모바일 폭에서도 사라지지 않게 함
                                                alignment=ft.Alignment(0, 0),
                                                content=ft.IconButton(
                                                    icon=ft.Icons.CHEVRON_RIGHT,
                                                    icon_color=ft.Colors.RED,
                                                    on_click=show_next_recommend,  # ✅ 오른쪽 화살표를 누르면 다음 추천사료 페이지로 이동
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                ft.Divider(),
                                ft.Text(
                                    "전체 상품",
                                    weight=ft.FontWeight.W_500,
                                    color=ft.Colors.BLACK,
                                ),
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