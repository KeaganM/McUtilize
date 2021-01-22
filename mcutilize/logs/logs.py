# todo may go into the project structurer
# todo may want to look into a way where we can set it up to run a script to set up logging from anywhere

import os
import json
import logging
from logging import config

from mcutilize.file_ops.file_ops import create_path

_default_log_settings = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
        # 'file': {
        #     'level': 'DEBUG',
        #     'formatter': 'standard',
        #     'class': 'logging.StreamHandler',
        #     'filename':'log.log',
        #     'mode':'w'
        # },

    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

def create_log_settings(settings_folder_path: str = './settings',overwrite=False, **kwargs):


    if not os.path.isdir(settings_folder_path):
        create_path(settings_folder_path)

    config_file_path = os.path.join(settings_folder_path,'logging_config.json')

    if not os.path.isfile(config_file_path) or overwrite:
        with open(config_file_path, 'w') as file:
            json.dump(_default_log_settings,file)

def create_logger(settings_folder_path: str = './settings/logging_config.json',logger:str='root') -> logging.getLogger:

    with open(settings_folder_path,'r') as file:
        config.dictConfig(json.load(file))
    return logging.getLogger(logger)


if __name__ == '__main__':
    from logging import config
    import logging

    create_log_settings('./settings')
    logger = create_logger(logger='root')

    # config.dictConfig(_default_log_settings)
    # logger = logging.getLogger('root')
    #
    def action():
        for x in range(10):
            logger.info(f'on item {x}')

    action()
