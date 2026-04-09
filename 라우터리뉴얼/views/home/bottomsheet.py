import flet as ft
import psycopg2
from datetime import datetime

from views.home.full_query import Product


# ============================================================
# ✅ 공통 헤더 바
# - 바텀시트 전용
# - 제목 + 선택 아이콘 + 닫기 버튼
# ============================================================
def sheet_head_bar(title, image_src=None):
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
        ft.Text(
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


# ============================================================
# ✅ DB 연결
# ============================================================
def get_connection():
    return psycopg2.connect(
        host="192.168.0.43",
        port=9934,
        dbname="dogdog",
        user="postgres",
        password="tiger",
        connect_timeout=3,
    )


# ============================================================
# ✅ 공통 UI 조각
# ============================================================
def sheet_text_field(hint_text=None, value=None, read_only=False):
    return ft.TextField(
        hint_text=hint_text,
        value=value,
        read_only=read_only,
        border_radius=9,
        width=float("inf"),
        border_color=ft.Colors.GREY_400,
    )


def sheet_datetime_row(date_text, time_text):
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30,
        controls=[
            ft.Row(
                spacing=6,
                controls=[
                    ft.Icon(
                        ft.Icons.CALENDAR_MONTH_OUTLINED,
                        size=18,
                        color=ft.Colors.BLACK54,
                    ),
                    ft.Text(date_text, color=ft.Colors.BLACK54),
                ],
            ),
            ft.Row(
                spacing=6,
                controls=[
                    ft.Icon(
                        ft.Icons.ACCESS_TIME,
                        size=18,
                        color=ft.Colors.BLACK54,
                    ),
                    ft.Text(time_text, color=ft.Colors.BLACK54),
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
        bgcolor=ft.Colors.YELLOW_600,
        content=ft.Text(
            "저장",
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD,
        ),
        on_click=on_click,
    )


def selector_box(text_control, on_click):
    return ft.Container(
        width=float("inf"),
        height=56,
        padding=ft.padding.symmetric(horizontal=12),
        alignment=ft.Alignment(-1, 0),
        border_radius=9,
        border=ft.border.all(1, ft.Colors.GREY_400),
        content=text_control,
        on_click=on_click,
    )


def empty_selector_box(text, on_click):
    return ft.Container(
        width=float("inf"),
        height=56,
        padding=ft.padding.symmetric(horizontal=12),
        alignment=ft.Alignment(-1, 0),
        border_radius=9,
        border=ft.border.all(1, ft.Colors.GREY_400),
        content=ft.Text(
            text,
            color=ft.Colors.GREY_600,
            size=14,
        ),
        on_click=on_click,
    )


def build_sheet(content, bgcolor=ft.Colors.WHITE, padding=10, on_dismiss=None):
    return ft.BottomSheet(
        open=True,
        scrollable=True,
        bgcolor=bgcolor,
        content=ft.Container(
            padding=padding,
            content=content,
        ),
        on_dismiss=on_dismiss,
    )


# ============================================================
# ✅ 오늘 기록 카드
# ============================================================
def summary_record_box(text, time_text):
    return ft.Container(
        width=float("inf"),
        height=70,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=16,
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    text,
                    size=14,
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.BLACK,
                ),
                ft.Text(
                    time_text,
                    size=14,
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.BLACK,
                ),
            ],
        ),
    )


# ============================================================
# ✅ 오늘 기록 바텀시트
# ============================================================
def today_record_bottomSheet():
    def handle_more(e):
        page = e.page
        page.pop_dialog()
        page.go("/log/weekly")

    content = ft.Container(
        padding=16,
        content=ft.Column(
            tight=True,
            spacing=14,
            controls=[
                ft.Text(
                    f"오늘의 기록: {datetime.now().strftime('%Y.%m.%d')}",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.BLACK,
                ),
                summary_record_box("물 10ml를 마셨습니다", "오전 07:30"),
                summary_record_box("사료 35g를 먹었습니다", "오전 08:10"),
                summary_record_box("산책 30분 했습니다", "오후 06:20"),
                ft.Container(
                    alignment=ft.Alignment(0, 0),
                    padding=ft.padding.only(top=6, bottom=4),
                    content=ft.Text(
                        "더보기",
                        size=14,
                        color=ft.Colors.GREY_500,
                        weight=ft.FontWeight.W_500,
                    ),
                    on_click=handle_more,
                ),
            ],
        ),
    )

    return build_sheet(content=content, bgcolor=ft.Colors.WHITE, padding=0)


# ============================================================
# ✅ 밥주기 바텀시트
# ============================================================
def feeding_bottomSheet():
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
                    content=ft.Text(
                        "40g",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
            ]
        ),
    )

    content = ft.Column(
        width=1000,
        tight=True,
        controls=[
            sheet_head_bar("밥주기", image_src="dogbowl.png"),
            ft.Text("오늘 츄츄에게 딱 알맞은 1회 급여량은..", size=16),
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    bowl_guide,
                    sheet_text_field(
                        value="가장 맛있는 시간 30일, 어덜트 치킨",
                        read_only=True,
                    ),
                    sheet_text_field(value="40g"),
                    sheet_text_field(hint_text="메모 (선택)"),
                    sheet_datetime_row("2026.03.19", "오전 08:00"),
                    sheet_save_button(lambda e: e.page.pop_dialog()),
                ],
            ),
        ],
    )

    return build_sheet(content)


