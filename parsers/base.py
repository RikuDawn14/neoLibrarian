class BaseParser:
    def parse_single(self, filepath):
        # For movies and books
        raise NotImplementedError
    
    def parse_batch(self, filepaths):
        # For TV shows
        raise NotImplementedError
    
    def _validate_and_format(self, metadata):
        # Check metadata against self.config validation rules
        warnings = []
        errors = []
        for field, severity in self.config['validation'].items():
            if metadata.get(field) is None:
                if severity == 'warning':
                    warnings.append(f'missing_{field}')
                elif severity == 'error':
                    errors.append(f'missing_{field}')
        return {'metadata': metadata, 'warnings': warnings, 'errors': errors}
    
    def extract_metadata(self, filepath_or_filepaths):
        # Child classes override this
        raise NotImplementedError("Child class must implement extract_metadata()")