from FPV.Helpers._base_service import BaseService


class Windows(BaseService):

    invalid_characters = '<>:"|?*'

    def __init__(self, path, auto_clean = False):
        super().__init__(path, auto_clean)
        self.max_length = 255 # I've also seen it as 260 in some places ?

        # Check for reserved names in Windows
        self.RESTRICTED_NAMES = {
            "CON", "PRN", "AUX", "NUL",
            "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
            "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
        }

    def check_if_valid(self):
        """Check validity of the full path for Windows, including base checks and Windows-specific checks."""
        super().check_if_valid()  # Calls the base validation logic
        for part in self.path_parts:
            if part.upper() in self.RESTRICTED_NAMES:
                raise ValueError(f'Reserved name "{part}" is not allowed in Windows.')

class MacOS(BaseService):
    # mac os doesn't have any invalid characters other than 
    # the obvious path delimiter but we're already handling that 
    # in the base class. 
    invalid_characters = '' 

    def __init__(self, path, auto_clean = False):
        super().__init__(path, auto_clean)

    def check_if_valid(self):
        super().check_if_valid()  # Call base validation first

        # Check for reserved file names (not explicitly required, but avoid common issues)
        self.RESTRICTED_NAMES = {
            ".DS_Store",
            "._myfile"
        }

        if self.filename in self.RESTRICTED_NAMES:
            raise ValueError(f'Reserved name "{self.filename}" is not allowed.')

        return True
    
    def get_cleaned_path(self, raise_error: bool = True):
        return super().get_cleaned_path(raise_error)


class Linux(BaseService):
    invalid_characters = '\0'  # Only null character is invalid in Linux

    def __init__(self, path, auto_clean = False):
        super().__init__(path, auto_clean)

    def check_if_valid(self):
        super().check_if_valid()  # Call base validation first

        # Linux-specific checks can go here if needed

        return True
    
    def get_cleaned_path(self, raise_error: bool = True):
        return super().get_cleaned_path(raise_error)
