import logging
import os
import gzip
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import time


class CompressedTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='midnight', interval=1, backupCount=0, encoding=None, delay=False, utc=False,
                 atTime=None):
        super().__init__(filename, when, interval, backupCount, encoding, delay, utc, atTime)

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None
        current_time = datetime.now().strftime("%Y%m%d")
        dfn = self.baseFilename + "." + current_time + ".log"
        if os.path.exists(dfn):
            os.remove(dfn)
        self.rotate(self.baseFilename, dfn)
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
        if not self.delay:
            self.stream = self._open()
        with open(dfn, 'rb') as f_in:
            with gzip.open(dfn + '.gz', 'wb') as f_out:
                f_out.writelines(f_in)
        os.remove(dfn)


class UTCFormatter(logging.Formatter):
    converter = time.gmtime

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = time.strftime(datefmt, ct)
        else:
            t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
            s = f"{t}.{record.msecs:03d}"
        return s


def setup_logger(name, log_file, level=logging.INFO):
    formatter = UTCFormatter(
        fmt='%(asctime)s.%(msecs)03d | %(levelname)8s | %(funcName)s:%(lineno)d | %(process)d | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler = CompressedTimedRotatingFileHandler(log_file, when="midnight", interval=1)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Usage
if __name__ == "__main__":
    logger = setup_logger('my_logger', 'app.log')

    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
