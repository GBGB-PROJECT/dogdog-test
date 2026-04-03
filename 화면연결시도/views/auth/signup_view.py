import flet as ft
from components.common.common_components import input_box
from components.layout.common_layout import build_screen
from components.navigation import go_next


def build_view(page: ft.Page):
    body_controls = [
        # ─────────────────────────────────────────────
        # 🟨 수정 1: 상단 헤더 전체 시작 위치를 아래로 내림
        # 이유:
        # - 기존 top=50 은 화면 상단에 너무 붙어 보였음
        # - 시안처럼 조금 더 아래에서 시작하게 top 여백 증가
        # ─────────────────────────────────────────────
        ft.Container(
            margin=ft.margin.only(top=20),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Text(
                        "Welcome to 똑똑",
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.BLACK,
                        size=30,
                    ),

                    # 🟨 welcome 아래 설명문까지 간격
                    ft.Container(height=12),

                    ft.Text(
                        "똑똑🚪✊ 우리집 강아지가 마지막 한알을 먹기 전",
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.BLACK,
                        size=15,
                    ),
                    ft.Text(
                        "문앞에 사료가 도착합니다",
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.BLACK,
                        size=15,
                    ),

                    # 🟨 설명문과 큰 제목 사이 간격 크게
                    ft.Container(height=46),

                    # ─────────────────────────────────────────────
                    # 🟨 수정 5: 메인 제목 배치 위치만 시안에 가깝게 조정
                    # ─────────────────────────────────────────────
                    ft.Text(
                        "프로필을 완성하세요.",
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors.BLACK,
                        size=28,
                    ),
                ],
            ),
        ),

        # ─────────────────────────────────────────────
        # 🟨 수정 6: 메인 제목 아래와 입력 구역 사이 간격 추가
        # 이유:
        # - 시안은 제목 바로 아래가 아니라 살짝 숨통이 있음
        # ─────────────────────────────────────────────
        ft.Container(height=8),

        # ─────────────────────────────────────────────
        # 🟨 수정 7: 라벨 폰트 크기만 시안 느낌으로 약간 정리
        # 이유:
        # - 너무 크지도 작지도 않게 14로 통일
        # - 기능은 그대로, 텍스트 스타일만 조정
        # ─────────────────────────────────────────────
        ft.Text("이메일", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=14),

        # 🟨 수정 8: 라벨과 입력칸 사이 간격 추가
        # ft.Container(height=1),
        input_box(label="example@gmail.com"),

        # 🟨 수정 9: 입력칸 블록끼리 간격 추가
        # ft.Container(height=1),
        ft.Text("닉네임", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=14),
        # ft.Container(height=1),
        input_box(label="닉네임"),

        # ft.Container(height=1),
        ft.Text("비밀번호", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=14),
        # ft.Container(height=1),
        input_box(label="비밀번호"),
    ]

    return build_screen(
        page=page,
        body_controls=body_controls,
        on_continue=lambda e: go_next(page),
        show_back=True,
        fixed_bottom=True,
    )