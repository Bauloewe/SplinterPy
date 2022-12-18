from typing import List, Dict


class Settings:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.submit_hashed_team: str = values.get("submit_hashed_team", None)
        self.mute_all: bool = values.get("mute_all", None)
        self.hide_results: bool = values.get("hide_results", None)
        self.notifications_enabled: bool = values.get("notifications_enabled", None)
        self.use_vessel: bool = values.get("use_vessel", None)
        self.default_currency: str = values.get("default_currency", None)
        self.disable_potions_reward_cards: bool = values.get("disable_potions_reward_cards", None)


class MessageItems:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.id: float = values.get("id", None)
        self.player: str = values.get("player", None)
        self.type: str = values.get("type", None)
        self.created_date: str = values.get("created_date", None)
        self.read_date: str = values.get("read_date", None)
        self.data: str = values.get("data", None)


class Messages(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [MessageItems(value) for value in values]


class BalanceItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.player: str = values.get("player", None)
        self.token: str = values.get("token", None)
        self.balance: str = values.get("balance", None)


class Balances(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [BalanceItem(value) for value in values]


class Quest:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.id: str = values.get("id", None)
        self.player: str = values.get("player", None)
        self.created_date: str = values.get("created_date", None)
        self.created_block: float = values.get("created_block", None)
        self.name: str = values.get("name", None)
        self.total_items: float = values.get("total_items", None)
        self.completed_items: float = values.get("completed_items", None)
        self.claim_trx_id: str = values.get("claim_trx_id", None)
        self.claim_date: str = values.get("claim_date", None)
        self.reward_qty: float = values.get("reward_qty", None)
        self.refresh_trx_id: str = values.get("refresh_trx_id", None)
        self.rewards: str = values.get("rewards", None)


class SeasonReward:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.reward_packs: str = values.get("reward_packs", None)


class Skins(list):
    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [SkinItem(value) for value in values]


class SkinItem:
    def __init__(self, values: dict):
        self.player: float = values.get("player", None)
        self.card_detail_id: int = values.get("card_detail_id", None)
        self.skin: str = values.get("skin", None)
        self.qty: int = values.get("qty", None)
        self.active: bool = values.get("active", None)


class DetailItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.id: float = values.get("id", None)
        self.name: str = values.get("name", None)
        self.type: str = values.get("type", None)
        self.sub_type: str = values.get("sub_type", None)
        self.data: str = values.get("data", None)
        self.transferable: bool = values.get("transferable", None)
        self.consumable: str = values.get("consumable", None)
        self.print_limit: str = values.get("print_limit", None)
        self.total_printed: float = values.get("total_printed", None)
        self.image_filename: str = values.get("image_filename", None)
        self.rarity: str = values.get("rarity", None)


class DetailItems(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [DetailItem(value) for value in values]


class Announcement:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.url: str = values.get("url", None)
        self.title: str = values.get("title", None)
        self.date: str = values.get("date", None)
        self.content: str = values.get("content", None)


class DidYouKnow(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [DidYouItems(value) for value in values]


class DidYouItems:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.title: str = values.get("title", None)
        self.content: str = values.get("content", None)
        self.url: str = values.get("url", None)


class DailyUpdates:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.enabled: bool = values.get("enabled", None)
        self.announcement = Announcement(values=values.get("announcement"))
        self.did_you_know: List[DidYouItems] = DidYouKnow(values=values.get("did_you_know"))


class Dyk:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.tips: List[str] = values.get("tips", None)
        self.lore: List[str] = values.get("lore", None)


class VerificationStatus:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.player: str = values.get("player", None)
        self.created_date: str = values.get("created_date", None)
        self.status: str = values.get("status", None)


# TODO add correct implementation
class SeasonDetails:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}


class PlayerDetails:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.name: str = values.get("name", None)
        self.join_date: str = values.get("join_date", None)
        self.rating: str = values.get("rating", None)
        self.battles: float = values.get("battles", None)
        self.wins: float = values.get("wins", None)
        self.current_streak: float = values.get("current_streak", None)
        self.longest_streak: float = values.get("longest_streak", None)
        self.max_rating: float = values.get("max_rating", None)
        self.max_rank: float = values.get("max_rank", None)
        self.champion_points: float = values.get("champion_points", None)
        self.capture_rate: float = values.get("capture_rate", None)
        self.last_reward_block: float = values.get("last_reward_block", None)
        self.guild: str = values.get("guild", None)
        self.starter_pack_purchase: bool = values.get("starter_pack_purchase", None)
        self.avatar_id: str = values.get("avatar_id", None)
        self.display_name: str = values.get("display_name", None)
        self.title_pre: str = values.get("title_pre", None)
        self.title_post: str = values.get("title_post", None)
        self.collection_power: float = values.get("collection_power", None)
        self.league: str = values.get("league", None)
        self.adv_msg_sent: str = values.get("adv_msg_sent", None)
        self.season_details = SeasonDetails(values=values.get("season_details"))


class Airdrop(list):
    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [AirdropItems(value) for value in values]


class AirdropItems:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.airdrop_day: float = values.get("airdrop_day", None)
        self.airdrop_date: str = values.get("airdrop_date", None)
        self.platform: str = values.get("platform", None)
        self.address: str = values.get("address", None)
        self.asset_symbol: str = values.get("asset_symbol", None)
        self.asset_quantity: str = values.get("asset_quantity", None)
        self.airdrop_points: float = values.get("airdrop_points", None)
        self.claim_date: str = values.get("claim_date", None)
        self.claim_sig: str = values.get("claim_sig", None)
        self.sps_received: str = values.get("sps_received", None)
        self.claim_tx: str = values.get("claim_tx", None)


class SPSOverview:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.total_staked: float = values.get("total_staked", None)
        self.total_airdrop_points: str = values.get("total_airdrop_points", None)
        self.reward_debt: float = values.get("reward_debt", None)
        self.unstaking: str = values.get("unstaking", None)
        self.airdrop: List[AirdropItems] = Airdrop(values=values.get("airdrop"))


class SpsGeneralData:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.total_supply: float = values.get("total_supply", None)
        self.wallet_balance: str = values.get("wallet_balance", None)


class CardItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.player: str = values.get("player", None)
        self.uid: str = values.get("uid", None)
        self.card_detail_id: int = values.get("card_detail_id", None)
        self.xp: int = values.get("xp", None)
        self.gold: bool = values.get("gold", None)
        self.edition: int = values.get("edition", None)
        self.market_id: str = values.get("market_id", None)
        self.buy_price: float = float(values.get("buy_price")) if values.get("buy_price") else None
        self.market_listing_type: str = values.get("market_listing_type", None)
        self.market_listing_status: int = values.get("market_listing_status", None)
        self.last_used_block: int = values.get("last_used_block", None)
        self.last_used_player: str = values.get("last_used_player", None)
        self.last_used_date: str = values.get("last_used_date", None)
        self.last_transferred_block: str = values.get("last_transferred_block", None)
        self.last_transferred_date: str = values.get("last_transferred_date", None)
        self.alpha_xp: str = values.get("alpha_xp", None)
        self.delegated_to: str = values.get("delegated_to", None)
        self.delegation_tx: str = values.get("delegation_tx", None)
        self.skin: str = values.get("skin", None)
        self.delegated_to_display_name: str = values.get("delegated_to_display_name", None)
        self.display_name: str = values.get("display_name", None)
        self.lock_days: str = values.get("lock_days", None)
        self.unlock_date: str = values.get("unlock_date", None)
        self.level: int = values.get("level", None)


class Cards(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [CardItem(value) for value in values]


class Collection:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.player: str = values.get("player", None)
        self.cards: List[CardItem] = Cards(values=values.get("cards"))


class MarketItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.fee_percent: float = values.get("fee_percent", None)
        self.uid: str = values.get("uid", None)
        self.seller: str = values.get("seller", None)
        self.card_detail_id: float = values.get("card_detail_id", None)
        self.xp: float = values.get("xp", None)
        self.gold: bool = values.get("gold", None)
        self.edition: float = values.get("edition", None)
        buy_price = values.get("buy_price", None)
        self.buy_price: float = float(buy_price) if buy_price else 0
        self.currency: str = values.get("currency", None)
        self.desc: str = values.get("desc", None)
        self.type: str = values.get("type", None)
        self.market_id: str = values.get("market_id", None)
        self.last_transferred_block: str = values.get("last_transferred_block", None)
        self.last_transferred_date: str = values.get("last_transferred_date", None)
        self.last_used_block: float = values.get("last_used_block", None)
        self.last_used_date: str = values.get("last_used_date", None)
        self.last_used_player: str = values.get("last_used_player", None)


class MarketResult(list):
    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [MarketItem(value) for value in values]


class DistributionItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.card_detail_id: float = values.get("card_detail_id", None)
        self.gold: bool = values.get("gold", None)
        self.edition: float = values.get("edition", None)
        self.num_cards: str = values.get("num_cards", None)
        self.total_xp: str = values.get("total_xp", None)
        self.num_burned: str = values.get("num_burned", None)
        self.total_burned_xp: str = values.get("total_burned_xp", None)


class Distribution(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [DistributionItem(value) for value in values]


class Stats:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.mana: List[int] = values.get("mana", None)
        self.attack: List[int] = values.get("attack", None)
        self.ranged: List[int] = values.get("ranged", None)
        self.magic: List[int] = values.get("magic", None)
        self.armor: List[int] = values.get("armor", None)
        self.health: List[int] = values.get("health", None)
        self.speed: List[int] = values.get("speed", None)
        self.abilities: List[str] = values.get("abilities", None)


class CardDetail:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.id: float = values.get("id", None)
        self.name: str = values.get("name", None)
        self.color: str = values.get("color", None)
        self.type: str = values.get("type", None)
        self.sub_type: str = values.get("sub_type", None)
        self.rarity: int = values.get("rarity", None)
        self.drop_rate: float = values.get("drop_rate", None)
        self.stats = Stats(values=values.get("stats"))
        self.is_starter: bool = values.get("is_starter", None)
        self.editions: str = values.get("editions", None)
        self.created_block_num: str = values.get("created_block_num", None)
        self.last_update_tx: str = values.get("last_update_tx", None)
        self.total_printed: float = values.get("total_printed", None)
        self.is_promo: bool = values.get("is_promo", None)
        self.tier: str = values.get("tier", None)
        self.distribution: List[DistributionItem] = Distribution(values=values.get("distribution"))


class CardDetails(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [CardDetail(value) for value in values]


###############################################################################


class SpsAirdrop:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.start_date: str = values.get("start_date", None)
        self.current_airdrop_day: float = values.get("current_airdrop_day", None)
        self.sps_per_day: float = values.get("sps_per_day", None)


class BatEventItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.id: str = values.get("id", None)
        self.bat: float = values.get("bat", None)


class BatEventList(list):
    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [BatEventItem(value) for value in values]


class QuestLodge:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.symbol: str = values.get("symbol", None)
        self.levels: List[float] = values.get("levels", None)


class GuildHall:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.symbol: str = values.get("symbol", None)
        self.levels: List[str] = values.get("levels", None)
        self.member_limit: List[float] = values.get("member_limit", None)


class CostItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.symbol: str = values.get("symbol", None)
        self.levels: List[float] = values.get("levels", None)


class Cost(list):

    def __init__(self, values: list = None):
        super().__init__()

        values = [values] if type(values) != list else values

        values = values if values is not None else []
        self[:] = [CostItem(value) for value in values]


class Arena:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.cost: List[CostItem] = Cost(values=values.get("cost"))


class Barracks:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.cost: List[CostItem] = Cost(values=values.get("cost"))


class GuildShop:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.cost: List[CostItem] = Cost(values=values.get("cost"))


class Dec:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.eth_withdrawal_fee: float = values.get("eth_withdrawal_fee", None)
        self.curve_reduction: float = values.get("curve_reduction", None)
        self.start_block: float = values.get("start_block", None)
        self.reduction_blocks: float = values.get("reduction_blocks", None)
        self.reduction_pct: float = values.get("reduction_pct", None)
        self.pool_size_blocks: float = values.get("pool_size_blocks", None)
        self.ecr_regen_rate: float = values.get("ecr_regen_rate", None)
        self.ecr_reduction_rate: float = values.get("ecr_reduction_rate", None)
        self.alpha_bonus: float = values.get("alpha_bonus", None)
        self.gold_bonus: float = values.get("gold_bonus", None)
        self.streak_bonus: float = values.get("streak_bonus", None)
        self.streak_bonus_max: float = values.get("streak_bonus_max", None)
        self.burn_rate: List[float] = values.get("burn_rate", None)
        self.untamed_burn_rate: List[float] = values.get("untamed_burn_rate", None)
        self.alpha_burn_bonus: float = values.get("alpha_burn_bonus", None)
        self.promo_burn_bonus: float = values.get("promo_burn_bonus", None)
        self.gold_burn_bonus: float = values.get("gold_burn_bonus", None)
        self.max_burn_bonus: float = values.get("max_burn_bonus", None)
        self.orbs_available: float = values.get("orbs_available", None)
        self.orb_cost: float = values.get("orb_cost", None)
        self.dice_available: float = values.get("dice_available", None)
        self.dice_cost: float = values.get("dice_cost", None)
        self.mystery_potion_blocks: float = values.get("mystery_potion_blocks", None)
        self.pool_cut_pct: float = values.get("pool_cut_pct", None)
        self.prize_pool_account: str = values.get("prize_pool_account", None)
        self.tokens_per_block: float = values.get("tokens_per_block", None)
        self.gold_burn_bonus_2: float = values.get("gold_burn_bonus_2", None)
        self.curve_constant: float = values.get("curve_constant", None)


class Guilds:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.merit_constant: float = values.get("merit_constant", None)
        self.merit_multiplier: List[float] = values.get("merit_multiplier", None)
        self.quest_lodge = QuestLodge(values=values.get("quest_lodge"))
        self.guild_hall = GuildHall(values=values.get("guild_hall"))
        self.rank_names: List[str] = values.get("rank_names", None)
        self.shop_discount_pct: List[str] = values.get("shop_discount_pct", None)
        self.dec_bonus_pct: List[float] = values.get("dec_bonus_pct", None)
        self.creation_fee: float = values.get("creation_fee", None)
        self.crown_split_pct: List[float] = values.get("crown_split_pct", None)
        self.crown_multiplier: List[float] = values.get("crown_multiplier", None)
        self.brawl_prep_duration: float = values.get("brawl_prep_duration", None)
        self.current_fray_edition: float = values.get("current_fray_edition", None)
        self.max_brawl_size: float = values.get("max_brawl_size", None)
        self.arena = Arena(values=values.get("arena"))
        self.barracks = Barracks(values=values.get("barracks"))
        self.guild_shop = GuildShop(values=values.get("guild_shop"))
        self.brawl_staggered_start_interval: float = values.get("brawl_staggered_start_interval", None)
        self.brawl_cycle_end_offset: float = values.get("brawl_cycle_end_offset", None)
        self.brawl_results_duration: float = values.get("brawl_results_duration", None)
        self.brawl_combat_duration: float = values.get("brawl_combat_duration", None)


class BarrackPerksBonus:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.bonus: str = values.get("bonus", None)


class BarracksPerksSublist(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [BarrackPerksBonus(value) for value in values]


class BarracksPerks(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [BarracksPerksSublist(value) for value in values]


class FrayItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.editions: List[str] = values.get("editions", None)
        self.foil: str = values.get("foil", None)
        self.rating_level: str = values.get("rating_level", None)


class FraySublist(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [FrayItem(value) for value in values]


class Frays(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [FraySublist(value) for value in values]


class CurrencyItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.name: str = values.get("name", None)
        self.currency: str = values.get("currency", None)
        self.type: str = values.get("type", None)
        self.tournament_enabled: bool = values.get("tournament_enabled", None)
        self.payment_enabled: bool = values.get("payment_enabled", None)
        self.usd_value: float = values.get("usd_value", None)
        self.precision: float = values.get("precision", None)


class SupportedCurrencies(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [CurrencyItem(value) for value in values]


class LandSale:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.plot_price: float = values.get("plot_price", None)
        self.tract_price: float = values.get("tract_price", None)
        self.region_price: float = values.get("region_price", None)
        self.plots_available: float = values.get("plots_available", None)
        self.plot_plots: float = values.get("plot_plots", None)
        self.tract_plots: float = values.get("tract_plots", None)
        self.region_plots: float = values.get("region_plots", None)
        self.start_date: str = values.get("start_date", None)


class ChaosAirdropItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.name: str = values.get("name", None)
        self.id: float = values.get("id", None)
        self.chance: float = values.get("chance", None)
        self.gold_guarantee: float = values.get("gold_guarantee", None)
        self.claim_date: str = values.get("claim_date", None)


class Airdrops(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [ChaosAirdropItem(value) for value in values]


class ChaosLegion:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.voucher_drop_start: str = values.get("voucher_drop_start", None)
        self.sale2_end: str = values.get("sale2_end", None)
        self.pre_sale_start: str = values.get("pre_sale_start", None)
        self.sale3_start: str = values.get("sale3_start", None)
        self.pre_sale_end: str = values.get("pre_sale_end", None)
        self.main_sale_start: str = values.get("main_sale_start", None)
        self.pack_price: float = values.get("pack_price", None)
        self.airdrops: List[ChaosAirdropItem] = Airdrops(values=values.get("airdrops"))


class Data:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.color: str = values.get("color", None)
        self.action: str = values.get("action", None)
        self.splinter: str = values.get("splinter", None)
        self.value: str = values.get("value", None)


class QuestDetails:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.name: str = values.get("name", None)
        self.active: bool = values.get("active", None)
        self.type: str = values.get("type", None)
        self.description: str = values.get("description", None)
        self.objective: str = values.get("objective", None)
        self.objective_short: str = values.get("objective_short", None)
        self.objective_type: str = values.get("objective_type", None)
        self.item_total: float = values.get("item_total", None)
        self.reward_qty: float = values.get("reward_qty", None)
        self.min_rating: str = values.get("min_rating", None)
        self.match_types: List[str] = values.get("match_types", None)
        self.reward_qty_by_league: List[float] = values.get("reward_qty_by_league", None)
        self.data = Data(values=values.get("data"))
        self.icon: str = values.get("icon", None)


class Quests(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [QuestDetails(value) for value in values]


class BonusesItems:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.min: float = values.get("min", None)
        self.bonus_pct: float = values.get("bonus_pct", None)


class Bonuses(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [BonusesItems(value) for value in values]


class PotionItem:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.id: str = values.get("id", None)
        self.name: str = values.get("name", None)
        self.item_id: float = values.get("item_id", None)
        self.price_per_charge: float = values.get("price_per_charge", None)
        self.value: float = values.get("value", None)
        self.bonuses: List[BonusesItems] = Bonuses(values=values.get("bonuses"))


class Potions(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [PotionItem(value) for value in values]


class StakingRewards:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.tokens_per_block: float = values.get("tokens_per_block", None)
        self.reduction_blocks: float = values.get("reduction_blocks", None)
        self.reduction_pct: float = values.get("reduction_pct", None)
        self.start_block: float = values.get("start_block", None)


class Sps:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.staking_rewards_acc_sps_per_share: float = values.get("staking_rewards_acc_sps_per_share", None)
        self.staking_rewards = StakingRewards(values=values.get("staking_rewards"))
        self.staking_rewards_last_reward_block: float = values.get("staking_rewards_last_reward_block", None)
        self.unstaking_periods: float = values.get("unstaking_periods", None)
        self.unstaking_interval_seconds: float = values.get("unstaking_interval_seconds", None)


class Season:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.id: float = values.get("id", None)
        self.name: str = values.get("name", None)
        self.ends: str = values.get("ends", None)
        self.reward_packs: List[str] = values.get("reward_packs", None)
        self.reset_block_num: str = values.get("reset_block_num", None)


class BrawlCycle:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.id: float = values.get("id", None)
        self.name: str = values.get("name", None)
        self.start: str = values.get("start", None)
        self.status: float = values.get("status", None)
        self.reset_block_num: str = values.get("reset_block_num", None)
        self.end: str = values.get("end", None)


class ChainProps:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.time: str = values.get("time", None)
        self.ref_block_num: float = values.get("ref_block_num", None)
        self.ref_block_id: str = values.get("ref_block_id", None)
        self.ref_block_prefix: float = values.get("ref_block_prefix", None)


class Ssc:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.rpc_url: str = values.get("rpc_url", None)
        self.chain_id: str = values.get("chain_id", None)
        self.hive_rpc_url: str = values.get("hive_rpc_url", None)
        self.hive_chain_id: str = values.get("hive_chain_id", None)
        self.alpha_token: str = values.get("alpha_token", None)
        self.beta_token: str = values.get("beta_token", None)
        self.pack_holding_account: str = values.get("pack_holding_account", None)


class CardHoldingAccount:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.blockchainName: str = values.get("blockchainName", None)
        self.accountName: str = values.get("accountName", None)


class Abi:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.status: str = values.get("status", None)
        self.message: str = values.get("message", None)
        self.result: str = values.get("result", None)


class EthCards:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.abi = Abi(values=values.get("abi"))
        self.address: str = values.get("address", None)


class Crystals:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.abi = Abi(values=values.get("abi"))
        self.address: str = values.get("address", None)


class Payments:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.abi = Abi(values=values.get("abi"))
        self.address: str = values.get("address", None)


class Contracts:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.cards = EthCards(values=values.get("cards"))
        self.crystals = Crystals(values=values.get("crystals"))
        self.payments = Payments(values=values.get("payments"))


class Ethereum:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.withdrawal_fee: float = values.get("withdrawal_fee", None)
        self.sps_withdrawal_fee: float = values.get("sps_withdrawal_fee", None)
        self.contracts = Contracts(values=values.get("contracts"))


class Token:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.account: str = values.get("account", None)


class Atomicassets:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.account: str = values.get("account", None)


class External:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.token = Token(values=values.get("token"))
        self.atomicassets = Atomicassets(values=values.get("atomicassets"))


class Wax:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.login_enabled: bool = values.get("login_enabled", None)
        self.client_id: str = values.get("client_id", None)
        self.auth_url: str = values.get("auth_url", None)
        self.external = External(values=values.get("external"))


class Bridge:
    class Ethereum:
        class Dec:
            def __init__(self, values: dict = None):
                values = values if values is not None else {}
                self.enabled: bool = values.get("enabled", None)
                self.game_wallet: str = values.get("game_wallet", None)
                self.min_amount: float = values.get("min_amount", None)
                self.fee_pct: float = values.get("fee_pct", None)

        class Sps:
            def __init__(self, values: dict = None):
                values = values if values is not None else {}
                self.enabled: bool = values.get("enabled", None)
                self.game_wallet: str = values.get("game_wallet", None)
                self.min_amount: float = values.get("min_amount", None)
                self.fee_pct: float = values.get("fee_pct", None)

        def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.DEC = self.Dec(values=values.get("DEC"))
            self.SPS = self.Sps(values=values.get("SPS"))

    class Bsc:
        class Dec:
            def __init__(self, values: dict = None):
                values = values if values is not None else {}
                self.enabled: bool = values.get("enabled", None)
                self.game_wallet: str = values.get("game_wallet", None)
                self.min_amount: float = values.get("min_amount", None)
                self.fee_pct: float = values.get("fee_pct", None)

        class Sps:
            def __init__(self, values: dict = None):
                values = values if values is not None else {}
                self.enabled: bool = values.get("enabled", None)
                self.game_wallet: str = values.get("game_wallet", None)
                self.min_amount: float = values.get("min_amount", None)
                self.fee_pct: float = values.get("fee_pct", None)

        def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.DEC = self.Dec(values=values.get("DEC"))
            self.SPS = self.Sps(values=values.get("SPS"))

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.ethereum = self.Ethereum(values=values.get("ethereum"))
        self.bsc = self.Bsc(values=values.get("bsc"))


class RulesetItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.active: bool = values.get("active", None)
        self.name: str = values.get("name", None)
        self.description: str = values.get("description", None)


class Rulesets(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [RulesetItem(value) for value in values]


class Modern:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.editions: List[float] = values.get("editions", None)
        self.tiers: List[float] = values.get("tiers", None)


class Battles:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.asset_url: str = values.get("asset_url", None)
        self.default_expiration_seconds: float = values.get("default_expiration_seconds", None)
        self.reveal_blocks: float = values.get("reveal_blocks", None)
        self.win_streak_wins: float = values.get("win_streak_wins", None)
        self.rulesets: List[RulesetItem] = Rulesets(values=values.get("rulesets"))
        self.modern = Modern(values=values.get("modern"))


class WildLeaderboard:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.Novice: List[str] = values.get("Novice", None)
        self.Bronze: List[float] = values.get("Bronze", None)
        self.Silver: List[float] = values.get("Silver", None)
        self.Gold: List[float] = values.get("Gold", None)
        self.Diamond: List[float] = values.get("Diamond", None)
        self.Champion: List[float] = values.get("Champion", None)


class LeaderboardPrizes:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.wild = WildLeaderboard(values=values.get("wild"))
        self.modern = ModernLeaderboard(values=values.get("modern"))


class ModernLeaderboard:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.Novice: List[str] = values.get("Novice", None)
        self.Bronze: List[float] = values.get("Bronze", None)
        self.Silver: List[float] = values.get("Silver", None)
        self.Gold: List[float] = values.get("Gold", None)
        self.Diamond: List[float] = values.get("Diamond", None)
        self.Champion: List[float] = values.get("Champion", None)


class LeagueItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.name: str = values.get("name", None)
        self.group: str = values.get("group", None)
        self.league_limit: float = values.get("league_limit", None)
        self.level: str = values.get("level", None)
        self.min_rating: str = values.get("min_rating", None)
        self.min_power: str = values.get("min_power", None)
        self.season_rating_reset: str = values.get("season_rating_reset", None)


class WildLeague(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [LeagueItem(value) for value in values]


class ModernLeague(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [LeagueItem(value) for value in values]


class Leagues:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.wild: List[LeagueItem] = WildLeague(values=values.get("wild"))
        self.modern: List[LeagueItem] = ModernLeague(values=values.get("modern"))


class Chest:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.base: float = values.get("base", None)
        self.step_multiplier: float = values.get("step_multiplier", None)
        self.max: float = values.get("max", None)


class LootChest(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [Chest(value) for value in values]


class LeagueBoost:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.rarity_boost: float = values.get("rarity_boost", None)
        self.token_multiplier: float = values.get("token_multiplier", None)


class Boosts:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.bronze = LeagueBoost(values=values.get("bronze"))
        self.silver = LeagueBoost(values=values.get("silver"))
        self.gold = LeagueBoost(values=values.get("gold"))
        self.diamond = LeagueBoost(values=values.get("diamond"))
        self.champion = LeagueBoost(values=values.get("champion"))


class SeasonListItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.base: float = values.get("base", None)
        self.step_multiplier: float = values.get("step_multiplier", None)
        self.max: float = values.get("max", None)


class SeasonList(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [SeasonListItem(value) for value in values]


class LootChests:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.quest: List[Chest] = LootChest(values=values.get("quest"))
        self.season: List[SeasonListItem] = SeasonList(values=values.get("season"))
        self.boosts = Boosts(values=values.get("boosts"))


class CardHoldingAccounts(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [CardHoldingAccount(value) for value in values]


class QuestData:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.color: str = values.get("color", None)
        self.action: str = values.get("action", None)
        self.splinter: str = values.get("splinter", None)
        self.value: str = values.get("value", None)
        self.description: str = values.get("description", None)


class QuestItem:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.name: str = values.get("name", None)
        self.active: bool = values.get("active", None)
        self.objective_type: str = values.get("objective_type", None)
        self.min_rating: str = values.get("min_rating", None)
        self.data = QuestData(values=values.get("data"))


class DailyQuests(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [QuestItem(value) for value in values]


class GuildStoreCost:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.symbol: str = values.get("symbol", None)
        self.amount: float = values.get("amount", None)


class GuildStoreItem:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.name: str = values.get("name", None)
        self.short_desc: str = values.get("short_desc", None)
        self.unlock_level: float = values.get("unlock_level", None)
        self.cost = GuildStoreCost(values=values.get("cost"))
        self.icon: str = values.get("icon", None)
        self.icon_sm: str = values.get("icon_sm", None)
        self.color: str = values.get("color", None)
        self.unit_of_purchase: str = values.get("unit_of_purchase", None)
        self.symbol: str = values.get("symbol", None)


class GuildStoreItems(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [GuildStoreItem(value) for value in values]


class GeneralSettings:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.asset_url: str = values.get("asset_url", None)
        self.gold_percent: float = values.get("gold_percent", None)
        self.starter_pack_price: float = values.get("starter_pack_price", None)
        self.booster_pack_price: float = values.get("booster_pack_price", None)
        self.market_fee: float = values.get("market_fee", None)
        self.num_editions: float = values.get("num_editions", None)
        self.modern_num_editions: float = values.get("modern_num_editions", None)
        self.core_editions: List[str] = values.get("core_editions", None)
        self.starter_editions: List[float] = values.get("starter_editions", None)
        self.soulbound_editions: List[float] = values.get("soulbound_editions", None)
        self.event_creation_whitelist: List[str] = values.get("event_creation_whitelist", None)
        self.bat_event_list: List[BatEventItem] = BatEventList(values=values.get("bat_event_list"))
        self.event_entry_fee_required: float = values.get("event_entry_fee_required", None)
        self.max_event_entrants: float = values.get("max_event_entrants", None)
        self.tournaments_creation_fee_dec: float = values.get("tournaments_creation_fee_dec", None)
        self.account: str = values.get("account", None)
        self.stats: bool = values.get("stats", None)
        self.rarity_pcts: List[float] = values.get("rarity_pcts", None)
        self.xp_levels: List[List[int]] = values.get("xp_levels", None)
        self.alpha_xp: List[int] = values.get("alpha_xp", None)
        self.gold_xp: List[int] = values.get("gold_xp", None)
        self.beta_xp: List[int] = values.get("beta_xp", None)
        self.beta_gold_xp: List[int] = values.get("beta_gold_xp", None)
        self.combine_rates: List[List[int]] = values.get("combine_rates", None)
        self.combine_rates_gold: List[List[int]] = values.get("combine_rates_gold", None)
        self.battles = Battles(values=values.get("battles"))
        self.multi_lb_start_season: float = values.get("multi_lb_start_season", None)
        self.leaderboard_prizes = LeaderboardPrizes(values=values.get("leaderboard_prizes"))
        self.leagues = Leagues(values=values.get("leagues"))
        self.dec = Dec(values=values.get("dec"))
        self.guilds = Guilds(values=values.get("guilds"))
        self.barracks_perks: List[BarracksPerksSublist] = BarracksPerks(values=values.get("barracks_perks"))
        self.frays: List[FraySublist] = Frays(values=values.get("frays"))
        self.supported_currencies: List[CurrencyItem] = SupportedCurrencies(values=values.get("supported_currencies"))
        self.transfer_cooldown_blocks: float = values.get("transfer_cooldown_blocks", None)
        self.untamed_edition_date: str = values.get("untamed_edition_date", None)
        self.active_auth_ops: List[str] = values.get("active_auth_ops", None)
        self.version: str = values.get("version", None)
        self.config_version: float = values.get("config_version", None)
        self.land_sale = LandSale(values=values.get("land_sale"))
        self.chaos_legion = ChaosLegion(values=values.get("chaos_legion"))
        self.potions: List[PotionItem] = Potions(values=values.get("potions"))
        self.promotions: List[str] = values.get("promotions", None)
        self.sps = Sps(values=values.get("sps"))
        self.battles_disabled: str = values.get("battles_disabled", None)
        self.blocks_are_behind: str = values.get("blocks_are_behind", None)
        self.loot_chests = LootChests(values=values.get("loot_chests"))
        self.daily_quests: List[QuestItem] = DailyQuests(values=values.get("daily_quests"))
        self.rpc_nodes: List[str] = values.get("rpc_nodes", None)
        self.dec_price: float = values.get("dec_price", None)
        self.sps_price: float = values.get("sps_price", None)
        self.maintenance_mode: str = values.get("maintenance_mode", None)
        self.season = Season(values=values.get("season"))
        self.brawl_cycle = BrawlCycle(values=values.get("brawl_cycle"))
        self.guild_store_items: List[GuildStoreItem] = GuildStoreItems(values=values.get("guild_store_items"))
        self.last_block: float = values.get("last_block", None)
        self.timestamp: float = values.get("timestamp", None)
        self.chain_props = ChainProps(values=values.get("chain_props"))
        self.circle_payments_enabled: str = values.get("circle_payments_enabled", None)
        self.transak_payments_enabled: float = values.get("transak_payments_enabled", None)
        self.zendesk_enabled: float = values.get("zendesk_enabled", None)
        self.dec_max_buy_amount: float = values.get("dec_max_buy_amount", None)
        self.sps_max_buy_amount: float = values.get("sps_max_buy_amount", None)
        self.show_special_store: bool = values.get("show_special_store", None)
        self.paypal_acct: str = values.get("paypal_acct", None)
        self.paypal_merchant_id: str = values.get("paypal_merchant_id", None)
        self.paypal_client_id: str = values.get("paypal_client_id", None)
        self.paypal_sandbox: str = values.get("paypal_sandbox", None)
        self.ssc = Ssc(values=values.get("ssc"))
        self.card_holding_accounts: List[CardHoldingAccount] = CardHoldingAccounts(
            values=values.get("card_holding_accounts"))
        self.bridge = Bridge(values=values.get("bridge"))
        self.ethereum = Ethereum(values=values.get("ethereum"))
        self.wax = Wax(values=values.get("wax"))
        self.sps_airdrop = SpsAirdrop(values=values.get("sps_airdrop"))
        self.api_ops: List[str] = values.get("api_ops", None)


class MarketGroupItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.card_detail_id: int = values.get("card_detail_id", None)
        self.gold: bool = values.get("gold", None)
        self.edition: int = values.get("edition", None)
        self.qty: float = values.get("qty", None)
        self.low_price_bcx: float = values.get("low_price_bcx", None)
        self.low_price: float = values.get("low_price", None)
        self.high_price: float = values.get("high_price", None)
        self.level: float = values.get("level", None)
        self.mana: float = values.get("mana", None)


class MarketGrouped(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [MarketGroupItem(value) for value in values]


class SummonerState:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.stats: List[str] = values.get("stats", None)
        self.abilities: List[str] = values.get("abilities", None)


class Summoner:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.uid: str = values.get("uid", None)
        self.xp: float = values.get("xp", None)
        self.gold: str = values.get("gold", None)
        self.card_detail_id: float = values.get("card_detail_id", None)
        self.level: float = values.get("level", None)
        self.edition: float = values.get("edition", None)
        self.state = SummonerState(values=values.get("state"))


class MonsterState:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.alive: bool = values.get("alive", None)
        self.stats: List[float] = values.get("stats", None)
        self.base_health: float = values.get("base_health", None)
        self.other: List[str] = values.get("other", None)


class Monster:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.uid: str = values.get("uid", None)
        self.xp: float = values.get("xp", None)
        self.gold: str = values.get("gold", None)
        self.card_detail_id: float = values.get("card_detail_id", None)
        self.level: float = values.get("level", None)
        self.edition: float = values.get("edition", None)
        self.state = MonsterState(values=values.get("state"))
        self.abilities: List[str] = values.get("abilities", None)


class Monsters(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [Monster(value) for value in values]


class BattleTeam:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.player: str = values.get("player", None)
        self.rating: float = values.get("rating", None)
        self.color: str = values.get("color", None)
        self.summoner = Summoner(values=values.get("summoner"))
        self.monsters: List[Monster] = Monsters(values=values.get("monsters"))


class BattleDetails:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.seed: str = values.get("seed", None)
        self.team1 = BattleTeam(values=values.get("team1"))
        self.team2 = BattleTeam(values=values.get("team2"))
        self.winner: str = values.get("winner", None)
        self.loser: str = values.get("loser", None)


class PlayerData:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.name: str = values.get("name", None)
        self.join_date: str = values.get("join_date", None)
        self.rating: float = values.get("rating", None)
        self.battles: float = values.get("battles", None)
        self.wins: float = values.get("wins", None)
        self.current_streak: str = values.get("current_streak", None)
        self.longest_streak: float = values.get("longest_streak", None)
        self.max_rating: float = values.get("max_rating", None)
        self.max_rank: float = values.get("max_rank", None)
        self.champion_points: str = values.get("champion_points", None)
        self.capture_rate: float = values.get("capture_rate", None)
        self.last_reward_block: float = values.get("last_reward_block", None)
        self.last_reward_time: str = values.get("last_reward_time", None)
        self.guild: str = values.get("guild", None)
        self.guild_name: str = values.get("guild_name", None)
        self.guild_motto: str = values.get("guild_motto", None)
        self.guild_data: str = values.get("guild_data", None)
        self.guild_level: str = values.get("guild_level", None)
        self.guild_quest_lodge_level: str = values.get("guild_quest_lodge_level", None)
        self.starter_pack_purchase: bool = values.get("starter_pack_purchase", None)
        self.avatar_id: float = values.get("avatar_id", None)
        self.display_name: str = values.get("display_name", None)
        self.title_pre: str = values.get("title_pre", None)
        self.title_post: str = values.get("title_post", None)
        self.collection_power: float = values.get("collection_power", None)
        self.league: float = values.get("league", None)
        self.adv_msg_sent: str = values.get("adv_msg_sent", None)
        self.alt_name: str = values.get("alt_name", None)


class BattleItem:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.battle_queue_id_1: str = values.get("battle_queue_id_1", None)
        self.battle_queue_id_2: str = values.get("battle_queue_id_2", None)
        self.player_1_rating_initial: float = values.get("player_1_rating_initial", None)
        self.player_2_rating_initial: float = values.get("player_2_rating_initial", None)
        self.winner: str = values.get("winner", None)
        self.player_1_rating_final: float = values.get("player_1_rating_final", None)
        self.player_2_rating_final: float = values.get("player_2_rating_final", None)
        self.details = BattleDetails(values=values.get("details"))
        self.player_1: str = values.get("player_1", None)
        self.player_2: str = values.get("player_2", None)
        self.created_date: str = values.get("created_date", None)
        self.match_type: str = values.get("match_type", None)
        self.mana_cap: float = values.get("mana_cap", None)
        self.current_streak: float = values.get("current_streak", None)
        self.ruleset: str = values.get("ruleset", None)
        self.inactive: str = values.get("inactive", None)
        self.settings: str = values.get("settings", None)
        self.block_num: float = values.get("block_num", None)
        self.rshares: float = values.get("rshares", None)
        self.dec_info: str = values.get("dec_info", None)
        self.leaderboard: float = values.get("leaderboard", None)
        self.reward_dec: str = values.get("reward_dec", None)
        self.reward_sps: str = values.get("reward_sps", None)
        self.player_1_data = PlayerData(values=values.get("player_1_data"))
        self.player_2_data = PlayerData(values=values.get("player_2_data"))


class BattlesHistory(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [BattleItem(value) for value in values]


class BattleHistory:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.player: str = values.get("player", None)
        self.battles: List[BattleItem] = BattlesHistory(values=values.get("battles"))


class BalanceHistoryItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.player: str = values.get("player", None)
        self.token: str = values.get("token", None)
        self.amount: str = values.get("amount", None)
        self.balance_start: str = values.get("balance_start", None)
        self.balance_end: str = values.get("balance_end", None)
        self.block_num: float = values.get("block_num", None)
        self.trx_id: str = values.get("trx_id", None)
        self.type: str = values.get("type", None)
        self.created_date: str = values.get("created_date", None)
        self.counterparty: str = values.get("counterparty", None)


class BalanceHistory(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [BalanceHistoryItem(value) for value in values]


class ActiveRentalItem:
    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.id: float = values.get("id", None)
        self.sell_trx_id: str = values.get("sell_trx_id", None)
        self.seller: str = values.get("seller", None)
        self.num_cards: float = values.get("num_cards", None)
        self.buy_price: str = values.get("buy_price", None)
        self.fee_percent: float = values.get("fee_percent", None)
        self.market_item_id: float = values.get("market_item_id", None)
        self.rental_tx: str = values.get("rental_tx", None)
        self.rental_date: str = values.get("rental_date", None)
        self.renter: str = values.get("renter", None)
        self.status: float = values.get("status", None)
        self.market_account: str = values.get("market_account", None)
        self.rental_days: float = values.get("rental_days", None)
        self.next_rental_payment: str = values.get("next_rental_payment", None)
        self.payment_currency: str = values.get("payment_currency", None)
        self.payment_amount: str = values.get("payment_amount", None)
        self.escrow_currency: str = values.get("escrow_currency", None)
        self.escrow_amount: str = values.get("escrow_amount", None)
        self.paid_amount: str = values.get("paid_amount", None)
        self.cancel_tx: str = values.get("cancel_tx", None)
        self.cancel_player: str = values.get("cancel_player", None)
        self.cancel_date: str = values.get("cancel_date", None)
        self.card_id: str = values.get("card_id", None)
        self.card_detail_id: float = values.get("card_detail_id", None)
        self.gold: bool = values.get("gold", None)
        self.xp: float = values.get("xp", None)
        self.edition: float = values.get("edition", None)


class ActiveRentals(list):

    def __init__(self, values: list = None):
        super().__init__()
        values = values if values is not None else []
        self[:] = [ActiveRentalItem(value) for value in values]
