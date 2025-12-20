from pathlib import Path
import re
from config import MOVIES

class MovieParser:
    def __inti__(self):
        self.config = MOVIES
    
    def extract_metadata(self, filepath):
        pattern = re.compile(r'(.+?) \((\d{4})\)')
        parent_dir = Path(filepath).parent.name

        match = re.match(pattern, parent_dir)
        if match:
            title, year = match.groups()
            year = int(year)
        else:
            title = None
            year = None

        return {'title': title, 'year': year}