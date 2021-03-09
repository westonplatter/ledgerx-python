from os.path import join, dirname
from dotenv import dotenv_values


def get_env_api_key() -> str:
    filename = join(dirname(__file__), "../.env")
    configs = dotenv_values(dotenv_path=filename, verbose=True)
    return configs["API_KEY"]
