from .login import *
from .fox import *

# 检查更新
def check_update():
    new_verision, time = update_syj()
    if not new_verision and not time:
        logger.error(f"兽云祭模块:无法获取最新的版本，当前版本为{syj_config.syj_version}，可能已经过时！")
    else:
        if new_verision <= syj_config.syj_version:
            logger.success(f"兽云祭模块:当前版本为{syj_config.syj_version},仓库版本为{new_verision}")
        else:
            logger.success("兽云祭模块:检查到本插件有新版本！")
            venv = os.getcwd()
            if os.path.exists(f"{venv}/.venv"):
                logger.success("正在自动更新中--找到虚拟环境![开始安装]")
                os.system(f'"{venv}/.venv/Scripts/python.exe" -m pip install nonebot-plugin-FurIllustrated=={new_verision} -i https://pypi.Python.org/simple/')
                logger.success(f"兽云祭模块:更新完成！最新版本为{new_verision}|当前使用版本为{syj_config.syj_version}")
                logger.warning(f"兽云祭模块:你可能需要重新启动nonebot来完成插件的重载")
            else:
                logger.warning("正在自动更新中--未找到虚拟环境！[安装在本地环境]")
                os.system(f'pip install nonebot-plugin-FurIllustrated=={new_verision} -i https://pypi.Python.org/simple/')
                logger.success(f"兽云祭模块:更新完成！最新版本为{new_verision}|当前使用版本为{syj_config.syj_version}")
                logger.warning(f"兽云祭模块:你可能需要重新启动nonebot来完成插件的重载")

#update-----syj
def update_syj():
    fails = 0
    while True:
        try:
            if fails >= 20:
                verision = False
                time = False
                break
            headers = {'content-type': 'application/json'}
            get_json = httpx.get(url="https://pypi.org/pypi/nonebot-plugin-FurIllustrated/json", headers=headers ,timeout=50)
            if get_json.status_code == 200:
                json = get_json.json()
                verision = json["info"]["version"]
                time = json["releases"][f"{verision}"][0]["upload_time"]
            else:
                continue
        except:
            fails += 1
            logger.warning("网络状况不佳，检查最新版本失败，正在重新尝试")
        else:
            break
    return verision,time


try:
    check_update()
except Exception as e:
    logger.opt(colors=True).error(f"检测更新失败！！{e}")
