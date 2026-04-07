import flet as ft

from backend.app.domains.auth.api.oauth_router import social_providers, master_route_handler 

# ==========
# 1. Header 컴포넌트
# ==========
def header_component():
    return ft.Column(
        controls=[
            # ft.Container(
            #     width=float("inf"), 
            #     alignment=ft.Alignment(-1, 0), 
            #     content=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: print("뒤로가기!"))
            # ),
            ft.Text("회원 가입", size=22, weight=ft.FontWeight.W_600, color=ft.Colors.BLACK)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

# =====
# 2. 소셜 로그인 버튼 컴포넌트(내역이 아닌 겉 테두리만을 의미)
# =====
## 2-1. 클릭 시 이동을 위해서 url_launcher를 외부에서 받아온다.
def social_buttons_component(url_launcher: ft.UrlLauncher):
    ## 2-2. 버튼의 내용물을 외부(특히 auth_service)에서 매개변수로 받아줘야 한다.
    def create_social_button(text, logo, text_color, icon_size, url=None):
        async def handle_click(e):
            await url_launcher.launch_url(ft.Url(url=url, target=ft.UrlTarget.SELF))

        return ft.Container(
            width=300,
            height=50,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            border=ft.Border.all(1,ft.Colors.BLACK_12),
            ink=True,
            on_click=handle_click,
            content=ft.Row(
              controls=[
                  ft.Container(
                    content=ft.Image(src=logo, width=icon_size, height=icon_size),
                                width=50, alignment=ft.Alignment.CENTER),
                  ft.Container(
                    content=ft.Text(text, color=text_color, size=16, weight='w600'),
                                expand=True, alignment=ft.Alignment.CENTER),
                  ft.Container(width=50)
                  ],
              alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
              spacing=0
            )
        )
    ## 2-3. 버튼의 내용물을 for문을 통해 하나씩 넣어줌 -> **p로 button을 넣어줌
    button_controls = [create_social_button(**p) for p in social_providers] 
    
    ## 2-4. 케이스를 이미 설치하고(button_controls) -> 이를 controls에 한 번에 넣어버림(이후 이것에 대해서 정렬, 간격 조정)
    return ft.Column(
        controls=button_controls, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
        spacing=16
    )

# =====
# 3. 나누기 선 컴포넌트
# =====
def divider_component():
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER, width=300, # 전체 길이 지정
        controls=[
            ft.Container(expand=True, height=1, bgcolor=ft.Colors.GREY_400),
            ft.Text("or", size=12), 
            ft.Container(expand=True, height=1, bgcolor=ft.Colors.GREY_400),
        ],
    )

# =====
# 4. 이메일 로그인 버튼 컴포넌트
# =====
def email_login_component():
  def email_login_button_click(e):
    print('이메일 버튼 클릭됨')

  return ft.Container(
  width=300,
  height=50,
  bgcolor=ft.Colors.WHITE,
  border_radius=10, # Container 외곽선
  border=ft.Border.all(1, ft.Colors.BLACK_12), # 경계 색깔지정
  ink=True, # 클릭버튼 효과 여부
  on_click=email_login_button_click, # 클릭 시 발생하는 event
  content=ft.Row(
   controls=[
    ft.Container(content=ft.Icon(ft.Icons.MAIL,size=18, color=ft.Colors.GREY_400), margin=ft.Margin.only(left=15)),
    ft.Text('Continue with Email',color=ft.Colors.BLACK, size=16, weight='w600', expand=True, text_align=ft.TextAlign.CENTER),
    ft.Container(width=33), # 오른쪽 균형을 위해 height 대신 width 적용
   ],
  alignment=ft.MainAxisAlignment.CENTER,
  spacing=10,
  ),
 )


# =====
# 5. 최종 조립 및 전체 페이지 설정
# =====
## 5-1. 가짜 이벤트 응답(Mocking)을 위한 클래스
class MockEvent: # 미리 테스트로 출력해보게 하는 기능
    def __init__(self, page): # 객체 생성 시 먼저 실행되는 초기 메서드(생성자) -> event&데이터 처리 목적
        self.page = page # 절달받은 page 객체를 => 내부 변수인 self.page에 저장
        self.route = page.route # 네트워크 요청을 가로채는 route 기능을 통해 self.route로 저장 -> 이후에 서버 요청 대신 가짜 응답으로 초기 세팅을 수행

## 5-2. 최종조립 main
async def signinup_view(page: ft.Page):
    ## 5-2-1. 페이지 설정
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # 화면 요소들을 수직 정중앙에 위치
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # 화면 요소들을 수평 정중앙에 위치
    page.window.width = 375
    page.window.height = 812   
    page.title = "Login Page"

    ## 5-2-2. 라우터 및 서비스 세팅(기존 창에서 로그인 후 진행하려는 목적-새창으로 진행하는 문제점)
    page.on_route_change = master_route_handler # 라우팅 규칙을 설정(auth_service에 기입됨)
    url_launcher = ft.UrlLauncher() # 실제 브라우저 -> 특정 웹사이트로 이동시키는 도구(새창 방지)
    page.services.append(url_launcher) # page.add 대신 보이지 않은 서랍(services)에 챙겨두는 과정 (새 창으로 이동하지 않고, 창 내부에서 시스템을 이용하게 하려는 목적임)

    # 💡 깔끔해진 메인 화면 조립 부분! 
    # 마치 '목차'를 보듯 어떤 컴포넌트들이 들어가는지 한눈에 파악할 수 있습니다.
    page.add( # 페이지 출력
      ft.Column(
          expand=True, # 화면을 꽉 채우기
          horizontal_alignment=ft.CrossAxisAlignment.CENTER, # column 내 값을 가로 기준으로 정중앙에 위치
          controls=[
              ft.Container(expand=1), # 상단 빈공간 부여 목적
              ft.Column( # 실 로그인 폼이 들어가는 자리
                  horizontal_alignment=ft.CrossAxisAlignment.CENTER, # 안쪽 요소를 수평으로 정중앙에 위치
                  spacing=20, # 각 항목들의 간격 벌려주기
                  controls=[
                      header_component(),
                      social_buttons_component(url_launcher),
                      divider_component(),
                      email_login_component()
                  ],
              ),
              ft.Container(expand=2) # 하단 빈공간
          ]
      )        
    )
    page.run_task(master_route_handler, MockEvent(page)) # 앱이 멈추지 않개 백그라운드에서 작업을 실행 시키는 flet 기능 -> 먼저 가짜이벤트(MockEvent) 실행
    page.update()
    await page.push_route(page.route) # 브라우저에 설정된 주소(/callback/000)로 강제로 이동, 화면이 즉시 보이게 만들어줌(await)

if __name__ == "__main__":
    ft.run(signinup_view, port=34636, view=ft.AppView.WEB_BROWSER, route_url_strategy="path")
