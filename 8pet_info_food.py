import flet as ft


def about_dog():
    return ft.Column(
        spacing=0,
        controls=[
            ft.Text("About your Dog", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=30),
            ft.Text("반려동물의 기본 정보를 입력하세요", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=15),
        ],
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


def input_box(label=None, hint_text=None):
    return ft.TextField(
        width=350,
        height=50,
        border_radius=10,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_400,
        hint_text=hint_text,
        label=label,  # 선택적으로 라벨도 넣을 수 있음
    )


def bottom_continue_button(on_click=None):
    return ft.Container(
        alignment=ft.Alignment(0, 1),
        padding=ft.padding.only(bottom=20),
        content=long_box(
            "Continue",
            bgcolor=ft.Colors.YELLOW,
            text_color=ft.Colors.BLACK,
            on_click=on_click,
        ),
    )


# 🟦 추가: 기존 input_box("현재 급여 중인 사료를 적어주세요") 를
# 🟦 단순 입력칸이 아니라 "클릭하면 바텀시트가 열리는 선택 박스"로 바꾸기 위한 함수
# 🟦 추가 이유:
# 🟦 - 일반 TextField는 클릭 시 키보드 포커스를 먼저 잡아서
# 🟦   바텀시트 열기용 UI로 쓰기 애매함
# 🟦 - 드롭다운 선택창처럼 "누르면 열리는 박스" 구조가 더 안정적임
def food_select_box(text="현재 급여 중인 사료를 적어주세요", on_click=None):
    is_placeholder = text == "현재 급여 중인 사료를 적어주세요"

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
                    ft.Icons.SEARCH,
                    color=ft.Colors.GREY_700,
                ),
            ],
        ),
    )


