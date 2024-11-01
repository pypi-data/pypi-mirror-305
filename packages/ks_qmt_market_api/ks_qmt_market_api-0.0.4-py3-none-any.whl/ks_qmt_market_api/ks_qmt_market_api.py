from futu import *
from datetime import datetime, timedelta
from xtquant import xtdata
from ks_trade_api.utility import extract_vt_symbol
from ks_trade_api.constant import (
    CHINA_TZ, US_EASTERN_TZ,
    Exchange as KsExchange, Product as KsProduct, SubscribeType as KsSubscribeType,
    RetCode as KsRetCode, RET_OK as KS_RET_OK, RET_ERROR as KS_RET_ERROR, ErrorCode as KsErrorCode
)
from ks_trade_api.object import (
    ErrorData, ContractData, MyTickData, MyBookData, MyRawTickData, QuoteData
)
from ks_utility import datetimes
from ks_utility.numbers import to_decimal
from decimal import Decimal
from dateutil.parser import parse
from ks_trade_api.base_market_api import BaseMarketApi
from typing import Optional, Union
from logging import DEBUG, INFO, WARNING, ERROR
import pytz

PRODUCT_MY2KS = {
    SecurityType.STOCK: KsProduct.EQUITY,
    SecurityType.DRVT: KsProduct.OPTION
}

RET_KS2MY = {
    KS_RET_OK: RET_OK,
    KS_RET_ERROR: RET_ERROR
}

RET_MY2KS = { v:k for k,v in RET_KS2MY.items() }

MARKET_KS2MY = {
    KsExchange.SEHK: TrdMarket.HK,
    KsExchange.SMART: TrdMarket.US,
    KsExchange.SSE: 'SH',
    KsExchange.SZSE: 'SZ'
}

MARKET_MY2KS = { v:k for k,v in MARKET_KS2MY.items() }

def symbol_ks2my(vt_symbol: str):
    if not vt_symbol:
        return ''
    symbol, ks_exchange = extract_vt_symbol(vt_symbol)
    return f'{symbol}.{MARKET_KS2MY.get(ks_exchange)}'

SUBTYPE_KS2MY = {
    KsSubscribeType.USER_ORDER: KsSubscribeType.USER_ORDER,
    KsSubscribeType.USER_TRADE: KsSubscribeType.USER_TRADE,
    KsSubscribeType.USER_POSITION: KsSubscribeType.USER_POSITION,
    KsSubscribeType.TRADE: SubType.TICKER,
    KsSubscribeType.BOOK: SubType.ORDER_BOOK
}

MAX_FLOAT = sys.float_info.max 
def adjust_price(price: float) -> float:
    """将异常的浮点数最大值（MAX_FLOAT）数据调整为0"""
    if price == MAX_FLOAT:
        price = 0
    return price

def extract_my_symbol(my_symbol: str):
    symbol, my_exchange_str = my_symbol.split('.')
    return symbol, MARKET_MY2KS.get(my_exchange_str)


