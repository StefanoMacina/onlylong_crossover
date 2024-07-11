from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from datetime import datetime
import yfinance as yf
import backtrader as bt
import pandas as pd
import Strategies
import mplfinance as mpf



if __name__ == '__main__':

    cerebro = bt.Cerebro()
    df = yf.download('GOOGL', start='2010-07-01')
    cerebro.adddata(bt.feeds.PandasData(dataname=df))
    cerebro.addstrategy(Strategies.SmaCross)
    cerebro.addsizer(bt.sizers.PercentSizer, percents=2)
    print('portfolio starting value %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('portfolio final value %.2f' % cerebro.broker.getvalue())
    cerebro.plot()

    #print(df)

