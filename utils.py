import requests
def wait_until_open(date, session):
    print("사이트 오픈 대기중...")
    while True:
        try:
            data = {
                'rent_date': str(date),
                'nyear': str(date)[:4],
                'nmonth': str(date)[4:6],
                'nday': str(date)[6:8],
                'stime': '',
                'etime': '',
                'place_opt': "6",
                'place_nm': f"테니스 {6}코트".encode(encoding='cp949'),
                'rent_gubun': '1001',
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Origin': 'https://yeyak.gys.or.kr',
                'Referer': 'https://yeyak.gys.or.kr/'
            }

            login(session)

            res = session.post('https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07', data=data, headers=headers)
            # print(res.content.decode('cp949'))
            # if "대관 신청접수 기간이 아닙니다" in res.content.decode('cp949'): continue
            if "대관 신청접수 기간이 아닙니다" not in res.content.decode('cp949'):
                break
        except:
            continue

def login(session):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Origin': 'https://yeyak.gys.or.kr',
        'Referer': 'https://yeyak.gys.or.kr/'
    }
    res = session.get('https://yeyak.gys.or.kr/fmcs/27?referer=https%3A%2F%2Fgbc.gys.or.kr%2F&login_check=skip',
                      headers=headers)
    security_token = res.text.split("SecurityToken")[1].split("value=")[1].split("/>")[0].replace('"', '')
    print(security_token)
    session.post('https://yeyak.gys.or.kr/fmcs/27?referer=https://gbc.gys.or.kr/&login_check=skip', headers=headers,
                 data={"userId": "hiseyong", "userPassword": "13579013579ahn", "SecurityToken": security_token})
    session.post('https://www.gys.or.kr/member/SSO/newlogin', headers=headers,
                 data={"memid": "hiseyong", "memno": "420117", "returl": "https://gbc.gys.or.kr/"})
    session.get(
        'https://gbc.gys.or.kr:446/member/sso_login_process.php?memid=hiseyong&memno=420177&returl=https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07',
        headers=headers)