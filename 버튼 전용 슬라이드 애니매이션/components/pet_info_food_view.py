import flet as ft
import psycopg2

from components.common.common_components import about_dog, input_box, bottom_continue_button
from components.layout.common_layout import build_screen_body
from components.navigation import go_next, go_back

# 🟦 추가:
# 🟦 full_query에서 사료 검색용 쿼리 클래스 import
# 🟦 예시 이름: Food
# 🟦 네 full_query.py 안 실제 이름이 다르면 여기만 바꾸면 됨
from views.onboarding.full_query import Product


# ✅ DB 연결 함수
def get_connection():
    return psycopg2.connect(
        host="192.168.0.43",
        port=9934,
        dbname="dogdog",
        user="postgres",
        password="tiger",
        connect_timeout=3,
    )


# 🟦 원본 8pet 기준:
# 🟦 "현재 급여 중인 사료" 입력칸을 일반 TextField가 아니라
# 🟦 클릭 시 바텀시트가 열리는 선택 박스로 사용
def food_select_box(text="현재 급여 중인 사료를 적어주세요", on_click=None):
    is_placeholder = text == "현재 급여 중인 사료를 적어주세요"

    return ft.Container(
        width=350,
        height=50,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=ft.Padding.symmetric(horizontal=12),
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    text,
                    size=14,
                    color=ft.Colors.GREY_600 if is_placeholder else ft.Colors.BLACK,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
                ft.Icon(
                    ft.Icons.SEARCH,
                    color=ft.Colors.GREY_700,
                ),
            ],
        ),
    )


