import flet as ft
import datetime
import psycopg2

from views.onboarding.full_query import Breed

from components.common.common_components import about_dog
from components.layout.common_layout import build_screen
from components.navigation import go_next, go_back


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


def dropdown_box1(label="품종 선택", options=None, width=350):
    if options is None:
        options = [
            ft.dropdown.Option("사과"),
            ft.dropdown.Option("바나나"),
            ft.dropdown.Option("포도"),
        ]

    return ft.Dropdown(
        width=width,
        height=56,
        hint_text=label,
        border=ft.InputBorder.OUTLINE,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_300,
        border_radius=10,
        content_padding=ft.padding.only(left=14, right=14, top=14, bottom=14),
        text_size=14,
        text_style=ft.TextStyle(
            color=ft.Colors.BLACK,
            size=14,
            weight=ft.FontWeight.W_500,
        ),
        hint_style=ft.TextStyle(
            color=ft.Colors.GREY_600,
            size=14,
        ),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        filled=False,
        options=options,
    )


def dropdown_box2(label="성별/중성화", options=None):
    if options is None:
        options = [
            ft.dropdown.Option("남자"),
            ft.dropdown.Option("여자"),
            ft.dropdown.Option("남자(중성화)"),
            ft.dropdown.Option("여자(중성화)"),
        ]

    return ft.Dropdown(
        width=350,
        height=56,
        hint_text=label,
        border=ft.InputBorder.OUTLINE,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_300,
        border_radius=10,
        content_padding=ft.padding.symmetric(horizontal=14, vertical=14),
        text_size=14,
        text_style=ft.TextStyle(
            color=ft.Colors.BLACK,
            size=14,
            weight=ft.FontWeight.W_500,
        ),
        hint_style=ft.TextStyle(
            color=ft.Colors.GREY_600,
            size=14,
        ),
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
                    color=ft.Colors.BLACK if text != "생년월일 선택" else ft.Colors.GREY_600,
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


def build_view(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLACK,
            on_primary=ft.Colors.WHITE,
            surface=ft.Colors.WHITE,
            on_surface=ft.Colors.BLACK,
            on_surface_variant=ft.Colors.BLACK,
        )
    )

    conn = None
    breed_error_text = None

    selected_breed_id = None
    selected_breed_text = "반려동물 품종 선택"
    selected_profile_image_text = "프로필 이미지를 등록하세요"

    pet_name_field = input_box(hint_text="반려동물 이름")
    gender_dropdown = dropdown_box2()
    age_year_dropdown = dropdown_box1(
        label="년 선택",
        width=160,
        options=[ft.dropdown.Option(f"{year}년") for year in range(0, 31)],
    )
    age_month_dropdown = dropdown_box1(
        label="개월 선택",
        width=160,
        options=[ft.dropdown.Option(f"{month}개월") for month in range(0, 12)],
    )
    weight_field = weight_input_box("4.5")

    # ✅ main.py에서 미리 등록한 FilePicker 재사용
    profile_image_picker = page.profile_image_picker

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

    birth_input_mode = None
    selected_birth_text = "생년월일 선택"

    breed_list_column = ft.Column(
        spacing=6,
        scroll=ft.ScrollMode.AUTO,
        height=300,
    )

    breed_search_field = input_box(hint_text="품종 검색")

    def ensure_db_connection():
        nonlocal conn, breed_error_text

        if conn is not None and getattr(conn, "closed", 1) == 0:
            breed_error_text = None
            return True

        try:
            conn = get_connection()
            breed_error_text = None
            return True
        except Exception as err:
            breed_error_text = f"DB 서버 연결 실패: {err}"
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"DB 연결 실패: {err}"),
                open=True,
            )
            page.update()
            return False

    def load_breed_list():
        nonlocal breed_error_text

        if not ensure_db_connection():
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(Breed.breed_list_query)
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
            breed_error_text = None
            return rows
        except Exception as err:
            conn.rollback()
            breed_error_text = f"품종 목록 조회 실패: {err}"
            print(f"breed_list_query error: {err}")
            return None

    def search_breed_list(keyword):
        nonlocal breed_error_text

        if not ensure_db_connection():
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(Breed.breed_search_query, (f"%{keyword}%",))
            rows = cursor.fetchall()
            conn.commit()
            cursor.close()
            breed_error_text = None
            return rows
        except Exception as err:
            conn.rollback()
            breed_error_text = f"품종 검색 실패: {err}"
            print(f"breed_search_query error: {err}")
            return None

    def select_breed(breed_id, breed_name):
        nonlocal selected_breed_id, selected_breed_text
        selected_breed_id = breed_id
        selected_breed_text = breed_name

        update_breed_list(breed_search_field.value if breed_search_field.value else "")
        rebuild_body()

        breed_bottom_sheet.open = False
        page.update()

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

    def update_breed_list(keyword=""):
        nonlocal breed_error_text

        if keyword.strip():
            breed_rows = search_breed_list(keyword.strip())
        else:
            breed_rows = load_breed_list()

        if breed_rows is None:
            breed_list_column.controls = [
                ft.Container(
                    padding=ft.padding.symmetric(vertical=20),
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        breed_error_text if breed_error_text else "DB 연결 오류가 발생했습니다.",
                        size=14,
                        color=ft.Colors.RED,
                        text_align=ft.TextAlign.CENTER,
                    ),
                )
            ]
        elif breed_rows:
            breed_list_column.controls = [breed_item(row[0], row[1]) for row in breed_rows]
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

    def on_breed_search_change(e):
        update_breed_list(e.control.value)

    breed_search_field.on_change = on_breed_search_change

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
                    ft.Text(
                        "품종 검색",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                    ),
                    breed_search_field,
                    ft.Container(height=12),
                    breed_list_column,
                    ft.Container(height=10),
                ],
            ),
        ),
    )
    if breed_bottom_sheet not in page.overlay:
        page.overlay.append(breed_bottom_sheet)

    def open_breed_bottom_sheet(e):
        breed_search_field.value = ""
        update_breed_list("")
        breed_bottom_sheet.open = True
        page.update()

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
    if date_picker not in page.overlay:
        page.overlay.append(date_picker)

    def open_date_picker(e):
        date_picker.open = True
        page.update()

    def change_birth_mode(e):
        nonlocal birth_input_mode
        birth_input_mode = e.control.value
        rebuild_body()

    body_content = ft.Column(
        width=350,
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        scroll=ft.ScrollMode.AUTO,
    )

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
                ft.Row(
                    width=350,
                    spacing=14,
                    controls=[
                        age_year_dropdown,
                        age_month_dropdown,
                    ],
                )
            )

        return controls

    def on_continue(e):
        print("선택한 품종 ID:", selected_breed_id)
        print("선택한 품종 이름:", selected_breed_text)
        print("선택한 프로필 이미지:", selected_profile_image_text)
        print("입력한 반려동물 이름:", pet_name_field.value)
        print("선택한 성별:", gender_dropdown.value)
        print("선택한 나이(년):", age_year_dropdown.value)
        print("선택한 나이(개월):", age_month_dropdown.value)

        go_next(page)

    def rebuild_body():
        body_content.controls = [
            ft.Container(
                margin=ft.margin.only(top=50),
                content=about_dog(),
            ),
            ft.Text("이름", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            pet_name_field,
            ft.Text("프로필 이미지", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
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
            gender_dropdown,
            ft.Text("무게", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            weight_field,
            ft.Container(height=20),
        ]
        page.update()

    rebuild_body()

    return build_screen(
        page=page,
        body_controls=[body_content],
        on_back=lambda e: go_back(page),
        on_continue=on_continue,
        show_back=True,
        fixed_bottom=True,
    )