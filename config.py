import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("27520331", ""))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("e166dd1c060060f5436bfdee7727e49f", "")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5461907810"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mayankrawat8553:9xzZ0VPuQTs65E0r@cluster0.wiza0ki.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
