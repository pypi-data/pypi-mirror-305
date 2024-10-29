"""A place for shared paths and settings."""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.absolute()
PACKAGE_ROOT = Path(__file__).parent.absolute()
PYPROJECT_TOML = PROJECT_ROOT / 'pyproject.toml'

DEFAULT_ENDPOINT_URL = (
    'https://ovsyndication.kicker.de/API/universal/3.0'
)
REQUEST_TIMEOUT_SEC = 30

debugMode = bool(os.getenv('KICKERDE_API_CLIENT_DEBUG'))
