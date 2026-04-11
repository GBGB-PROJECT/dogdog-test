import flet as ft
from datetime import datetime

from components.common.texts import Txt
from database.db import get_connection
from database.queries import Product
from views.home.bottomsheet_props import (
    sheet_text_field,
    sheet_datetime_row,
    register_box,
    build_sheet,
    form_bottom_sheet,
    today_record_box,
)


# ============================================================
# ✅ 개별 바텀시트
# - 실제로 화면에서 열리는 바텀시트들
# ============================================================
def today_record_bottomSheet():
    # ============================================================
    # ✅ 오늘 기록 바텀시트
    # ============================================================
    def watch_more(e):
        page = e.page
        page.pop_dialog()
        page.open_log_weekly()

    content = ft.Container(
        padding=16,
        content=ft.Column(
            tight=True,
            spacing=14,
            controls=[
                Txt(
                    f"오늘의 기록: {datetime.now().strftime('%Y.%m.%d')}",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.BLACK,
                ),
                today_record_box("물 10ml를 마셨습니다", "오전 07:30"),
                today_record_box("사료 35g를 먹었습니다", "오전 08:10"),
                today_record_box("산책 30분 했습니다", "오후 06:20"),
                ft.Container(
                    alignment=ft.Alignment(0, 0),
                    padding=ft.padding.only(top=6, bottom=4),
                    content=Txt(
                        "더보기",
                        size=14,
                        color=ft.Colors.GREY_500,
                        weight=ft.FontWeight.W_500,
                    ),
                    on_click=watch_more,
                ),
            ],
        ),
    )

    return build_sheet(content=content, bgcolor=ft.Colors.WHITE, padding=0)


