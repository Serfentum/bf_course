import logging


# To turn logging on    - change logging level to DEBUG
# To turn logging off   - change logging level to something higher e.g. INFO
logging.basicConfig(filename='my_log.log',
                    filemode='w',
                    format='%(asctime)s from %(pathname)s with %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


logger.info('Starting work...')
summa = 0
for i in range(10):
    summa += i
    logger.debug('i is %s', i)
    logger.debug('summa is %s', summa)

print(summa)
logger.info("Job's done!")
