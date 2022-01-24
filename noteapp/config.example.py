ALLOW_REGISTER=False
SECRET_KEY=''
DEBUG=False
ALLOWED_HOSTS=[]
LOG_FILENAME=''
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