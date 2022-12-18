from enum import Enum
from typing import List, Tuple, Dict


class MarketListing:
    """
    @param order_type: type of the order rent, sell etc
    @params order_fee: fee of the order taken by the marketplace, integer e.g. 500 = 5% .
    @param orders: List of Tuples where the first argument is the uid and the second the price in DEC
    """

    def __init__(self, order_type: str, order_fee: int, orders: List[Tuple[str, float]]):
        if orders:
            self.cards = []
            for order in orders:
                self.cards.append([order[0], order[1]])

        self.type = order_type
        self.fee = order_fee


class MarketListingWrapper:

    def __init__(self, order_type: str, order_fee: int, orders: List[Tuple[str, float]]):
        self.listing_trx: List[MarketListing] = []
        if orders:
            temp_listings = []
            estimated_trx_len = 0

            for order in orders:

                temp_listings.append(order)
                estimated_trx_len += 2  # opening square bracket + comma
                estimated_trx_len += len(order[0])
                estimated_trx_len += len(str(order[1]))
                estimated_trx_len += 2  # closing square bracket + comma

                if estimated_trx_len > 7000:
                    listing_item = MarketListing(order_type,order_fee, temp_listings)
                    temp_listings = []
                    estimated_trx_len = 0

                    self.listing_trx.append(listing_item)

            if temp_listings:
                listing_item = MarketListing(order_type, order_fee, temp_listings)
                self.listing_trx.append(listing_item)


class MarketUpdatePrice:
    class UpdatePriceItem:

        def __init__(self, price: float, market_id: str = None):
            self.ids: List[str] = []
            if market_id:
                self.ids.append(market_id)
            self.new_price: float = price

        def append_id(self, market_id: str):
            if market_id:
                self.ids.append(market_id)

    """
        @param orders: List of Tuples where the first argument is the market id and the second the updated sprice in DEC

    """

    def __init__(self, orders_items: List[Tuple[str, float]]):
        self.orders: Dict = {}

        if orders_items:
            for order in orders_items:
                order_entry = self.orders.get(order[1], self.UpdatePriceItem(order[1]))
                order_entry.append_id(order[0])
                self.orders[order[1]] = order_entry


class CancelRental:

    def __init__(self, items: List[str]):
        self.items: List[str] = items


class CancelRentalWrapper:

    def __init__(self, rentals: List[str]):
        self.cancel_rental_trx: List[CancelRental] = []
        if rentals:
            rental_ids = []

            estimated_trx_len = 0
            for rental in rentals:

                rental_ids.append(rental)
                estimated_trx_len += len(rental)

                if estimated_trx_len > 7000:
                    cancel_item = CancelRental(rental_ids)
                    rental_ids = []
                    estimated_trx_len = 0

                    self.cancel_rental_trx.append(cancel_item)

            if rental_ids:
                cancel_item = CancelRental(rental_ids)
                self.cancel_rental_trx.append(cancel_item)


class MarketType(Enum):
    RENTAL = 0
    SALE = 1


class CurrencyType(Enum):
    DEC = "DEC"
    CREDIT = "CREDITS"


class MarketPurchase:
    class MarketPurchaseItem:
        items: List[str]
        price: float
        currency: str

        def __init__(self, price: float, currency: CurrencyType, market_ids: List[str]):
            self.items = []
            if market_ids:
                self.items = market_ids
            self.price = price
            self.currency = currency.value

    purchase_trx: List[MarketPurchaseItem] = []

    def __init__(self, currency: CurrencyType, orders: List[Tuple[str, float]]):
        if orders:
            market_ids = []
            total_price = 0
            estimated_trx_len = 0
            for order in orders:
                total_price += order[1]
                market_ids.append(order[0])
                estimated_trx_len += len(order[0])

                if estimated_trx_len > 7000:
                    market_item = self.MarketPurchaseItem(total_price, currency, market_ids)
                    market_ids = []
                    total_price = 0
                    estimated_trx_len = 0

                    self.purchase_trx.append(market_item)

            if market_ids:
                market_item = self.MarketPurchaseItem(total_price, currency, market_ids)
                self.purchase_trx.append(market_item)
