from typing import Optional, Union


class ApplicationError(Exception):
    """Use this class when the application identifies there's been a problem and the client should be informed.

    Example: raise ApplicationError("Critical error", "DB")

    or

    raise ApplicationError("Title number invalid", "E102", http_code=400)

    or

    raise ApplicationError("Title number invalid", "E102", http_code=400, force_logging=True)
    """

    def __init__(
        self, message: str, code: Optional[Union[str, int]] = None, http_code: int = 500, force_logging: bool = False
    ) -> None:
        """Create an instance of the error.

        Keyword arguments:

        http_code - handler methods will use this to determine the http code to set in the returned Response
        (default 500)

        force_logging - handler methods will use this to determine whether to log at debug or info, when
        the http code being returned is not 500 (500s are always considered error-level worthy) (default False)
        """
        Exception.__init__(self)
        self.message = message
        self.http_code = http_code
        self.code = code
        self.force_logging = force_logging
