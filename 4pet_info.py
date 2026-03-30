import flet as ft
import datetime


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


# ✅ 수정: 텍스트가 너무 아래에 보이던 문제 해결
# ✅ 이유:
# - 기존에는 Container의 padding=10 때문에 TextField 전체가 안쪽으로 밀렸음
# - 그래서 글자가 시각적으로 아래에 깔린 것처럼 보였음
# ✅ 해결:
# - Container padding 제거
# - TextField 내부 content_padding으로 세로 정렬을 직접 조정
def input_box(hint_text="", width=350):
    return ft.TextField(
        width=width,
        height=50,
        hint_text=hint_text,
        border=ft.InputBorder.OUTLINE,  # ✅ 수정
        border_color=ft.Colors.GREY_300,  # ✅ 수정
        focused_border_color=ft.Colors.GREY_300,  # ✅ 수정
        border_radius=10,  # ✅ 수정
        content_padding=ft.padding.only(
            left=14, right=14, top=0, bottom=0
        ),  # ✅ 수정: 왼쪽 시작점 맞춤
        text_size=14,
        text_align=ft.TextAlign.LEFT,  # ✅ 수정: 왼쪽 정렬 고정
        cursor_height=18,
        filled=False,
    )


# ✅ 수정: Dropdown도 input_box와 동일한 높이감으로 맞춤
# ✅ 이유:
# - Dropdown도 Container padding 때문에 안쪽 내용이 아래로 깔려 보일 수 있음
# - input_box와 동일한 기준으로 맞춰야 전체 UI가 정돈돼 보임
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
        padding=0,  # ✅ 수정: 바깥 패딩 제거
        alignment=ft.Alignment(0, 0),
        content=ft.Dropdown(
            label=label,
            width=350,
            border=ft.InputBorder.NONE,
            content_padding=ft.padding.only(
                left=14, right=14, top=12, bottom=12
            ),  # ✅ 수정
            text_size=14,
            options=options,
        ),
    )


# ✅ 수정: DatePicker 박스는 TextField가 아니라 Row 구조이므로
# ✅ 상하 패딩을 과하게 주지 않고 좌우 중심으로만 정리
def datepicker_box(text="생년월일 선택", on_click=None):
    return ft.Container(
        width=350,
        height=50,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=ft.padding.symmetric(horizontal=12),  # ✅ 수정: 좌우 여백만 줌
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


# 🟧 추가: 생년월일 입력 방식을 고르는 라디오 박스
# 🟧 기능: "생년월일을 알아요" / "대략적인 나이만 알고 있어요" 중 하나 선택
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


# ✅ 수정: dropdown_box1과 같은 기준으로 통일
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
        padding=0,  # ✅ 수정: 바깥 패딩 제거
        alignment=ft.Alignment(0, 0),
        content=ft.Dropdown(
            label=label,
            width=350,  # ✅ 수정: 내부 폭 통일
            border=ft.InputBorder.NONE,
            content_padding=ft.padding.symmetric(
                horizontal=12,
                vertical=12,
            ),  # ✅ 수정: 내부 위치 통일
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

            # ✅ 참고:
            # 여기 label="츄츄"는 Dropdown의 떠 있는 라벨처럼 보일 수 있음
            # placeholder 느낌으로 쓰고 싶으면 value/힌트 방식으로 따로 바꾸는 게 더 자연스러움
            dropdown_box1(label="반려동물 품종"),

            *build_birth_controls(),

            ft.Text("성별", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            dropdown_box2(),
            ft.Text("무게", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            input_box(hint_text="4.5kg"),

            # 🟧 추가: 하단 고정 버튼에 내용이 가리지 않도록 아래 여백 확보
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
            content=bottom_continue_button(),
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
                # 🟧 위쪽: 스크롤되는 본문
                ft.Container(
                    expand=True,
                    content=body_content,
                ),

                # 🟧 아래쪽: 고정 버튼
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