import ast
import logging
import os

from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(format="%(asctime)s |%(name)s| %(levelname)s: %(message)s", level=logging.INFO)
log = logging.getLogger(__name__)


# Rabbitmq
RABBITMQ_URL = os.environ.get('RABBITMQ_URL')
QUEUE_OPTIMIZER = os.environ.get('QUEUE_OPTIMIZER')
CONSUMER_TAG = os.environ.get('CONSUMER_TAG')

# Redis



def load():
    log.info('Loading settings...')
    required_env_vars = [
        'RABBITMQ_URL',
        'QUEUE_OPTIMIZER',
        'CONSUMER_TAG',
    ]

    for env_var in required_env_vars:
        if env_var not in os.environ:
            raise EnvironmentError(f'Environment variable not founded.')
