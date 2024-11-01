from typing import Protocol

from xync_schema.models import Agent, Ex, User, OrderStatus, Coin, Cur, Order, Fiat, Pm, PmType, Ad, AdStatus


class AgentProto(Protocol):
    property()

    def __init__(self, agent: Agent):
        self.agent: Agent = agent
        self.public: AgentProto.PublicProto = AgentProto.PublicProto(agent.ex)
        self.pre_url: str = agent.ex.host

    # 0: Получшение ордеров в статусе status, по монете coin, в валюте coin, продаже(is_sell=True)/покупке(is_sell=False)
    def get_orders(
        self, stauts=OrderStatus.active, coin: Coin = None, cur: Cur = None, is_sell: bool = None
    ) -> list[Order]: ...

    class OrderProto(Protocol):
        def __init__(self, order: Order):
            self.order: Order = order

        # 1: [T] Получшение ордеров в статусе status, по монете coin, в валюте coin, продаже(is_sell=True)/покупке(is_sell=False)
        def order_request(self, ad_id: int, amount: float) -> Order: ...

        # 2: [T] Отмена запроса на сделку
        def cancel_request(self, ad_id: int, amount: float) -> Order: ...

        # 3: [M] Одобрить запрос на сделку
        def accept_request(self) -> bool: ...

        # 4: [M] Отклонить запрос на сделку
        def reject_request(self) -> bool: ...

        # 5: [B] Перевод сделки в состояние "оплачено", c отправкой чека
        def mark_payed(self, receipt): ...

        # 6: [B] Отмена сделки
        def cancel_order(self) -> bool: ...

        # 7: [S] Подтвердить получение оплаты
        def confirm(self) -> bool: ...

        # 9, 10: [S, B] Подать аппеляцию cо скриншотом / видео / файлом
        def start_appeal(self, file) -> bool: ...

        # 11, 12: [S, B] Встречное оспаривание полученной аппеляции cо скриншотом / видео / файлом
        def dispute_appeal(self, file) -> bool: ...

        # 15: [B, S] Отмена аппеляции
        def cancel_appeal(self) -> bool: ...

        # 16: Отправка сообщения юзеру в чат по ордеру с приложенным файлом
        def send_order_msg(self, msg: str, file=None) -> bool: ...

        # 17: Отправка сообщения по апелляции
        def send_appeal_msg(self, file, msg: str = None) -> bool: ...

    class PublicProto(Protocol):
        def __init__(self, ex: Ex):
            self.ex: Ex = ex

        # 21: Список поддерживаемых валют
        def curs(self) -> list[Cur]: ...

        # 22: Список торгуемых монет (с ограничениям по валютам, если есть)
        def coins(self, cur: Cur = None) -> list[Coin]: ...

        # 23: Список платежных методов по каждой валюте
        def pms(self, cur: Cur) -> list[Pm]: ...

        # 24: Список объяв по (buy/sell, cur, coin, pm)
        def ads(self, coin: Coin, cur: Cur, is_sell: bool, pms: list[Pm] = None) -> list[Ad]: ...

    # # # Fiat
    # 25: Список реквизитов моих платежных методов
    def my_fiats(self, cur: Cur = None) -> list[Fiat]: ...

    # 26: Создание
    def fiat_new(self, cur: Cur, pm: Pm, detail: str, type_: PmType = None) -> Fiat: ...

    # 27: Редактирование
    def fiat_upd(self, detail: str = None, type_: PmType = None) -> bool: ...

    # 28: Удаление
    def fiat_del(self, fiat_id: int) -> bool: ...

    # # # Ad
    # 29: Список моих ad
    def my_ads(self) -> list[Ad]: ...

    # 30: Создание ad:
    def ad_new(
        self,
        coin: Coin,
        cur: Cur,
        is_sell: bool,
        pms: list[Pm],
        price: float,
        is_float: bool = True,
        min_fiat: int = None,
        details: str = None,
        autoreply: str = None,
        status: AdStatus = AdStatus.active,
    ) -> Ad: ...

    # 31: Редактирование
    def ad_upd(
        self,
        pms: [Pm] = None,
        price: float = None,
        is_float: bool = None,
        min_fiat: int = None,
        details: str = None,
        autoreply: str = None,
        status: AdStatus = None,
    ) -> bool: ...

    # 32: Удаление
    def ad_del(self) -> bool: ...

    # 33: Вкл/выкл объявления
    def ad_switch(self) -> bool: ...

    # 34: Вкл/выкл всех объявлений
    def ads_switch(self) -> bool: ...

    # # # User
    # 35: Получить объект юзера по его ид
    def get_user(self, user_id) -> User: ...

    # 36: Отправка сообщения юзеру с приложенным файло
    def send_user_msg(self, msg: str, file=None) -> bool: ...

    # 37: (Раз)Блокировать юзера
    def block_user(self, is_blocked: bool = True) -> bool: ...

    # 38: Поставить отзыв юзеру
    def rate_user(self, positive: bool) -> bool: ...
