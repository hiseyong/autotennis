import requests
import config
from datetime import datetime, timedelta
import time

# 수정 가능한 부분
date = [20240607,20240608]  # 날짜 YYYYMMDD 형식으로 작성, 콤마로 구분
court = [1,1]  # 코트번호, 콤마로 구분
starttime = [10,10]  # 시작하는 시각을 24시간 형식(오후 1시 = 13)으로 작성, 콤마로 구분

# 이 아래는 수정 금지

session = requests.session()

datels = config.makeData(date, court, starttime, session)
print(datels)
if datels == 0:
    exit()

# 현재 날짜와 시간을 가져옴
now = datetime.now()

# 날짜가 25일이면서 10시가 되기 전까지 기다림

if now.day > 25:
    print("날짜가 25일이 지났습니다. 다음 달 25일에 시도하세요")
    exit()

while now.day < 25:
    print("아직 25일이 되지 않았습니다. 자동으로 대기 후 25일 10시에 예약합니다.")
    print("현재 날짜:",str(now.day)+"일")

if now.day == 25:
    while now.hour < 10:
        print("아직 10시가 되지 않았습니다. 기다리는 중...", "현재 시각:", str(now.hour)+'시',str(now.minute)+'분',str(now.second)+'초')
        time.sleep(1)  # 1초 동안 대기
        now = datetime.now()

    # 10시가 되었거나 넘었으면 서버에 요청을 보냄


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Origin': 'https://yeyak.gys.or.kr',
        'Referer': 'https://yeyak.gys.or.kr/'
    }

    res = session.get(
        'https://gbc.gys.or.kr:446/member/sso_login_process.php?memid=hiseyong&memno=420177&returl=https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07',
        headers=headers)
    print(res.text)

    for i in datels:
        prereq = session.post('	https://gbc.gys.or.kr:446/rent/rent_period_apply-1.php', headers=headers, data=i)
        respon = session.post('https://gbc.gys.or.kr:446/rent/rent_period_proc.php', headers=headers, data=i)
        print(respon.content.decode('cp949'))
else:
    print("날짜가 25일이 아니므로 서버에 요청을 보내지 않습니다.")
