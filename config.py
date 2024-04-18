from rent_chk import *

def makeData(date, court, starttime, session):
    ls=[]
    if len(date) != len(court) or len(date) != len(starttime):
        print('입력 값들의 길이가 서로 다릅니다')
        return 0
    for i in range(len(date)):
        dt = str(date[i])
        strstarttime = ''
        strendtime = ''
        if starttime[i] < 10:
            strstarttime = '0' + str(starttime[i])
            strendtime = '0' + str(starttime[i] + 2)
        else:
            strstarttime = str(starttime[i])
            strendtime = str(starttime[i] + 2)
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
            'stime': strstarttime,  # 시작시간
            'etime': strendtime,  # 끝시간
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
            'place_opt': str(court[i]+5),#코트번호
            'place_nm': ('테니스 '+str(court[i])+'코트').encode(encoding='cp949'),
            'rent_gubun': '1001',
            'rent_chk[]': get_rent_chk(session, date[i], court[i], starttime[i]),
            'etc_item_cd_sel': 'I000123',
            'etc_item_cnt_sel': '1',
            'etc_item_amt_sel': '7000',
            'etc_item_amt_sel': '1000',
            'TotalPay': '0',
            'none':'none'
        })
    return ls