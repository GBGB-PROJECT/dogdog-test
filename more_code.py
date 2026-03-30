import flet as ft


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
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=16,
        padding=ft.Padding.symmetric(horizontal=16, vertical=12),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
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


def main(page: ft.Page):
    page.title = "더보기 테스트"
    page.padding = 20
    page.bgcolor = ft.Colors.WHITE
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    # ☑️ 알림 데이터
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

    # ☑️ 처음에는 3개만 보이게 설정
    visible_count = 3

    # ☑️ 알림 박스들이 들어갈 영역
    notification_list = ft.Column(
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # ☑️ 더보기 버튼
    more_button = ft.TextButton(
        "더보기",
        style=ft.ButtonStyle(
            color=ft.Colors.BLACK,
        ),
    )

    # ☑️ 현재 visible_count 만큼 알림 다시 그림
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

        # ☑️ 더 보여줄 알림이 없으면 버튼 숨김
        more_button.visible = visible_count < len(notifications)

        page.update()

    # ☑️ 더보기 버튼 클릭 시 3개씩 추가
    def show_more(e):
        nonlocal visible_count

        visible_count += 3

        if visible_count > len(notifications):
            visible_count = len(notifications)

        refresh_notifications()

    more_button.on_click = show_more

    # ☑️ 화면 구성
    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
            controls=[
                notification_list,
                more_button,
            ],
        )
    )

    # ☑️ 첫 화면에 3개 먼저 표시
    refresh_notifications()


if __name__ == "__main__":
    ft.run(main)