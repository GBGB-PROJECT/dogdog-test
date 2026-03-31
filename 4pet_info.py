import flet as ft
import datetime

# ✅ PostgreSQL 예시
# 네 DB가 MySQL이면 아래 psycopg2 대신 mysql.connector로 바꿔야 함
import psycopg2

from full_query import Breed


# ✅ DB 연결 함수
# 여기는 네 환경에 맞게 수정해야 함
# ─────────────────────────────────────────────
# 🟨 DB 흐름 1
# 🟨 설명:
# - 이 함수가 실제로 DB 서버에 접속을 시도하는 시작점
# - host, port, dbname, user, password 정보를 이용해서
#   PostgreSQL 서버에 연결함
# - 즉, "DB 서버 작동 여부"를 가장 직접적으로 확인하는 코드
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


def about_dog():
    return ft.Column(
        spacing=0,
        controls=[
            ft.Text(
                "About your Dog",
                weight=ft.FontWeight.W_500,
                color=ft.Colors.BLACK,
                size=30,
            ),
            ft.Text(
                "반려동물의 기본 정보를 입력하세요",
                weight=ft.FontWeight.W_500,
                color=ft.Colors.BLACK,
                size=15,
            ),
        ],
    )


def input_box(hint_text="", width=350):
    return ft.TextField(
        width=width,
        height=50,
        hint_text=hint_text,
        border=ft.InputBorder.OUTLINE,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_300,
        border_radius=10,
        content_padding=ft.padding.only(left=14, right=14, top=0, bottom=0),
        text_size=14,

        # ─────────────────────────────────────────────
        # ✅ 수정: 입력 글자색/힌트 글자색을 직접 지정
        # ✅ 수정 이유:
        # - 기본 스타일에 맡겨두면 입력한 글자가 흐리게 보일 수 있음
        # - text_style 은 사용자가 실제 입력하는 글자 스타일
        # - hint_style 은 placeholder(힌트 문구) 스타일
        # - 입력 글자는 검정으로 선명하게,
        #   힌트 글자는 회색으로 구분되게 설정
        # ─────────────────────────────────────────────
        text_style=ft.TextStyle(
            color=ft.Colors.BLACK,
            size=14,
        ),
        hint_style=ft.TextStyle(
            color=ft.Colors.GREY_600,
            size=14,
        ),

        text_align=ft.TextAlign.LEFT,
        cursor_height=18,
        filled=False,
    )


def weight_input_box(hint_text="4.5"):
    return ft.Container(
        width=350,
        height=50,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=ft.Padding.only(left=14, right=14),
        alignment=ft.Alignment(0, 0),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.TextField(
                    expand=True,
                    hint_text=hint_text,
                    border=ft.InputBorder.NONE,
                    content_padding=0,
                    text_size=14,

                    # ─────────────────────────────────────────────
                    # ✅ 수정: 무게 입력칸도 동일하게 입력 글자색/힌트색 지정
                    # ✅ 수정 이유:
                    # - 이 TextField 역시 기본값으로 두면 글자가 연하게 보일 수 있음
                    # - 실제 입력 숫자는 BLACK
                    # - 힌트값(예: 4.5)은 GREY_600 으로 분리
                    # ─────────────────────────────────────────────
                    text_style=ft.TextStyle(
                        color=ft.Colors.BLACK,
                        size=14,
                    ),
                    hint_style=ft.TextStyle(
                        color=ft.Colors.GREY_600,
                        size=14,
                    ),

                    keyboard_type=ft.KeyboardType.NUMBER,
                ),
                ft.Text(
                    "kg",
                    size=14,
                    color=ft.Colors.BLACK,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        ),
    )


# ✅ 품종 선택용 박스
def breed_select_box(text="반려동물 품종 선택", on_click=None):
    is_placeholder = text == "반려동물 품종 선택"

    return ft.Container(
        width=350,
        height=50,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=ft.padding.symmetric(horizontal=12),
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
                ),
                ft.Icon(
                    ft.Icons.KEYBOARD_ARROW_DOWN_ROUNDED,
                    color=ft.Colors.GREY_700,
                ),
            ],
        ),
    )


