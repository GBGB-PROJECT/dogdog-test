import flet as ft
from components.common.common_components import about_dog
from components.layout.common_layout import build_screen
from components.navigation import go_next, go_back


def build_view(page: ft.Page):
    body_score_descriptions = {
        1: "✅ 1단계:\n갈비뼈, 요추, 골반 뼈와 모든 뼈의 윤곽이 뚜렷하게 드러납니다.",
        2: "✅ 2단계:\n갈비뼈, 요추, 골반 뼈가 쉽게 보입니다.",
        3: "✅ 3단계:\n갈비뼈가 쉽게 만져지며 체지방이 적습니다.",
        4: "✅ 4단계:\n적당한 지방이 덮인 갈비뼈가 쉽게 만져집니다.",
        5: "✅ 5단계:\n과도한 지방 없이 갈비뼈가 잘 만져집니다.",
        6: "✅ 6단계:\n갈비뼈가 약간의 지방에 덮여 있어 만져지긴 하지만, 허리 구분이 모호해지기 시작합니다.",
        7: "✅ 7단계:\n두꺼운 지방층 때문에 갈비뼈를 만지기 힘듭니다.",
        8: "✅ 8단계:\n많은 지방이 덮여 있어 갈비뼈가 전혀 만져지지 않습니다.",
        9: "✅ 9단계:\n목, 척추, 꼬리 부분에 매우 많은 양의 지방이 축적되어 있습니다.",
    }

    body_score_text = ft.Text(
        "현재 선택: 6단계",
        size=14,
        weight=ft.FontWeight.W_500,
        color=ft.Colors.BLUE_700,
        text_align=ft.TextAlign.CENTER,
    )

    body_score_description_text = ft.Text(
        body_score_descriptions[6],
        size=14,
        color=ft.Colors.BLACK,
        weight=ft.FontWeight.W_500,
    )

    def slider_changed(e):
        selected_value = int(e.control.value)
        body_score_text.value = f"현재 선택: {selected_value}단계"
        body_score_description_text.value = body_score_descriptions[selected_value]
        page.update()

    body_score_slider = ft.Slider(
        min=1,
        max=9,
        divisions=8,
        value=6,
        label="{value}",
        active_color=ft.Colors.BLUE_400,
        inactive_color=ft.Colors.BLUE_100,
        thumb_color=ft.Colors.WHITE,
        on_change=slider_changed,
        width=330,
    )

    body_controls = [
        ft.Container(width=350, margin=ft.margin.only(top=50), content=about_dog()),
        ft.Text("반려동물의 체형은 몇단계인가요?", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
        ft.Image(src="obesity.png", width=350, fit=ft.BoxFit.CONTAIN),
        body_score_text,
        body_score_slider,
        body_score_description_text,
    ]

    return build_screen(
        page=page,
        body_controls=body_controls,
        on_back=lambda e: go_back(page),
        on_continue=lambda e: go_next(page),
    )