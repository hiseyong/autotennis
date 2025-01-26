import requests
def wait_until_open(date):
    print("사이트 오픈 대기중...")
    while True:
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
        session = requests.Session()
        session.get(
            'https://gbc.gys.or.kr:446/member/sso_login_process.php?memid=hiseyong&memno=420177&returl=https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07',
            headers=headers)
        res = session.post('https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07', data=data, headers=headers)
        # print(res.content.decode('cp949'))
        # if "대관 신청접수 기간이 아닙니다" in res.content.decode('cp949'): continue
        if "대관 신청접수 기간이 아닙니다" not in res.content.decode('cp949'): break