"""Lambda function handler."""

# must be the first import in files with lambda function handlers
import lambdainit  # noqa: F401

import config
import icebreakers
import lambdalogging

import json
import requests

LOG = lambdalogging.getLogger(__name__)
JSON_HEADER = {'Content-Type': 'application/json'}


def send_ice_breaker(event, context):
    """Lambda function handler."""
    data = {'Content': _get_message()}
    LOG.debug('Sending Chime message: %s', data['Content'])
    requests.post(config.CHIME_URL, data=json.dumps(data), headers=JSON_HEADER)


def _get_message():
    return "/md @Present Let's get to know each other a little better!\n\n" \
        "\n\n**Ice Breaker:** {}".format(icebreakers.get_random())
