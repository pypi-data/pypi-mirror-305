import json
import time

from ..api_provider import ApiProvider
from ..utils.cache_utils import CacheUtils
from ..utils.setting_utils import SettingUtils


def get_json_file():
    with open("config.test.json", "r") as f:
        try:
            return json.loads(f.read())
        except:
            return {}
def save_json_file(data):
    with open("config.test.json", "w+") as f:
        f.write(json.dumps(data))


def cache_get(key):
    a = get_json_file()
    if "cache" in a and key in a["cache"] and (
            "expire_at" not in a["cache"][key] or a["cache"][key]["expire_at"] >= time.time()):
        return a["cache"][key]["value"]
    return None


def cache_set(key, value, expire=None):
    a = get_json_file()
    if "cache" not in a:
        a["cache"] = {}
    if key not in a["cache"]:
        a["cache"][key] = {}
    a["cache"][key]["value"] = value
    if expire is not None:
        a["cache"][key]["expire_at"] = time.time() + expire
    save_json_file(a)


def set_setting(api_provider: ApiProvider, key: str, value: str, expire: int = None):
    a = get_json_file()
    if "setting" not in a:
        a["setting"] = {}
    if key not in a["setting"]:
        a["setting"][key] = {}
    a["setting"][key]["value"] = value
    if expire is not None:
        a["setting"][key]["expire_at"] = time.time() + expire
    save_json_file(a)


def get_setting(api_provider: ApiProvider, key: str, default: str = None):
    a = get_json_file()
    if "setting" in a and key in a["setting"] and (
            "expire_at" not in a["setting"][key] or a["setting"][key]["expire_at"] >= time.time()):
        return a["setting"][key]["value"]
    return None


def reg_setting_cache_test():
    CacheUtils.register_get(cache_get)
    SettingUtils.register_get_setting(get_setting)
    CacheUtils.register_set(cache_set)
    SettingUtils.register_set_setting(set_setting)
