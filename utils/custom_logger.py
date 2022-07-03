import logging


class LogsGeneration:

    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\logs\\automation.log",
                            datefmt="'%Y-%m-%d %H:%M:%S")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