def dropdown_box1(label="품종 선택", options=None):
    if options is None:
        options = [
            ft.dropdown.Option("사과"),
            ft.dropdown.Option("바나나"),
            ft.dropdown.Option("포도"),
        ]

    # ─────────────────────────────────────────────
    # ✅ 수정: 바깥 Container가 테두리/높이를 잡던 구조 제거
    # ✅ 수정 이유:
    # - Container + Dropdown 이중 테두리 구조 때문에
    #   모바일 웹에서 상자가 잘려 보였음
    # - 이제 Dropdown 자신이 직접 테두리와 높이를 가짐
    # ─────────────────────────────────────────────
    return ft.Dropdown(
        width=350,

        # ─────────────────────────────────────────────
        # ✅ 수정: 상자 높이는 Dropdown 자신에게 직접 적용
        # ✅ 수정 이유:
        # - 바깥 Container 높이 고정으로 인한 클리핑 방지
        # ─────────────────────────────────────────────
        height=56,

        # ─────────────────────────────────────────────
        # ✅ 수정: label 대신 hint_text 사용
        # ✅ 수정 이유:
        # - label 은 선택 시 위로 뜨는 구조라서
        #   모바일 웹에서 글자가 잘려 보이기 쉬움
        # - hint_text 로 바꾸면 한 줄 안에서 안정적으로 표시됨
        # ─────────────────────────────────────────────
        hint_text=label,

        # ─────────────────────────────────────────────
        # ✅ 수정: Dropdown 자신이 직접 outline 테두리를 그림
        # ✅ 수정 이유:
        # - 이중 테두리 제거
        # - 잘려 보이는 현상 완화
        # ─────────────────────────────────────────────
        border=ft.InputBorder.OUTLINE,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_300,
        border_radius=10,

        # ─────────────────────────────────────────────
        # ✅ 수정: 패딩 조정
        # ✅ 수정 이유:
        # - 상하 여백을 Dropdown 안쪽에서 직접 관리
        # ─────────────────────────────────────────────
        content_padding=ft.padding.only(
            left=14, right=14, top=14, bottom=14
        ),
        text_size=14,

        # ─────────────────────────────────────────────
        # ✅ 수정: 선택된 값 / 힌트 글자 스타일을 명확히 지정
        # ✅ 수정 이유:
        # - 선택된 값은 진한 검정
        # - placeholder 는 회색
        # ─────────────────────────────────────────────
        text_style=ft.TextStyle(
            color=ft.Colors.BLACK,
            size=14,
            weight=ft.FontWeight.W_500,
        ),
        hint_style=ft.TextStyle(
            color=ft.Colors.GREY_600,
            size=14,
        ),

        # ─────────────────────────────────────────────
        # ✅ 수정: Dropdown 필드 색 강제 지정
        # ✅ 수정 이유:
        # - 모바일 웹에서 선택 텍스트/아이콘이 연하게 나오는 현상 완화
        # ─────────────────────────────────────────────
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        filled=False,

        options=options,
    )


def datepicker_box(text="생년월일 선택", on_click=None):
    return ft.Container(
        width=350,
        height=50,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=ft.padding.symmetric(horizontal=12),
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    text,
                    size=14,
                    color=ft.Colors.BLACK
                    if text != "생년월일 선택"
                    else ft.Colors.GREY_600,
                ),
                ft.Icon(ft.Icons.CALENDAR_MONTH, color=ft.Colors.GREY_700),
            ],
        ),
    )


def birth_mode_box(group_value=None, on_change=None):
    return ft.Container(
        width=350,
        border=None,
        border_radius=0,
        padding=12,
        content=ft.RadioGroup(
            value=group_value,
            on_change=on_change,
            content=ft.Column(
                spacing=8,
                controls=[
                    ft.Radio(
                        value="birthday_known",
                        label="생년월일을 알아요",
                        label_style=ft.TextStyle(
                            color=ft.Colors.BLACK,
                            weight=ft.FontWeight.W_500,
                            size=14,
                        ),
                    ),
                    ft.Radio(
                        value="age_only",
                        label="대략적인 나이만 알고 있어요",
                        label_style=ft.TextStyle(
                            color=ft.Colors.BLACK,
                            weight=ft.FontWeight.W_500,
                            size=14,
                        ),
                    ),
                ],
            ),
        ),
    )


