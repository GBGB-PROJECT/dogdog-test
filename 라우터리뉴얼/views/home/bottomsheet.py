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
        host="pg.nas6418.ddns.net",
        port=9934,
        dbname="Dogdog",
        user="dog_5",
        password="kosmo",
        connect_timeout=3,
    )


# ============================================================
# ✅ 공통 UI 조각
# ============================================================
def sheet_text_field(hint_text=None, value=None, read_only=False):
    return ft.TextField(
        hint_text=hint_text,
        width=float("inf"), # 👈 이게 없으면 급여량, 메모 텍스트필드 길이가 짧아짐 
        value=value,
        read_only=read_only,
        border_radius=9,
        border_color=ft.Colors.GREY_400,
    )


def sheet_datetime_row(date_text, time_text):
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER, # 👈 이게 없으면 바텀시트 하단 날짜랑 시간이 왼쪽으로 몰림
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
                    ft.Text(date_text, color=ft.Colors.BLACK54),
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
        # width=float("inf"),
        # height=56,
        # padding=ft.padding.symmetric(horizontal=12),
        alignment=ft.Alignment(-1, 0),
        border_radius=9,
        border=ft.border.all(1, ft.Colors.GREY_400),
        content=text_control,
        on_click=on_click,
    )


def register_box(text, on_click):
    return ft.Container(
        height=56,
        padding=ft.padding.symmetric(horizontal=12), # 👈 없으면 등록된 항목이 없어요 글자가 왼쪽에 쳐박힘 
        alignment=ft.Alignment(-1, 0), # 👈 없으면 등록된 항목이 없어요 상자가 짧아진다. 
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
        # open=True,
        bgcolor=bgcolor,
        content=ft.Container(
            padding=padding, # 👈 이게 없으면 바텀시트 안이 꽉참
            content=content, # 👈 이게 없으면 바텀시트 안이 텅빈다 
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
    bgcolor=ft.Colors.WHITE,
    padding=10,
):
    if fields is None:
        fields = [] # 입력칸이 하나도 없는 바텀시트도 허용

    form_controls = [] # 내부에 들어갈 내용 담을 리스트

    if top_content:
        form_controls.append(top_content) # 바텀시트 입력칸 위에 뭐든 넣어도 된다는 의미

    form_controls.extend(fields) # extend는 텍스트필드 여러개 추가 
    form_controls.append(
        sheet_save_button(on_save or (lambda e: e.page.pop_dialog()))
    )

    content_controls = [
        sheet_head_bar(title, image_src=image_src), # 바텀시트 상단에 들어갈 타이틀
    ]

    if subtitle: # 바텀시트에 들어갈 부제목
        content_controls.append(
            ft.Text(
                subtitle,
                size=16,
            )
        )

    content_controls.append( # form_controls의 내용들을 세로로 쌓아서 감싸는 부분
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

    return build_sheet(
        content=content,
        bgcolor=bgcolor,
        padding=padding,
    )


# ============================================================
# ✅ 오늘 기록 카드
# ============================================================
def today_record_box(text, time_text):
    return ft.Container(
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
                today_record_box("물 10ml를 마셨습니다", "오전 07:30"),
                today_record_box("사료 35g를 먹었습니다", "오전 08:10"),
                today_record_box("산책 30분 했습니다", "오후 06:20"),
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


# ============================================================
# ✅ 물주기 바텀시트
# ============================================================
def water_bottomSheet():
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
                content=ft.Text(f"DB 연결 실패: {err}"),
                open=True,
            )
            page.update()
            return False

    def fetch_food_data(keyword=""):
        nonlocal food_error_text
        cursor = None # 👉 DB 커서 변수 준비

        if not ensure_db_connection(): # 👉 DB 연결 안 되어 있으면 바로 종료
            return None

        try: # 👉 DB 작업은 항상 try 안에서 함
            cursor = conn.cursor() # 👉 conn = DB 연결 객체 / cursor = SQL 실행 도구

            if keyword.strip():
                cursor.execute(Product.product_search_query, (f"%{keyword.strip()}%",)) # 👉 SQL LIKE 검색용
            else:
                cursor.execute(Product.product_list_query) # 👉 검색어 없을 때는 전체 목록 가져온다

            rows = cursor.fetchall()  # 👉 DB 결과 전부 가져오기
            food_error_text = None 
            return rows

        except Exception as err:
            conn.rollback() 
            food_error_text = f"사료 조회 실패: {err}"
            return None

        finally: 
            if cursor: # 👉 커서 닫기
                cursor.close()

    def grey_food_item(food_id, food_name):
        is_selected = selected_food_id == food_id

        return ft.Container(
            padding=ft.padding.symmetric(horizontal=14, vertical=14), # 👉 이거 없으면 간격없이 사료가 막나옴 
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

    def message_item(message, color):
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
        food_rows = fetch_food_data(keyword)

        if food_rows is None:
            food_list_column.controls = [
                message_item(
                    food_error_text if food_error_text else "DB 연결 오류가 발생했습니다.",
                    ft.Colors.RED,
                )
            ]
        elif food_rows: # 👉 이거 없으면 사료 안나오고 검색 결과 없습니다 나옴. 
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

        refresh_food_list(food_search_field.value or "") # 👈 이게 없으면 사료 선택해도 회색 띠랑 체크 표시 안보임

        if on_food_selected:
            on_food_selected(food_id, food_name)

    def on_food_search_change(e):
        refresh_food_list(e.control.value)

    def close_food_search_bs(e=None):
        if bs:
            bs.open = False
            page.update()

    def handle_bs_dismiss(e): # 👈 이거 없으면 사료 검색 안뜨고 터짐
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