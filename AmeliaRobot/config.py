class Config(object):
    LOGGER = True

    API_ID = "7376402"
    API_HASH = "f3ed41c9c67ccf319f7d26dc25cecc47"
    TOKEN = "1844045546:AAEVqdxLt7DXvgHfbjypyx9AhhtpCRgmYz4"
    OWNER_ID = "2097320259"
    OWNER_USERNAME = "xAbhish3k"
    SUPPORT_CHAT = "warbotzsupport"
    JOIN_LOGGER = "AmeliaLogupdate"
    EVENT_LOGS = "AmeliaLogupdate"

    SQLALCHEMY_DATABASE_URI = "postgres://gibcjdbt:g5ABuDeknFP_q5HgPHjXT50-6DtWSrcv@rajje.db.elephantsql.com/gibcjdbt"
    MONGO_DB_URI = "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS =  ""
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "6198858059"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = ""
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = ""
    WOLVES = ""

    DONATION_LINK = ""
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = "PRPSG4AY3Q3H0QG0"
    TIME_API_KEY = "S3J6EISOC17L"
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = ""
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ARQ_API_KEY = "LJMETG-DPHBCX-DGHJCD-TMFIGB-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
