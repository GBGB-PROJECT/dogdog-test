import asyncio
import flet as ft

import views.auth.signup_view as signup_view
import views.auth.signup_success_view as signup_success_view
import views.onboarding.pet_basic_info_view as pet_basic_info_view
import views.onboarding.pet_info_obesity_view as pet_info_obesity_view
import views.onboarding.pet_info_activity_view as pet_info_activity_view
import views.onboarding.pet_info_health_view as pet_info_health_view
import components.pet_info_food_view as pet_info_food_view

from components.common.common_components import arrow_back, bottom_continue_button


# ─────────────────────────────────────────────
# 🟦 화면 이동 순서표
# ─────────────────────────────────────────────
ROUTES = [
    "/signup",
    "/pet_info",
    "/pet_info_obesity",
    "/pet_info_activity",
    "/pet_info_health",
    "/pet_info_food",
    "/signup_success",
]


# ─────────────────────────────────────────────
# 🟦 route별 실제 화면 생성 함수 연결표
# ─────────────────────────────────────────────
ROUTE_BUILDERS = {
    "/signup": signup_view.build_view,
    "/pet_info": pet_basic_info_view.build_view,
    "/pet_info_obesity": pet_info_obesity_view.build_view,
    "/pet_info_activity": pet_info_activity_view.build_view,
    "/pet_info_health": pet_info_health_view.build_view,
    "/pet_info_food": pet_info_food_view.build_view,
    "/signup_success": signup_success_view.build_view,
}


# ─────────────────────────────────────────────
# 🟨 슬라이드 애니메이션 설정
# ─────────────────────────────────────────────
ANIMATION_MS = 340
ANIMATION_CURVE = ft.AnimationCurve.EASE_IN_OUT

# ✅ 모바일에서 첫 프레임이 씹히지 않도록 여유 시간
PRE_ANIMATION_DELAY = 0.10
POST_ANIMATION_BUFFER = 0.10


