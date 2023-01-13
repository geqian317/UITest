"""生成器配置"""
import logging.config

# 路径在调用的地方填写
def get_log(path):
    logging.config.fileConfig(path)
    return logging.getLogger()