def long_box(
    text,
    bgcolor=ft.Colors.WHITE,
    text_color=ft.Colors.BLACK,
    border_color=ft.Colors.GREY_300,
    on_click=None,
    icon=None,
):
    controls = []

    if icon:
        controls.append(ft.Icon(icon, size=18, color=text_color))

    controls.append(
        ft.Text(
            text,
            size=14,
            weight=ft.FontWeight.W_500,
            color=text_color,
        )
    )

    return ft.Container(
        width=350,
        height=50,
        bgcolor=bgcolor,
        border=ft.Border.all(1, border_color),
        border_radius=10,
        padding=10,
        alignment=ft.Alignment(0, 0),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
            controls=controls,
        ),
    )


def dropdown_box2(label="성별/중성화", options=None):
    if options is None:
        options = [
            ft.dropdown.Option("남자"),
            ft.dropdown.Option("여자"),
            ft.dropdown.Option("남자(중성화)"),
            ft.dropdown.Option("여자(중성화)"),
        ]

    # ─────────────────────────────────────────────
    # ✅ 수정: 성별 Dropdown도 동일하게 바깥 Container 제거
    # ✅ 수정 이유:
    # - 모바일 웹에서 상자 잘림 원인이 같기 때문
    # ─────────────────────────────────────────────
    return ft.Dropdown(
        width=350,

        # ─────────────────────────────────────────────
        # ✅ 수정: 높이를 Dropdown 자신에게 직접 적용
        # ─────────────────────────────────────────────
        height=56,

        # ─────────────────────────────────────────────
        # ✅ 수정: label 대신 hint_text 사용
        # ✅ 수정 이유:
        # - label 구조가 위로 뜨면서 값과 겹쳐 보여
        #   상자가 잘려 보이는 핵심 원인이 되었음
        # ─────────────────────────────────────────────
        hint_text=label,

        # ─────────────────────────────────────────────
        # ✅ 수정: Dropdown 자신이 outline 테두리를 직접 그림
        # ─────────────────────────────────────────────
        border=ft.InputBorder.OUTLINE,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_300,
        border_radius=10,

        content_padding=ft.padding.symmetric(
            horizontal=14,
            vertical=14,
        ),
        text_size=14,

        # ─────────────────────────────────────────────
        # ✅ 수정: 선택된 값 / 힌트 스타일 지정
        # ✅ 수정 이유:
        # - 선택값은 BLACK 으로 진하게
        # - 힌트는 GREY_600 으로 유지
        # ─────────────────────────────────────────────
        text_style=ft.TextStyle(
            color=ft.Colors.BLACK,
            size=14,
            weight=ft.FontWeight.W_500,
        ),
        hint_style=ft.TextStyle(
            color=ft.Colors.GREY_600,
            size=14,
        ),

        # ─────────────────────────────────────────────
        # ✅ 수정: 필드 자체 색 강제 지정
        # ✅ 수정 이유:
        # - 모바일 웹에서 선택 텍스트와 화살표가 연하게 보이는 현상 완화
        # ─────────────────────────────────────────────
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        filled=False,

        options=options,
    )


def bottom_continue_button(on_click=None):
    return ft.Container(
        alignment=ft.Alignment(0, 0),
        content=long_box(
            "Continue",
            bgcolor=ft.Colors.YELLOW,
            text_color=ft.Colors.BLACK,
            on_click=on_click,
        ),
    )


