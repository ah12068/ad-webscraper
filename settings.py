from dotenv import find_dotenv, load_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

AD_USER = os.environ['AD_USER']
AD_PWD = os.environ['AD_PW']

SELENIUM_DL_SETTINGS = {
        "download.default_directory": os.getcwd(),
        "download.prompt_for_download": False,
        "download.directory_upgrade": False,
        "safebrowsing.enabled":  True
    }