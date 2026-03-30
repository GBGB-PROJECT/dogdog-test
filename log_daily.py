import flet as ft


def custom_appbar(title="중앙 텍스트"):
    right_icons = ft.Row(
        spacing=8,
        controls=[
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
                ft.Container(width=56),
                ft.Text(
                    title,
                    size=20,
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.BLACK,
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
                ft.Icon(icon, color=ft.Colors.BLACK, size=24),
                ft.Text(
                    label,
                    color=ft.Colors.BLACK,
                    size=12,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        ),
    )


def custom_bottom_appbar(selected_index=0, on_tab_change=None):
    items = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.EDIT_NOTE, "Log"),
        (ft.Icons.MENU_BOOK, "Contents"),
        (ft.Icons.PERSON, "MyPage"),
    ]

    return ft.BottomAppBar(
        bgcolor=ft.Colors.YELLOW,
        shape=ft.CircularRectangleNotchShape(),
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


def banner(
    text="",
    image_src=None,
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    arrow_bgcolor=ft.Colors.WHITE,
    on_click=None,
):
    left_controls = []

    if image_src:
        left_controls.append(
            ft.Container(
                width=50,
                height=50,
                border_radius=25,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=ft.Image(
                    src=image_src,
                    width=50,
                    height=50,
                    fit=ft.BoxFit.COVER,
                ),
            )
        )

    left_controls.append(
        ft.Text(
            text,
            size=18,
            weight=ft.FontWeight.W_600,
            color=text_color,
        )
    )

    # ✅ 배너가 흰색이면 화살표 배경은 노란색, 아니면 흰색
    arrow_bg = "#F4D52A" if bgcolor == ft.Colors.WHITE else ft.Colors.WHITE

    return ft.Container(
        width=350,
        height=72,
        bgcolor=bgcolor,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=16,
        padding=ft.Padding(left=14, top=0, right=14, bottom=0),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=left_controls,
                ),
                ft.Container(
                    width=40,
                    height=40,
                    bgcolor=arrow_bg,
                    border_radius=20,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Icon(
                        ft.Icons.ARROW_FORWARD,
                        color=ft.Colors.BLACK,
                    ),
                ),
            ],
        ),
    )


def white_long_box2(
    text,
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    right_icon=ft.Icons.ADD,
    on_click=None
):
    return ft.Container(
        width=350,
        height=70,
        bgcolor=bgcolor,
        border=None,
        border_radius=16,
        padding=ft.Padding.symmetric(horizontal=16),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    text,
                    size=14,
                    weight=ft.FontWeight.W_500,
                    color=text_color,
                ),
                ft.Icon(
                    right_icon,
                    color=text_color,
                    size=22,
                ),
            ],
        ),
    )


def white_long_box3(
    text,
    time_text="오전 07:30",
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    time_color=ft.Colors.BLACK,
    on_click=None,
):
    return ft.Container(
        width=350,
        height=70,
        bgcolor=bgcolor,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=16,
        padding=ft.Padding.symmetric(horizontal=16),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    text,
                    size=14,
                    weight=ft.FontWeight.W_500,
                    color=text_color,
                ),
                ft.Text(
                    time_text,
                    size=14,
                    weight=ft.FontWeight.W_600,
                    color=time_color,
                ),
            ],
        ),
    )

def mid_box(text):
    return ft.Container(
        padding=ft.Padding.symmetric(horizontal=12, vertical=6),  # 👉 더 큼
        bgcolor=ft.Colors.YELLOW_600,  
        border_radius=8,
        content=ft.Text(
            text,
            size=12,  # 👉 글자도 조금 키움
            weight=ft.FontWeight.W_500,
            color=ft.Colors.BLACK,
        ),
    )

def mid_box2(text):
    return ft.Container(
        padding=ft.Padding.symmetric(horizontal=12, vertical=6),  # 👉 더 큼
        bgcolor=ft.Colors.GREY_100,  
        border_radius=8,
        content=ft.Text(
            text,
            size=12,  # 👉 글자도 조금 키움
            weight=ft.FontWeight.W_500,
            color=ft.Colors.BLACK,
        ),
    )



