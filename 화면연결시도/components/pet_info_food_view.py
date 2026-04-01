import flet as ft
from components.common.common_components import about_dog, input_box, bottom_continue_button
from components.layout.common_layout import build_screen
from components.navigation import go_next, go_back


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


def build_view(page: ft.Page):
    # 🟩 현재 선택된 사료 이름 상태값
    selected_food_text = "현재 급여 중인 사료를 적어주세요"

    # 🟩 원본 8pet의 예시 사료 목록
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

    # 🟩 사료 1개 행
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

    # 🟩 검색 결과 리스트 다시 그리기
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

    # 🟩 검색창 입력 시 목록 필터링
    def on_food_search_change(e):
        update_food_list(e.control.value)

    food_search_field.on_change = on_food_search_change

    # 🟩 사료 선택 시 실행
    def select_food(food_name):
        nonlocal selected_food_text
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
    def open_food_bottom_sheet(e):
        food_search_field.value = ""
        update_food_list("")
        harim_bottom_tip_sheet.open = True
        page.update()

    # 🟩 본문 다시 그리기
    def rebuild_body():
        body_content.controls = [
            ft.Container(
                margin=ft.margin.only(top=50),
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

    return build_screen(
        page=page,
        body_controls=[body_content],
        on_back=lambda e: go_back(page),
        on_continue=lambda e: go_next(page),
        show_back=True,
        fixed_bottom=True,
    )