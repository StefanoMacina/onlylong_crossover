from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import yfinance as yf
import backtrader as bt

import Strategies


if __name__ == '__main__':
    cerebro = bt.Cerebro()
    df = yf.download('GOOGL', start='2010-07-01')
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(Strategies.Whoa)
    print('Starting portfolio value %.2f' % cerebro.broker.get_value())
    cerebro.run()
    print('final portfolio value %.2f' % cerebro.broker.get_value())
    cerebro.plot()
