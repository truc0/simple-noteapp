### App Settings

# production settings
ALLOWED_HOSTS=[]
DEBUG=True

## app config

# see https://djecrety.ir/
SECRET_KEY=''  

ALLOW_REGISTER=True


### Log Settings

# set LOGGING to None to disable logging
LOGGING=None

LOG_FILENAME=''

# an example custom logging setting
"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_FILENAME
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}
"""

