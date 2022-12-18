from typing import Dict, List

from SM_Framework.SMBotFramework.api.data.SplinterlandsData import CardItem, GeneralSettings, CardDetails
from SM_Framework.SMBotFramework.api.util.UtilApi import UtilApi


class CardUtil:
    details: Dict[int, CardItem]
    settings: GeneralSettings

    def determine_base_xp(self, rarity: int, xp_table: List[int], alpha: bool, beta: bool, gold: bool):
        return xp_table[rarity - 1] if alpha or beta or gold else xp_table[0]

    def determine_xp_table(self, rarity: int, alpha: bool, beta: bool, gold: bool, settings: GeneralSettings = None):
        xp_table: List[int] = []

        if not settings:
            self.settings = UtilApi().get_settings()

        if alpha:
            xp_table = self.settings.beta_gold_xp if gold else self.settings.alpha_xp
        elif beta:
            xp_table = self.settings.beta_gold_xp if gold else self.settings.beta_xp
        else:
            xp_table = self.settings.gold_xp if gold else self.settings.xp_levels[rarity - 1]

        return xp_table

    def is_beta(self, card_detail_id: int, edition: int):
        return edition == 1 or (edition in [2, 3] and card_detail_id <= 223)

    def is_alpha(self, edition: int):
        return edition == 0
