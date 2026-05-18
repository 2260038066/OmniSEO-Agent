import logging
import colorlog

# 配置终端带有颜色的日志输出，显得非常专业
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - [%(levelname)s] - %(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
))

logger = colorlog.getLogger('OmniSEO')
logger.addHandler(handler)
logger.setLevel(logging.INFO)