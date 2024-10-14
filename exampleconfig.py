from sample_config import Config
class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 22792746
    API_HASH = "4b6f9f5ab64dd8600044bb95c9ed02c6"
    # the name to display in your alive message
    ALIVE_NAME = "•"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:your_password@localhost:5432/aljoke"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1ApWapzMBu7Qe8k0GwDdc4RP5VYQqVFTBNf6FtVULkElHZ9fBKwHDVsQAGerGyfscwis6rh6VuXtYt47AmI-QdBIGya8IE_rosCtq1e-0VrmyLg0zN26XoA0M9_spErJw0KfcogmxusJxBoKchj1-EeBbsxvROxC2w4dGU_Kkpv8jnQaR-F-d75f6gS_5kJdlxr1F8nAh3_9IfRQsgxpRx4BDcJZhT9HhA91wNvI5QcsEiTw7tiLydlZmz1Vm2iOdRbzbQ6CCOzut9GZcuGYurDg4sdxQEB4ygEAdIpBGxeN4Drk_RTKS5DjguI9T0fWF_M3wlfPx4VreEWo-yOhHPqKTQ519swg="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "7310855662:AAEeMlFLeTjQduKSeWCUm70UPVdUMfbyjaI"
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
