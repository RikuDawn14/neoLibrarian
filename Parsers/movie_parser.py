from os import path
import re

def extract_metadata(filepath):
    pattern = re.compile(r'(.+?) \((\d{4})\)')
    parent_dir = os.path.basename(filepath)

    match = re.match(pattern, parent_dir)
    title, year = match.groups()

    return {'title': f"{title}", 'year': f"{year}"}