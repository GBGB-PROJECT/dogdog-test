import flet as ft
from components.common.common_components import arrow_back, bottom_continue_button


def build_screen(
    page: ft.Page,
    body_controls: list, # 👉 본문에 넣을 UI 리스트
    on_continue=None, # 👉 Continue 눌렀을 때 실행
    on_back=None, # 👉 뒤로가기 눌렀을 때 실행
    show_back=True, # 👉 뒤로가기 버튼 보여줄지
    fixed_bottom=True, # 👉 Continue 버튼 고정 여부
):
    # ─────────────────────────────────────────────
    # 🟨 수정 1: 화살표를 본문 top_controls에서 제거
    # 이유:
    # - 기존에는 화살표가 body_content 안에 들어가서
    #   화면마다 위치가 달라 보였음
    # - 이제는 상단 고정 app bar 에서 따로 관리
    # ─────────────────────────────────────────────
    body_content = ft.Column(
        width=350,
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            *body_controls,
            ft.Container(height=20),
        ],
    )

    # ─────────────────────────────────────────────
    # 🟨 수정 2: 투명 상단 app bar 추가
    # 이유:
    # - 화살표를 항상 같은 위치에 고정하기 위해
    # - 본문과 분리된 상단 고정 영역 필요
    # ─────────────────────────────────────────────
    top_appbar = ft.Container(
        width=float("inf"),
        height=64,
        bgcolor=ft.Colors.TRANSPARENT,
        padding=ft.padding.only(left=16, right=16, top=12, bottom=12),
        alignment=ft.Alignment(-1, 0),

        # 👉 show_back이 True면 뒤로가기 버튼 표시, 아니면 숨김
        content=arrow_back(on_click=on_back) if show_back else None, 
    )

    # ─────────────────────────────────────────────
    # 🟨 수정 3: 본문은 app bar 아래에 오도록 배치
    # 이유:
    # - 화살표는 위에 고정
    # - 본문은 그 아래에서 시작
    # ─────────────────────────────────────────────
    scroll_area = ft.Container(
        expand=True,
        padding=ft.padding.only(left=16, right=16),  # 👉 좌우 여백
        alignment=ft.Alignment(0, -1),
        content=body_content,
    )

    if fixed_bottom:
        fixed_button = ft.Container(
            width=float("inf"),
            alignment=ft.Alignment(0, 0),
            padding=ft.padding.only(left=16, right=16, top=10, bottom=20), # 👉 좌우 여백
            content=ft.Container(
                width=350,
                alignment=ft.Alignment(0, 0),
                
                # 👉 Continue 버튼 생성 + 클릭 시 on_continue 함수 실행
                content=bottom_continue_button(on_click=on_continue),
            ),
        )

        return ft.Container(
            expand=True,
            content=ft.Column(
                expand=True,
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    top_appbar,
                    scroll_area,
                    fixed_button,
                ],
            ),
        )

    return ft.Container(
        expand=True,
        content=ft.Column(
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                top_appbar,
                scroll_area,
            ],
        ),
    )