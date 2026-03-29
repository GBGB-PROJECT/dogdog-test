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


def white_notification_box(
    left_text="알림",
    right_text="오른쪽 내용",
    date_text="2026.03.24",
    bgcolor=ft.Colors.WHITE,
    left_text_color=ft.Colors.BLACK,
    right_text_color=ft.Colors.BLACK,
    date_text_color=ft.Colors.GREY_600,
    on_click=None,
):
    return ft.Container(
        width=350,
        height=70,
        bgcolor=bgcolor,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=16,
        padding=ft.Padding.symmetric(horizontal=16, vertical=12),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # ✅ 왼쪽 텍스트
                ft.Container(
                    expand=1,
                    alignment=ft.Alignment(-1, 0),
                    content=ft.Text(
                        left_text,
                        size=15,
                        weight=ft.FontWeight.W_600,
                        color=left_text_color,
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
                ),

                # ✅ 오른쪽 텍스트 + 날짜
                ft.Container(
                    expand=1,
                    alignment=ft.Alignment(1, 0),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=6,
                        controls=[
                            ft.Text(
                                right_text,
                                size=14,
                                color=right_text_color,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                text_align=ft.TextAlign.RIGHT,
                            ),
                            ft.Text(
                                date_text,
                                size=12,
                                color=date_text_color,
                                text_align=ft.TextAlign.RIGHT,
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )


def change_tab(index):
    print("선택된 탭:", index)


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.TRANSPARENT
    page.appbar = None

    # ☑️ 추가: 알림 데이터를 리스트로 따로 모아둠
    # ☑️ 기능: white_notification_box를 직접 6번 쓰지 않고, 데이터만 바꿔서 반복 생성 가능
    notifications = [
        {"left_text": "물주기", "right_text": "츄츄, 물 줄 시간입니다", "date_text": "2026.03.24"},
        {"left_text": "물주기", "right_text": "츄츄, 물 줄 시간입니다", "date_text": "2026.03.23"},
        {"left_text": "물주기", "right_text": "츄츄, 물 줄 시간입니다", "date_text": "2026.03.22"},
        {"left_text": "물주기", "right_text": "츄츄, 물 줄 시간입니다", "date_text": "2026.03.21"},
        {"left_text": "물주기", "right_text": "츄츄, 물 줄 시간입니다", "date_text": "2026.03.20"},
        {"left_text": "물주기", "right_text": "츄츄, 물 줄 시간입니다", "date_text": "2026.03.19"},
        {"left_text": "물주기", "right_text": "츄츄, 물 줄 시간입니다", "date_text": "2026.03.18"},
        {"left_text": "물주기", "right_text": "츄츄, 물 줄 시간입니다", "date_text": "2026.03.17"},
        {"left_text": "물주기", "right_text": "츄츄, 물 줄 시간입니다", "date_text": "2026.03.16"},
    ]

    # ☑️ 추가: 처음에는 3개만 보여주도록 개수 저장
    # ☑️ 기능: 첫 화면에서는 최근 알림만 보이게 함
    visible_count = 3

    # ☑️ 추가: 알림 박스들이 들어갈 전용 Column
    # ☑️ 기능: refresh_notifications()가 이 안을 다시 채워 넣음
    notification_list = ft.Column(
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # ☑️ 추가: 더보기 버튼 생성
    # ☑️ 기능: 누를 때마다 숨겨진 알림을 더 보여줌
    more_button = ft.TextButton(
        "더보기",
        style=ft.ButtonStyle(
            color=ft.Colors.BLACK,
        ),
    )

    # ☑️ 추가: 현재 visible_count 개수만큼 알림 박스를 다시 그림
    # ☑️ 기능: 처음 화면 생성 / 더보기 클릭 후 화면 갱신
    def refresh_notifications():
        notification_list.controls.clear()

        for item in notifications[:visible_count]:
            notification_list.controls.append(
                white_notification_box(
                    left_text=item["left_text"],
                    right_text=item["right_text"],
                    date_text=item["date_text"],
                )
            )

        # ☑️ 추가: 더 보여줄 알림이 없으면 더보기 버튼 숨김
        # ☑️ 기능: 마지막까지 다 펼쳐졌을 때 버튼 자동 제거
        more_button.visible = visible_count < len(notifications)

        page.update()

    # ☑️ 추가: 더보기 클릭 이벤트
    # ☑️ 기능: 한 번 누를 때마다 알림 3개씩 추가로 보여줌
    def show_more(e):
        nonlocal visible_count

        visible_count += 3

        if visible_count > len(notifications):
            visible_count = len(notifications)

        refresh_notifications()

    # ☑️ 추가: 버튼과 함수 연결
    # ☑️ 기능: 더보기 버튼 클릭 시 show_more 실행
    more_button.on_click = show_more

    # ✅ 기존: Pagelet 생성
    pagelet = ft.Pagelet(
        expand=True,
        content=ft.Container(),
        bgcolor=ft.Colors.YELLOW,
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

    # ✅ 기존: FAB 위치를 하단 중앙에 도킹
    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    # ✅ 기존: 하단바 연결
    pagelet.bottom_appbar = custom_bottom_appbar(
        selected_index=0,
        on_tab_change=change_tab,
    )

    # ✅ 기존 본문 유지
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
                    custom_appbar("알림"),
                    ft.Divider(),

                    ft.Container(height=10),

                    # ☑️ 변경: 예전의 white_notification_box 6개 하드코딩 대신
                    # ☑️ 기능: notification_list가 현재 보여줄 알림들만 출력
                    notification_list,

                    ft.Container(height=8),

                    # ☑️ 추가: 더보기 버튼 배치
                    # ☑️ 기능: 알림 리스트 아래에서 추가 알림 펼치기
                    more_button,
                ],
            ),
        ),
    )

    # ☑️ 추가: 첫 화면 진입 시 알림 3개 먼저 그려줌
    # ☑️ 기능: 앱 시작하자마자 notification_list에 실제 박스들이 들어감
    refresh_notifications()

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