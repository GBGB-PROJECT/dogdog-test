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
        user="아이디",
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

    # ✅ DB 연결
    try:
        conn = get_connection()
    except Exception as err:
        page.add(ft.Text(f"DB 연결 실패: {err}", color=ft.Colors.RED))
        return

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
        # - dropdown_box2()가 Container를 반환하므로
        #   실제 Dropdown 값은 gender_dropdown.content.value 에 들어 있음
        # - 이후 DB 저장 시 이 값을 그대로 사용하면 됨
        # ─────────────────────────────────────────────
        print("선택한 성별:", gender_dropdown.content.value)

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