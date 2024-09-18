def get_rent_chk(session, date, court, starttime):

    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Origin':'https://yeyak.gys.or.kr',
        'Referer':'https://yeyak.gys.or.kr/'
    }

    res = session.get('https://gbc.gys.or.kr:446/member/sso_login_process.php?memid=hiseyong&memno=420177&returl=https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07', headers=headers)
    print(res.text)

    data = {
        'rent_date': str(date),
        'regno': '',
        'com_nm': '',
        'use_tel': '',
        'use_hp': '',
        'use_fax': '',
        'use_zipcd': '',
        'use_addr': '',
        'use_event_name': '',
        'inwon': '',
        'etc': '',
        'rent_type': '50',
        'offline_yn': '',
        'use_concept': '',
        'sort_order': '',
        'stime': '',
        'etime': '',
        'min_time': '2',
        'use_time': '0',
        'observance': '',
        'addtime_type': '1001',
        'addtime_rate': '',
        'TempPay': '0',
        'etc01': '0',
        'etc02': '0',
        'rent_file':'',
        'nyear': str(date)[:4],
        'nmonth': str(date)[4:6],
        'nday': str(date)[6:],
        'rentMaxTime': '2',
        'part_opt': '07',
        'part_nm': '테니스장'.encode(encoding='cp949'),
        'pay_opt': '',
        'account_no': '301-0056-1027-91',
        'tel': '',
        'part_hp_no': '031-932-4667',
        'toMail': '',
        'place_opt': str(court+5),
        'place_nm': ('테니스 '+str(court)+'코트').encode(encoding='cp949'),
        'rent_gubun': '1001',
        'etc_item_cd_sel': 'I000254',
        'etc_item_cnt_sel': '1',
        'etc_item_amt_sel': '1000',
        'TotalPay': '0',
        'none': 'none'
    }

    strstarttime = ''
    strendtime = ''
    if starttime < 10:
        strstarttime = '0'+str(starttime)
        strendtime = '0'+str(starttime+2)
    else :
        strstarttime = str(starttime)
        strendtime = str(starttime+2)

    while True:
        try:
            response = session.post('https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07',headers=headers, data=data)
            content = response.content.decode(encoding='cp949')
            idx = content.index(strstarttime + '00' + strendtime + '00')
            rent_chk = content[idx:idx + 11]
            break
        except:
            pass


    return rent_chk