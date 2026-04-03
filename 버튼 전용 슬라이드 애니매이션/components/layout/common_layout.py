import flet as ft


def build_screen_body(body_controls: list):
    # ─────────────────────────────────────────────
    # 🟦 체크 1: 이 파일은 이제 본문 전용 레이아웃만 담당
    # 이유:
    # - 예전 build_screen() 은 상단 화살표 / 하단 Continue 버튼까지
    #   같이 만들고 있었음
    # - 이제 상단/하단은 main.py 고정 shell 에서 관리
    #   여기서는 body 내용만 감싸줌
    # ─────────────────────────────────────────────
    return ft.Column(
        width=350,
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            *body_controls,
            ft.Container(height=20),
        ],
    )