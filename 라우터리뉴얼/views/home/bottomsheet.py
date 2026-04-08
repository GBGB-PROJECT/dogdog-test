import flet as ft
import psycopg2
from datetime import datetime

# ✅ 실제 경로에 맞게 수정
from views.home.full_query import Product


def top_bar(title, image_src=None):
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    [
                        ft.Row(
                            spacing=8,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                # 🟦 추가: 이모지 대신 이미지 사용 가능
                                *(
                                    [
                                        ft.Image(
                                            src=image_src,
                                            width=24,
                                            height=24,
                                            fit=ft.BoxFit.CONTAIN,
                                        )
                                    ]
                                    if image_src
                                    else []
                                ),
                                ft.Text(
                                    title,
                                    size=20,
                                    weight=ft.FontWeight.W_600,
                                ),
                            ],
                        ),
                        ft.Container(
                            alignment=ft.Alignment(1, 0),
                            content=ft.IconButton(
                                icon=ft.Icons.CLOSE_SHARP,
                                icon_color=ft.Colors.GREY_700,
                                icon_size=30,
                                on_click=lambda e: e.page.pop_dialog(), # 👈 바텀시트 닫기
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
        ],
    )


# ─────────────────────────────────────────────
# ✅ DB 연결 함수
# ─────────────────────────────────────────────
def get_connection():
    return psycopg2.connect(
        host="192.168.0.43",
        port=9934,
        dbname="dogdog",
        user="postgres",
        password="tiger",
        connect_timeout=3,
    )

# 👇 손가락 1: 오늘의 기록 미리보기 바텀시트용 카드
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


# 👇 오늘의 기록 카드 클릭 시 열릴 바텀시트
def today_record_bottomSheet():
    def handle_more(e):
        page = e.page
        page.pop_dialog() # 👈 이게 없으면 더보기 눌러도 바텀시트가 안내려감 

        page.go("/log/weekly") # 👈 이거 없으면 더보기 눌러도 log_weekly로 이동안됨 

    bs = ft.BottomSheet(
        open=True,
        scrollable=True,
        bgcolor=ft.Colors.WHITE,
        content=ft.Container(
            padding=16,
            content=ft.Column(
                tight=True,
                spacing=14,
                controls=[
                # 👇 오늘 날짜 자동 표시
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
        ),
        on_dismiss=lambda e: print("Dismissed!"),
    )

    return bs


def feeding_bottomSheet():
    bs = ft.BottomSheet(
        open=True,
        scrollable=True,
        bgcolor=ft.Colors.WHITE,
        content=ft.Container(
            content=ft.Column(
                width=1000,
                controls=[
                    # 🟦 수정: 이모지 텍스트 대신 이미지 사용
                    top_bar("밥주기", image_src="dogbowl.png"),
                    ft.Text("오늘 츄츄에게 딱 알맞은 1회 급여량은..", size=16),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
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
                            ),
                            ft.TextField(
                                value="가장 맛있는 시간 30일, 어덜트 치킨",
                                read_only=True,
                                border_radius=9,
                                width=float("inf"),
                                border_color=ft.Colors.GREY_400,
                            ),
                            ft.TextField(
                                value="40g",
                                border_radius=9,
                                width=float("inf"),
                                border_color=ft.Colors.GREY_400,
                            ),
                            ft.TextField(
                                hint_text="메모 (선택)",
                                border_radius=9,
                                width=float("inf"),
                                border_color=ft.Colors.GREY_400,
                            ),
                            ft.Row(
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
                                            ft.Text("2026.03.19", color=ft.Colors.BLACK54),
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
                                            ft.Text("오전 08:00", color=ft.Colors.BLACK54),
                                        ],
                                    ),
                                ],
                            ),
                            ft.Container(
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
                                on_click=lambda e: e.page.pop_dialog(), # 👈 닫기
                            ),
                        ],
                    ),
                ],
                tight=True,
            ),
            padding=10,
        ),
        on_dismiss=lambda e: print("Dismissed!"),
    )

    return bs


def water_bottomSheet():
    bs = ft.BottomSheet(
        open=True,
        scrollable=True,
        bgcolor=ft.Colors.WHITE,
        content=ft.Container(
            content=ft.Column(
                width=1000,
                controls=[
                    # 🟦 수정: 이모지 텍스트 대신 이미지 사용
                    top_bar("물주기", image_src="waterdrop.png"),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                alignment=ft.Alignment(0, 0),
                                content=ft.Stack(controls=[]),
                            ),
                            ft.TextField(
                                hint_text="물 섭취량(ml)",
                                border_radius=9,
                                width=float("inf"),
                                border_color=ft.Colors.GREY_400,
                            ),
                            ft.TextField(
                                hint_text="메모 (선택)",
                                border_radius=9,
                                width=float("inf"),
                                border_color=ft.Colors.GREY_400,
                            ),
                            ft.Row(
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
                                            ft.Text("2026.03.19", color=ft.Colors.BLACK54),
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
                                            ft.Text("오전 08:00", color=ft.Colors.BLACK54),
                                        ],
                                    ),
                                ],
                            ),
                            ft.Container(
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
                                on_click=lambda e: e.page.pop_dialog(), # 👈 닫기
                            ),
                        ],
                    ),
                ],
                tight=True,
            ),
            padding=10,
        ),
        on_dismiss=lambda e: print("Dismissed!"),
    )

    return bs