class KsQmtMarketApi(BaseMarketApi):
    gateway_name: str = 'KS_QMT'

    def __init__(self, setting: dict):
        gateway_name = setting.get('gateway_name', self.gateway_name)
        dd_secret = setting.get('dd_secret')
        dd_token = setting.get('dd_token')
        super().__init__(gateway_name=gateway_name, dd_secret=dd_secret, dd_token=dd_token)

        self.init_handlers()


    # 初始化行回调和订单回调
    def init_handlers(self):
        pass

        

        

    # 订阅行情
    def subscribe(self, vt_symbols, vt_subtype_list, extended_time=True) -> tuple[KsRetCode, Optional[ErrorData]]:
        if not vt_symbols:
            return KS_RET_OK, None
        
        if isinstance(vt_symbols, str):
            vt_symbols = [vt_symbols]

        my_symbols = [symbol_ks2my(x) for x in vt_symbols]
        my_subtype_list = [SUBTYPE_KS2MY.get(x) for x in vt_subtype_list]

        trade = self
        if KsSubscribeType.USER_ORDER in my_subtype_list:
            my_subtype_list.remove(KsSubscribeType.USER_ORDER)     

        if KsSubscribeType.USER_TRADE in my_subtype_list:
            my_subtype_list.remove(KsSubscribeType.USER_TRADE)

        # futu没有持仓回调
        if KsSubscribeType.USER_POSITION in my_subtype_list:
            my_subtype_list.remove(KsSubscribeType.USER_POSITION)

        # 剩下的是订阅行情
        if my_subtype_list:
            for my_symbol in my_symbols:
                code = xtdata.subscribe_quote(my_symbol, period='tick', count=-1, callback=self._handle_tick_data)
                if code == -1:
                    return KS_RET_ERROR, None

        return KS_RET_OK, None
    
    def _handle_tick_data(self, data):
        for my_symbol, data in data.items():
            data = data[-1]
            symbol, exchange = extract_my_symbol(my_symbol)
            
            dt: datetime = datetime.fromtimestamp(data['time']/1000)
            dt: datetime = dt.replace(tzinfo=CHINA_TZ)
            tick: MyTickData = MyTickData(
                symbol=symbol,
                exchange=exchange,
                datetime=dt,
                name=symbol,
                volume=data["volume"],
                last_price=adjust_price(data["lastPrice"]),
                open_price=adjust_price(data["open"]),
                high_price=adjust_price(data["high"]),
                low_price=adjust_price(data["low"]),
                pre_close=adjust_price(data["lastClose"]),
                gateway_name=self.gateway_name
            )
            tick.settlement_price = tick.last_price
            tick.pre_settlement_price = tick.pre_close

            book: MyBookData = MyBookData(
                gateway_name=self.gateway_name,
                symbol=symbol,
                exchange=exchange,
                datetime=dt,
            )

            for index, bid_price in enumerate(data['bidPrice']):
                i = index + 1
                # breakpoint()
                bid_price = to_decimal(bid_price)
                bid_volume = to_decimal(data['bidVol'][index])
                ask_price = to_decimal(data['askPrice'][index])
                ask_volume = to_decimal(data['askVol'][index])

                setattr(tick, f'bid_price_{i}', bid_price)
                setattr(tick, f'bid_volume_{i}', bid_volume)
                setattr(tick, f'ask_price_{i}', ask_price)
                setattr(tick, f'ask_volume_{i}', ask_volume)

                setattr(book, f'bid_price_{i}', bid_price)
                setattr(book, f'bid_volume_{i}', bid_volume)
                setattr(book, f'ask_price_{i}', ask_price)
                setattr(book, f'ask_volume_{i}', ask_volume)
            
            self.on_book(book)
            self.on_tick(tick)

            
            

              
    def get_error(self, *args, **kvargs):
        method = sys._getframe(1).f_code.co_name
        error = ErrorData(
            code=kvargs.get('code'),
            msg=kvargs.get('msg'),
            method=method,
            args=args,
            kvargs=kvargs,
            traceback=traceback.format_exc(),
            gateway_name=self.gateway_name
        )
        self.log(error, tag=f'api_error.{method}', level=ERROR)
        return error

    # 获取静态信息
    def query_contract(self, vt_symbol: str) -> tuple[KsRetCode, ContractData]:
        symbol, exchange = extract_vt_symbol(vt_symbol)
        my_symbol = symbol_ks2my(vt_symbol)
        data = xtdata.get_instrument_detail(my_symbol)

        product: KsProduct = KsProduct.EQUITY
        lot_size: Decimal = Decimal('100')
        size: int = Decimal('1') if product == KsProduct.EQUITY else lot_size
        min_volume: int = lot_size if product == KsProduct.EQUITY else Decimal('1')
        contract = ContractData(
            symbol=data['InstrumentID'],
            exchange=MARKET_MY2KS[data['ExchangeID']],
            name=data["InstrumentName"],
            product=product,
            size=size,
            min_volume=min_volume,
            # size=100, # todo 暴力使用100，以后使用期权再说
            pricetick=Decimal(str(data["PriceTick"])),
            gateway_name=self.gateway_name
        )
        return KS_RET_OK, contract
    
    # 获取静态信息
    def query_contracts(self, vt_symbols: str) -> tuple[KsRetCode, list[ContractData]]:
        contracts: list[ContractData] = []
        for vt_symbol in vt_symbols:
            ret, contract = self.query_contract(vt_symbol)
            if ret == KS_RET_ERROR:
                return ret, contract
            contracts.append(contract)
        return KS_RET_OK, contracts
    
    def query_book(self, vt_symbol: str) -> tuple[KsRetCode,  MyBookData]:
        my_symbol = symbol_ks2my(vt_symbol)
        ret_sub, sub_data = self.quote_ctx.subscribe([my_symbol], [SubType.ORDER_BOOK], subscribe_push=False)
        # 先订阅买卖摆盘类型。订阅成功后 OpenD 将持续收到服务器的推送，False 代表暂时不需要推送给脚本
        ret_code = RET_ERROR
        ret_data = None
        if ret_sub == RET_OK:  # 订阅成功
            ret, data = self.quote_ctx.get_order_book(my_symbol, num=5)  # 获取一次 3 档实时摆盘数据
            if ret == RET_OK:
                ret_code = KS_RET_OK
                ret_data = self.book_my2ks(data)
            else:
                ret_data = ret_data
        else:
            ret_data = sub_data
        return ret_code, ret_data
    
    def book_my2ks(self, data) -> MyBookData:
        symbol, exchange = extract_my_symbol(data['code'])
        book: MyBookData = MyBookData(
            symbol=symbol,
            exchange=exchange,
            datetime=datetimes.now(),
            name=symbol,
            gateway_name=self.gateway_name
        )

        for index, bid_item in enumerate(data['Bid']):
            i = index + 1
            
            bid_price = Decimal(str(bid_item[0]))
            bid_volume = Decimal(str(bid_item[1]))
            
            setattr(book, f'bid_price_{i}', bid_price)
            setattr(book, f'bid_volume_{i}', bid_volume)
            
            if data['Ask']:
                ask_item = data['Ask'][index]
                ask_price = Decimal(str(ask_item[0]))
                ask_volume = Decimal(str(ask_item[1]))
                setattr(book, f'ask_price_{i}', ask_price)
                setattr(book, f'ask_volume_{i}', ask_volume)
        return book
    
    def query_quotes(self, vt_symbols: list[str]) -> Union[KsRetCode, list[QuoteData]]:
        if not vt_symbols:
            return KsRetCode, []
        
        my_symbols = [symbol_ks2my(x) for x in vt_symbols]

        res: dict = xtdata.get_full_tick(my_symbols)
        quotes = []
        for my_symbol, quote in res.items():
            symbol, exchange = extract_my_symbol(my_symbol)
            quote: dict = res[my_symbol]
            quotes.append(QuoteData(
                gateway_name=self.gateway_name,
                symbol=symbol,
                exchange=exchange,
                datetime=parse(quote['timetag']).astimezone(pytz.timezone('PRC')),
                volume=Decimal(quote['volume']),
                # turnover=Decimal(quote.turnover),
                last_price=quote['lastPrice'],
                open_price=quote['open'],
                high_price=quote['high'],
                low_price=quote['low'],
                pre_close=quote['lastClose'],
                localtime=datetimes.now()
            ))
        
    def query_ticks(self, vt_symbol: str, length: int = 1) -> Union[KsRetCode, list[MyRawTickData]]:
        if not vt_symbol:
            return KsRetCode, []
        
        my_symbol = symbol_ks2my(vt_symbol)
        ret_sub, data_sub = self.quote_ctx.subscribe([my_symbol], [SubType.TICKER], subscribe_push=False, extended_time=True)
        # 先订阅 K 线类型。订阅成功后 OpenD 将持续收到服务器的推送，False 代表暂时不需要推送给脚本
        if ret_sub == RET_OK:  # 订阅成功
            ret_quote, data_quote = self.quote_ctx.get_rt_ticker(my_symbol, length)  # 获取订阅股票报价的实时数据
            quotes: list[QuoteData] = []
            if ret_quote == RET_OK:
                for index, quote in data_quote.iterrows():
                    symbol, exchange = extract_my_symbol(quote.code)
                    tz = CHINA_TZ if exchange == KsExchange.SEHK else US_EASTERN_TZ
                    dt = tz.localize(parse(f'{quote.time}')).astimezone(CHINA_TZ)
                    quotes.append(MyRawTickData(
                        gateway_name=self.gateway_name,
                        symbol=symbol,
                        exchange=exchange,
                        datetime=dt,
                        volume=Decimal(str(quote.volume)),
                        last_price=Decimal(str(quote.price))
                    ))
                return KS_RET_OK, quotes
            else:
                return KS_RET_ERROR, self.get_error(vt_symbol=vt_symbol, msg=data_quote)
        else:
            return KS_RET_ERROR, self.get_error(vt_symbol=vt_symbol, msg=data_sub)


    # 关闭上下文连接
    def close(self):
        pass
        # self.quote_ctx.close()


        