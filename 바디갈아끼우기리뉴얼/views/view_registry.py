from datetime import datetime

import components as components
import views as views
from components.common.texts import Txt


def make_view_config(top, body, bottom_index):
    return {
        "top": top,
        "body": body,
        "bottom_index": bottom_index,
    }


def build_view_config(page, open_back, name: str, data=None):
    target_date = data or datetime.today().date()

    def log_top_bar():
        return components.top_bar("Log", on_back=open_back)

    view_builders = {
        "home": lambda: make_view_config(
            components.top_bar(),
            views.home_view(page),
            0,
        ),
        "log": lambda: make_view_config(
            log_top_bar(),
            views.log_view(page),
            1,
        ),
        "contents": lambda: make_view_config(
            components.top_bar("Contents", on_back=open_back),
            Txt("콘텐츠 페이지 준비 중"),
            2,
        ),
        "mypage": lambda: make_view_config(
            components.top_bar("My Page", on_back=open_back),
            views.mypage_view(page),
            3,
        ),
        "food_remain": lambda: make_view_config(
            components.top_bar("급여중인 제품", on_back=open_back),
            views.food_remain_view(page),
            3,
        ),
        "food_select": lambda: make_view_config(
            components.top_bar("사료 등록", on_back=open_back),
            views.food_select_view(page),
            99,
        ),
        "log_daily": lambda: make_view_config(
            log_top_bar(),
            views.log_daily_view(page, target_date),
            1,
        ),
        "log_daily_create": lambda: make_view_config(
            log_top_bar(),
            views.log_daily_create_view(page, target_date),
            1,
        ),
        "log_weekly": lambda: make_view_config(
            log_top_bar(),
            views.log_weekly_view(page),
            1,
        ),
        "shop": lambda: make_view_config(
            components.top_bar("Shop", on_back=open_back),
            Txt("샵 페이지 준비 중"),
            99,
        ),
    }

    if name not in view_builders:
        raise ValueError(f"알 수 없는 화면 이름: {name}")

    return view_builders[name]()