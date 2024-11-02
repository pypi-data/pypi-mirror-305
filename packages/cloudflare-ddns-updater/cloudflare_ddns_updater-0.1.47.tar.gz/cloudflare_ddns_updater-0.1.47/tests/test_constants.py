import os

# Fallbacks if XDG directories are not set
config_dir = "config-test"
data_dir = "share-test"

# Paths for configuration and logs
CONFIG_DIR = os.path.join(config_dir, "cloudflare_ddns_updater")
CONFIG_FILE = "cf_updater_config.json"
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, CONFIG_FILE)
LOG_DIR = os.path.join(data_dir, "cloudflare_ddns_updater")
LOG_FILE_PATH = os.path.join(LOG_DIR, "cf_updater.log")

# Ensure directories exist
os.makedirs(CONFIG_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Set directory permissions to allow only the owner to access
# os.chmod(CONFIG_DIR, 0o700)
# os.chmod(LOG_DIR, 0o700)