def main(page: ft.Page):
    page.title = "Dog Dog"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.HIDDEN
    page.theme_mode = ft.ThemeMode.LIGHT

    # ─────────────────────────────────────────────
    # ✅ 폰트 등록
    # - 기본 한글/전체 UI: Pretendard
    # - 영문 강조 텍스트: Mulish
    # ─────────────────────────────────────────────
    page.fonts = {
        "Mulish": "fonts/Mulish.ttf",
        "Pretendard": "fonts/Pretendard-Regular.otf",
    }

    # ─────────────────────────────────────────────
    # ✅ 앱 전체 기본 폰트는 Pretendard로 적용
    # - 한글 깨짐/기기별 fallback 문제 방지
    # - 영문은 필요한 Text에서만 font_family="Mulish" 직접 지정
    # ─────────────────────────────────────────────
    page.theme = ft.Theme(
        font_family="Pretendard"
    )

    # ─────────────────────────────────────────────
    # 🟪 FilePicker 서비스 등록용 bootstrap
    # ─────────────────────────────────────────────
    page.views.append(ft.View(route="/__bootstrap__", controls=[]))
    page.profile_image_picker = ft.FilePicker()
    page.services.append(page.profile_image_picker)
    page.views.clear()

    # ─────────────────────────────────────────────
    # 🟦 현재 보고 있는 페이지 번호 저장
    # ─────────────────────────────────────────────
    current_index = 0

    # ─────────────────────────────────────────────
    # 🟦 route 동기화 중복 방지 플래그
    # ─────────────────────────────────────────────
    route_sync_in_progress = False

    # ─────────────────────────────────────────────
    # ✅ 이동 중복/연타 방지 플래그
    # ─────────────────────────────────────────────
    is_navigating = False

    # ─────────────────────────────────────────────
    # 🟩 route 문자열 → index 번호 변환
    # ─────────────────────────────────────────────
    def route_to_index(route_name: str) -> int:
        try:
            return ROUTES.index(route_name)
        except ValueError:
            return 0

    # ─────────────────────────────────────────────
    # 🟩 각 화면을 공통 껍데기 안에 넣는 함수
    # ─────────────────────────────────────────────
    def build_page_shell(route_name: str):
        builder = ROUTE_BUILDERS[route_name]

        # 회원가입 완료 페이지는 예외 처리
        if route_name == "/signup_success":
            return ft.Container(
                expand=True,
                bgcolor=ft.Colors.WHITE,
                content=builder(page),
            )

        return ft.Container(
            expand=True,
            bgcolor=ft.Colors.WHITE,
            alignment=ft.Alignment(0, -1),
            content=ft.Container(
                expand=True,
                alignment=ft.Alignment(0, -1),
                padding=ft.Padding.only(left=16, right=16),
                content=builder(page),
            ),
        )

    # ─────────────────────────────────────────────
    # 🟦 상단 고정 영역
    # ─────────────────────────────────────────────
    top_appbar = ft.Container(
        width=float("inf"),
        height=64,
        bgcolor=ft.Colors.TRANSPARENT,
        padding=ft.Padding.only(left=16, right=16, top=12, bottom=12),
        alignment=ft.Alignment(-1, 0),
    )

    # ─────────────────────────────────────────────
    # 🟦 하단 고정 영역
    # ─────────────────────────────────────────────
    fixed_button = ft.Container(
        width=float("inf"),
        alignment=ft.Alignment(0, 0),
        padding=ft.Padding.only(left=16, right=16, top=10, bottom=20),
    )

    # ─────────────────────────────────────────────
    # 🟦 본문 스택
    # ─────────────────────────────────────────────
    body_stack = ft.Stack(
        expand=True,
        fit=ft.StackFit.EXPAND,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        controls=[],
    )

    # ─────────────────────────────────────────────
    # 🟦 현재/들어오는 레이어 변수
    # ─────────────────────────────────────────────
    current_layer = ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        offset=ft.Offset(0, 0),
        animate_offset=ft.Animation(ANIMATION_MS, ANIMATION_CURVE),
        content=None,
    )

    incoming_layer = None

    # ─────────────────────────────────────────────
    # 🟨 현재 화면과 브라우저 URL 동기화
    # ─────────────────────────────────────────────
    async def sync_route_to_current_index():
        nonlocal route_sync_in_progress
        route_sync_in_progress = True
        try:
            await page.push_route(ROUTES[current_index])
        finally:
            route_sync_in_progress = False

    # ─────────────────────────────────────────────
    # 🟩 현재 페이지에 맞게 상단/하단 고정 UI 바꾸기
    # ─────────────────────────────────────────────
    def apply_shell_by_index(index: int):
        is_success = ROUTES[index] == "/signup_success"

        if is_success:
            top_appbar.content = None
            top_appbar.height = 0
            top_appbar.padding = 0

            fixed_button.content = None
            fixed_button.padding = 0
            return

        top_appbar.height = 64
        top_appbar.padding = ft.Padding.only(left=16, right=16, top=12, bottom=12)

        # ✅ signup 포함 모든 일반 화면에서 화살표 표시
        top_appbar.content = arrow_back(on_click=on_back_click)

        fixed_button.padding = ft.Padding.only(left=16, right=16, top=10, bottom=20)
        fixed_button.content = ft.Container(
            width=350,
            alignment=ft.Alignment(0, 0),
            content=bottom_continue_button(on_click=on_continue_click),
        )

    # ─────────────────────────────────────────────
    # 🟩 현재 화면 즉시 표시
    # ─────────────────────────────────────────────
    def show_index_immediately(index: int):
        nonlocal current_layer, incoming_layer

        current_layer = ft.Container(
            expand=True,
            bgcolor=ft.Colors.WHITE,
            offset=ft.Offset(0, 0),
            animate_offset=ft.Animation(ANIMATION_MS, ANIMATION_CURVE),
            content=build_page_shell(ROUTES[index]),
        )

        incoming_layer = None
        body_stack.controls.clear()
        body_stack.controls.append(current_layer)

        apply_shell_by_index(index)

    # ─────────────────────────────────────────────
    # 🟥 핵심 1: 버튼 전용 슬라이드 애니메이션 이동
    # ─────────────────────────────────────────────
    async def go_to_index(index: int, direction: int):
        nonlocal current_index, is_navigating, current_layer, incoming_layer

        if is_navigating:
            return

        index = max(0, min(index, len(ROUTES) - 1))
        if index == current_index:
            return

        is_navigating = True

        try:
            next_route = ROUTES[index]

            # ✅ 다음 화면은 딱 한 번만 생성
            next_layer = ft.Container(
                expand=True,
                bgcolor=ft.Colors.WHITE,
                offset=ft.Offset(direction, 0),
                animate_offset=ft.Animation(ANIMATION_MS, ANIMATION_CURVE),
                content=build_page_shell(next_route),
            )

            incoming_layer = next_layer

            # ✅ 현재 화면 + 다음 화면을 스택에 올림
            body_stack.controls.clear()
            body_stack.controls.append(current_layer)
            body_stack.controls.append(next_layer)

            # ✅ 버튼/상단 UI는 도착 페이지 기준으로 먼저 바꿈
            current_index = index
            apply_shell_by_index(current_index)
            page.update()

            # ✅ 모바일에서 첫 프레임을 확실히 그릴 시간 확보
            await asyncio.sleep(PRE_ANIMATION_DELAY)

            # ✅ 새 화면만 슬라이드 인
            next_layer.offset = ft.Offset(0, 0)
            page.update()

            # ✅ 애니메이션 완료까지 충분히 대기
            await asyncio.sleep((ANIMATION_MS / 1000) + POST_ANIMATION_BUFFER)

            # ✅ 새 레이어를 현재 레이어로 확정
            current_layer = next_layer
            incoming_layer = None
            current_layer.offset = ft.Offset(0, 0)

            body_stack.controls.clear()
            body_stack.controls.append(current_layer)

            page.update()
            await sync_route_to_current_index()

        finally:
            is_navigating = False

    # ─────────────────────────────────────────────
    # 🟥 핵심 2: Continue 버튼 클릭 시 다음 화면
    # ─────────────────────────────────────────────
    async def on_continue_click(e):
        if current_index >= len(ROUTES) - 1 or is_navigating:
            return
        await go_to_index(current_index + 1, direction=1)

    # ─────────────────────────────────────────────
    # 🟥 핵심 3: 뒤로가기 클릭 시 이전 화면
    # ─────────────────────────────────────────────
    async def on_back_click(e):
        if current_index <= 0 or is_navigating:
            return
        await go_to_index(current_index - 1, direction=-1)

    # ─────────────────────────────────────────────
    # 🟨 브라우저 route가 바뀌었을 때 화면도 맞춰주기
    # ─────────────────────────────────────────────
    def route_change(e: ft.RouteChangeEvent):
        nonlocal current_index

        if route_sync_in_progress:
            return

        target_index = route_to_index(page.route)
        if target_index != current_index:
            current_index = target_index
            show_index_immediately(current_index)
            page.update()

    # ─────────────────────────────────────────────
    # 🟦 전체 앱 껍데기 View
    # ─────────────────────────────────────────────
    page.views.append(
        ft.View(
            route="/app_shell",
            padding=0,
            spacing=0,
            bgcolor=ft.Colors.WHITE,
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        expand=True,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            top_appbar,
                            ft.Container(expand=True, content=body_stack),
                            fixed_button,
                        ],
                    ),
                )
            ],
        )
    )

    page.on_route_change = route_change

    # ─────────────────────────────────────────────
    # ✅ 시작 route 보정
    # ─────────────────────────────────────────────
    initial_route = page.route or "/signup"

    if initial_route == "/signup_success":
        initial_route = "/signup"

    current_index = route_to_index(initial_route)
    show_index_immediately(current_index)
    page.update()

    page.run_task(page.push_route, ROUTES[current_index])


if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )