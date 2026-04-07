import asyncio
import flet as ft


# ─────────────────────────────────────────────
# ✅ 공통 배너 박스
# ─────────────────────────────────────────────
def banner(
    text="",
    image_src=None,
    on_click=None,
):
    # ✅ 오른쪽 화살표 원
    arrow_circle = ft.Container(
        width=40,
        height=40,
        bgcolor="#FEF3B9",
        border_radius=20,
        alignment=ft.Alignment(0, 0),
        content=ft.Icon(
            ft.Icons.ARROW_FORWARD,
            color=ft.Colors.BLACK,
            size=22,
        ),
    )

    # ✅ 왼쪽 고정 칸
    left_slot = ft.Container(
        width=50,
        height=50,
        alignment=ft.Alignment(0, 0),
        content=(
            ft.Container(
                width=50,
                height=50,
                border_radius=25,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=ft.Image(
                    src=image_src,
                    width=50,
                    height=50,
                    fit=ft.BoxFit.COVER,
                ),
            )
            if image_src
            else None
        ),
    )

    # ✅ 가운데 텍스트 칸
    center_slot = ft.Container(
        expand=True,
        alignment=ft.Alignment(0, 0),
        content=ft.Text(
            text,
            size=18,
            weight=ft.FontWeight.W_600,
            color=ft.Colors.BLACK,
            text_align=ft.TextAlign.CENTER,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
        ),
    )

    # ✅ 오른쪽 고정 칸
    right_slot = ft.Container(
        width=50,
        height=50,
        alignment=ft.Alignment(0, 0),
        content=arrow_circle,
    )

    box = ft.Container(
        width=330,
        height=72,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=16,
        padding=ft.padding.symmetric(horizontal=14),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                left_slot,
                center_slot,
                right_slot,
            ],
        ),
    )

    box.arrow_circle = arrow_circle
    return box


def white_long_box(
    text,
    left_icon=ft.Icons.HOME,
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    on_click=None,
    show_left_icon=True,   # ✅ 추가
    show_chevron=True,     # ✅ 추가
):
    left_controls = []

    if show_left_icon:
        left_controls.append(
            ft.Icon(left_icon, color=text_color, size=20)
        )

    left_controls.append(
        ft.Text(
            text,
            size=14,
            weight=ft.FontWeight.W_500,
            color=text_color,
        )
    )

    return ft.Container(
        width=330,
        height=64,
        bgcolor=bgcolor,
        border_radius=16,
        padding=ft.padding.symmetric(horizontal=16),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    spacing=10,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=left_controls,
                ),
                ft.Icon(
                    ft.Icons.CHEVRON_RIGHT,
                    color=text_color,
                    size=22,
                ) if show_chevron else ft.Container(width=22),
            ],
        ),
    )


def build_view(page: ft.Page):
    banner_boxes = []

    def open_food_remain(e=None):
        if hasattr(page, "open_food_remain"):
            page.open_food_remain()
        else:
            print("page.open_food_remain 가 없습니다.")

    def set_selected_banner(index):
        for i, box in enumerate(banner_boxes):
            if i == index:
                box.bgcolor = "#FEF3B9"
                box.arrow_circle.bgcolor = ft.Colors.WHITE
            else:
                box.bgcolor = ft.Colors.WHITE
                box.arrow_circle.bgcolor = "#FEF3B9"
        page.update()

    def select_banner(index):
        def handler(e):
            set_selected_banner(index)
        return handler

    async def select_and_open_food_remain(e):
        set_selected_banner(1)
        await asyncio.sleep(0.3)
        open_food_remain(e)

    banner_0 = banner(
        image_src="대추.jpg",
        text="내 반려동물 정보",
        on_click=select_banner(0),
    )

    banner_1 = banner(
        text="급여중인 제품 보러가기",
        on_click=select_and_open_food_remain,
    )

    banner_boxes.extend([banner_0, banner_1])

    return ft.Container(
        expand=True,
        width=float("inf"),
        alignment=ft.Alignment(0, -1),
        padding=ft.padding.only(left=10, right=10, top=12, bottom=12),
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            controls=[
                ft.Container(height=18),

                banner_0,
                ft.Container(height=14),

                banner_1,
                ft.Container(height=14),

                white_long_box("내 정보", left_icon=ft.Icons.PERSON_OUTLINE),
                ft.Container(height=6),

                white_long_box("마이 쇼핑", left_icon=ft.Icons.STOREFRONT_OUTLINED),
                ft.Container(height=6),

                white_long_box("공지사항", left_icon=ft.Icons.NOTIFICATIONS_NONE),
                ft.Container(height=6),

                white_long_box("문의하기", left_icon=ft.Icons.HELP_OUTLINE),
                ft.Container(height=6),

                # ✅ 로그아웃도 같은 박스 구조 사용
                white_long_box(
                    "로그아웃",
                    text_color=ft.Colors.GREY_300,
                    show_left_icon=False,
                    show_chevron=False,
                ),

                ft.Container(height=20),
            ],
        ),
    )