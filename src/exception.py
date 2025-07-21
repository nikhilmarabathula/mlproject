import sys

def get_error_message(error_message, error_details: sys):
    """
    Returns a formatted error message with traceback details.
    """
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return f"Error occurred in file: {file_name}, line: {line_number}, message: {error_message}"

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message, error_details)

    def __str__(self):
        return self.error_message
