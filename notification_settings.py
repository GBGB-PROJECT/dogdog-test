import flet as ft


def custom_appbar(title="중앙 텍스트"):
    right_icons = ft.Row(
        spacing=8,
        controls=[
            ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.BLACK),
        ],
    )

    return ft.Container(
        height=60,  # 🟩 상단 앱바 높이
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(width=56),  # 🟩 왼쪽 빈자리
                ft.Text(
                    title,
                    size=20,  # 🟩 앱바 제목 글자 크기
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
        height=70,  # 🟩 하단 탭 높이
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
                    size=24,  # 🟩 하단 아이콘 크기
                ),
                ft.Text(
                    label,
                    color=ft.Colors.BLACK,
                    size=12,  # 🟩 하단 글자 크기
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


def switch_info_box(
    title,
    subtitle,
    is_on=True,
    width=None,
    height=70,
):
    # ✅ 이 함수는 "한 줄짜리 스위치 설정 박스"를 만드는 함수
    # ✅ 아래 build_page_content()에서 마지막 설정 카드로 재사용됨
    return ft.Container(
        width=width,  # ✅ 바깥에서 card_width를 넘겨받아 카드 너비에 맞춤
        height=height,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_300),  # ✅ 카드 테두리
        border_radius=10,
        padding=ft.padding.symmetric(horizontal=14, vertical=10),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # ✅ 왼쪽 텍스트 / 오른쪽 스위치를 양끝 배치
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    expand=True,  # ✅ 남는 공간을 왼쪽 텍스트 영역이 차지
                    spacing=2,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Text(
                            title,  # ✅ 설정 제목 표시
                            size=15,
                            weight=ft.FontWeight.W_600,
                            color=ft.Colors.BLACK,
                            max_lines=1,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                        ft.Text(
                            subtitle,  # ✅ 설정 설명 표시
                            size=11,
                            color=ft.Colors.GREY_600,
                        ),
                    ],
                ),
                ft.Container(
                    width=54,  # ✅ 스위치 영역 너비를 고정해서 정렬이 흔들리지 않게 함
                    alignment=ft.Alignment(0, 0),
                    content=ft.Switch(
                        value=is_on,  # ✅ 현재 스위치 ON/OFF 기본값
                        scale=0.78,
                        active_track_color=ft.Colors.YELLOW,
                        active_color=ft.Colors.WHITE,
                        inactive_thumb_color=ft.Colors.WHITE,
                    ),
                ),
            ],
        ),
    )


def change_tab(index):
    print("선택된 탭:", index)


def build_time_options():
    # ✅ 이 함수는 "시간 드롭다운 안에 들어갈 선택지 목록"만 따로 만들어주는 함수
    # ✅ reminder_box() 안의 time Dropdown에서 options=build_time_options()로 사용됨
    return [
        ft.dropdown.Option("06:00 AM"),
        ft.dropdown.Option("07:00 AM"),
        ft.dropdown.Option("08:00 AM"),
        ft.dropdown.Option("09:00 AM"),
        ft.dropdown.Option("10:00 AM"),
        ft.dropdown.Option("11:00 AM"),
        ft.dropdown.Option("12:00 PM"),
        ft.dropdown.Option("01:00 PM"),
        ft.dropdown.Option("02:00 PM"),
        ft.dropdown.Option("03:00 PM"),
        ft.dropdown.Option("04:00 PM"),
        ft.dropdown.Option("05:00 PM"),
        ft.dropdown.Option("06:00 PM"),
        ft.dropdown.Option("07:00 PM"),
        ft.dropdown.Option("08:00 PM"),
    ]


def build_interval_options():
    # ✅ 이 함수는 "알림 간격 드롭다운에 들어갈 선택지 목록"을 따로 만드는 함수
    # ✅ reminder_box() 안의 interval Dropdown에서 options=build_interval_options()로 사용됨
    return [
        ft.dropdown.Option("4시간"),
        ft.dropdown.Option("8시간"),
        ft.dropdown.Option("12시간"),
    ]


