import inspect
import logging


class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)

        filehander = logging.FileHandler("logfile.log")
        formattor = logging.Formatter("%(asctime)s: %(levelname)s :%(name)s :%(message)s")
        filehander.setFormatter(formattor)
        logger.addHandler(filehander)

        logger.setLevel(logging.debug())
        return logger