# 🟦 수정: 기존 "텍스트필드 + 업로드 버튼" 구조를 없애고
# 🟦 수정: 하나의 클릭 가능한 박스로 합친 함수
# 🟦 수정 이유:
# 🟦 - 사용자가 프로필 이미지 영역 아무 데나 눌러도 파일 선택 가능
# 🟦 - UI가 더 깔끔해짐
# 🟦 - read_only TextField 따로 둘 필요가 없어짐
def profile_image_picker_box(text="프로필 이미지를 등록하세요", on_click=None):
    is_placeholder = text == "프로필 이미지를 등록하세요"

    return ft.Container(
        width=350,
        height=50,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=ft.padding.symmetric(horizontal=12),
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
                    ft.Icons.UPLOAD_FILE,
                    color=ft.Colors.GREY_700 if is_placeholder else ft.Colors.BLACK,
                ),
            ],
        ),
    )


def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.HIDDEN
    page.title = "For Dog"

    # ✅ 추가: 모바일에서도 라이트 테마 강제
    # ✅ 이유:
    # - 시스템 다크모드 영향을 받아 DatePicker가 검은 배경으로 뜨는 문제 방지
    page.theme_mode = ft.ThemeMode.LIGHT

    # ─────────────────────────────────────────────
    # ✅ 추가: 모바일 웹 Dropdown 글자색 테마 강제 지정
    # ✅ 추가 이유:
    # - 선택 목록 펼쳤을 때 글자가 너무 흐리게 보이는 문제 완화
    # - Dropdown 옵션/필드가 surface 계열 색 영향을 덜 받도록 설정
    # ─────────────────────────────────────────────
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLACK,
            on_primary=ft.Colors.WHITE,
            surface=ft.Colors.WHITE,
            on_surface=ft.Colors.BLACK,
            on_surface_variant=ft.Colors.BLACK,
        )
    )

    # ─────────────────────────────────────────────
    # ✅ 추가: 모바일 웹 Dropdown 글자색 테마 강제 지정
    # ✅ 추가 이유:
    # - 선택 목록 펼쳤을 때 글자가 너무 흐리게 보이는 문제 완화
    # - Dropdown 옵션/필드가 surface 계열 색 영향을 덜 받도록 설정
    # ─────────────────────────────────────────────
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLACK,
            on_primary=ft.Colors.WHITE,
            surface=ft.Colors.WHITE,
            on_surface=ft.Colors.BLACK,
            on_surface_variant=ft.Colors.BLACK,
        )
    )

    # ✅ DB 연결
    conn = None

    # ✅ 추가: 품종 조회/검색 에러 메시지 상태값
    # ✅ 설명:
    # - DB 연결 실패와 "검색 결과 없음"을 구분해서 화면에 보여주기 위한 변수
    breed_error_text = None

    # 🟩 선택된 품종 상태값
    # 🟩 설명:
    # - selected_breed_id: DB에 저장할 품종 번호
    # - selected_breed_text: 화면에 보여줄 품종 이름
    selected_breed_id = None
    selected_breed_text = "반려동물 품종 선택"

    # 🟦 수정: 프로필 이미지 파일명 상태값만 따로 저장
    # 🟦 기존 TextField 변수는 제거
    selected_profile_image_text = "프로필 이미지를 등록하세요"

    # ─────────────────────────────────────────────
    # ✅ 추가: 이름 입력칸 상태 유지용 컨트롤
    # ✅ 추가 설명:
    # - rebuild_body() 안에서 input_box()를 직접 다시 만들면
    #   버튼 클릭 시마다 새로운 TextField가 생성됨
    # - 그래서 사용자가 입력한 이름 값이 초기화됨
    # - 여기서 한 번만 만들어 두고 rebuild_body()에서는
    #   이 컨트롤을 계속 재사용해야 입력값이 유지됨
    # ─────────────────────────────────────────────
    pet_name_field = input_box(hint_text="반려동물 이름")

    # ─────────────────────────────────────────────
    # ✅ 추가: 성별 선택 상태 유지용 컨트롤
    # ✅ 추가 설명:
    # - rebuild_body() 안에서 dropdown_box2()를 매번 새로 만들면
    #   사용자가 고른 성별/중성화 값이 다시 초기화됨
    # - 그래서 성별 Dropdown도 main()에서 한 번만 생성해두고
    #   rebuild_body()에서는 계속 재사용해야 선택값이 유지됨
    # ─────────────────────────────────────────────
    gender_dropdown = dropdown_box2()

    # 🟦 수정: 프로필 이미지 선택용 FilePicker
    profile_image_picker = ft.FilePicker()
    page.services.append(profile_image_picker)

    # 🟦 수정: 프로필 이미지 선택 함수
    # 🟦 박스 전체를 누르면 이 함수가 실행되도록 변경
    async def pick_profile_image(e):
        nonlocal selected_profile_image_text

        files = await profile_image_picker.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE,
        )

        if files:
            selected_profile_image_text = files[0].name
        else:
            selected_profile_image_text = "프로필 이미지를 등록하세요"

        rebuild_body()

    # 🟧 추가: 생년월일 입력 방식 상태 저장
    birth_input_mode = None

    # 🟧 추가: 선택된 생년월일 텍스트 상태 저장
    selected_birth_text = "생년월일 선택"

    # 🟩 품종 목록 영역
    # 🟩 설명:
    # - spacing=6 으로 각 품종 줄 사이를 조금 띄워서
    #   선택된 줄의 배경색이 더 잘 보이게 함
    breed_list_column = ft.Column(
        spacing=6,
        scroll=ft.ScrollMode.AUTO,
        height=300,
    )

    # 🟩 품종 검색창
    breed_search_field = input_box(hint_text="품종 검색")

    # ✅ 추가: 품종 기능이 필요할 때만 DB 연결
    # ─────────────────────────────────────────────
    # 🟨 DB 흐름 2
    # 🟨 설명:
    # - 품종 조회/검색이 필요해졌을 때 가장 먼저 실행되는 연결 확인 단계
    # - conn 이 이미 살아 있으면 기존 연결을 재사용
    # - conn 이 없거나 닫혀 있으면 get_connection() 을 호출해서
    #   새로 DB 서버 연결 시도
    # - 즉, "매번 무조건 새 연결"이 아니라 "있으면 재사용, 없으면 재연결"
    # ─────────────────────────────────────────────
    def ensure_db_connection():
        nonlocal conn, breed_error_text  # ✅ 수정: 에러 상태값도 같이 사용

        if conn is not None and getattr(conn, "closed", 1) == 0:
            breed_error_text = None  # ✅ 추가: 연결 정상일 때 에러 상태 초기화
            return True

        try:
            # ─────────────────────────────────────────────
            # 🟨 DB 흐름 3
            # 🟨 설명:
            # - 실제로 get_connection() 을 호출해서
            #   DB 서버 접속을 시도하는 부분
            # - 여기서 아이디/비밀번호/호스트/포트가 틀리거나
            #   서버가 꺼져 있으면 except 로 이동함
            # ─────────────────────────────────────────────
            conn = get_connection()
            breed_error_text = None  # ✅ 추가: 재연결 성공 시 에러 상태 초기화
            return True
        except Exception as err:
            # ✅ 수정: 스낵바만 띄우지 말고, 화면용 에러 메시지도 저장
            breed_error_text = f"DB 서버 연결 실패: {err}"

            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"DB 연결 실패: {err}"),
                open=True,
            )
            page.update()
            return False

    # 🟩 DB에서 전체 품종 가져오기
    # ─────────────────────────────────────────────
    # 🟨 DB 흐름 4
    # 🟨 설명:
    # - 검색어 없이 품종 목록 전체를 가져오는 단계
    # - 먼저 ensure_db_connection() 으로 연결 확인
    # - 연결 성공 시 cursor 를 만들고 SQL 실행
    # - Breed.breed_list_query 가 실제 전체 조회 SQL
    # ─────────────────────────────────────────────
    def load_breed_list():
        nonlocal breed_error_text  # ✅ 추가

        if not ensure_db_connection():
            return None  # ✅ 수정: 연결 실패는 [] 말고 None 으로 구분

        try:
            # ─────────────────────────────────────────────
            # 🟨 DB 흐름 5
            # 🟨 설명:
            # - conn.cursor() : DB 작업용 커서 생성
            # - cursor.execute(...) : SQL 실행
            # - cursor.fetchall() : 조회 결과 전부 가져오기
            # - 즉, "DB 서버에 요청 보내고 결과 받는" 실제 조회 구간
            # ─────────────────────────────────────────────
            cursor = conn.cursor()
            cursor.execute(Breed.breed_list_query)
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
            breed_error_text = None  # ✅ 추가: 조회 성공 시 에러 상태 초기화
            return rows
        except Exception as err:
            conn.rollback()
            breed_error_text = f"품종 목록 조회 실패: {err}"  # ✅ 추가
            print(f"breed_list_query error: {err}")
            return None  # ✅ 수정

    # 🟩 DB에서 검색된 품종 가져오기
    # ─────────────────────────────────────────────
    # 🟨 DB 흐름 6
    # 🟨 설명:
    # - 사용자가 검색창에 입력한 keyword 를 가지고
    #   DB에서 조건 검색하는 단계
    # - 구조는 load_breed_list() 와 거의 같고
    #   SQL만 Breed.breed_search_query 로 바뀜
    # ─────────────────────────────────────────────
    def search_breed_list(keyword):
        nonlocal breed_error_text  # ✅ 추가

        if not ensure_db_connection():
            return None  # ✅ 수정: 연결 실패는 None 으로 구분

        try:
            # ─────────────────────────────────────────────
            # 🟨 DB 흐름 7
            # 🟨 설명:
            # - 검색 SQL 실행 구간
            # - (f"%{keyword}%",) 형태로 검색어를 전달해서
            #   보통 LIKE 검색에 사용됨
            # - 여기서도 execute → fetchall 순서로 결과를 받음
            # ─────────────────────────────────────────────
            cursor = conn.cursor()
            cursor.execute(Breed.breed_search_query, (f"%{keyword}%",))
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
            breed_error_text = None  # ✅ 추가: 조회 성공 시 에러 상태 초기화
            return rows
        except Exception as err:
            conn.rollback()
            breed_error_text = f"품종 검색 실패: {err}"  # ✅ 추가
            print(f"breed_search_query error: {err}")
            return None  # ✅ 수정

    # 🟩 품종 선택 시 실행
    def select_breed(breed_id, breed_name):
        nonlocal selected_breed_id, selected_breed_text
        selected_breed_id = breed_id
        selected_breed_text = breed_name

        update_breed_list(breed_search_field.value if breed_search_field.value else "")
        rebuild_body()

        breed_bottom_sheet.open = False
        page.update()

    # 🟩 목록 한 줄
    def breed_item(breed_id, breed_name):
        is_checked = selected_breed_id == breed_id

        return ft.Container(
            padding=ft.padding.symmetric(vertical=14, horizontal=10),
            border_radius=10,
            bgcolor=ft.Colors.GREY_100 if is_checked else ft.Colors.WHITE,
            on_click=lambda e, b_id=breed_id, b_name=breed_name: select_breed(b_id, b_name),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        breed_name,
                        size=14,
                        color=ft.Colors.BLACK,
                        weight=ft.FontWeight.W_500,
                    ),
                    ft.Icon(
                        ft.Icons.CHECK,
                        color=ft.Colors.BLACK if is_checked else ft.Colors.TRANSPARENT,
                        size=18,
                    ),
                ],
            ),
        )

    # 🟩 품종 목록 다시 그리기
    # ─────────────────────────────────────────────
    # 🟨 DB 흐름 8
    # 🟨 설명:
    # - 이 함수가 DB 조회의 분기점
    # - keyword 가 있으면 search_breed_list()
    # - keyword 가 없으면 load_breed_list()
    # - 즉, "전체조회냐 검색이냐"를 결정하는 중간 관제실 역할
    # ─────────────────────────────────────────────
    def update_breed_list(keyword=""):
        nonlocal breed_error_text  # ✅ 추가

        if keyword.strip():
            breed_rows = search_breed_list(keyword.strip())
        else:
            breed_rows = load_breed_list()

        # ✅ 추가: DB 연결 실패 / 조회 실패일 때
        # ─────────────────────────────────────────────
        # 🟨 DB 흐름 9
        # 🟨 설명:
        # - DB에서 받은 결과(breed_rows)를 화면에 반영하는 단계
        # - None 이면: 연결 실패/조회 실패
        # - 값이 있으면: 목록 표시
        # - 빈 리스트면: 검색 결과 없음
        # - 즉, DB 결과를 사용자가 실제로 보게 되는 마지막 단계
        # ─────────────────────────────────────────────
        if breed_rows is None:
            breed_list_column.controls = [
                ft.Container(
                    padding=ft.padding.symmetric(vertical=20),
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        breed_error_text if breed_error_text else "DB 연결 오류가 발생했습니다.",
                        size=14,
                        color=ft.Colors.RED,  # ✅ 추가: 에러는 빨간색
                        text_align=ft.TextAlign.CENTER,  # ✅ 추가
                    ),
                )
            ]

        elif breed_rows:
            breed_list_column.controls = [
                breed_item(row[0], row[1]) for row in breed_rows
            ]
        else:
            breed_list_column.controls = [
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

    # 🟩 검색창 입력 시 DB 검색
    # ─────────────────────────────────────────────
    # 🟨 DB 흐름 10
    # 🟨 설명:
    # - 사용자가 품종 검색창에 글자를 입력하면
    #   on_change 이벤트로 update_breed_list() 가 호출됨
    # - 즉, 사용자 입력이 실제 DB 검색으로 이어지는 시작점
    # ─────────────────────────────────────────────
    def on_breed_search_change(e):
        update_breed_list(e.control.value)

    breed_search_field.on_change = on_breed_search_change

    # 🟩 바텀시트
    breed_bottom_sheet = ft.BottomSheet(
        open=False,
        barrier_color=ft.Colors.TRANSPARENT,
        size_constraints=ft.BoxConstraints(
            max_height=700,
            min_height=430,
        ),
        content=ft.Container(
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.border_radius.only(
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
                    ft.Text("품종 검색", size=25, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    breed_search_field,
                    ft.Container(height=12),
                    breed_list_column,
                    ft.Container(height=10),
                ],
            ),
        ),
    )
    page.overlay.append(breed_bottom_sheet)

    # 🟩 바텀시트 열기
    # ─────────────────────────────────────────────
    # 🟨 DB 흐름 11
    # 🟨 설명:
    # - 사용자가 "품종 선택" 박스를 누르면 이 함수가 실행됨
    # - 여기서 update_breed_list("") 를 호출하므로
    #   바텀시트를 여는 순간 전체 품종 목록 DB 조회가 시작됨
    # - 즉, 사용자의 클릭이 DB 조회로 이어지는 대표적인 시작점
    # ─────────────────────────────────────────────
    def open_breed_bottom_sheet(e):
        breed_search_field.value = ""
        update_breed_list("")
        breed_bottom_sheet.open = True
        page.update()

    # 🟧 추가: DatePicker 생성
    def on_date_change(e):
        nonlocal selected_birth_text
        if e.control.value:
            selected_birth_text = e.control.value.strftime("%Y-%m-%d")
            rebuild_body()

    date_picker = ft.DatePicker(
        first_date=datetime.datetime(2000, 1, 1),
        last_date=datetime.datetime.now(),
        on_change=on_date_change,
    )
    page.overlay.append(date_picker)

    # 🟧 추가: DatePicker 열기 함수
    def open_date_picker(e):
        date_picker.open = True
        page.update()

    # 🟧 추가: 라디오 선택 변경 함수
    def change_birth_mode(e):
        nonlocal birth_input_mode
        birth_input_mode = e.control.value
        rebuild_body()

    # 🟧 추가: 본문 전용 스크롤 컬럼
    body_content = ft.Column(
        width=350,
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        scroll=ft.ScrollMode.AUTO,
    )

    # 🟧 추가: 생년월일 섹션 동적 생성
    def build_birth_controls():
        controls = [
            ft.Text(
                "생년월일",
                weight=ft.FontWeight.W_500,
                color=ft.Colors.BLACK,
            ),
            birth_mode_box(
                group_value=birth_input_mode,
                on_change=change_birth_mode,
            ),
        ]

        if birth_input_mode == "birthday_known":
            controls.append(
                datepicker_box(
                    text=selected_birth_text,
                    on_click=open_date_picker,
                )
            )
        elif birth_input_mode == "age_only":
            controls.append(
                dropdown_box1(
                    label="대략적인 나이 선택",
                    options=[
                        ft.dropdown.Option("1살 미만"),
                        ft.dropdown.Option("1살"),
                        ft.dropdown.Option("2살"),
                        ft.dropdown.Option("3살"),
                        ft.dropdown.Option("4살"),
                        ft.dropdown.Option("5살 이상"),
                    ],
                )
            )

        return controls

    # 🟩 continue 눌렀을 때 확인용
    def on_continue(e):
        print("선택한 품종 ID:", selected_breed_id)
        print("선택한 품종 이름:", selected_breed_text)
        print("선택한 프로필 이미지:", selected_profile_image_text)

        # ─────────────────────────────────────────────
        # ✅ 추가: 이름 입력값 확인용 출력
        # ✅ 추가 설명:
        # - pet_name_field.value 로 현재 입력된 반려동물 이름 확인 가능
        # - 이후 DB 저장할 때도 이 값을 그대로 사용하면 됨
        # ─────────────────────────────────────────────
        print("입력한 반려동물 이름:", pet_name_field.value)

        # ─────────────────────────────────────────────
        # ✅ 추가: 성별 선택값 확인용 출력
        # ✅ 추가 설명:
        # - dropdown_box2()가 Dropdown 을 직접 반환하므로
        #   value 는 gender_dropdown.value 에 들어 있음
        # ─────────────────────────────────────────────
        print("선택한 성별:", gender_dropdown.value)

    # 🟧 추가: 본문 전체 다시 그리기
    def rebuild_body():
        body_content.controls = [
            ft.Container(
                margin=ft.margin.only(top=50),
                content=about_dog(),
            ),
            ft.Text("이름", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),

            # ─────────────────────────────────────────────
            # ✅ 수정: input_box()를 여기서 새로 만들지 않고
            # ✅ 수정: main()에서 한 번 생성한 pet_name_field 재사용
            # ✅ 수정 이유:
            # - rebuild_body() 호출 시 입력값 초기화되는 문제 방지
            # - 사용자가 입력한 이름을 그대로 유지
            # ─────────────────────────────────────────────
            pet_name_field,

            ft.Text("프로필 이미지", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),

            # 🟦 수정: 기존 Row(텍스트필드 + 업로드 버튼) 삭제
            # 🟦 수정: 클릭 가능한 단일 박스로 교체
            profile_image_picker_box(
                text=selected_profile_image_text,
                on_click=pick_profile_image,
            ),

            ft.Text("품종", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),

            breed_select_box(
                text=selected_breed_text,
                on_click=open_breed_bottom_sheet,
            ),

            *build_birth_controls(),

            ft.Text("성별", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),

            # ─────────────────────────────────────────────
            # ✅ 수정: dropdown_box2()를 여기서 새로 만들지 않고
            # ✅ 수정: main()에서 한 번 생성한 gender_dropdown 재사용
            # ✅ 수정 이유:
            # - rebuild_body() 호출 시 성별 선택값 초기화되는 문제 방지
            # - 사용자가 고른 성별/중성화 값을 그대로 유지
            # ─────────────────────────────────────────────
            gender_dropdown,

            ft.Text("무게", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            weight_input_box("4.5"),

            ft.Container(height=20),
        ]
        page.update()

    # 🟧 추가: 하단 고정 버튼 영역
    fixed_button = ft.Container(
        width=float("inf"),
        alignment=ft.Alignment(0, 0),
        padding=ft.padding.only(top=10, bottom=20),
        content=ft.Container(
            width=350,
            alignment=ft.Alignment(0, 0),
            content=bottom_continue_button(on_click=on_continue),
        ),
    )

    body = ft.Container(
        padding=ft.padding.only(top=0),
        expand=True,
        content=ft.Column(
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    expand=True,
                    content=body_content,
                ),
                fixed_button,
            ],
        ),
    )

    rebuild_body()
    page.add(body)


if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.app(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )