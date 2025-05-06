from config import *
import requests
import asyncio
from utils import *
import ssl
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.set_ciphers('DEFAULT@SECLEVEL=1')  # 낮은 보안 수준 허용
        kwargs['ssl_context'] = context
        self.poolmanager = PoolManager(*args, **kwargs)

#이부분을 수정할것
date = [20250508,20250512,20250515,20250519,20250522,20250526,20250529,20250507,20250514,20250521,20250528]  # 날짜 YYYYMMDD 형식으로 작성, 콤마로 구분
court = [1,1,1,1,1,1,1,2,2,2,2]  # 코트번호, 콤마로 구분
starttime = [10,10,10,10,10,10,10,10,10,10,10]  # 시작하는 시각을 24시간 형식(오후 1시 = 13)으로 작성, 콤마로 구분


#이 아래는 수정 금지

async def main():
    wait_until_open(date[0])
    datels = await make_data(date, court, starttime)
    print(datels)
    session = requests.Session()
    session.mount("https://", SSLAdapter())

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Origin': 'https://yeyak.gys.or.kr',
        'Referer': 'https://yeyak.gys.or.kr/'
    }
    ssl_context = ssl.create_default_context()
    ssl_context.set_ciphers('DEFAULT@SECLEVEL=1')  # 낮은 보안 레벨 허용
    session.post('https://www.gys.or.kr/member/SSO/newlogin', headers=headers, data={"memid":"hiseyong", "memno":"420177", "returl": "https://gbc.gys.or.kr/"})
    session.get('https://gbc.gys.or.kr:446/member/sso_login_process.php?memid=hiseyong&memno=420177&returl=https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07', headers=headers)
    for i in datels:
        prereq = session.post('	https://gbc.gys.or.kr:446/rent/rent_period_apply-1.php', headers=headers, data=i)
        respon = session.post('https://gbc.gys.or.kr:446/rent/rent_period_proc.php', headers=headers, data=i)
        print(respon.content.decode('cp949'))


asyncio.run(main())