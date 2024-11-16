#!/usr/bin/python3
"""Module to return the JSON string representation of an object."""

import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object."""
    return json.dumps(my_obj)

