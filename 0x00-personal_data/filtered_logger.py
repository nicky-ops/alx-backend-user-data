#!/usr/bin/env python3
'''
This module implements message logging
'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    '''
    This function constructs a regex pattern to match the specified
    fields and uses re.sub to replace the values of these fields
    with the redaction string.
    '''
    pattern = pattern = '|'.join(f"{field}=[^{separator}]*" for field in fields)
    return re.sub(pattern, lambda m: f"{m.group().split('=')[0]}={redaction}", message)
