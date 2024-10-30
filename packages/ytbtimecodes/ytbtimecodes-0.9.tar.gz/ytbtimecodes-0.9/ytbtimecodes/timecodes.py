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


def timedelta_from_seconds(seconds: str) -> str:
    """Create a string representation of a timedelta object from a string representing seconds."""
    time_delta = datetime.timedelta(seconds=int(seconds))  # Convert string to int
    return str(time_delta)  # Return the string representation of the timedelta


def standardize_time_format(time_str: str) -> str:
    _time = str(time_str)
    if _time == '0:00':
        return '0:00'

    if _time == '00:00':
        return '0:00'

    if _time == '0:00:00':
        return '0:00'

    if _time == '00:00:00':
        return '0:00'

    if _time.startswith('00:00:0'):
        return _time.replace('00:00:0', '0:0')

    if _time.startswith('0:00:0'):
        return _time.replace('0:00:0', '0:0')

    if _time.startswith('00:00:'):
        return _time.replace('00:00:', '0:')

    if _time.startswith('0:00:'):
        return _time.replace('0:00:', '0:')

    _time = f'@@{_time}##'
    _time = _time.replace('@@00:00:0', '@@0:0')
    _time = _time.replace('@@0:0', '@@')
    _time = _time.replace('@@0:', '@@')

    return _time.replace('@@', '').replace('##', '')


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
