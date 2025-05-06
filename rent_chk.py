import ssl

async def get_rent_chk(session, date, court, starttime):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Origin': 'https://yeyak.gys.or.kr',
        'Referer': 'https://yeyak.gys.or.kr/'
    }

    login_url = 'https://gbc.gys.or.kr:446/member/sso_login_process.php'
    rent_url = 'https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07'

    login_params = {
        'memid': 'hiseyong',
        'memno': '420177',
        'returl': 'https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07'
    }

    ssl_context = ssl.create_default_context()
    ssl_context.set_ciphers('DEFAULT@SECLEVEL=1')  # 낮은 보안 레벨 허용

    async with session.post('https://www.gys.or.kr/member/SSO/newlogin', headers=headers, data={"memid":"hiseyong", "memno":"420177", "returl": "https://gbc.gys.or.kr/"}, ssl=ssl_context) as res:
        pass

    async with session.get(login_url, headers=headers, params=login_params) as res:
        pass

    strstarttime = f"{starttime:02}"
    strendtime = f"{starttime + 2:02}"

    data = {
        'rent_date': str(date),
        'nyear': str(date)[:4],
        'nmonth': str(date)[4:6],
        'nday': str(date)[6:],
        'stime': '',
        'etime': '',
        'place_opt': str(court + 5),
        'place_nm': f"테니스 {court}코트".encode(encoding='cp949'),
        'rent_gubun': '1001',
    }

    try:
        async with session.post(rent_url, headers=headers, data=data) as response:
            print(await response.text(encoding='cp949'))
            content = await response.text(encoding='cp949')
            idx = content.index(strstarttime + '00' + strendtime + '00')
            end_idx = content.index('"', idx)
            rent_chk = content[idx:end_idx]
            return rent_chk
    except ValueError:
        print("날짜 혹은 시간 값에 문제가 있습니다, 확인해주세요")
        exit()