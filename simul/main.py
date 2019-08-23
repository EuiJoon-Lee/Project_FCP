from env import Env
from agent import Agent
import csv


if __name__ == "__main__":
    KRT = Env(10000000000, 1.0, 0.001, "KRT")
    UST = Env(50000000, 1.0, 0.001, "UST")
    EJ = Agent(["KRT", "UST"], [200000000, 1000])

    f = open('USDKRW_deviation.csv', 'rt')
    data = csv.reader(f)
    deviation_set = list()
    for line in data:
        if not data:
            break
        deviation_set.append(line)

    # KRT_rate_set = []  # 환율 데이터
    # UST_rate_set

    for i, deviation_ in enumerate(deviation_set):
        # KRT.change_rate(KRT_rate_set[i])
        # UST~~

        deviation = float(deviation_[0])
        if deviation > 0:
            max_profit, max_offer_amount, max_ask_amount = EJ.calculate_profit(
                KRT, UST, KRT.tobin, deviation, 100)
            if max_profit == None:
                continue
            KRT.change_pool(max_offer_amount, True)
            UST.change_pool(max_ask_amount, False)

            print("Round:", i, "\tKRT->UST", end='\t')
            print("max_profit:", max_profit, "\tmax_offer_amount:",
              max_offer_amount, "\tmax_ask_amount:", max_ask_amount, end='\t')
            print("UST.pool:", UST.pool, "\tKRT.pool:", KRT.pool)

        else:
            max_profit, max_offer_amount, max_ask_amount = EJ.calculate_profit(
                UST, KRT, UST.tobin, deviation, 0.1)
            if max_profit == None:
                continue
            UST.change_pool(max_offer_amount, True)
            KRT.change_pool(max_ask_amount, False)

            print("Round:", i, "\tUST->KRT", end='\t')
            print("max_profit:", max_profit, "\tmax_offer_amount:",
              max_offer_amount, "\tmax_ask_amount:", max_ask_amount, end='\t')
            print("UST.pool:", UST.pool, "\tKRT.pool:", KRT.pool)

        KRT.reg_pool(2000000)  # 2분 = 20블록 1블록에 10만원
        UST.reg_pool(5000)   # 2분 = 20블록