def build_view(page: ft.Page):
    # 🟩 현재 선택된 사료 이름 상태값
    selected_food_id = None
    selected_food_text = "현재 급여 중인 사료를 적어주세요"

    # 🟦 추가:
    # 🟦 DB 연결 객체 / 에러 메시지 상태값
    conn = None
    food_error_text = None

    # 🟩 검색 결과가 들어갈 리스트 영역
    food_list_column = ft.Column(
        spacing=6,
        scroll=ft.ScrollMode.AUTO,
        height=300,
    )

    # 🟩 바텀시트 안 검색창
    food_search_field = input_box(label="Search")

    # 🟩 본문 전용 컬럼
    body_content = ft.Column(
        width=350,
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        scroll=ft.ScrollMode.AUTO,
    )

    # ─────────────────────────────────────────────
    # 🟦 추가: DB 연결 보장 함수
    # 🟦 설명:
    # 🟦 - a 코드에서 쓰던 방식 그대로 적용
    # 🟦 - conn이 살아있으면 재사용
    # 🟦 - 끊겼거나 없으면 get_connection()으로 재연결
    # ─────────────────────────────────────────────
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

    # ─────────────────────────────────────────────
    # 🟦 추가: 사료 전체 목록 조회
    # 🟦 설명:
    # 🟦 - 기존 가짜 food_items 대신
    # 🟦 - full_query의 food_list_query 실행
    # ─────────────────────────────────────────────
    def load_food_list():
        nonlocal food_error_text

        if not ensure_db_connection():
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(Product.product_list_query)
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
            food_error_text = None
            return rows
        except Exception as err:
            conn.rollback()
            food_error_text = f"사료 목록 조회 실패: {err}"
            print(f"food_list_query error: {err}")
            return None

    # ─────────────────────────────────────────────
    # 🟦 추가: 사료 검색 조회
    # 🟦 설명:
    # 🟦 - 검색창 입력값을 LIKE 검색으로 전달
    # 🟦 - full_query의 food_search_query 사용
    # ─────────────────────────────────────────────
    def search_food_list(keyword):
        nonlocal food_error_text

        if not ensure_db_connection():
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(Product.product_search_query, (f"%{keyword}%",))
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
            food_error_text = None
            return rows
        except Exception as err:
            conn.rollback()
            food_error_text = f"사료 검색 실패: {err}"
            print(f"food_search_query error: {err}")
            return None

    # 🟩 사료 1개 행
    # 🟦 수정:
    # 🟦 - 이제 row[0]=food_id, row[1]=food_name 구조를 사용한다고 가정
    def food_item(food_id, food_name):
        is_selected = selected_food_id == food_id

        return ft.Container(
            padding=ft.Padding.symmetric(vertical=14, horizontal=10),
            border_radius=10,
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
                        color=ft.Colors.BLACK if is_selected else ft.Colors.TRANSPARENT,
                        size=18,
                    ),
                ],
            ),
        )

    # ─────────────────────────────────────────────
    # 🟦 수정: 검색 결과 리스트 다시 그리기
    # 🟦 기존:
    # 🟦 - food_items라는 가짜 리스트를 필터링
    # 🟦 변경:
    # 🟦 - DB에서 전체 목록 또는 검색 결과를 받아와서 출력
    # ─────────────────────────────────────────────
    def update_food_list(keyword=""):
        nonlocal food_error_text

        if keyword.strip():
            food_rows = search_food_list(keyword.strip())
        else:
            food_rows = load_food_list()

        if food_rows is None:
            food_list_column.controls = [
                ft.Container(
                    padding=ft.Padding.symmetric(vertical=20),
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
                    padding=ft.Padding.symmetric(vertical=20),
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        "검색 결과가 없습니다.",
                        size=14,
                        color=ft.Colors.GREY_600,
                    ),
                )
            ]

        page.update()

    # 🟩 검색창 입력 시 목록 필터링
    # 🟦 수정:
    # 🟦 - 이제 단순 리스트 필터링이 아니라 DB 검색 호출
    def on_food_search_change(e):
        update_food_list(e.control.value)

    food_search_field.on_change = on_food_search_change

    # 🟩 사료 선택 시 실행
    # 🟦 수정:
    # 🟦 - food_id도 같이 저장
    def select_food(food_id, food_name):
        nonlocal selected_food_id, selected_food_text
        selected_food_id = food_id
        selected_food_text = food_name

        rebuild_body()

        harim_bottom_tip_sheet.open = False
        page.update()

    # 🟩 바텀시트
    harim_bottom_tip_sheet = ft.BottomSheet(
        open=False,
        barrier_color=ft.Colors.TRANSPARENT,
        size_constraints=ft.BoxConstraints(
            max_height=700,
            min_height=430,
        ),
        content=ft.Container(
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.BorderRadius.only(
                top_left=20,
                top_right=20,
            ),
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
                offset=ft.Offset(0, -4),
            ),
            content=ft.Column(
                tight=True,
                controls=[
                    ft.Container(
                        width=40,
                        height=5,
                        border_radius=10,
                        bgcolor=ft.Colors.GREY_400,
                        alignment=ft.Alignment(0, 0),
                    ),
                    ft.Container(height=10),
                    ft.Text(
                        "사료 검색",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                    ),
                    food_search_field,
                    ft.Container(height=12),
                    food_list_column,
                    ft.Container(height=10),
                ],
            ),
        ),
    )

    if harim_bottom_tip_sheet not in page.overlay:
        page.overlay.append(harim_bottom_tip_sheet)

    # 🟩 바텀시트 열기 함수
    # 🟦 수정:
    # 🟦 - 열릴 때 DB 전체 목록 불러오기
    def open_food_bottom_sheet(e):
        food_search_field.value = ""
        update_food_list("")
        harim_bottom_tip_sheet.open = True
        page.update()

    # 🟩 Continue 버튼 클릭 시
    # 🟦 추가:
    # 🟦 - 선택한 사료 정보 로그 확인 가능
    def on_continue(e):
        print("선택한 사료 ID:", selected_food_id)
        print("선택한 사료 이름:", selected_food_text)
        go_next(page)

    # 🟩 본문 다시 그리기
    def rebuild_body():
        body_content.controls = [
            ft.Container(
                margin=ft.Margin.only(top=50),
                content=about_dog(),
            ),
            ft.Text(
                "현재 급여 중인 사료",
                weight=ft.FontWeight.W_500,
                color=ft.Colors.BLACK,
            ),
            food_select_box(
                text=selected_food_text,
                on_click=open_food_bottom_sheet,
            ),
            ft.Text(
                "현재 급여 중인 사료 잔여량",
                weight=ft.FontWeight.W_500,
                color=ft.Colors.BLACK,
            ),
            input_box(label="현재 급여 중인 사료 잔여량을 적어주세요"),
            ft.Container(height=20),
        ]
        page.update()

    rebuild_body()

    return build_screen_body([body_content])