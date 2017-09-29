import logging
import datetime

def GetLog():
    fileName = datetime.date.strftime(datetime.datetime.now(), "%Y%m%d")
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='backup_{0}.log'.format(fileName),
                        filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    log = logging.getLogger('Backup')
    return log
