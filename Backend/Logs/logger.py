import logging
import sys


class Logger:
    @staticmethod
    def CreateLog(level, message):
        logging.basicConfig(filename="Backend\\Files\\Log_Files\\file.log",
                            format='%(asctime)s %(message)s', filemode='a')

        # Creating an object
        logger = logging.getLogger()

        # Test messages
        logger.log(level, message)
