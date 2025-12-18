class BaseParser:
    def parse_single(self, filepath):
        # For movies and books
        raise NotImplementedError
    
    def parse_batch(self, filepaths):
        # For TV shows
        raise NotImplementedError