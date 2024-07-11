from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import yfinance as yf
import backtrader as bt


class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=10,  # period for the fast moving average
        pslow=30  # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif self.crossover < 0:  # in the market & cross to the downside
            # close long position
            self.close()


if __name__ == '__main__':
    cerebro = bt.Cerebro()
    df = yf.download('AAPL', start='2010-07-01')
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(SmaCross)
    print('Starting portfolio value %.2f'% cerebro.broker.get_value())
    cerebro.run()
    print('final portfolio value %.2f' % cerebro.broker.get_value())
    cerebro.plot()