def feeding_bottomSheet():
    # ============================================================
    # ✅ 밥주기 눌렀을때 사료가 있으면 나오는 바텀시트 (현재는 안나옴)
    # ============================================================
    bowl_guide = ft.Container(
        alignment=ft.Alignment(0, 0),
        content=ft.Stack(
            controls=[
                ft.Container(
                    alignment=ft.Alignment(0, 0),
                    content=ft.Image(
                        src="밥그릇.png",
                        width=200,
                        height=130,
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(top=45),
                    alignment=ft.Alignment(0, 0),
                    content=Txt(
                        "40g",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
            ]
        ),
    )

    return form_bottom_sheet(
        title="밥주기",
        image_src="dogbowl.png",
        subtitle="오늘 츄츄에게 딱 알맞은 1회 급여량은..",
        top_content=bowl_guide,
        fields=[
            sheet_text_field(
                value="가장 맛있는 시간 30일, 어덜트 치킨",
                read_only=True,
            ),
            sheet_text_field(value="40g"),
            sheet_text_field(hint_text="메모 (선택)"),
            sheet_datetime_row("2026.03.19", "오전 08:00"),
        ],
    )


def water_bottomSheet():
    # ============================================================
    # ✅ 물주기 바텀시트
    # ============================================================
    water_guide = ft.Container(
        alignment=ft.Alignment(0, 0),
        content=ft.Stack(controls=[]),
    )

    return form_bottom_sheet(
        title="물주기",
        image_src="waterdrop.png",
        top_content=water_guide,
        fields=[
            sheet_text_field(hint_text="물 섭취량(ml)"),
            sheet_text_field(hint_text="메모 (선택)"),
            sheet_datetime_row("2026.03.19", "오전 08:00"),
        ],
    )


# ============================================================
# ✅ 검색형 바텀시트
# - 검색 / DB 조회 / 선택 상태 담당
# ============================================================
def food_search_bottomSheet(
    page: ft.Page,
    on_food_selected=None,
    initial_selected_food_id=None,
    initial_selected_food_name=None,
):
    # ============================================================
    # ✅ 사료 검색 바텀시트
    # - 검색 / DB 조회 / 선택 상태 담당
    # ============================================================
    conn = None
    food_error_text = None
    bs = None

    selected_food_id = (
        initial_selected_food_id
        if initial_selected_food_id is not None
        else page.session.store.get("selected_food_id")
    )
    selected_food_name = (
        initial_selected_food_name
        if initial_selected_food_name is not None
        else page.session.store.get("selected_food_name")
    )

    food_list_column = ft.Column(
        spacing=8,
        scroll=ft.ScrollMode.AUTO,
        height=320,
    )

    food_search_field = ft.TextField(
        hint_text="Search",
        border_radius=12,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_300,
        content_padding=ft.padding.symmetric(horizontal=12, vertical=14),
        text_style=ft.TextStyle(size=14, color=ft.Colors.BLACK),
        hint_style=ft.TextStyle(size=14, color=ft.Colors.GREY_500),
    )

    def ensure_db_connection():
        nonlocal conn, food_error_text

        if conn is not None and getattr(conn, "closed", 1) == 0:
            food_error_text = None
            return True

        try:
            conn = get_connection()
            food_error_text = None
            return True
        except Exception as err:
            food_error_text = f"DB 서버 연결 실패: {err}"
            page.snack_bar = ft.SnackBar(
                content=Txt(f"DB 연결 실패: {err}"),
                open=True,
            )
            page.update()
            return False

    def fetch_food_data(keyword=""):
        nonlocal food_error_text
        cursor = None  # 👉 DB 커서 변수 준비

        if not ensure_db_connection():  # 👉 DB 연결 안 되어 있으면 바로 종료
            return None

        try:  # 👉 DB 작업은 항상 try 안에서 함
            cursor = conn.cursor()  # 👉 conn = DB 연결 객체 / cursor = SQL 실행 도구

            if keyword.strip():
                cursor.execute(
                    Product.product_search_query,
                    (f"%{keyword.strip()}%",),
                )  # 👉 SQL LIKE 검색용
            else:
                cursor.execute(Product.product_list_query)  # 👉 검색어 없을 때는 전체 목록 가져온다

            rows = cursor.fetchall()  # 👉 DB 결과 전부 가져오기
            food_error_text = None
            return rows

        except Exception as err:
            conn.rollback()
            food_error_text = f"사료 조회 실패: {err}"
            return None

        finally:
            if cursor:  # 👉 커서 닫기
                cursor.close()

    def grey_food_item(food_id, food_name):
        is_selected = selected_food_id == food_id

        return ft.Container(
            padding=ft.padding.symmetric(horizontal=14, vertical=14),  # 👉 이거 없으면 간격없이 사료가 막나옴
            border_radius=12,
            bgcolor=ft.Colors.GREY_100 if is_selected else ft.Colors.WHITE,
            on_click=lambda e, f_id=food_id, f_name=food_name: select_food(f_id, f_name),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    Txt(
                        food_name,
                        size=14,
                        color=ft.Colors.BLACK,
                        weight=ft.FontWeight.W_500,
                    ),
                    ft.Icon(
                        ft.Icons.CHECK,
                        size=20,
                        color=ft.Colors.BLACK if is_selected else ft.Colors.TRANSPARENT,
                    ),
                ],
            ),
        )

    def message_item(message, color):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=20),
            alignment=ft.Alignment(0, 0),
            content=Txt(
                message,
                size=14,
                color=color,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.W_500,
            ),
        )

    def refresh_food_list(keyword=""):
        food_rows = fetch_food_data(keyword)

        if food_rows is None:
            food_list_column.controls = [
                message_item(
                    food_error_text if food_error_text else "DB 연결 오류가 발생했습니다.",
                    ft.Colors.RED,
                )
            ]
        elif food_rows:  # 👉 이거 없으면 사료 안나오고 검색 결과 없습니다 나옴.
            food_list_column.controls = [
                grey_food_item(row[0], row[1]) for row in food_rows
            ]
        else:
            food_list_column.controls = [
                message_item("검색 결과가 없습니다.", ft.Colors.GREY_600)
            ]

        page.update()

    def select_food(food_id, food_name):
        nonlocal selected_food_id, selected_food_name

        selected_food_id = food_id
        selected_food_name = food_name

        page.session.store.set("selected_food_id", food_id)
        page.session.store.set("selected_food_name", food_name)

        refresh_food_list(food_search_field.value or "")  # 👈 이게 없으면 사료 선택해도 회색 띠랑 체크 표시 안보임

        if on_food_selected:
            on_food_selected(food_id, food_name)

    def on_food_search_change(e):
        refresh_food_list(e.control.value)

    def close_food_search_bs(e=None):
        if bs:
            bs.open = False
            page.update()

    def handle_bs_dismiss(e):  # 👈 이거 없으면 사료 검색 안뜨고 터짐
        nonlocal conn
        if conn is not None and getattr(conn, "closed", 1) == 0:
            conn.close()

    food_search_field.on_change = on_food_search_change

    bs = ft.BottomSheet(
        open=True,
        scrollable=True,
        barrier_color=ft.Colors.TRANSPARENT,
        bgcolor=ft.Colors.TRANSPARENT,
        content=ft.Container(
            height=400,
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.border_radius.only(
                top_left=24,
                top_right=24,
            ),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=10,
                color=ft.Colors.with_opacity(0.08, ft.Colors.BLACK),
                offset=ft.Offset(0, -2),
            ),
            content=ft.Column(
                tight=True,
                spacing=12,
                controls=[
                    ft.Container(
                        width=38,
                        height=5,
                        border_radius=10,
                        bgcolor=ft.Colors.GREY_400,
                    ),
                    ft.Container(height=4),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            Txt(
                                "사료 검색",
                                size=23,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE,
                                icon_size=22,
                                icon_color=ft.Colors.GREY_700,
                                on_click=close_food_search_bs,
                                style=ft.ButtonStyle(padding=0),
                            ),
                        ],
                    ),
                    food_search_field,
                    ft.Container(height=8),
                    food_list_column,
                ],
            ),
        ),
        on_dismiss=handle_bs_dismiss,
    )

    refresh_food_list()
    return bs


def select_feeding_bottomSheet():
    # ============================================================
    # ✅ 밥주기 선택 바텀시트
    # - 등록된 사료가 없을 때 food-select 화면으로 이동
    # ============================================================
    def handle_open_food_select(e):
        page = e.page
        page.pop_dialog()
        page.open_food_select()

    return form_bottom_sheet(
        title="밥주기",
        image_src="dogbowl.png",
        subtitle="사료 선택",
        fields=[
            register_box("등록된 항목이 없어요", handle_open_food_select),
            sheet_text_field(hint_text="급여량(g)"),
            sheet_text_field(hint_text="메모 (선택)"),
            sheet_datetime_row("2026.04.07", "오전 08:00"),
        ],
    )