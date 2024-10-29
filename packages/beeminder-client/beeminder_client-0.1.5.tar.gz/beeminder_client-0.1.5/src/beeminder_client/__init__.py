"""A Python client library and terminal interface for Beeminder."""

from .beeminder import BeeminderAPI
from .models import BeeminderGoal, Datapoint, Contract

__version__ = "0.1.0"
__all__ = ['BeeminderAPI', 'BeeminderGoal', 'Datapoint', 'Contract']