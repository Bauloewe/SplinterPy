import time
from typing import List, Tuple, Union, Dict

from SM_Framework.SMBotFramework.api.base.BaseApiCaller import BaseApiCaller
from SM_Framework.SMBotFramework.api.card.CardApi import CardApi
from SM_Framework.SMBotFramework.api.data.Endpoints import BASE_API2, GET_RENT_BY_CARD, GET_RENT_GROUPED, \
    GET_SALE_GROUPED, GET_SALE_BY_CARD, GET_ACTIVE_RENTALS
from SM_Framework.SMBotFramework.api.data.SplinterlandsData import CardItem, MarketResult, MarketGrouped, ActiveRentals
from SM_Framework.SMBotFramework.api.market.MarketAdapter import MarketAdapter
from SM_Framework.SMBotFramework.api.market.MarketUtil import MarketUtil
from SM_Framework.SMBotFramework.api.market.data.MarketHiveTransactions import MarketListing, MarketUpdatePrice, \
    MarketType, CurrencyType, MarketPurchase, CancelRentalWrapper, MarketListingWrapper
from SM_Framework.SMBotFramework.data.Session import Session


class MarketApi:
    base_caller: BaseApiCaller
    adapter: MarketAdapter
    cardApi: CardApi
    util: MarketUtil

    def __init__(self):
        self.base_caller = BaseApiCaller()
        self.adapter = MarketAdapter()
        self.cardApi = CardApi()
        self.util = MarketUtil()

    def get_rent_by_card(self, card: CardItem, session=None):
        return self.get_rent_by_card_param(card.card_detail_id, card.edition, card.gold, session)

    def get_rent_by_card_param(self, card_id: int, edition: int, gold: bool = False, session=None):
        url = BASE_API2 + GET_RENT_BY_CARD
        request: dict = self.adapter.adapt_market_by_card(card_id, edition, gold, session)
        return MarketResult(self.base_caller.call_get(url, request))

    def get_sale_by_card(self, card: CardItem, session=None):
        return self.get_sale_by_card_param(card.card_detail_id, card.edition, card.gold, session)

    def get_sale_by_card_param(self, card_id: int, edition: int, gold: bool = False, session=None):
        url = BASE_API2 + GET_SALE_BY_CARD
        request: dict = self.adapter.adapt_market_by_card(card_id, edition, gold, session)
        return MarketResult(self.base_caller.call_get(url, request))

    def calc_price_per_bcx(self, card: CardItem):
        result: MarketResult = self.get_rent_by_card(card)
        price_per_bcx = []
        for entry in result:
            per_bcx = entry.buy_price / self.cardApi.calc_bcx_param(entry.xp, entry.card_detail_id, entry.edition,
                                                                    entry.gold)
            price_per_bcx.append(per_bcx)

        price_per_bcx.sort(key=lambda x: x, reverse=False)

        return price_per_bcx

    def get_rentals_grouped(self, lvl: str, session: Session = None):
        url: str = BASE_API2 + GET_RENT_GROUPED
        request: dict = self.adapter.adapt_grouped_market(lvl, session)
        return MarketGrouped(self.base_caller.call_get(url, request))

    def get_sales_grouped(self, lvl: str, session: Session = None):
        url: str = BASE_API2 + GET_SALE_GROUPED
        request: dict = self.adapter.adapt_grouped_market(lvl, session)
        return MarketGrouped(self.base_caller.call_get(url, request))

    """
        Executes 10 API calls
        Function to create dictionary which contains all the current market or rental prices.
        The dictionary key structure is: 
        
            detail_id#lvl#edition#gold
            
            e.g. 1#10#1#False 
            for a regular foil max level beta goblin shaman
    """

    def create_market_table(self, market_type: MarketType, session: Session = None):
        market_table = {}
        for lvl in range(1, 11):
            if MarketType.RENTAL == market_type:
                group_result = self.get_rentals_grouped(str(lvl), session)
                self.__add_to_market_table(market_table, group_result)
            elif MarketType.SALE == market_type:
                group_result = self.get_sales_grouped(str(lvl), session)
                self.__add_to_market_table(market_table, group_result)

        return market_table

    def __add_to_market_table(self, table: Dict[str, float], market_groups: MarketGrouped):

        for group in market_groups:
            pattern: str = str(group.card_detail_id) + "#"
            pattern += str(group.level) + "#"
            pattern += str(group.edition) + "#"
            pattern += str(group.gold)

            table[pattern] = group

    def create_listing(self, session: Session, order_type: str, order_fee: int, orders: List[Tuple[str, float]]):
        listings: MarketListingWrapper = MarketListingWrapper(order_type, order_fee, orders)

        for trx in listings.listing_trx:
            request = trx.__dict__

            session.hive.custom_json("sm_market_list", json_data=request, required_posting_auths=[session.user])

            time.sleep(3)

    def update_prices(self, session: Session, orders: List[Tuple[str, float]]):
        orders: MarketUpdatePrice = MarketUpdatePrice(orders)
        for order in orders.orders.values():
            session.hive.custom_json("sm_update_price", json_data=order.__dict__,
                                     required_auths=[session.user])

    def cancel_rental(self, session: Session, rentals: List[str]):
        rentals = CancelRentalWrapper(rentals)
        for trx in rentals.cancel_rental_trx:
            request = trx.__dict__
            trx_id = session.hive.custom_json("sm_market_cancel_rental", json_data=request, required_posting_auths=[session.user])["trx_id"]
            print("Canceling rentals" + trx_id)
            time.sleep(3)

    def purchase_cards(self, session: Session, currency: CurrencyType, market_ids: List[Tuple[str, float]],
                       ignore_price: bool = False, all_or_none: bool = False):
        market_purchase = MarketPurchase(currency, market_ids)
        for trx in market_purchase.purchase_trx:
            request = trx.__dict__
            if ignore_price:
                request.pop('price', None)
            print(session.hive.custom_json("sm_market_purchase", json_data=request, required_auths=[session.user])[
                      "trx_id"])

    def getBestPriceForCard(self, card_id: int, edition: int, bcx: int, gold: bool = False, session=None):
        listings: MarketResult = self.get_sale_by_card_param(card_id, edition, gold, session)
        price_nodes: Dict[str, Tuple] = {}
        for listing in listings:
            bcx = self.cardApi.calc_bcx_param(listing.xp, listing.card_detail_id, listing.edition, listing.gold)
            price_nodes[listing.uid] = (listing.uid, listing.market_id, listing.buy_price, bcx)

    def get_active_rentals(self, owner: str, renter: str, limit: int, skip: int, session: Session = None):
        url: str = BASE_API2 + GET_ACTIVE_RENTALS
        request: dict = self.adapter.adapt_active_rentals(owner, renter, limit, skip, session)
        return ActiveRentals(self.base_caller.call_get(url, request))

    def get_all_active_rentals(self, owner: str, renter: str, limit: int, session: Session = None):
        url: str = BASE_API2 + GET_ACTIVE_RENTALS
        skip = 0
        active_rentals = []
        response_list = []
        while skip == 0 or response_list:
            request: dict = self.adapter.adapt_active_rentals(owner, renter, limit, skip, session)
            response_list = self.base_caller.call_get(url, request)
            print(len(response_list))
            active_rentals += response_list
            skip += limit
        return ActiveRentals(active_rentals)

