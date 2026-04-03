import flet as ft


# ─────────────────────────────────────────────
# 🟦 [추가]
# 하단 탭 1개 UI
# - selected 상태에 따라 색상 변경
# - 클릭 시 main.py의 render_page(index) 실행용 콜백 호출
# ─────────────────────────────────────────────
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
                    color=ft.Colors.BLACK if selected else ft.Colors.BROWN_300,
                    size=24,
                ),
                ft.Text(
                    label,
                    color=ft.Colors.BLACK if selected else ft.Colors.BROWN_300,
                    size=12,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        ),
    )


# ─────────────────────────────────────────────
# 🟦 [추가]
# FAB가 가운데 끼어드는 BottomAppBar
# - Home / Log / Contents / MyPage
# - 가운데는 개밥그릇 FAB 자리
# ─────────────────────────────────────────────
def custom_bottom_appbar(selected_index=0, on_tab_change=None):
    return ft.BottomAppBar(
        bgcolor=ft.Colors.YELLOW_600,
        shape=ft.CircularRectangleNotchShape(),
        content=ft.Container(
            height=70,
            padding=ft.padding.symmetric(horizontal=10),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    nav_item(
                        ft.Icons.HOME,
                        "Home",
                        selected=(selected_index == 0),
                        on_click=lambda e: on_tab_change(0) if on_tab_change else None,
                    ),
                    nav_item(
                        ft.Icons.CALENDAR_MONTH,
                        "Log",
                        selected=(selected_index == 1),
                        on_click=lambda e: on_tab_change(1) if on_tab_change else None,
                    ),

                    # ─────────────────────────────────────────────
                    # 🟦 [추가]
                    # 가운데 FAB 자리 확보
                    # ─────────────────────────────────────────────
                    ft.Container(width=70),

                    nav_item(
                        ft.Icons.MESSENGER_OUTLINE_ROUNDED,
                        "Contents",
                        selected=(selected_index == 2),
                        on_click=lambda e: on_tab_change(2) if on_tab_change else None,
                    ),
                    nav_item(
                        ft.Icons.PERSON_OUTLINE,
                        "MyPage",
                        selected=(selected_index == 3),
                        on_click=lambda e: on_tab_change(3) if on_tab_change else None,
                    ),
                ],
            ),
        ),
    )


# ─────────────────────────────────────────────
# 🟥 [삭제]
# 기존 CupertinoNavigationBar 반환 함수 제거
# 이유:
# - 가운데 FAB 도킹 구조와 맞지 않음
# ─────────────────────────────────────────────