class OrderFactory(object):

    def __init__(self):
        pass

    def generate_limit_order(self, qty, symbol, price, acct):
        pass

    def generate_opg_market_order(self, qty, symbol, acct):
        pass

    def generate_moc_market_order(self, qty, symbol, acct):
        pass

    def generate_opg_limit_order(self, qty, symbol, price, acct):
        pass

    def generate_loc_limit_order(self, qty, symbol, price, acct):
        pass

    def generate_nite_vwap_order(self, qty, symbol, start_time, end_time, stop_price, acct):
        pass

    def generate_stop_limit_order(self, qty, symbol, stop_price, stop_limit, acct):
        pass

    def generate_stop_market_order(self, qty, symbol, stop_price, acct):
        pass

    def sell_command(self, command):
        pass

    def buy_command(self, command):
        pass
