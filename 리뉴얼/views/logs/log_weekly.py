import flet as ft

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
        padding=ft.padding.symmetric(horizontal=16),
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
        # 👇 손가락 1: 버튼 자체 크기 키움
        width=72,
        height=40,
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        bgcolor=ft.Colors.YELLOW_600,
        border_radius=10,
        content=ft.Text(
            text,
            size=13,
            weight=ft.FontWeight.W_600,
            color=ft.Colors.BLACK,
        ),
    )


def mid_box2(text):
    return ft.Container(
        # 👇 손가락 2: 버튼 자체 크기 키움
        width=72,
        height=40,
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        bgcolor=ft.Colors.GREY_100,
        border_radius=10,
        content=ft.Text(
            text,
            size=13,
            weight=ft.FontWeight.W_600,
            color=ft.Colors.BLACK,
        ),
    )


def log_weekly_view(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.WHITE

    selected_top_tab = {"index": 0}

    # 👇 손가락 1: 선택된 white_long_box3 하나를 기억하는 상태 추가
    selected_item = {"key": None}

    top_tabs_area = ft.Container(width=350)
    tab_content = ft.Container(
        width=350,
        expand=True,
    )

    # 👇 손가락 2: 현재 화면에 그려진 박스들을 기억
    item_controls = {}

    # 👇 손가락 3: 박스 클릭 시 전체를 다시 그리지 말고 색만 바꿈
    def select_item(item_key):
        selected_item["key"] = item_key

        for key, control in item_controls.items():
            control.bgcolor = (
                ft.Colors.GREY_200 if key == selected_item["key"] else ft.Colors.WHITE
            )

        tab_content.update()

    # 👇 손가락 4: 선택 가능한 박스를 만드는 공통 함수 추가
    def selectable_box(item_key, text, time_text):
        box = white_long_box3(
            text,
            time_text,
            bgcolor=ft.Colors.GREY_200 if selected_item["key"] == item_key else ft.Colors.WHITE,
            on_click=lambda e, key=item_key: select_item(key),
        )
        item_controls[item_key] = box
        return box

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

    def change_top_tab(index):
        selected_top_tab["index"] = index

        # 👇 손가락 5: 탭 바뀔 때만 목록 새로 만들기 전에 refs 초기화
        item_controls.clear()
        selected_item["key"] = None

        if index == 0:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    selectable_box("all_1", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_2", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_3", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_4", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_5", "사료 35g를 먹었습니다", "오전 07:30"),
                    selectable_box("all_6", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_7", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_8", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_9", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_10", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_11", "물 10ml를 마셨습니다", "오전 07:30"),
                    selectable_box("all_12", "물 10ml를 마셨습니다", "오전 07:30"),
                ],
            )

        elif index == 1:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    selectable_box("feed_1", "아침 급여량", "오전 07:30"),
                    selectable_box("feed_2", "저녁 급여량", "오전 07:30"),
                    selectable_box("feed_3", "점심 급여량", "오후 12:30"),
                    selectable_box("feed_4", "간식 급여량", "오후 03:00"),
                    selectable_box("feed_5", "야식 급여량", "오후 09:00"),
                ],
            )

        elif index == 2:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    selectable_box("water_1", "오늘 음수량", "오전 07:30"),
                    selectable_box("water_2", "물 리필 기록", "오전 09:30"),
                    selectable_box("water_3", "추가 음수", "오후 01:10"),
                    selectable_box("water_4", "저녁 물 보충", "오후 07:20"),
                ],
            )

        elif index == 3:
            tab_content.content = ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=12,
                controls=[
                    selectable_box("activity_1", "산책 기록", "오전 07:30"),
                    selectable_box("activity_2", "놀이 기록", "오후 02:00"),
                    selectable_box("activity_3", "저녁 산책", "오후 06:20"),
                    selectable_box("activity_4", "공놀이", "오후 08:10"),
                ],
            )

        top_tabs_area.content = build_top_tabs()
        page.update()

    top_tabs_area.content = build_top_tabs()
    change_top_tab(0)

    return ft.Container(
        expand=True,
        alignment=ft.Alignment(0, -1),
        padding=ft.padding.only(top=20, left=20, right=20, bottom=0),
        content=ft.Column(
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # 👇 맨 위: 날짜 + 더하기
                ft.Container(
                    width=350,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "2026.04.06~04.13",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.ADD,
                                icon_size=26,
                                icon_color=ft.Colors.BLACK,
                            ),
                        ],
                    ),
                ),

                ft.Container(height=12),

                # 👇 그 아래: 상단 탭
                top_tabs_area,

                # 👇 그 아래: 회색 선
                ft.Container(
                    width=350,
                    content=ft.Divider(
                        thickness=1,
                        color=ft.Colors.GREY_300,
                    ),
                ),

                ft.Container(height=30),

                # 👇 그 아래: 탭 내용
                tab_content,

                # 👇 맨 아래: 버튼 영역
                ft.Container(
                    # 👇 손가락 3: 버튼 영역 자체를 넓히고
                    width=350,

                    # 👇 손가락 4: FAB 위로 띄우기 위해 아래 마진 추가
                    margin=ft.margin.only(bottom=30),

                    # 👇 손가락 5: 내부 여백 키워서 답답함 줄임
                    padding=ft.padding.only(top=8, bottom=8),

                    bgcolor=ft.Colors.WHITE,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=12,
                        controls=[
                            mid_box("수정"),
                            mid_box("삭제"),
                            mid_box2("저장"),
                        ],
                    ),
                ),
            ],
        ),
    )