def reminder_box(title, subtitle, default_time, default_interval, is_on=True):
    # ✅ 이 함수는 "시간 드롭다운 + 간격 드롭다운 + 스위치"가 들어간 알림 한 줄을 만드는 함수
    # ✅ build_page_content() 안에서 밥주기 / 물주기 / 약먹이기 줄을 만들 때 여러 번 호출됨
    return ft.Container(
        height=78,  # 🟩 알림 한 줄 박스 높이
        padding=ft.padding.symmetric(horizontal=12, vertical=10),  # 🟩 박스 안쪽 여백
        border_radius=10,  # 🟩 모서리 둥글기
        bgcolor=ft.Colors.WHITE,  # 🟩 각 줄 박스 배경색
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # =========================
                # 왼쪽 설명 영역
                # =========================
                ft.Container(
                    expand=4,  # ✅ 전체 가로폭 중 왼쪽 설명영역 비율
                    content=ft.Column(
                        spacing=2,  # 🟩 제목/설명 사이 간격
                        tight=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                title,  # ✅ "밥주기", "물주기" 같은 항목 이름 표시
                                size=15,  # 🟩 왼쪽 제목 글자 크기
                                weight=ft.FontWeight.W_600,
                                color=ft.Colors.BLACK,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Text(
                                subtitle,  # ✅ "12시간 알림 간격" 같은 설명 표시
                                size=10,  # 🟩 왼쪽 설명 글자 크기
                                color=ft.Colors.GREY_600,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                        ],
                    ),
                ),

                ft.Container(width=8),

                ft.Container(
                    expand=6,  # ✅ 오른쪽 컨트롤(시간/간격/스위치) 영역 비율
                    content=ft.Row(
                        spacing=6,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.Container(
                                expand=4,
                                content=ft.Dropdown(
                                    value=default_time,  # ✅ 이 줄이 각 항목의 "기본 시작 시간"을 정함
                                    options=build_time_options(),  # ✅ 시간 선택지는 build_time_options()가 공급
                                    dense=True,
                                    filled=False,
                                    bgcolor=ft.Colors.WHITE,
                                    text_size=13,
                                    height=42,
                                    border_color=ft.Colors.GREY_300,
                                    content_padding=ft.padding.symmetric(horizontal=10, vertical=8),
                                ),
                            ),
                            ft.Container(
                                expand=3,
                                content=ft.Dropdown(
                                    value=default_interval,  # ✅ 이 줄이 각 항목의 "기본 알림 간격"을 정함
                                    options=build_interval_options(),  # ✅ 간격 선택지는 build_interval_options()가 공급
                                    dense=True,
                                    filled=False,
                                    bgcolor=ft.Colors.WHITE,
                                    text_size=13,
                                    height=42,
                                    border_color=ft.Colors.GREY_300,
                                    content_padding=ft.padding.symmetric(horizontal=10, vertical=8),
                                ),
                            ),
                            ft.Container(
                                width=54,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Switch(
                                    value=is_on,  # ✅ 각 알림 항목의 ON/OFF 기본 상태
                                    scale=0.78,
                                    active_track_color=ft.Colors.YELLOW,
                                    active_color=ft.Colors.WHITE,
                                    inactive_thumb_color=ft.Colors.WHITE,
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )


def subscribe_reminder_box(title, subtitle, is_on=True):
    # ✅ reminder_box()와 다르게 드롭다운은 없고, 텍스트 + 스위치만 있음
    return ft.Container(
        height=78,  # 🟩 알림 한 줄 박스 높이
        padding=ft.Padding.symmetric(horizontal=12, vertical=10),  # 🟩 박스 안쪽 여백
        border_radius=10,  # 🟩 모서리 둥글기
        bgcolor=ft.Colors.WHITE,  # 🟩 각 줄 박스 배경색
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # =========================
                # 왼쪽 설명 영역
                # =========================
                ft.Container(
                    expand=True,  # ✅ 텍스트 영역이 가능한 만큼 넓게 사용
                    content=ft.Column(
                        spacing=2,
                        tight=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                title,  # ✅ "3일 전", "7일 전" 같은 제목
                                size=15,
                                weight=ft.FontWeight.W_600,
                                color=ft.Colors.BLACK,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Text(
                                subtitle,  # ✅ 구독 배송 관련 설명 문구
                                size=10,
                                color=ft.Colors.GREY_600,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                        ],
                    ),
                ),

                # =========================
                # 오른쪽 스위치 영역
                # =========================
                ft.Container(
                    width=54,  # ✅ 오른쪽 스위치 자리 고정
                    alignment=ft.Alignment(0, 0),
                    content=ft.Switch(
                        value=is_on,  # ✅ 구독 알림의 기본 ON/OFF 상태
                        scale=0.78,
                        active_track_color=ft.Colors.YELLOW,
                        active_color=ft.Colors.WHITE,
                        inactive_thumb_color=ft.Colors.WHITE,
                    ),
                ),
            ],
        ),
    )


def build_page_content(page: ft.Page, pagelet: ft.Pagelet):
    # ✅ 이 함수는 "이 화면 전체 본문 UI를 실제로 조립하는 핵심 함수"
    # ✅ 처음 화면이 열릴 때도 호출되고, handle_resize()에서도 다시 호출됨
    screen_width = page.width if page.width else 393
    # ✅ 현재 화면 너비를 읽음. 없으면 기본값 393 사용

    card_width = min(420, max(320, screen_width - 24))
    # ✅ 카드 너비를 화면 크기에 맞춰 자동 계산
    # ✅ 너무 작아지면 320, 너무 커지면 420으로 제한

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
        # ✅ pagelet 안에 들어갈 실제 화면 내용을 여기서 통째로 다시 만들어 넣음

        content=ft.SafeArea(
            expand=True,
            # ✅ 노치, 상태바 같은 영역을 피해서 안전하게 내용 표시

            content=ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,  # ✅ 내용이 길어지면 자동 스크롤 가능
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=16,
                controls=[
                    custom_appbar("알림 설정"),
                    ft.Divider(height=1, color=ft.Colors.GREY_300),

                    # ✅ 첫 번째 카드
                    ft.Container(
                        width=card_width,  # ✅ 위에서 계산한 반응형 카드 너비 적용
                        padding=16,
                        bgcolor=ft.Colors.WHITE,
                        border=ft.border.all(1, "#D0D0D0"),
                        border_radius=14,
                        content=ft.Column(
                            spacing=14,
                            controls=[
                                ft.Column(
                                    spacing=4,
                                    controls=[
                                        ft.Text(
                                            "알림 간격",
                                            size=17,
                                            weight=ft.FontWeight.W_700,
                                            color=ft.Colors.BLACK,
                                        ),
                                        ft.Text(
                                            "첫 알림 시작 시간에서 일정 시간이 지나면 알림을 보내드려요.",
                                            size=11,
                                            color=ft.Colors.GREY_700,
                                        ),
                                    ],
                                ),
                                reminder_box("밥주기", "12시간 알림 간격", "08:00 AM", "12시간", True),
                                reminder_box("물주기", "4시간 알림 간격", "08:00 AM", "4시간", True),
                                reminder_box("약먹이기", "12시간 알림 간격", "08:00 AM", "12시간", False),
                                
                            ],
                        ),
                    ),

                    # ✅ 두 번째 카드
                    ft.Container(
                        width=card_width,  
                        padding=16,
                        bgcolor=ft.Colors.WHITE,
                        border=ft.border.all(1, "#D0D0D0"),
                        border_radius=14,
                        content=ft.Column(
                            spacing=14,
                            controls=[
                                ft.Column(
                                    spacing=4,
                                    controls=[
                                        ft.Text(
                                            "구독 알림 설정",
                                            size=17,
                                            weight=ft.FontWeight.W_700,
                                            color=ft.Colors.BLACK,
                                        ),
                                    ],
                                ),
                                subscribe_reminder_box("3일 전", "구독 배송 3일 전 안내", True),
                                subscribe_reminder_box("7일 전", "구독 배송 7일 전 안내", True),
                                
                            ],
                        ),
                    ),

                    switch_info_box(
                        "사료 소진일 알림 설정",
                        "제품이 소진되기 3일, 7일 전 마라 알림을 받을 수 있어요.",
                        width=card_width,
                    ),
                    
                ],
            ),
        ),
    )

    page.update()
    # ✅ 위에서 다시 만든 화면 내용을 실제 페이지에 반영


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = ft.Colors.TRANSPARENT
    page.appbar = None

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

    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    pagelet.bottom_appbar = custom_bottom_appbar(
        selected_index=0,
        on_tab_change=change_tab,
    )

    build_page_content(page, pagelet)
    # ✅ 앱 시작 직후 처음 화면 내용을 만들어서 pagelet 안에 넣음

    def handle_resize(e):
        # ✅ 이 함수는 창 크기가 바뀔 때마다 다시 화면을 그리는 역할
        # ✅ 즉, 가로/세로 크기가 달라져도 card_width가 다시 계산되게 해줌
        build_page_content(page, pagelet)
        # ✅ resize가 발생하면 build_page_content()를 다시 호출해서 반응형 재배치

    page.on_resized = handle_resize
    # ✅ 창 크기 변경 이벤트가 생기면 handle_resize 함수가 실행되도록 연결

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