ROUTES = [
    "/signup",
    "/pet_info",
    "/pet_info_obesity",
    "/pet_info_activity",
    "/pet_info_health",
    "/pet_info_food",
    "/signup_success",
]


def go_next(page):
    if page.route in ROUTES:
        idx = ROUTES.index(page.route)
        if idx < len(ROUTES) - 1:
            page.go(ROUTES[idx + 1])


def go_back(page):
    if page.route in ROUTES:
        idx = ROUTES.index(page.route)
        if idx > 0:
            page.go(ROUTES[idx - 1])