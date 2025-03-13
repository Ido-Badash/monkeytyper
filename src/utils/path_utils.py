from pathlib import Path

class SafePath:
    def __init__(self, relative_path: str = None):
        self._abs_path = Path(relative_path) if relative_path else Path.cwd()

    def get_abs_path(self) -> Path:
        """Get the absolute path of the file"""
        return self._abs_path
    
    def set_abs_path(self, relative_path: str):
        """Set the absolute path of the file"""
        self._abs_path = Path(relative_path)

    def path(self, path: str = "", as_string: bool = False) -> str | Path:
        """
        Get the path in the base folder.
        Raises:
            FileNotFoundError: If the path does not exist
        """
        result_path = (self._abs_path / path).resolve()
        if not Path(result_path).exists():
            raise FileNotFoundError(f"Path not found: {result_path}")
        if as_string:
            return str(result_path)
        else:
            return result_path
        
    def __str__(self):
        return self.path(as_string=True)
