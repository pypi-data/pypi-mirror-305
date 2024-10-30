import logging
import datetime
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Constants
TIMECODES_THRESHOLD_COUNT = 3
TIMECODE_PATTERN = r'(\d*:*\d+:+\d+)'
STRIP_CHARS = ' #$%&@()*+[\\]^_`{|}~--−–—'
DOTS_CHARS = '.,;:?!'

# Replacement patterns to clean text
REPLACEMENTS = [
    '---', '--', '===', '==', ' =', '___', '__', '_ _ _', '_ _', ' _',
    '\n-', '\n=', '\n_', '\n -', '\n =', '\n _'
]


def clean_text(text):
    """Removes unwanted patterns and trims whitespace from the text."""
    for pattern in REPLACEMENTS:
        text = text.replace(pattern, '')
    return text.strip()


def time_to_seconds(time_str):
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


def find_timecodes_block(text):
    """Finds the block of text containing multiple timecodes."""
    if not text:
        return ''
    for part in text.split('\n\n'):
        if len(re.findall(TIMECODE_PATTERN, part)) > TIMECODES_THRESHOLD_COUNT:
            return part
    return ''


def extract_timecodes(text):
    """Extracts timecodes and associated titles from the text."""
    timecodes_block_text = clean_text(find_timecodes_block(text))

    timecodes = []
    for row in timecodes_block_text.split('\n'):
        if not (matched := re.findall(TIMECODE_PATTERN, row)):
            continue

        timecode_raw = matched[0]
        title = row.replace(timecode_raw, '').strip(STRIP_CHARS).lstrip(DOTS_CHARS)

        timecodes.append({
            'time': time_to_seconds(timecode_raw),
            'title': title,
        })

    return timecodes
