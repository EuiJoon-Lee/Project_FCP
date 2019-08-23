#initial env value [pool_size]
SDT = 50000000 
UST = 50000000
KRT = 10000000000
TobinA = 0.00001
TobinB = 0.000005
SDT_Reg = 5000
UST_Reg = 5000
KRT_Reg = 1000000

def get_oracle_rate(): # get oracle rate from oracle module
    return SDT_rate, UST_rate, KRT_rate
def get_terra_pool(): # get virtual terra pool from market module
    return SDT.pool, UST.pool, KRT.pool

def Forex_Constant_ProductA(offer_denom, offer_amount, ask_denom):
    x = KRT_pool
    y = KRT_pool*SDT_rate/KRT_rate
    constant_product = x * y
    result = x - constant_product/(y + offer_amount)
    ask_amount = result - offer_amount*KRT_rate/SDT_rate*TobinA
    total_fee = (offer_amount*KRT_rate/SDT_rate - ask_amount)/(offer_amount*KRT_rate/SDT_rate)*100
    if total_fee and ask_amount > 0:
        return result, offer_amount*KRT_rate/SDT_rate, ask_amount, total_fee
    else:
        return 'ERROR'

def Forex_Constant_ProductB(offer_denom, offer_amount, ask_denom):
    x = KRT_pool
    y = KRT_pool*SDT_rate/KRT_rate
    constant_product = x * y
    result = x - constant_product/(y + offer_amount)
    ask_amount = result - offer_amount*KRT_rate/SDT_rate*TobinB
    total_fee = (offer_amount*KRT_rate/SDT_rate - ask_amount)/(offer_amount*KRT_rate/SDT_rate)*100
    if total_fee and ask_amount > 0:
        return result, offer_amount*KRT_rate/SDT_rate, ask_amount, total_fee
    else:
        return 'ERROR'

def adjust_pool(offer_denom, offer_amount, ask_denom, ask_amount):
    offer_denom.pool - offer_amount
    ask_denom.pool + ask_amount
    return SDT UST KRT
def reg_pool()


# 1block, 1swap
def reg_
MsgSwap(offer_denom, offer_amount, ask_denom):
    get_oracle_rate()
    get_terra_pool()
    if offer_denom or ask_denom is KRT:
        Forex_Constant_ProductA(offer_denom, offer_amount, ask_denom)
    else
        Forex_Constant_ProductB(offer_denom, offer_amount, ask_denom)
    adjust_pool(offer_denom, offer_amount, ask_amount, ask_denom)
    return 

Block()
    reg_pool()