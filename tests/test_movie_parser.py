from parsers.movie_parser import MovieParser

parser = MovieParser()

# Test cases
test_paths = [
    '/Movies/The Matrix (1999)/The Matrix (1999).mkv',
    '/Movies/SomeMovie/file.mkv',
    '/Movies/Invalid [2020]/file.mkv',
]

for path in test_paths:
    result = parser.extract_metadata(path)
    print(f"{path}")
    print(f"  Result: {result}")
    print()