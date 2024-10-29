from jira.model.issue_base import IssueBase
from datetime import datetime

import pytz

tz = pytz.timezone('America/Lima')


class Dependency:
    def __init__(self, name, issue):
        self.name = name
