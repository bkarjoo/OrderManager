from Observer import *


class tif_type:
    day = 'DAY'
    ioc = 'IOC'
    opg = 'OPG'


class operation_type:
    new_order = 'N'
    htb_new_order = 'M'
    cancel = 'C'
    none = None


class side_type:
    buy = 'B'
    sell = 'S'
    short = 'T'
    buy_to_cover = 'BC'
    none = None


class channel:
    CSFB = 'CSFB'
    NITE = 'NITE'


class order_type:
    limit = 'L'
    market = 'M'
    stop = 'T'
    moc = '5'
    loc = 'B'


class display_mode:
    hidden = 'N'
    lit = 'Y'


class algo_type:
    twap = '5'
    vwap = '6'


class msg_status_type:
    pending = 'P'
    open = 'O'
    canceled = 'C'
    rejected = 'R'
    executed = 'E'


class order_status_type:
    submitting = 0
    acknowledged = 1  # acknowledged by hydra, but not the exchange
    open = 2
    canceled = 3
    rejected = 4
    partial_open = 5
    partial_canceled = 6
    executed = 7


class Order(object):

    def __init__(self):
        self.statusChangeNotifier = Order.StatusChangeNotifier(self)
        self.account = ''
        self.parent_id = ''
        self.order_id = ''
        self.operation = operation_type.none
        self.symbol = ''
        self.side = side_type.none
        self.quantity = 0
        self.order_price = ''
        self.contra = ''
        self.channel_of_execution = channel.CSFB
        self.tif = ''
        self.type = ''
        self.display = display_mode.lit
        self.stop_limit_price = ''
        self.reserve_size = ''
        self.cancel_replace_id = ''
        self.ticket_id = ''
        self.algo_fields = ''
        self.security_type = ''
        self.security_id = ''
        self.is_submitted = False
        self.cancel_submitted = False
        self.executed_quantity = 0
        self.execution_list = []
        self.status = order_status_type.submitting
        self.error = ''
        self.leaves_qty = 0

    def __str__(self):
        return self.craft_message()

    def craft_message(self):
        pass

    def craft_cancel_message(self):
        pass

    def change_status(self, stat):
        self.status = stat
        self.statusChangeNotifier.notifyObservers(self)

    def get_average_execution_price(self):
        sum_of_shares = 0
        sum_of_dollar_values = 0.0
        for t in self.execution_list:
            sum_of_shares += t[0]
            sum_of_dollar_values += (t[0] * t[1])
        return sum_of_dollar_values / sum_of_shares

    def update_order(self, tokens):
        pass

    class StatusChangeNotifier(Observable):

        def __init__(self, outer):
            Observable.__init__(self)
            self.outer = outer

        def notifyObservers(self, arg):
            self.setChanged()
            Observable.notifyObservers(self, arg)

