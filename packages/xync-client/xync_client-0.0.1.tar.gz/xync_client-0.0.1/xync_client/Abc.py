import logging
from abc import abstractmethod

from aiohttp import ClientResponse
from aiohttp.http_exceptions import HttpProcessingError
from x_client.aiohttp import Client
from xync_schema.models import Agent, Ex, User, OrderStatus, Coin, Cur, Order, Pm, PmType, Ad, AdStatus
from xync_schema.pydantic import FiatForm


class OrderOutClient:
    def __init__(self, cl: Client, order: Order):
        self.cl: Client = cl
        self.order: Order = order

    # 2: [T] Отмена запроса на сделку
    @abstractmethod
    async def cancel_request(self) -> Order: ...

    # 3: [M] Одобрить запрос на сделку
    @abstractmethod
    async def accept_request(self) -> bool: ...

    # 4: [M] Отклонить запрос на сделку
    @abstractmethod
    async def reject_request(self) -> bool: ...

    # 5: [B] Перевод сделки в состояние "оплачено", c отправкой чека
    @abstractmethod
    async def mark_payed(self, receipt): ...

    # 6: [B] Отмена сделки
    @abstractmethod
    async def cancel_order(self) -> bool: ...

    # 7: [S] Подтвердить получение оплаты
    @abstractmethod
    async def confirm(self) -> bool: ...

    # 9, 10: [S, B] Подать аппеляцию cо скриншотом / видео / файлом
    @abstractmethod
    async def start_appeal(self, file) -> bool: ...

    # 11, 12: [S, B] Встречное оспаривание полученной аппеляции cо скриншотом / видео / файлом
    @abstractmethod
    async def dispute_appeal(self, file) -> bool: ...

    # 15: [B, S] Отмена аппеляции
    @abstractmethod
    async def cancel_appeal(self) -> bool: ...

    # 16: Отправка сообщения юзеру в чат по ордеру с приложенным файлом
    @abstractmethod
    async def send_order_msg(self, msg: str, file=None) -> bool: ...

    # 17: Отправка сообщения по апелляции
    @abstractmethod
    async def send_appeal_msg(self, file, msg: str = None) -> bool: ...


class PublicClient(Client):
    ex: Ex

    def __init__(self, ex: Ex):
        self.ex = ex
        super().__init__(ex.host_p2p)

    # 21: Список поддерживаемых валют
    @abstractmethod
    async def curs(self) -> list[Cur]: ...

    # 22: Список торгуемых монет (с ограничениям по валютам, если есть)
    @abstractmethod
    async def coins(self, cur: Cur = None) -> list[Coin]: ...

    # 23: Список платежных методов по каждой валюте
    @abstractmethod
    async def pms(self, cur: Cur) -> list[Pm]: ...

    # 24: Список объяв по (buy/sell, cur, coin, pm)
    @abstractmethod
    async def ads(self, coin: Coin, cur: Cur, is_sell: bool, pms: list[Pm] = None) -> list[Ad]: ...


class AgentClient(Client):
    def __init__(self, agent: Agent):
        self.agent: Agent = agent
        assert isinstance(agent.ex, Ex), "`ex` should be fetched in `agent`"
        assert agent.ex.host_p2p, "`ex.host_p2p` shouldn't be empty"
        self.meth = {
            "GET": self._get,
            "POST": self._post,
        }
        super().__init__(agent.ex.host_p2p)

    # -1: Login: returns auth headers dict
    @abstractmethod
    async def _get_auth_hdrs(self) -> dict[str, str]: ...

    async def login(self) -> None:
        auth_hdrs: dict[str, str] = await self._get_auth_hdrs()
        self.session.headers.update(auth_hdrs)

    # 0: Получшение ордеров в статусе status, по монете coin, в валюте coin, продаже(is_sell=True)/покупке(is_sell=False)
    @abstractmethod
    async def get_orders(
        self, stauts: OrderStatus = OrderStatus.active, coin: Coin = None, cur: Cur = None, is_sell: bool = None
    ) -> list[Order]: ...

    # 1: [T] Получшение ордеров в статусе status, по монете coin, в валюте coin, продаже(is_sell=True)/покупке(is_sell=False)
    @abstractmethod
    async def order_request(self, ad_id: int, amount: float) -> Order: ...

    # async def start_order(self, order: Order) -> OrderOutClient:
    #     return OrderOutClient(self, order)

    # # # Fiat
    # 25: Список реквизитов моих платежных методов
    @abstractmethod
    async def my_fiats(self, cur: Cur = None) -> list[FiatForm]: ...

    # 26: Создание
    @abstractmethod
    async def fiat_new(self, fiat: FiatForm) -> FiatForm: ...

    # 27: Редактирование
    @abstractmethod
    async def fiat_upd(self, detail: str = None, type_: PmType = None) -> bool: ...

    # 28: Удаление
    @abstractmethod
    async def fiat_del(self, fiat_id: int) -> bool: ...

    # # # Ad
    # 29: Список моих ad
    @abstractmethod
    async def my_ads(self) -> list[Ad]: ...

    # 30: Создание ad:
    @abstractmethod
    async def ad_new(
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
    @abstractmethod
    async def ad_upd(
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
    @abstractmethod
    async def ad_del(self) -> bool: ...

    # 33: Вкл/выкл объявления
    @abstractmethod
    async def ad_switch(self) -> bool: ...

    # 34: Вкл/выкл всех объявлений
    @abstractmethod
    async def ads_switch(self) -> bool: ...

    # # # User
    # 35: Получить объект юзера по его ид
    @abstractmethod
    async def get_user(self, user_id) -> User: ...

    # 36: Отправка сообщения юзеру с приложенным файло
    @abstractmethod
    async def send_user_msg(self, msg: str, file=None) -> bool: ...

    # 37: (Раз)Блокировать юзера
    @abstractmethod
    async def block_user(self, is_blocked: bool = True) -> bool: ...

    # 38: Поставить отзыв юзеру
    @abstractmethod
    async def rate_user(self, positive: bool) -> bool: ...

    async def _proc(self, resp: ClientResponse, data: dict = None) -> dict | str:
        try:
            return await super()._proc(resp)
        except HttpProcessingError as e:
            if e.code == 401:
                logging.warning(e)
                await self.login()
                res = await self.meth[resp.method](resp.url.path, data)
                return res
