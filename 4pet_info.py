import flet as ft
import datetime

# ✅ PostgreSQL 예시
# 네 DB가 MySQL이면 아래 psycopg2 대신 mysql.connector로 바꿔야 함
import psycopg2

from full_query import Breed


# ✅ DB 연결 함수
# 여기는 네 환경에 맞게 수정해야 함
def get_connection():
    return psycopg2.connect(
        host="192.168.0.43",
        port=9934,
        dbname="dogdog",
        user="유저 아이디",
        password="비밀번호",
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
        text_align=ft.TextAlign.LEFT,
        cursor_height=18,
        filled=False,
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

    return ft.Container(
        width=350,
        height=50,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=0,
        alignment=ft.Alignment(0, 0),
        content=ft.Dropdown(
            label=label,
            width=350,
            border=ft.InputBorder.NONE,
            content_padding=ft.padding.only(
                left=14, right=14, top=12, bottom=12
            ),
            text_size=14,
            options=options,
        ),
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

    return ft.Container(
        width=350,
        height=50,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=0,
        alignment=ft.Alignment(0, 0),
        content=ft.Dropdown(
            label=label,
            width=350,
            border=ft.InputBorder.NONE,
            content_padding=ft.padding.symmetric(
                horizontal=12,
                vertical=12,
            ),
            text_size=14,
            options=options,
        ),
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


def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.HIDDEN
    page.title = "For Dog"

    # ✅ DB 연결
    try:
        conn = get_connection()
    except Exception as err:
        page.add(ft.Text(f"DB 연결 실패: {err}", color=ft.Colors.RED))
        return

    # 🟩 선택된 품종 상태값
    selected_breed_id = None
    selected_breed_text = "반려동물 품종 선택"

    # 🟧 추가: 프로필 이미지 파일명 표시용 TextField
    profile_image_field = input_box(
        hint_text="프로필 이미지를 등록하세요",
        width=282,
    )
    profile_image_field.read_only = True

    # 🟧 추가: 프로필 이미지 선택용 FilePicker
    profile_image_picker = ft.FilePicker()
    page.services.append(profile_image_picker)

    # 🟧 추가: 프로필 이미지 선택 함수
    async def pick_profile_image(e):
        files = await profile_image_picker.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE,
        )

        if files:
            profile_image_field.value = ", ".join([f.name for f in files])
        else:
            profile_image_field.value = ""

        page.update()

    # 🟧 추가: 생년월일 입력 방식 상태 저장
    birth_input_mode = None

    # 🟧 추가: 선택된 생년월일 텍스트 상태 저장
    selected_birth_text = "생년월일 선택"

    # 🟩 품종 목록 영역
    breed_list_column = ft.Column(
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        height=300,
    )

    # 🟩 품종 검색창
    breed_search_field = input_box(hint_text="품종 검색")

    # 🟩 DB에서 전체 품종 가져오기
    def load_breed_list():
        try:
            cursor = conn.cursor()
            cursor.execute(Breed.breed_list_query)
            rows = cursor.fetchall()
            conn.commit()
            return rows
        except Exception as err:
            conn.rollback()
            print(f"breed_list_query error: {err}")
            return []

    # 🟩 DB에서 검색된 품종 가져오기
    def search_breed_list(keyword):
        try:
            cursor = conn.cursor()
            cursor.execute(Breed.breed_search_query, (f"%{keyword}%",))
            rows = cursor.fetchall()
            conn.commit()
            return rows
        except Exception as err:
            conn.rollback()
            print(f"breed_search_query error: {err}")
            return []

    # 🟩 품종 선택 시 실행
    def select_breed(breed_id, breed_name):
        nonlocal selected_breed_id, selected_breed_text
        selected_breed_id = breed_id
        selected_breed_text = breed_name
        breed_bottom_sheet.open = False
        rebuild_body()
        page.update()

    # 🟩 목록 한 줄
    def breed_item(breed_id, breed_name):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=14, horizontal=4),
            border=ft.border.only(bottom=ft.BorderSide(1, ft.Colors.GREY_200)),
            on_click=lambda e, b_id=breed_id, b_name=breed_name: select_breed(b_id, b_name),
            content=ft.Text(
                breed_name,
                size=14,
                color=ft.Colors.BLACK,
                weight=ft.FontWeight.W_500,
            ),
        )

    # 🟩 품종 목록 다시 그리기
    def update_breed_list(keyword=""):
        if keyword.strip():
            breed_rows = search_breed_list(keyword.strip())
        else:
            breed_rows = load_breed_list()

        if breed_rows:
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
                    ft.Text("품종 검색", size=25, weight=ft.FontWeight.BOLD),
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

    # 🟧 추가: 본문 전체 다시 그리기
    def rebuild_body():
        body_content.controls = [
            ft.Container(
                margin=ft.margin.only(top=50),
                content=about_dog(),
            ),
            ft.Text("이름", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            input_box(hint_text="반려동물 이름"),
            ft.Text("프로필 이미지", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            ft.Row(
                spacing=8,
                controls=[
                    profile_image_field,
                    ft.Container(
                        width=60,
                        height=50,
                        border=ft.Border.all(1, ft.Colors.GREY_300),
                        border_radius=10,
                        alignment=ft.Alignment(0, 0),
                        on_click=pick_profile_image,
                        content=ft.Icon(
                            ft.Icons.UPLOAD_FILE,
                            color=ft.Colors.BLACK,
                        ),
                    ),
                ],
            ),
            ft.Text("품종", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),

            # 🟩 여기만 기존 dropdown_box1 대신 교체
            breed_select_box(
                text=selected_breed_text,
                on_click=open_breed_bottom_sheet,
            ),

            *build_birth_controls(),

            ft.Text("성별", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            dropdown_box2(),
            ft.Text("무게", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            input_box(hint_text="4.5kg"),

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