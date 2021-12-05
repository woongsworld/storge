import pyupbit

access = "WpTiSTjk4hNE6OMCBFwqPKwPP2UwEvx0mbj6ztVP"          # 본인 값으로 변경
secret = "OkvGdXTvkxvojv7wxVhIRmnSbR66wwF9CmnTGKeA"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-비트코인 조회할거임
print(upbit.get_balance("KRW-ETC"))     # 이더리움 개수 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
