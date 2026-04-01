import flet as ft

import views.auth.signup_view as signup_view
import views.auth.signup_success_view as signup_success_view
import views.onboarding.pet_basic_info_view as pet_basic_info_view
import views.onboarding.pet_info_obesity_view as pet_info_obesity_view
import views.onboarding.pet_info_activity_view as pet_info_activity_view
import views.onboarding.pet_info_health_view as pet_info_health_view
import components.pet_info_food_view as pet_info_food_view


def router(page: ft.Page):
    page.views.clear()

    routes = {
        "/signup": signup_view.build_view,
        "/pet_info": pet_basic_info_view.build_view,
        "/pet_info_obesity": pet_info_obesity_view.build_view,
        "/pet_info_activity": pet_info_activity_view.build_view,
        "/pet_info_health": pet_info_health_view.build_view,
        "/pet_info_food": pet_info_food_view.build_view,
        "/signup_success": signup_success_view.build_view,
    }

    builder = routes.get(page.route, signup_view.build_view)

    page.views.append(
        ft.View(
            route=page.route,
            padding=0,
            spacing=0,
            bgcolor=ft.Colors.WHITE,
            controls=[builder(page)],
        )
    )

    page.update()


def main(page: ft.Page):
    page.title = "Dog App"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.HIDDEN

    # ✅ FilePicker 서비스 등록을 위해 임시 view 1개 먼저 넣기
    page.views.append(ft.View(route="/__bootstrap__", controls=[]))

    # ✅ 페이지 전체에서 재사용할 FilePicker
    page.profile_image_picker = ft.FilePicker()
    page.services.append(page.profile_image_picker)

    # ✅ 임시 view 제거
    page.views.clear()

    page.on_route_change = lambda e: router(page)
    page.go("/signup")


if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )