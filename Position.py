class Position(object):

    def __init__(self, symbol, qty=0, price=0.0):
        self.symbol = symbol
        self.qty = qty # total qty buys - sells
        self.transactions = []
        if qty != 0:
            self.transactions.append(qty*price*-1)

    def dollar_value(self):
        return sum(self.transactions)

    def add_fill(self, qty, price):
        self.transactions.append(qty*price*-1)
        self.qty += qty

    def open_pnl(self, current_price):
        return self.dollar_value() + (self.qty * current_price)

    # def current_state(self, current_price):
    #     return '{}\t{}\t{}'.format(
    #         self.qty, self.dollar_value(), self.open_pnl(current_price)
    #     )

# p = Position('SPY', 100, 20)
# print p.current_state(20)
# p.add_fill(-100,10)
# print p.current_state(20)
# p.add_fill(100,10)
# print p.current_state(20)
# p.add_fill(-100,15)
# print p.current_state(20)
# p.add_fill(100,15)
# print p.current_state(20)
# p.add_fill(100,20)
# print p.current_state(20)
# p.add_fill(-100,25)
# print p.current_state(20)
# p.add_fill(-100,30)
# print p.current_state(20)
#
