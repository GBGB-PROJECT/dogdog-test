import flet as ft


def food_remain_view(page: ft.Page):
    # ✅ 상단 탭 상태 저장용
    selected_top_tab = {"index": 0}

    # ✅ 탭 내용 들어갈 영역
    tab_content = ft.Container(
        width=330,
        expand=True,
    )

    # ✅ 상단 탭이 실제로 들어갈 자리
    top_tabs_area = ft.Container(
        width=330,
    )

    # ─────────────────────────────────────────────
    # 🟦 사료 등록 화면으로 이동
    # ─────────────────────────────────────────────
    def open_food_select(e):
        page.open_food_select()

    # ─────────────────────────────────────────────
    # 🟦 divider 아래 남은량 정보 영역
    # ─────────────────────────────────────────────
    def remain_info_box2():
        return ft.Column(
            spacing=10,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            "???g / ???kg",
                            size=14,
                            color=ft.Colors.BLACK,
                            weight=ft.FontWeight.W_600,
                        ),
                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=10, vertical=4),
                            bgcolor=ft.Colors.GREY_200,
                            border_radius=8,
                            alignment=ft.Alignment(0, 0),
                            content=ft.Text(
                                "??일치 남음",
                                size=12,
                                color=ft.Colors.BLACK,
                                weight=ft.FontWeight.W_500,
                            ),
                        ),
                    ],
                ),
                ft.ProgressBar(
                    width=298,
                    height=10,
                    value=0,
                    bgcolor=ft.Colors.GREY_300,
                    color=ft.Colors.GREY_300,
                    border_radius=10,
                ),
                ft.Text(
                    "예상 소진일",
                    size=12,
                    color=ft.Colors.GREY_600,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        )

    # ─────────────────────────────────────────────
    # 🟦 큰 제품 카드
    # - 위 2/3: 제품 이미지 자리
    # - 현재는 선택된 제품이 없으므로 안내 문구 표시
    # - 아래 1/3: 잔여량 정보 영역
    # ─────────────────────────────────────────────
    def product_big_box():
        return ft.Container(
            width=330,
            height=330,
            border_radius=16,
            border=ft.border.all(1, ft.Colors.GREY_300),
            bgcolor=ft.Colors.WHITE,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Column(
                spacing=0,
                controls=[
                    # ✅ 위쪽 2/3 영역
                    ft.Container(
                        height=220,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Text(
                            "등록된 제품이 없습니다",
                            size=16,
                            color=ft.Colors.GREY_600,
                            weight=ft.FontWeight.W_500,
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ),

                    # ✅ 2/3 지점 divider
                    ft.Divider(
                        height=1,
                        thickness=1,
                        color=ft.Colors.GREY_300,
                    ),

                    # ✅ 아래 1/3 영역
                    ft.Container(
                        expand=True,
                        padding=ft.padding.symmetric(horizontal=16, vertical=12),
                        content=remain_info_box2(),
                    ),
                ],
            ),
        )

    # ─────────────────────────────────────────────
    # 🟦 상단 탭 UI 만드는 함수
    # ─────────────────────────────────────────────
    def build_top_tabs():
        labels = ["전체", "사료", "간식", "영양제"]
        tab_controls = []

        for i, label in enumerate(labels):
            is_selected = selected_top_tab["index"] == i

            tab_controls.append(
                ft.Container(
                    on_click=lambda e, idx=i: change_top_tab(idx),
                    padding=ft.padding.only(top=6, bottom=6, left=4, right=4),
                    content=ft.Column(
                        spacing=6,
                        alignment=ft.MainAxisAlignment.END,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                label,
                                size=15,
                                color=ft.Colors.BLACK if is_selected else ft.Colors.GREY,
                                weight=ft.FontWeight.W_700 if is_selected else ft.FontWeight.W_500,
                            ),
                            ft.Container(
                                height=3,
                                width=42,
                                bgcolor=ft.Colors.BLACK if is_selected else ft.Colors.TRANSPARENT,
                                border_radius=10,
                            ),
                        ],
                    ),
                )
            )

        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    spacing=10,
                    controls=tab_controls,
                ),
                ft.Container(
                    height=30,
                    padding=ft.padding.symmetric(horizontal=10),
                    border_radius=8,
                    bgcolor=ft.Colors.GREY_200,
                    alignment=ft.Alignment(0, 0),
                    on_click=open_food_select,
                    content=ft.Row(
                        spacing=4,
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "사료 등록",
                                size=12,
                                color=ft.Colors.BLACK,
                                weight=ft.FontWeight.W_500,
                            ),
                            ft.Icon(
                                ft.Icons.EDIT,
                                size=13,
                                color=ft.Colors.BLACK,
                            ),
                        ],
                    ),
                ),
            ],
        )

    # ─────────────────────────────────────────────
    # 🟦 탭 눌렀을 때 내용 바꾸는 함수
    # ─────────────────────────────────────────────
    def change_top_tab(index):
        selected_top_tab["index"] = index

        # if index == 0:
        #     tab_content.content = ft.Column(
        #         expand=True,
        #         scroll=ft.ScrollMode.AUTO,
        #         spacing=12,
        #         controls=[
        #             product_big_box(),
        #         ],
        #     )

        # elif index == 1:
        #     tab_content.content = ft.Column(
        #         expand=True,
        #         scroll=ft.ScrollMode.AUTO,
        #         spacing=12,
        #         controls=[
        #             product_big_box(),
        #         ],
        #     )

        # elif index == 2:
        #     tab_content.content = ft.Column(
        #         expand=True,
        #         scroll=ft.ScrollMode.AUTO,
        #         spacing=12,
        #         controls=[
        #             product_big_box(),
        #         ],
        #     )

        # elif index == 3:
        #     tab_content.content = ft.Column(
        #         expand=True,
        #         scroll=ft.ScrollMode.AUTO,
        #         spacing=12,
        #         controls=[
        #             product_big_box(),
        #         ],
        #     )

        tab_content.content = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=12,
        controls=[product_big_box()],
    )

        # ✅ 탭 모양 다시 그림
        top_tabs_area.content = build_top_tabs()

        # ✅ 최종 화면 갱신
        page.update()

    # ✅ 처음 탭 UI 넣기
    top_tabs_area.content = build_top_tabs()

    # ✅ 처음 실행 시 기본 탭 세팅
    change_top_tab(0)

    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        alignment=ft.Alignment(0, -1),
        content=ft.Container(
            width=330,
            padding=ft.padding.only(top=20, bottom=20),
            content=ft.Column(
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    top_tabs_area,
                    ft.Container(
                        width=330,
                        margin=ft.margin.only(top=6, bottom=16),
                        content=ft.Divider(
                            thickness=1,
                            color=ft.Colors.GREY_300,
                        ),
                    ),
                    tab_content,
                ],
            ),
        ),
    )