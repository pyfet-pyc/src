import logging
import time

from flask import make_response, request
from flask_restful import abort
from funcy import project
from sqlalchemy.exc import IntegrityError

from redash import models
from redash.handlers.base import BaseResource, get_object_or_404, require_fields
from redash.permissions import (
    require_access as acc,
    require_admin as ad,
    require_permission as pe,
)