def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.WHITE
    page.appbar = None

    def change_tab(index):
        print("선택된 하단 탭:", index)

    # ✅ 상단 탭 상태 저장용
    selected_top_tab = {"index": 0}

    # ✅ [스크롤 수정 1]
    # tab_content가 남은 세로 공간을 먹도록 expand=True 추가
    # 그래야 내부 Column의 scroll이 정상 동작함
    tab_content = ft.Container(
        width=350,
        expand=True,
    )

    # ✅ 상단 탭 UI 만드는 함수
    def build_top_tabs():
        labels = ["전체", "급여량", "음수량", "활동량"]
        tab_controls = []

        for i, label in enumerate(labels):
            is_selected = selected_top_tab["index"] == i

            tab_controls.append(
                ft.Container(
                    expand=True,
                    height=50,
                    on_click=lambda e, idx=i: change_top_tab(idx),
                    content=ft.Column(
                        spacing=6,
                        alignment=ft.MainAxisAlignment.END,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                label,
                                size=16,
                                color=ft.Colors.BLACK if is_selected else ft.Colors.GREY,
                                weight=ft.FontWeight.W_700 if is_selected else ft.FontWeight.W_500,
                            ),
                            ft.Container(
                                height=3,
                                width=60,
                                bgcolor=ft.Colors.BLACK if is_selected else ft.Colors.TRANSPARENT,
                                border_radius=10,
                            ),
                        ],
                    ),
                )
            )

        return ft.Container(
            width=350,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=tab_controls,
            ),
        )

    # ✅ 상단 탭이 실제로 들어갈 자리
    top_tabs_area = ft.Container()

    # ✅ 탭 눌렀을 때 내용 바꾸는 함수
    def change_top_tab(index):
        selected_top_tab["index"] = index

        # ✅ [스크롤 수정 2]
        # 각 탭 내용 Column에 scroll=ft.ScrollMode.AUTO 추가
        # 그리고 expand=True도 같이 줘서 남은 공간 안에서 스크롤되게 함
        if index == 0:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    white_long_box3("물 10ml를 마셨습니다", "오전 07:30"),
                    white_long_box3("물 10ml를 마셨습니다", "오전 07:30"),
                    white_long_box3("물 10ml를 마셨습니다", "오전 07:30"),
                    white_long_box3("물 10ml를 마셨습니다", "오전 07:30"),
                    white_long_box3("사료 35g를 먹었습니다", "오전 07:30"),
                    white_long_box3("물 10ml를 마셨습니다", "오전 07:30"),
                    white_long_box3("물 10ml를 마셨습니다", "오전 07:30"),
                    white_long_box3("물 10ml를 마셨습니다", "오전 07:30"),
                    white_long_box3("물 10ml를 마셨습니다", "오전 07:30"),
                    white_long_box3("물 10ml를 마셨습니다", "오전 07:30"),
                    white_long_box3("물 10ml를 마셨습니다", "오전 07:30"),
                    white_long_box3("물 10ml를 마셨습니다", "오전 07:30", bgcolor=ft.Colors.GREY_200),
                ],
            )

        elif index == 1:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    white_long_box3("아침 급여량", "오전 07:30"),
                    white_long_box3("저녁 급여량", "오전 07:30"),
                    white_long_box3("점심 급여량", "오후 12:30"),
                    white_long_box3("간식 급여량", "오후 03:00"),
                    white_long_box3("야식 급여량", "오후 09:00"),
                ],
            )

        elif index == 2:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    white_long_box3("오늘 음수량", "오전 07:30"),
                    white_long_box3("물 리필 기록", "오전 09:30"),
                    white_long_box3("추가 음수", "오후 01:10"),
                    white_long_box3("저녁 물 보충", "오후 07:20"),
                ],
            )

        elif index == 3:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    white_long_box3("산책 기록", "오전 07:30"),
                    white_long_box3("놀이 기록", "오후 02:00"),
                    white_long_box3("저녁 산책", "오후 06:20"),
                    white_long_box3("공놀이", "오후 08:10"),
                ],
            )

        # ✅ 탭 모양도 다시 그려서 선택 상태 반영
        top_tabs_area.content = build_top_tabs()

        # ✅ 최종 화면 갱신
        page.update()

    pagelet = ft.Pagelet(
        expand=True,
        bgcolor=ft.Colors.YELLOW,
        content=ft.Container(),
    )

    pagelet.floating_action_button = ft.FloatingActionButton(
        content=ft.Container(
            width=60,
            height=60,
            alignment=ft.Alignment(0, 0),
            content=ft.Image(
                src="bowlradius.png",
                fit=ft.BoxFit.CONTAIN,
            ),
        ),
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        elevation=0,
        on_click=lambda e: print("가운데 버튼 클릭"),
    )

    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    pagelet.bottom_appbar = custom_bottom_appbar(
        selected_index=0,
        on_tab_change=change_tab,
    )

    # ✅ 처음 탭 UI 넣기
    top_tabs_area.content = build_top_tabs()

    # ✅ 처음 실행 시에도 '전체' 탭 내용이 바로 보이게 강제 실행
    change_top_tab(0)

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
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    custom_appbar("Log"),

                    # ✅ 이건 탭 바깥에 항상 고정으로 보이는 박스
                    white_long_box2("2026.03.19", right_icon=ft.Icons.ADD),

                    # ✅ 상단 탭
                    top_tabs_area,

                    # ✅ 탭 아래 회색 선
                    ft.Container(
                        width=350,
                        content=ft.Divider(
                            thickness=1,
                            color=ft.Colors.GREY_300,
                        ),
                    ),
                    ft.Container(height=30),

                    # ✅ [스크롤 수정 3]
                    # tab_content 자체가 expand=True라서
                    # 위 요소들은 고정되고, 아래 내용 영역만 남은 공간에서 스크롤됨
                    tab_content,
                    ft.Container(
                        height=50,
                        bgcolor=ft.Colors.WHITE,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                mid_box("수정"),
                                mid_box("삭제"),
                                mid_box2("저장"),
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