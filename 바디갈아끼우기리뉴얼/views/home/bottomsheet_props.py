import flet as ft
from components.common.texts import Txt
from components.common.colors import (
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    SURFACE_WHITE,
    BORDER_LIGHT,
    BORDER_MEDIUM,
    ACCENT_YELLOW,
)

# ============================================================
# ✅ 공통 UI 조각
# - 바텀시트 여러 곳에서 재사용하는 작은 부품들
# ============================================================
def sheet_head_bar(title, image_src=None):
    # ============================================================
    # ✅ 공통 헤더 바
    # - 바텀시트 전용
    # - 제목 + 선택 아이콘 + 닫기 버튼
    # ============================================================
    left_controls = []

    if image_src:
        left_controls.append(
            ft.Image(
                src=image_src,
                width=24,
                height=24,
                fit=ft.BoxFit.CONTAIN,
            )
        )

    left_controls.append(
        Txt(
            title,
            size=20,
            weight=ft.FontWeight.W_600,
        )
    )

    return ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=left_controls,
                ),
                ft.IconButton(
                    icon=ft.Icons.CLOSE_SHARP,
                    icon_color=ft.Colors.GREY_700,
                    icon_size=30,
                    on_click=lambda e: e.page.pop_dialog(),
                ),
            ],
        ),
    )


def sheet_text_field(hint_text=None, value=None, read_only=False):
    return ft.TextField(
        hint_text=hint_text,
        width=float("inf"),  # 👈 이게 없으면 급여량, 메모 텍스트필드 길이가 짧아짐
        value=value,
        read_only=read_only,
        border_radius=9,
        border_color=BORDER_MEDIUM,
    )


def sheet_datetime_row(date_text, time_text):
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,  # 👈 이게 없으면 바텀시트 하단 날짜랑 시간이 왼쪽으로 몰림
        spacing=30,
        controls=[
            ft.Row(
                # spacing=6,
                controls=[
                    ft.Icon(
                        ft.Icons.CALENDAR_MONTH_OUTLINED,
                        size=18,
                        color=ft.Colors.BLACK54,
                    ),
                    Txt(
                        date_text,
                        color=ft.Colors.BLACK54,
                        weight=ft.FontWeight.W_500,
                    ),
                ],
            ),
            ft.Row(
                # spacing=6,
                controls=[
                    ft.Icon(
                        ft.Icons.ACCESS_TIME,
                        size=18,
                        color=ft.Colors.BLACK54,
                    ),
                    Txt(
                        time_text,
                        color=ft.Colors.BLACK54,
                        weight=ft.FontWeight.W_500,
                    ),
                ],
            ),
        ],
    )


def sheet_save_button(on_click):
    return ft.Container(
        width=65,
        height=35,
        alignment=ft.Alignment(0, 0),
        border_radius=9,
        bgcolor=ACCENT_YELLOW,
        content=Txt(
            "저장",
            color=SURFACE_WHITE,
            weight=ft.FontWeight.BOLD,
        ),
        on_click=on_click,
    )

def register_box(text, on_click):
    return ft.Container(
        height=56,
        padding=ft.padding.symmetric(horizontal=12),  # 👈 없으면 등록된 항목이 없어요 글자가 왼쪽에 쳐박힘
        alignment=ft.Alignment(-1, 0),  # 👈 없으면 등록된 항목이 없어요 상자가 짧아진다.
        border_radius=9,
        border=ft.border.all(1, BORDER_MEDIUM),
        content=Txt(
            text,
            color=TEXT_SECONDARY,
            size=14,
            weight=ft.FontWeight.W_500,
        ),
        on_click=on_click,
    )


# ============================================================
# ✅ 공통 바텀시트 틀
# - 바텀시트 생성용 공통 뼈대
# ============================================================
def build_sheet(content, bgcolor=SURFACE_WHITE, padding=10, on_dismiss=None):
    return ft.BottomSheet(
        # open=True,
        bgcolor=bgcolor,
        content=ft.Container(
            padding=padding,  # 👈 이게 없으면 바텀시트 안이 꽉참
            content=content,  # 👈 이게 없으면 바텀시트 안이 텅빈다
        ),
        # on_dismiss=on_dismiss,
    )


# ============================================================
# ✅ 폼형 바텀시트 공통 틀
# - 헤더 / 부제목 / 상단 커스텀 영역 / 필드들 / 저장 버튼
# ============================================================
def form_bottom_sheet(
    title,
    image_src=None,
    subtitle=None,
    fields=None,
    top_content=None,
    on_save=None,
    bgcolor=SURFACE_WHITE,
    padding=10,
):
    if fields is None:
        fields = []  # 입력칸이 하나도 없는 바텀시트도 허용

    form_controls = []  # 내부에 들어갈 내용 담을 리스트

    if top_content:
        form_controls.append(top_content)  # 바텀시트 입력칸 위에 뭐든 넣어도 된다는 의미

    form_controls.extend(fields)  # extend는 텍스트필드 여러개 추가
    form_controls.append(
        sheet_save_button(on_save or (lambda e: e.page.pop_dialog()))
    )

    content_controls = [
        sheet_head_bar(title, image_src=image_src),  # 바텀시트 상단에 들어갈 타이틀
    ]

    if subtitle:  # 바텀시트에 들어갈 부제목
        content_controls.append(
            Txt(
                subtitle,
                size=16,
                weight=ft.FontWeight.W_500,
            )
        )

    content_controls.append(  # form_controls의 내용들을 세로로 쌓아서 감싸는 부분
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=form_controls,
        )
    )

    content = ft.Column(
        width=1000,
        tight=True,
        controls=content_controls,
    )

    return build_sheet(  # 이게 없으니 밥주기 버튼 누르면 에러 발생
        content=content,
        # bgcolor=bgcolor,
        # padding=padding,
    )


# ============================================================
# ✅ 작은 공통 카드
# - 특정 바텀시트 안에서 재사용되는 카드 UI
# ============================================================
def today_record_box(text, time_text):
    # ============================================================
    # ✅ 오늘 기록 카드
    # ============================================================
    return ft.Container(
        height=70,
        bgcolor=SURFACE_WHITE,
        border=ft.border.all(1, BORDER_LIGHT),
        border_radius=16,
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                Txt(
                    text,
                    size=14,
                    weight=ft.FontWeight.W_500,
                    color=TEXT_PRIMARY,
                ),
                Txt(
                    time_text,
                    size=14,
                    weight=ft.FontWeight.W_600,
                    color=TEXT_PRIMARY,
                ),
            ],
        ),
    )