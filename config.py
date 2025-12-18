Movies = {
    'extensions': [mkv, mp4, avi, mov, m4v],
    'output_pattern': '{title} ({year}){ext}',
    'input_patterns': [
        Pattern 1: Title.Year.Other.Stuff.ext
        Pattern 2: Title (Year) [Quality].ext
        Pattern 3: Title_Year_quality.ext
    ],
    'metadata_fields': ['title', 'year'],
}