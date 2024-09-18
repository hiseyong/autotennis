import requests
import config


#이부분을 수정할것
date = [20240807,20240808,20240820,20240821]  # 날짜 YYYYMMDD 형식으로 작성, 콤마로 구분
court = [1,1,2,2]  # 코트번호, 콤마로 구분
starttime = [10,10,10,10]  # 시작하는 시각을 24시간 형식(오후 1시 = 13)으로 작성, 콤마로 구분

#이 아래는 수정 금지

session=requests.session()

datels=config.makeData(date,court,starttime, session)
print(datels)
if datels == 0:
    exit()

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Origin':'https://yeyak.gys.or.kr',
    'Referer':'https://yeyak.gys.or.kr/'
}

res = session.get('https://gbc.gys.or.kr:446/member/sso_login_process.php?memid=hiseyong&memno=420177&returl=https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07', headers=headers)
print(res.text)


for i in datels:
    prereq = session.post('	https://gbc.gys.or.kr:446/rent/rent_period_apply-1.php', headers=headers, data=i)
    respon = session.post('https://gbc.gys.or.kr:446/rent/rent_period_proc.php', headers=headers, data=i)
    print(respon.content.decode('cp949'))