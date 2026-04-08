import flet as ft
from components.common.ui_boxes import mid_box, mid_box2


# ✅ 로그 화면 공통 하단 액션 버튼
def build_log_action_buttons(bottom_margin=30, vertical_padding=8):
    return ft.Container(
        width=350,
        margin=ft.margin.only(bottom=bottom_margin),
        padding=ft.padding.only(top=vertical_padding, bottom=vertical_padding),
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
    )