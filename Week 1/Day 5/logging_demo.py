import logging

logging.basicConfig(filename="newfile.log",
                    format='%(asctime) s  %(message) s', filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("Internet connection lost")
