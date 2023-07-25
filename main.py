import requests
import config



date=[20230810]
court=[1]
starttime=[14]



datels=config.makeData(date,court,starttime)
print(datels)
if datels == 0:
    exit()
session=requests.session()

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Origin':'https://yeyak.gys.or.kr',
    'Referer':'https://yeyak.gys.or.kr/'
}

res = session.get('https://gbc.gys.or.kr:446/member/sso_login_process.php?memid=dkstjdclf&memno=10440&returl=https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07', headers=headers)
print(res.text)


for i in datels:
    respon = session.post('https://gbc.gys.or.kr:446/rent/rent_period_proc.php', headers=headers, data=i)
    print(respon.content.decode('cp949'))