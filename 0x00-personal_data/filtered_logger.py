#!/usr/bin/env python3
'''
This module implements message logging
'''
import re
from typing import List
import logging


PII_FIELDS = ('phone', 'ssn', 'password', 'email', 'name')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        This function filters values in incoming log records
        '''
        original_message = super().format(record)
        return filter_datum(self.fields,
                            self.REDACTION, original_message, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''
    This function constructs a regex pattern to match the specified
    fields and uses re.sub to replace the values of these fields
    with the redaction string.
    '''
    pattern = '|'.join(f"{field}=[^{separator}]*" for field in fields)
    return re.sub(pattern,
                  lambda m: f"{m.group().split('=')[0]}={redaction}", message)


def get_logger() -> logging.Logger:
    '''
    This function creates and configures a logger
    '''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
