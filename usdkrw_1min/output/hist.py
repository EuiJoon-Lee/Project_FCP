import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    df = pd.read_csv("USDKRW_deviation.csv")
    deviations = df['deviation']
    counts, bins, bars = plt.hist(deviations, bins=200, log=True)
    y_max = max(counts)
    x_min = 0
    y_min = 0
    ax = plt.gca()
    plt.title('2014~2019 USD/KRW 2min Max deviation')
    ax.set_xlabel('2min Max deviation (%)')
    ax.set_ylabel('numbers (log)')
    vals = ax.get_xticks()
    ax.set_xticklabels(['{:,.4%}'.format(x/100+0.002) for x in vals])
    var1 = deviations.quantile(0.95)
    var2 = deviations.quantile(0.99)
    var3 = deviations.quantile(0.999)
    var4 = deviations.quantile(0.9999)
    ax.plot([var1,var1],[0,y_max],color='xkcd:orange',ls='--')
    ax.plot([var2,var2],[0,y_max],color='xkcd:red',ls='--')
    ax.plot([var3,var3],[0,y_max],color='xkcd:crimson',ls='--')
    ax.plot([var4,var4],[0,y_max],color='xkcd:black',ls='--')
    ax.legend(['95% VaR','99% VaR','99.9% VaR','99.99% VaR'])
    print(deviations.quantile([0.9,0.95,0.975,0.99,0.991,0.992, 0.993, 0.994, 0.9951,0.9952, 0.9953, 0.9954, 0.9955,0.9956,0.99999]))
    plt.xlim(left=0.0)
    plt.show()
