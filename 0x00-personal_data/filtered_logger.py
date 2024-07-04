#!/usr/bin/env python3
'''
This module implements message logging
'''
import logger


logging.basicConfig(fields=[''])


def filter_datum(fields, redaction, message, seperator):
    '''
    This function returns the log message obfuscated
    '''
