class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 17709832
    API_HASH = "7d0c80809165a904c90d247e77a6f646"

    CASH_API_KEY = "Y8PLP1SQTRPQOR9P"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://vzwtemwi:TCzHsKkUSDDJCqCZb09qKFurdMJ0tIdS@john.db.elephantsql.com/vzwtemwi"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001652285559)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://aujla:aujla@aujla12.uattc6l.mongodb.net/"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://graph.org/file/d01e516a4c81239a6c432.jpg"

    SUPPORT_CHAT = "PunjabiChat_Group"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5995512417:AAFYg0myhMw8NGVZiNzfzXQpO2vMYRtaXqc"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "KT0E715ZOR89"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6006788639  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = [-1001652285559]  # List of groups that you want blacklisted.
    DRAGONS = [6006788639]  # User id of sudo users
    DEV_USERS = [6006788639]  # User id of dev users
    DEMONS = [6006788639]  # User id of support users
    TIGERS = [6006788639]  # User id of tiger users
    WOLVES = [6006788639]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
