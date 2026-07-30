# src/gitrec/core/logging.py

from __future__ import annotations

import logging
from logging import getHandlerByName
from logging.config import Handler
from logging.handlers import RotatingFileHandler, HTTPHandler


class GitRecLogger:
    def __init__(self) -> None:
        pass
        