from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "2f1bc8786f6f8d6902bafd8896d6aa80)
      API_ID = int(getenv("API_ID", "15481135"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7786848718:AAHqjAOtxjjhvn171wPEQGkISFCg8-KExFw")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002256901984:-1002280361394").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
