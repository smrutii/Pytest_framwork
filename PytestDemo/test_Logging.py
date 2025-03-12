import logging

def test_loggingDemo():

    logger =logging.getLogger(__name__)

    filehander =logging.FileHandler("logfile.log")
    formattor = logging.Formatter("%(asctime)s: %(levelname)s :%(name)s :%(message)s")
    filehander.setFormatter(formattor)

    logger.addHandler(filehander)

    logger.setLevel(logging.CRITICAL)
    logger.debug("This is a debug Statement")
    logger.info("This is a Info Statement")
    logger.warning("This is a warning Statement")
    logger.error("This is an error Statement")
    logger.critical("Critical issue")