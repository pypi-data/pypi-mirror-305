import logging

LOG_FORMAT_VERBOSE = '%(asctime)s.%(msecs)03d:%(levelname)8s [%(filename)20s:%(lineno)4d] %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'

def configure_and_get_logger(level, name):
    logging.basicConfig(
        datefmt=LOG_DATE_FORMAT,
        format=LOG_FORMAT_VERBOSE,
        level=logging.INFO if level == 'info' else logging.DEBUG
    )

    return logging.getLogger(name)