# ============================================================
# ✅ 물주기 바텀시트
# ============================================================
def water_bottomSheet():
    content = ft.Column(
        width=1000,
        tight=True,
        controls=[
            sheet_head_bar("물주기", image_src="waterdrop.png"),
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        alignment=ft.Alignment(0, 0),
                        content=ft.Stack(controls=[]),
                    ),
                    sheet_text_field(hint_text="물 섭취량(ml)"),
                    sheet_text_field(hint_text="메모 (선택)"),
                    sheet_datetime_row("2026.03.19", "오전 08:00"),
                    sheet_save_button(lambda e: e.page.pop_dialog()),
                ],
            ),
        ],
    )

    return build_sheet(content)


# ============================================================
# ✅ 사료 검색 바텀시트
# - 검색 / DB 조회 / 선택 상태 담당
# ============================================================
def food_search_bottomSheet(
    page: ft.Page,
    on_food_selected=None,
    initial_selected_food_id=None,
    initial_selected_food_name=None,
):
    conn = None
    food_error_text = None
    bs = None

    selected_food_id = (
        initial_selected_food_id
        if initial_selected_food_id is not None
        else getattr(page, "selected_food_id", None)
    )
    selected_food_name = (
        initial_selected_food_name
        if initial_selected_food_name is not None
        else getattr(page, "selected_food_name", None)
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
                content=ft.Text(f"DB 연결 실패: {err}"),
                open=True,
            )
            page.update()
            return False

    def fetch_food_rows(keyword=""):
        nonlocal food_error_text
        cursor = None

        if not ensure_db_connection():
            return None

        try:
            cursor = conn.cursor()

            if keyword.strip():
                cursor.execute(Product.product_search_query, (f"%{keyword.strip()}%",))
            else:
                cursor.execute(Product.product_list_query)

            rows = cursor.fetchall()
            conn.commit()
            food_error_text = None
            return rows

        except Exception as err:
            conn.rollback()
            if keyword.strip():
                food_error_text = f"사료 검색 실패: {err}"
            else:
                food_error_text = f"사료 목록 조회 실패: {err}"
            return None

        finally:
            if cursor:
                cursor.close()

    def build_food_item(food_id, food_name):
        is_selected = selected_food_id == food_id

        return ft.Container(
            padding=ft.padding.symmetric(horizontal=14, vertical=14),
            border_radius=12,
            bgcolor=ft.Colors.GREY_100 if is_selected else ft.Colors.WHITE,
            on_click=lambda e, f_id=food_id, f_name=food_name: select_food(f_id, f_name),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
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

    def build_message_item(message, color):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=20),
            alignment=ft.Alignment(0, 0),
            content=ft.Text(
                message,
                size=14,
                color=color,
                text_align=ft.TextAlign.CENTER,
            ),
        )

    def refresh_food_list(keyword=""):
        food_rows = fetch_food_rows(keyword)

        if food_rows is None:
            food_list_column.controls = [
                build_message_item(
                    food_error_text if food_error_text else "DB 연결 오류가 발생했습니다.",
                    ft.Colors.RED,
                )
            ]
        elif food_rows:
            food_list_column.controls = [
                build_food_item(row[0], row[1]) for row in food_rows
            ]
        else:
            food_list_column.controls = [
                build_message_item("검색 결과가 없습니다.", ft.Colors.GREY_600)
            ]

        page.update()

    def select_food(food_id, food_name):
        nonlocal selected_food_id, selected_food_name

        selected_food_id = food_id
        selected_food_name = food_name

        page.selected_food_id = food_id
        page.selected_food_name = food_name

        if on_food_selected:
            on_food_selected(food_id, food_name)

        refresh_food_list(food_search_field.value or "")

    def on_food_search_change(e):
        refresh_food_list(e.control.value)

    def close_food_search_bs(e=None):
        if bs:
            bs.open = False
            page.update()

    def handle_bs_dismiss(e):
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
                    ft.Container( # 👈 
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
                            ft.Text(
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


# ============================================================
# ✅ 밥주기 선택 바텀시트
# - 등록된 사료가 없을 때 food-select 화면으로 이동
# ============================================================
def select_feeding_bottomSheet():
    def handle_open_food_select(e):
        page = e.page
        page.pop_dialog()
        page.go("/food-select")

    content = ft.Column(
        width=1000,
        tight=True,
        controls=[
            sheet_head_bar("밥주기", image_src="dogbowl.png"),
            ft.Text("사료 선택", size=16),
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    empty_selector_box("등록된 항목이 없어요", handle_open_food_select),
                    sheet_text_field(hint_text="급여량(g)"),
                    sheet_text_field(hint_text="메모 (선택)"),
                    sheet_datetime_row("2026.04.07", "오전 08:00"),
                    sheet_save_button(lambda e: e.page.pop_dialog()),
                ],
            ),
        ],
    )

    return build_sheet(content)