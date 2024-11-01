import json
import traceback
from typing import Callable, Optional, Union

from flask import Flask, Response, current_app
from werkzeug.exceptions import HTTPException, default_exceptions

from .application_error import ApplicationError


class ExceptionHandlers(object):
    def __init__(self, app: Optional[Flask] = None, allow_codes: Optional[list[int]] = None) -> None:
        self.app = app
        self.on_application_error_render: Optional[Callable] = None
        self.on_unhandled_error_render: Optional[Callable] = None
        self.on_http_error_render: Optional[Callable] = None
        self.allow_codes = allow_codes

        if app is not None:
            self.init_app(app, allow_codes)

    def init_app(self, app: Flask, allow_codes: Optional[list[int]] = None) -> None:
        self._register_exception_handlers(app)

        # Avoid potentially overwriting set self.allow_codes with default None parameter
        if allow_codes is not None:
            self.allow_codes = allow_codes

    def _get_result_code(self, http_code: int) -> int:
        if self.allow_codes is None:
            return http_code

        if http_code in self.allow_codes:
            return http_code

        return 500

    def _register_exception_handlers(self, app: Flask) -> None:
        app.register_error_handler(ApplicationError, self.application_error_handler)
        app.register_error_handler(Exception, self.unhandled_error_handler)

        for exception in default_exceptions:
            app.register_error_handler(exception, self.http_error_handler)

        app.logger.info("Exception handlers registered")

    def application_error_handler(self, e: ApplicationError) -> Response:
        if e.http_code == 500:
            current_app.logger.exception(
                "Application Exception (message: %s, code: %s): %s", e.message, e.code, repr(e)
            )
        elif e.force_logging:
            current_app.logger.info(
                "Application Exception (message: %s, code: %s): %s", e.message, e.code, repr(e), exc_info=True
            )
        else:
            current_app.logger.debug(
                "Application Exception (message: %s, code: %s): %s", e.message, e.code, repr(e), exc_info=True
            )

        http_code = self._get_result_code(e.http_code)
        if self.on_application_error_render:
            return self.on_application_error_render(e.message, e.code, http_code, e)

        return self._default_application_error(e)

    def unhandled_error_handler(self, e: BaseException) -> Union[Response, HTTPException]:
        current_app.logger.exception("Unhandled Exception: %s", repr(e))
        if self.on_unhandled_error_render:
            return self.on_unhandled_error_render("Internal server error", 500, 500, e)

        return self._default_unhandled_error(e)

    def http_error_handler(self, e: BaseException) -> Response:
        # By default, only the UI needs to handle this specifically (to generate a custom page)
        if isinstance(e, HTTPException) and e.code is not None:
            http_code = self._get_result_code(e.code)
        else:
            http_code = 500

        error_code: Union[int, None] = None
        if isinstance(e, HTTPException):
            error_code = e.code

        if self.on_http_error_render:
            return self.on_http_error_render(None, error_code, http_code, e)

        return self._default_http_error(e, http_code)

    def _default_http_error(self, e: BaseException, http_code: int) -> Response:
        response_dict = {"error_message": "", "error_code": http_code}

        # Werkzeug exceptions have a 'description' attribute
        if hasattr(e, "description"):
            response_dict["error_message"] = e.description
        elif hasattr(e, "message"):
            response_dict["error_message"] = e.message

        return Response(
            response=json.dumps(response_dict, separators=(",", ":")), mimetype="application/json", status=http_code
        )

    def _default_application_error(self, e: BaseException) -> Response:
        response_dict = {"error_message": "", "error_code": ""}

        if hasattr(e, "message"):
            response_dict["error_message"] = e.message
        elif hasattr(e, "description"):
            # Shouldn't happen - HTTPExceptions are handled elsewhere, but should someone change the callbacks...
            response_dict["error_message"] = e.description

        if hasattr(e, "code"):
            response_dict["error_code"] = e.code

        # If we are logging at debug level, also return the stack trace for greater visibility
        if current_app.config.get("FLASK_LOG_LEVEL", "INFO").upper() == "DEBUG":
            response_dict["stacktrace"] = traceback.format_exc()

        http_code = 500
        if hasattr(e, "http_code"):
            http_code = e.http_code

        return Response(
            response=json.dumps(response_dict, separators=(",", ":")), mimetype="application/json", status=http_code
        )

    def _default_unhandled_error(self, e: BaseException) -> Union[Response, HTTPException]:
        if isinstance(e, HTTPException):
            return e

        response_dict = {"error_message": "Internal Server Error", "error_code": 500}

        # If we are logging at debug level, also return the stack trace for greater visibility
        if current_app.config.get("FLASK_LOG_LEVEL", "INFO").upper() == "DEBUG":
            response_dict["stacktrace"] = traceback.format_exc()

        return Response(
            response=json.dumps(response_dict, separators=(",", ":")), mimetype="application/json", status=500
        )
