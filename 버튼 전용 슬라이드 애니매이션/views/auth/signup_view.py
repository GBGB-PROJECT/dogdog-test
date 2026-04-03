import flet as ft
from components.common.common_components import input_box
from components.layout.common_layout import build_screen_body


def build_view(page: ft.Page):
    body_controls = [
        # ─────────────────────────────────────────────
        # 🟨 기존 주석/구조 유지
        # ─────────────────────────────────────────────
        ft.Container(
            margin=ft.Margin.only(top=20),
            content=ft.Column(
                spacing=0,
                controls=[
                    # ✅ 수정:
                    # - "Welcome to 똑똑"을 한 개 Text로 두지 않고
                    #   영어 / 한글을 분리해서 각각 폰트 적용
                    ft.Row(
                        spacing=0,
                        controls=[
                            ft.Text(
                                "Welcome to ",
                                font_family="Mulish",
                                weight=ft.FontWeight.W_500,
                                color=ft.Colors.BLACK,
                                size=30,
                            ),
                            ft.Text(
                                "똑똑",
                                font_family="Pretendard",
                                weight=ft.FontWeight.W_700,
                                color=ft.Colors.BLACK,
                                size=30,
                            ),
                        ],
                    ),

                    ft.Container(height=12),

                    ft.Text(
                        "똑똑🚪✊ 우리집 강아지가 마지막 한알을 먹기 전",
                        font_family="Pretendard",
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.BLACK,
                        size=14,
                    ),
                    ft.Text(
                        "문앞에 사료가 도착합니다🔔",
                        font_family="Pretendard",
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.BLACK,
                        size=14,
                    ),

                    ft.Container(height=46),

                    ft.Text(
                        "프로필을 완성하세요.",
                        font_family="Pretendard",
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.BLACK,
                        size=28,
                    ),
                ],
            ),
        ),

        ft.Container(height=8),

        ft.Text(
            "이메일",
            font_family="Pretendard",
            weight=ft.FontWeight.W_500,
            color=ft.Colors.BLACK,
            size=14,
        ),
        input_box(label="example@gmail.com"),

        ft.Text(
            "닉네임",
            font_family="Pretendard",
            weight=ft.FontWeight.W_500,
            color=ft.Colors.BLACK,
            size=14,
        ),
        input_box(label="닉네임"),
    ]

    # ─────────────────────────────────────────────
    # 🟩 체크: build_screen(...) 제거
    # 이유:
    # - 상단/하단은 main.py 에서 고정 관리
    # - 이 파일은 본문만 반환
    # ─────────────────────────────────────────────
    return build_screen_body(body_controls)