BASE_API2 = "https://api2.splinterlands.com"
BASE_EC_API = "https://ec-api.splinterlands.com"
BASE_BATTLE: str = "https://battle.splinterlands.com"

""" PLAYERS ENDPOINTS """
GET_PLAYERS_VERIFY: str = "/players/verify_email"  # GET requires email, timestamp and signature
GET_PLAYERS_AUTH: str = "/players/authenticate"
GET_PLAYERS_LOGIN: str = "/players/login"  # GET requires query params name, timestamp (ms) and signature
GET_PLAYERS_FAQ: str = "/players/faq"  # GET endpoint requires local as path suffix
GET_PLAYERS_SKIN: str = "/players/skins"
GET_PLAYERS_ITEMDET: str = "/players/item_details"
GET_PLAYERS_DAILYUPDATES: str = "/players/daily_updates"
GET_PLAYERS_DYK: str = "/players/dyk"  # requires locale as path suffix
GET_PLAYERS_VERSTATUS: str = "/players/id_verification_status"
GET_PLAYERS_MARKASREAD: str = "/players/mark_as_read"  # requires message id
GET_PLAYERS_MESSAGES: str = "/players/messages"
GET_PLAYERS_REFRESH_GUILD: str = "/players/refresh_guild"
GET_PLAYERS_OUTSTANDING_MATCH: str = "/players/outstanding_match"  # TODO: Test with actual match
GET_PLAYERS_EXISTS: str = "/players/exists"
GET_PLAYERS_DETAILS: str = "/players/details"
GET_PLAYERS_DELEGATION: str = "/players/delegation"  # TODO: Implement
GET_PLAYERS_SPS: str = "/players/sps"
GET_PLAYER_BAL_HISTORY: str = "/players/balance_history"
"/players/refresh_season_data"
"/players/wallets"

"""
email = email.toLowerCase();
        let params = {
            email: email
        };
        let password_key = steem.auth.getPrivateKeys(email, password).owner;
        params.ts = Date.now();
        params.sig = eosjs_ecc.sign(email + params.ts, password_key);
        let response = await SM.ApiAsync("/players/login_email", params);
"""

"""
("/players/details", {
            name: SM.Player.name
        });
"""

"""

"""

""" PLAYERS EC-API ENDPOINTS """
GET_EC_PLAYERS_SPSDATA: str = "/players/sps_data"  # ?v=1639574126087&token=XXXXX&username=aicu
GET_EC_PLAYERS_CLAIMSPSAIR: str = "/players/claim_sps_airdrop"  # ?platform=hive&address=aicu&sig=SIG_K1_KgDVzi1C5&ts=1639589244825&v=1639589245059&token=XXXXXXX&username=aicu

"""" MARKET ENDPOINTS """
GET_MARKET_BASE: str = "/market"  # TODO: Implement
GET_RENT_BY_CARD: str = "/market/for_rent_by_card"  # ?card_detail_id=130&gold=false&edition=2
GET_SALE_BY_CARD: str = "/market/for_sale_by_card"
GET_RENT_GROUPED: str = "/market/for_rent_grouped"
GET_SALE_GROUPED: str = "/market/for_sale_grouped"
GET_ACTIVE_RENTALS: str = "/market/active_rentals"
"/market/status?"  # ids = " + market_ids
"/market/validateListing"  # ?${queryString}

""" CARD ENDPOINTS"""
GET_CARDS_COLLECTION: str = "/cards/collection"  # GET Endpoint requires name as part of path TODO: Implement
GET_CARDS_DETAILS: str = "/cards/get_details"  # TODO: Implement
GET_CARDS_FIND: str = "/cards/find"  # TODO: Implement
"/cards/collection_by_card"

""" PURCHASE ENDPOINTS"""
PURCHASES_START: str = "/purchases/start"  # TODO: Implement
PURCHASES_STARTCODE: str = "/purchases/start_code"  # TODO: Implement
"/purchases/paypal"

""" BATTLE ENDPOINTS """
GET_BATTLE_STATUS: str = "/battle/status"  # TODO: Implement
GET_BATTLE_RESULTS: str = "/battle/result"  # TODO: Implement
GET_BATTLE_HISTORY: str = "/battle/history2"  # ?player=aicu&leaderboard=0&v=164107023450&token=ODVVPQBL68&username=aicu

""" BASE TRX API """
POST_TRX: str = "https://bcast.splinterlands.com/send"
""" BASE Battle API Endpoints """
POST_BATTLE_TRX: str = "/battle/battle_tx"
"""
           var params = {
                trx_id: queue_trx,
                summoner: summoner,
                monsters: monsters.join(),
                secret: secret
            };
            var team_result = await SM.ApiAsync("/battle/send_team", params);
"""

""" UTIL ENDPOINT"""
GET_SETTINGS: str = "/settings"
"/transactions/lookup_se"

"""
,
    async GetPlayerProperties() {
        return await SM.ApiAsync("/player_properties")
    },
    async GetPlayerProperty(propName) {
        return await SM.ApiAsync(`/player_properties/${propName}`)
    },
    async SetPlayerProperty(propName, value) {
        return await SM.Post(`/player_properties/${propName}`, {
            value: value
        })
    },
    async UpdatePlayerProperty(player, propName, value) {
        return await SM.Put(`/player_properties/${propName}`, {
            value: value
        })
    },
    async DeletePlayerProperty(propName) {
        return await SM.Delete(`/player_properties/${propName}`)
    },
"""

""" TOURNAMENT ENDPOINTS"""
"/tournaments/in_progress"
"/tournaments/upcoming"
"/tournaments/find"
"/tournaments/battles, {id: match.tournament_id,round: 1,player: SM.Player.name,reverse: 0});"
"/tournaments/find, {id: match.tournament_id,player_limit: 100});"

""" GUILD ENDPOINTS"""
"/guilds/list"
"/guilds/find"
