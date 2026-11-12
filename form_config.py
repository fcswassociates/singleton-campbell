"""Shared public FormSubmit action. This URL is not a private API key."""
from pathlib import Path
from urllib.parse import urlsplit
import json

def form_action():
    config=json.loads((Path(__file__).parent/'config/forms.json').read_text())
    action=config['action']
    url=urlsplit(action)
    if (url.scheme!='https' or url.netloc!='formsubmit.co' or url.query or url.fragment
            or len([part for part in url.path.split('/') if part])!=1):
        raise ValueError('Use the public HTTPS FormSubmit form action, not an activation or API URL.')
    return action
