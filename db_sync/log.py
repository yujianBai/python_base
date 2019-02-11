import logging
import datetime

def get_logger(name, log_file=None, level=logging.DEBUG):
    log_format = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d]: %(message)s"
    formatter = logging.Formatter(log_format)
    logger = logging.getLogger(name)
    if isinstance(log_file, str):
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    else:
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    logger.setLevel(level)
    return logger

today = str(datetime.datetime.now())[:10]
log = get_logger('sync_data_%s'%today, './sync_data_%s.log'%today)
