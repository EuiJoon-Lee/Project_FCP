UST_rate = 0.75
UST_rate = 1
KRT_rate = 1200
SDT_pool = 5000000
UST_pool = 5000000
KRT_pool = 1000000000
Tobin = 0.0012

def Forex_Constant_Product(offer_denom, offer_amount, ask_denom):
    x = KRT_pool
    # y = KRT_pool*UST_rate/KRT_rate
    # constant_product = x * y
    
    # 비슷한 숫자끼리의 뺼셈
    # result = x - constant_product/(y + offer_amount)
    result = (x * KRT_rate * offer_amount) / (x * UST_rate + KRT_rate * offer_amount)


    # 매우 큰 수에서 작은 수 빼기
    ask_amount = result - offer_amount*KRT_rate/UST_rate*Tobin

    # 비슷한 숫자끼리의 뺄셈
    # 매우 큰 수로 나누기
    total_fee = (offer_amount*KRT_rate/UST_rate - ask_amount)/(offer_amount*KRT_rate/UST_rate)*100

    if total_fee and ask_amount > 0:
        return ask_amount, total_fee
    else:
        return 'ERROR'

# def adjust_pool(offer_denom, offer_amount, ask_denom, ask_amount):
#     if offer_denom == 'SDT' and ask_denom == 'KRT':
#         SDT_pool = SDT_pool + offer_amount
#         KRT_pool = KRT_pool - ask_amount
#     return SDT_pool, UST_pool, KRT_pool

if __name__ == "__main__":
    print(Forex_Constant_Product('UST', 3773.2, 'KRW'))