import logging
import datetime
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Constants
TIMECODE_THRESHOLD_COUNT = 3
TIMECODE_REGEX = r'(\d*:*\d+:+\d+)'
TRIM_CHARS = ' #$%&@()*+[\\]^_`{|}~--−–—'
PUNCTUATION_CHARS = '.,;:?!'

# Patterns to clean text
REPLACEMENT_PATTERNS = [
    '---', '--', '===', '==', ' =', '___', '__', '_ _ _', '_ _', ' _',
    '\n-', '\n=', '\n_', '\n -', '\n =', '\n _'
]


def standardize_time_format(time_str):
    """Standardizes various time formats."""
    time_str = str(time_str)

    # Standardize '0' hour and minute formats
    if time_str in {'0:00', '00:00', '0:00:00', '00:00:00'}:
        return '0:00'

    # Remove unnecessary leading zeros
    if time_str.startswith(('00:00:', '0:00:')):
        return time_str.replace('00:00:', '0:').replace('0:00:', '0:')

    # Further refine format if leading zeros in seconds
    if time_str.startswith(('00:00:0', '0:00:0')):
        return time_str.replace('00:00:0', '0:0').replace('0:00:0', '0:0')

    return time_str


def clean_input_text(text):
    """Cleans unwanted patterns and trims whitespace from the text."""
    for pattern in REPLACEMENT_PATTERNS:
        text = text.replace(pattern, '')
    return text.strip()


def convert_time_to_seconds(time_str):
    """Converts a time string in 'MM:SS' or 'HH:MM:SS' format to seconds."""
    try:
        if time_str.count(':') == 1:
            time_obj = datetime.datetime.strptime(time_str, '%M:%S')
            return time_obj.minute * 60 + time_obj.second
        elif time_str.count(':') == 2:
            time_obj = datetime.datetime.strptime(time_str, '%H:%M:%S')
            return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
    except ValueError:
        raise ValueError("Unrecognized time format")


def locate_timecodes_block(text):
    """Finds a block of text containing multiple timecodes."""
    if not text:
        return ''

    for block in text.split('\n\n'):
        if len(re.findall(TIMECODE_REGEX, block)) > TIMECODE_THRESHOLD_COUNT:
            return block
    return ''


def extract_timecodes(text):
    """Extracts timecodes and their associated titles from the text."""
    timecodes_block = clean_input_text(locate_timecodes_block(text))

    timecodes = []
    for line in timecodes_block.split('\n'):
        if not (matches := re.findall(TIMECODE_REGEX, line)):
            continue

        raw_timecode = matches[0]
        title = line.replace(raw_timecode, '').strip(TRIM_CHARS).lstrip(PUNCTUATION_CHARS)

        timecodes.append({
            'time': convert_time_to_seconds(raw_timecode),
            'title': title,
        })

    return timecodes


def filter_timecodes_within_bounds(timecodes, start_time, end_time):
    """Filters timecodes that fall within the specified start and end times."""
    start_time, end_time = int(start_time), int(end_time)
    return [timecode for timecode in timecodes if start_time <= int(timecode.get('time')) <= end_time]
