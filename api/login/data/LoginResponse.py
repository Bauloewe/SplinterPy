from typing import List

from SM_Framework.SMBotFramework.api.data.SplinterlandsData import Settings, Messages, BalanceItem, \
    MessageItems, SeasonReward, Quest, Balances


class LoginResponse:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.timestamp: float = values.get("timestamp", None)
        self.name: str = values.get("name", None)
        self.token: str = values.get("token", None)
        self.starter_pack_purchase: bool = values.get("starter_pack_purchase", None)
        self.join_date: str = values.get("join_date", None)
        self.is_admin: bool = values.get("is_admin", None)
        self.is_cs_admin: bool = values.get("is_cs_admin", None)
        self.is_team: bool = values.get("is_team", None)
        self.referred_by: str = values.get("referred_by", None)
        self.rating: str = values.get("rating", None)
        self.max_rating: float = values.get("max_rating", None)
        self.battles: float = values.get("battles", None)
        self.wins: float = values.get("wins", None)
        self.current_streak: float = values.get("current_streak", None)
        self.longest_streak: float = values.get("longest_streak", None)
        self.max_rank: float = values.get("max_rank", None)
        self.champion_points: float = values.get("champion_points", None)
        self.capture_rate: float = values.get("capture_rate", None)
        self.last_reward_block: float = values.get("last_reward_block", None)
        self.last_reward_time: str = values.get("last_reward_time", None)
        self.require_active_auth: bool = values.get("require_active_auth", None)
        self.settings = Settings(values=values.get("settings"))
        self.avatar_id: str = values.get("avatar_id", None)
        self.display_name: str = values.get("display_name", None)
        self.title_pre: str = values.get("title_pre", None)
        self.title_post: str = values.get("title_post", None)
        self.collection_power: float = values.get("collection_power", None)
        self.league: str = values.get("league", None)
        self.adv_msg_sent: str = values.get("adv_msg_sent", None)
        self.use_proxy: bool = values.get("use_proxy", None)
        self.alt_name: str = values.get("alt_name", None)
        self.email: str = values.get("email", None)
        self.messages: List[MessageItems] = Messages(values=values.get("messages"))
        self.balances: List[BalanceItem] = Balances(values=values.get("balances"))
        self.guild: str = values.get("guild", None)
        self.unrevealed_rewards: List[str] = values.get("unrevealed_rewards", None)
        self.season_max_league: str = values.get("season_max_league", None)
        self.quest = Quest(values=values.get("quest"))
        self.season_reward = SeasonReward(values=values.get("season_reward"))
        self.has_keys: bool = values.get("has_keys", None)
        self.keys_available: bool = values.get("keys_available", None)
        self.outstanding_match: str = values.get("outstanding_match", None)