# ─────────────────────────────────────────────
# ✅ DB 연동 사료 검색 바텀시트
# ✅ food_select_view.py 에서 열 것
# ─────────────────────────────────────────────
def food_search_bottomSheet(
    page: ft.Page,
    on_food_selected=None,
    initial_selected_food_id=None,
    initial_selected_food_name=None,
):
    conn = None
    food_error_text = None

    # ✅ 기존 선택값 유지
    # ✅ 함수로 받은 값이 없으면 page에 저장된 마지막 선택값 사용
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
        text_style=ft.TextStyle(
            size=14,
            color=ft.Colors.BLACK,
        ),
        hint_style=ft.TextStyle(
            size=14,
            color=ft.Colors.GREY_500,
        ),
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

    def load_food_list():
        nonlocal food_error_text
        cursor = None

        if not ensure_db_connection():
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(Product.product_list_query)
            rows = cursor.fetchall()
            conn.commit()
            food_error_text = None
            return rows
        except Exception as err:
            conn.rollback()
            food_error_text = f"사료 목록 조회 실패: {err}"
            print(f"product_list_query error: {err}")
            return None
        finally:
            if cursor:
                cursor.close()

    def search_food_list(keyword):
        nonlocal food_error_text
        cursor = None

        if not ensure_db_connection():
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(Product.product_search_query, (f"%{keyword}%",))
            rows = cursor.fetchall()
            conn.commit()
            food_error_text = None
            return rows
        except Exception as err:
            conn.rollback()
            food_error_text = f"사료 검색 실패: {err}"
            print(f"product_search_query error: {err}")
            return None
        finally:
            if cursor:
                cursor.close()

    def select_food(food_id, food_name):
        nonlocal selected_food_id, selected_food_name
        selected_food_id = food_id
        selected_food_name = food_name

        # ✅ 마지막 선택값을 page에 저장
        page.selected_food_id = food_id
        page.selected_food_name = food_name

        # ✅ 부모 화면의 텍스트도 바로 갱신
        if on_food_selected:
            on_food_selected(food_id, food_name)

        # ✅ 바텀시트는 닫지 않고 선택 표시만 갱신
        update_food_list(food_search_field.value if food_search_field.value else "")

    def food_item(food_id, food_name):
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

    def update_food_list(keyword=""):
        if keyword.strip():
            food_rows = search_food_list(keyword.strip())
        else:
            food_rows = load_food_list()

        if food_rows is None:
            food_list_column.controls = [
                ft.Container(
                    padding=ft.padding.symmetric(vertical=20),
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        food_error_text if food_error_text else "DB 연결 오류가 발생했습니다.",
                        size=14,
                        color=ft.Colors.RED,
                        text_align=ft.TextAlign.CENTER,
                    ),
                )
            ]
        elif food_rows:
            food_list_column.controls = [food_item(row[0], row[1]) for row in food_rows]
        else:
            food_list_column.controls = [
                ft.Container(
                    padding=ft.padding.symmetric(vertical=20),
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        "검색 결과가 없습니다.",
                        size=14,
                        color=ft.Colors.GREY_600,
                    ),
                )
            ]

        page.update()

    def on_food_search_change(e):
        update_food_list(e.control.value)

    food_search_field.on_change = on_food_search_change

    bs = None

    def close_food_search_bs(e=None):
        if bs:
            bs.open = False
            page.update()

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
                        alignment=ft.Alignment(-1, 0),
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
                                style=ft.ButtonStyle(
                                    padding=0,
                                ),
                            ),
                        ],
                    ),
                    food_search_field,
                    ft.Container(height=8),
                    food_list_column,
                ],
            ),
        ),
        on_dismiss=lambda e: print("Dismissed!"),
    )

    update_food_list("")
    return bs


def select_feeding_bottomSheet():
    # ─────────────────────────────────────────────
    # ✅ 수정: 등록된 항목이 없어요 클릭 → main.py 의 open_food_select 사용
    # ─────────────────────────────────────────────
    def handle_open_food_select(e):
        page = e.page

        # 현재 바텀시트 닫기
        page.pop_dialog()

        page.go("/food-select")

    bs = ft.BottomSheet(
        open=True,
        scrollable=True,
        bgcolor=ft.Colors.WHITE,
        content=ft.Container(
            content=ft.Column(
                width=1000,
                tight=True,
                controls=[
                    # 🟦 수정: 이모지 텍스트 대신 이미지 사용
                    top_bar("밥주기", image_src="dogbowl.png"),
                    ft.Text("사료 선택", size=16),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                width=float("inf"),
                                height=56,
                                padding=ft.padding.symmetric(horizontal=12),
                                alignment=ft.Alignment(-1, 0),
                                border_radius=9,
                                border=ft.border.all(1, ft.Colors.GREY_400),
                                content=ft.Text(
                                    "등록된 항목이 없어요",
                                    color=ft.Colors.GREY_600,
                                    size=14,
                                ),
                                on_click=handle_open_food_select,
                            ),
                            ft.TextField(
                                hint_text="급여량(g)",
                                border_radius=9,
                                width=float("inf"),
                                border_color=ft.Colors.GREY_400,
                            ),
                            ft.TextField(
                                hint_text="메모 (선택)",
                                border_radius=9,
                                width=float("inf"),
                                border_color=ft.Colors.GREY_400,
                            ),
                            ft.Row(
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
                                            ft.Text("2026.04.07", color=ft.Colors.BLACK54),
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
                                            ft.Text("오전 08:00", color=ft.Colors.BLACK54),
                                        ],
                                    ),
                                ],
                            ),
                            ft.Container(
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
                                on_click=lambda e: e.page.pop_dialog(),
                            ),
                        ],
                    ),
                ],
            ),
            padding=10,
        ),
        on_dismiss=lambda e: print("Dismissed!"),
    )

    return bs