import flet as ft
from components.common.texts import Txt
from components.common.ui_boxes import white_long_box3

# ✅ 로그 화면 공통 상단 탭 라벨
LOG_TAB_LABELS = ["전체", "급여량", "음수량", "활동량"]


# ✅ 공통 상단 탭 UI
# - selected_index: 현재 선택된 탭 index
# - on_tab_change: 탭 클릭 시 실행할 함수
def build_log_top_tabs(selected_index, on_tab_change):
    tab_controls = []

    for i, label in enumerate(LOG_TAB_LABELS):
        is_selected = selected_index == i

        tab_controls.append(
            ft.Container(
                expand=True,
                height=50,
                on_click=lambda e, idx=i: on_tab_change(idx),
                content=ft.Column(
                    spacing=6,
                    alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        Txt(
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


# ✅ 공통 선택형 로그 박스
# - 선택된 item이면 회색 배경
def build_selectable_log_box(item_key, text, time_text, selected_key, on_select):
    return white_long_box3(
        text,
        time_text,
        bgcolor=ft.Colors.GREY_200 if selected_key == item_key else ft.Colors.WHITE,
        on_click=lambda e, key=item_key: on_select(key),
    )