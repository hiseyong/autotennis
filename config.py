import aiohttp
import asyncio
from rent_chk import *

async def make_data(date, court, starttime):
    async with aiohttp.ClientSession() as session:
        # 입력 데이터 길이 확인
        if len(date) != len(court) or len(date) != len(starttime):
            print('입력 값들의 길이가 서로 다릅니다')
            return []

        tasks = []
        for i in range(len(date)):
            # rent_chk 데이터를 비동기로 가져오기 위한 태스크 생성
            tasks.append(
                asyncio.create_task(
                    get_rent_chk(session, date[i], court[i], starttime[i])
                )
            )

        # rent_chk 리스트 비동기로 가져오기
        results = await asyncio.gather(*tasks, return_exceptions=True)

        rent_chk_list = []

        for result in results:
            # 예외 발생 시 gather는 Exception 객체를 반환함
            if isinstance(result, Exception):
                # 원하는 경우 로그 찍기 가능
                # print("get_rent_chk error:", result)
                continue  # rent_chk_list에 추가하지 않음
            rent_chk_list.append(result)

        ls = []
        for i, rent_chk in enumerate(rent_chk_list):
            dt = str(date[i])
            strstarttime = f"{starttime[i]:02}"
            strendtime = f"{starttime[i] + 2:02}"

            # 모든 필드 포함
            ls.append({
                'rent_date': dt,
                'regno': '',
                'com_nm': '',
                'use_tel': '',
                'use_hp': '010-8392-0725',
                'use_fax': '',
                'use_zipcd': '10441',
                'use_addr': '경기도 고양시 덕양구 강매동 193-4'.encode(encoding='cp949'),
                'use_event_name': '',
                'inwon': '2',
                'etc': '',
                'rent_type': '50',
                'offline_yn': '',
                'use_concept': '',
                'sort_order': '',
                'stime': strstarttime,
                'etime': strendtime,
                'min_time': '2',
                'use_time': '2',
                'observance': '',
                'addtime_type': '1001',
                'addtime_rate': '',
                'TempPay': '0',
                'etc01': '0',
                'etc02': '0',
                'rent_file': '',
                'nyear': dt[:4],
                'nmonth': dt[4:6],
                'nday': dt[6:],
                'rentMaxTime': '2',
                'part_opt': '07',
                'part_nm': '테니스장'.encode(encoding='cp949'),
                'pay_opt': '',
                'account_no': '301-0056-1027-91',
                'tel': '',
                'part_hp_no': '031-932-4667',
                'toMail': '',
                'place_opt': str(court[i] + 5),
                'place_nm': f"테니스 {court[i]}코트".encode(encoding='cp949'),
                'rent_gubun': '1001',
                'rent_chk[]': rent_chk,
                'etc_item_cd_sel': 'I000123',
                'etc_item_cnt_sel': '1',
                'etc_item_amt_sel': '7000',
                'etc_item_amt_sel': '1000',
                'TotalPay': '0',
                'none': 'none',
            })

        return ls