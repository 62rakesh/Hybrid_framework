import logging

logging.basicConfig(filename="D://Hybrid_framework//Logs//automation.log",
                    format='%(asctime)s:%(levelname)s:%(message)s:')
logger=logging.getLogger()
logger.setLevel(logging.INFO)

logger.info("********** This is a info message **********")
logger.debug("This is a debug message")
logger.critical("This is a crictical message")
logger.warning("This is a warning message")