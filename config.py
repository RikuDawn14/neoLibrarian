COMMON_SETTINGS = {
    # Title formatting
    'title_case': True,
    'character_replace':{
        '-': ' ',
        "'": '',
        ':': '',
        '?': '',
        '!': '',
    },
    'keep_alphanumeric': True,
},

MOVIES = {
    'extensions': ['.mkv', '.mp4', '.avi', '.mov', '.m4v'],
    **COMMON_SETTINGS,
    
    # Output patterns
    'output_pattern': '{title} ({year}){ext}',
    'output_pattern_no_year': '{title}{ext}',

    'validation': {
        'year': 'warning',
        'title': 'error',
    },
}

TV_SHOWS = {
    'extensions': ['.mkv', '.mp4', '.avi', '.mov', '.m4v'],
    **COMMON_SETTINGS,

    # Output patterns
    'output_pattern': '{title} S{season:02d}E{episode:02d}{ext}',

    'validation': {
        'season': 'error',
        'title': 'error',
    },
}

BOOKS = {
    'extensions': ['.epub', '.cbz'],
    **COMMON_SETTINGS,

    # Output patterns
    'output_pattern': '{title} v{volume:02d}{ext}',

    'validation': {
        'title': 'error',
    },
}

THEMES = {
    'dark': {
        'background': '#1e1e1e',
        'surface': '#2d2d2d',
        'primary': '#4a9eff',
        'text': '#ffffff',
        'text_muted': '#a0a0a0',
        'success': '#50fa7b',
        'warning': '#f1fa8c',
        'error': '#ff5555',
        'highlight': '#bd93f9',
    },
    'light': {
        'background': '#ffffff',
        'surface': '#f5f5f5',
        'primary': '#0066cc',
        'text': '#000000',
        'text_muted': '#666666',
        'success': '#28a745',
        'warning': '#ffc107',
        'error': '#dc3545',
        'highlight': '#6f42c1',
    }
}

UI_SETTINGS = {
    'active_theme': 'dark',
}

FILE_OPERATIONS = {
    'dry_run_default': True,
    'create_undo_log': True,
    'confirm_before_rename': True, 
}

LOGGING = {
    'log_errors': True,
    'log_operations': True,
    'output_to_console': True,
    'log_file_path': None,
}