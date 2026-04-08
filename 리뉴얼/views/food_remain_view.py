import flet as ft


def food_remain_view(page: ft.Page):
    selected_top_tab = {"index": 0}

    tab_content = ft.Container(
        width=330,
        expand=True,
    )

    top_tabs_area = ft.Container(
        width=330,
    )

    def open_food_select(e=None):
        if hasattr(page, "open_food_select"):
            page.open_food_select()
        else:
            print("page.open_food_select 가 없습니다.")

    def remain_info_box():
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

                    ft.Divider(
                        height=1,
                        thickness=1,
                        color=ft.Colors.GREY_300,
                    ),

                    ft.Container(
                        expand=True,
                        padding=ft.padding.symmetric(horizontal=16, vertical=12),
                        content=remain_info_box(),
                    ),
                ],
            ),
        )

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

    def change_top_tab(index):
        selected_top_tab["index"] = index

        tab_content.content = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=12,
        controls=[product_big_box()],
    )

        
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