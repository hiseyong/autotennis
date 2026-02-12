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
date = [20260205,20260227,20260220,20260219,20260212,20260211,20260204]  # 날짜 YYYYMMDD 형식으로 작성, 콤마로 구분
court = [2,2,2,2,2,2,2]  # 코트번호, 콤마로 구분
starttime = [10,10,10,10,8,10,10]  # 시작하는 시각을 24시간 형식(오후 1시 = 13)으로 작성, 콤마로 구분


#이 아래는 수정 금지

async def main():
    session = requests.Session()
    session.mount("https://", SSLAdapter())

    login(session)

    wait_until_open(date[0], session)
    datels = await make_data(date, court, starttime)
    print(datels)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Origin': 'https://yeyak.gys.or.kr',
        'Referer': 'https://yeyak.gys.or.kr/'
    }

    for i in datels:
        prereq = session.post('	https://gbc.gys.or.kr:446/rent/rent_period_apply-1.php', headers=headers, data=i)
        respon = session.post('https://gbc.gys.or.kr:446/rent/rent_period_proc.php', headers=headers, data=i)
        print(respon.content.decode('cp949'))


asyncio.run(main())