def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.title = "Pet info food"

    # 🟩 추가: 현재 선택된 사료 이름 상태값
    # 🟩 설명:
    # - 바텀시트에서 사료를 선택하면 이 텍스트가 바뀜
    selected_food_text = "현재 급여 중인 사료를 적어주세요"

    # 🟩 추가: 예시 사료 목록
    # 🟩 설명:
    # - 지금은 검색 기능 동작 확인용으로 리스트를 직접 넣음
    # - 나중에 DB 연결할 거면 이 부분만 쿼리 결과로 바꾸면 됨
    food_items = [
        "하림 가맛시",
        "하림 더리얼",
        "하림 밥이보약",
        "하림 가맛시",
        "하림 더리얼",
        "하림 밥이보약",
        "하림 가맛시",
        "하림 더리얼",
        "하림 밥이보약",
        "하림 가맛시",
        "하림 더리얼",
        "하림 밥이보약",
    ]

    # 🟩 추가: 검색 결과가 들어갈 리스트 영역
    food_list_column = ft.Column(
        spacing=6,
        scroll=ft.ScrollMode.AUTO,
        height=300,
    )

    # 🟩 추가: 바텀시트 안 검색창
    food_search_field = input_box("Search")

    # 🟩 추가: 사료 1개 행
    def food_item(food_name):
        is_selected = selected_food_text == food_name

        return ft.Container(
            padding=ft.padding.symmetric(vertical=14, horizontal=10),
            border_radius=10,
            bgcolor=ft.Colors.GREY_100 if is_selected else ft.Colors.WHITE,
            on_click=lambda e, name=food_name: select_food(name),
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

    # 🟩 추가: 검색 결과 리스트 다시 그리기
    def update_food_list(keyword=""):
        keyword = keyword.strip().lower()

        if keyword:
            filtered_foods = [food for food in food_items if keyword in food.lower()]
        else:
            filtered_foods = food_items

        if filtered_foods:
            food_list_column.controls = [food_item(food) for food in filtered_foods]
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

    # 🟩 추가: 검색창 입력 시 목록 필터링
    def on_food_search_change(e):
        update_food_list(e.control.value)

    food_search_field.on_change = on_food_search_change

    # 🟩 추가: 사료 선택 시 실행
    def select_food(food_name):
        nonlocal selected_food_text
        selected_food_text = food_name

        rebuild_body()

        harim_bottom_tip_sheet.open = False
        page.update()

    harim_bottom_tip_sheet = ft.BottomSheet(
        open=False,

        # ✅ 1. 배경 어둡게 → 시선 집중 (핵심)
        # 살짝 어둡게 바꿔야 "떠있는 느낌" 남
        # barrier_color=ft.Colors.with_opacity(0.4, ft.Colors.BLACK), 
        # ✅ 2. 배경 밝게 → FIGMA 디자인 기준
        barrier_color=ft.Colors.TRANSPARENT,

        size_constraints=ft.BoxConstraints(
            max_height=700,
            min_height=430,
        ),

        content=ft.Container(
            padding=20,
            bgcolor=ft.Colors.WHITE,

            # ✅ 2. 둥근 상단 → 바텀시트 느낌 강화
            border_radius=ft.border_radius.only(
                top_left=20,
                top_right=20,
            ),

            # ✅ 3. 그림자 효과 → 떠있는 느낌
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
                offset=ft.Offset(0, -4),  # 위쪽 그림자
            ),

            content=ft.Column(
                tight=True,
                controls=[
                    
                    # ✅ 4. 드래그 핸들 (요즘 앱 필수 요소)
                    ft.Container(
                        width=40,
                        height=5,
                        border_radius=10,
                        bgcolor=ft.Colors.GREY_400,
                        alignment=ft.Alignment(0, 0),  # ✅ 가운데 정렬,
                    ),

                    ft.Container(height=10),  # 여백

                    # 🟦 수정: 기존 텍스트는 "사료 검색" 유지
                    ft.Text("사료 검색", size=25, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),

                    # 🟦 수정: 바텀시트 안에서 실제 검색 가능한 입력창으로 사용
                    food_search_field,

                    # 🟦 수정: 기존 하드코딩된 ft.Text(...) 여러 줄 대신
                    # 🟦 검색 결과 리스트가 동적으로 들어가도록 변경
                    ft.Container(height=12),
                    food_list_column,

                    ft.Container(height=10),
                ],
            ),
        )
    )

    # 🟦 수정: 앱 시작할 때 자동으로 열리던 방식 제거
    # 🟦 이유:
    # 🟦 - 이제는 특정 input 박스를 눌렀을 때만 열려야 하기 때문
    # def show_inital_tip(e=None):
    #   harim_bottom_tip_sheet.open = True
    #   page.update()

    # 🟩 추가: 바텀시트 열기 함수
    def open_food_bottom_sheet(e):
        food_search_field.value = ""
        update_food_list("")
        harim_bottom_tip_sheet.open = True
        page.update()

    # 🟩 추가: 본문을 다시 그리기 위한 전용 컬럼
    body_content = ft.Column(
        width=350,  # 🔥 (2) Column 자체의 너비를 고정
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.START,  # center를 start로 바꿈
        scroll=ft.ScrollMode.AUTO,
    )

    # 🟩 추가: 본문 다시 그리기 함수
    # 🟩 설명:
    # - 사료 선택 후 화면의 박스 텍스트를 바꿔주기 위해 필요
    def rebuild_body():
        body_content.controls = [
            ft.Container(
                margin=ft.margin.only(top=50),
                content=about_dog(),
            ),
            ft.Text("현재 급여 중인 사료", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),

            # 🟦 수정: 기존 input_box("현재 급여 중인 사료를 적어주세요")
            # 🟦 -> 클릭 시 바텀시트가 열리는 food_select_box 로 변경
            food_select_box(
                text=selected_food_text,
                on_click=open_food_bottom_sheet,
            ),

            ft.Text("현재 급여 중인 사료 잔여량", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            input_box("현재 급여 중인 사료 잔여량을 적어주세요"),

            bottom_continue_button(),
        ]
        page.update()

    body = ft.Container(
        padding=ft.padding.only(top=0),  # 🔥 (1) 전체 레이아웃을 아래로 내림 음수 제거
        content=ft.Column(
            width=350,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                body_content,
            ],
        ),
    )

    ### 페이지에 BottomSheet를 등록하기
    page.overlay.append(harim_bottom_tip_sheet)

    # 🟦 수정: 시작하자마자 바텀시트 띄우는 코드 제거
    # show_inital_tip()

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