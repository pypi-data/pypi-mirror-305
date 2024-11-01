# Flask Exception Handlers

Defines an extension for standardising exception handling in HMLR's Flask applications.

## Basic Usage

Initialise as any Flask extension:

```python
exception_handlers = ExceptionHandlers()

def register_extensions(app):
    exception_handlers.init_app(app)
```

## Custom Renderers

If you need to change how the errors are returned to the client, use the `on_http_error_render`, `on_application_error_render` and `on_unhandled_error_render` event handlers:

```python
def http_error_renderer(description, code, http_code, e=None):
    return render_template('app/errors/unhandled.html', http_code=http_code), http_code


def unhandled_error_renderer(description, code, http_code, e=None):
    return render_template('app/errors/unhandled.html', http_code=http_code), http_code


def application_error_renderer(description, code, http_code, e=None):
    try:
        return render_template('app/errors/application/{}.html'.format(e.code), description=e.message, code=e.code,
                               http_code=http_code, e=e), http_code
    except TemplateNotFound:
        return render_template('app/errors/application.html', description=e.message, code=e.code, http_code=http_code),
                               http_code


def register_exception_handlers(app):
    handlers = ExceptionHandlers()
    handlers.init_app(app)
    handlers.on_http_error_render = http_error_renderer
    handlers.on_application_error_render = application_error_renderer
    handlers.on_unhandled_error_render = unhandled_error_renderer
```

## Suppressing HTTP Response Codes

Want your app to only send certain HTTP response codes? Supply the list of **allowed** codes to `init_app`:

```python
handlers = ExceptionHandlers()
handlers.init_app(app, [403, 404])
# Or...
handlers = ExceptionHandlers(app=app, allow_codes=[418])
```

(Anything not in the list gets replaced with a 500).

The helper list `ALLOWED_UI_RESPONSES` (403, 404, 429 and 500) is available:

```python
from landregistry.exceptions import ExceptionHandlers, ALLOWED_UI_RESPONSES

handlers = ExceptionHandlers()
handlers.init_app(app, ALLOWED_UI_RESPONSES)
```

## ApplicationError

Use this class when the application identifies there's been a problem and the client should be informed.

*exception* **ApplicationError**(*message: str, error_code: str, http_code: int, force_logging: bool*)

`message` The text of the exception message.

`error_code` Unique identifier for the error. Can be anything, but useful to reference in support documentation or
knowledge items.

`http_code` Defaults to 500. Specifies the HTTP response code to send.

`force_logging` Defaults to False. Forces logging to Info if True (Debug otherwise). If the http code is 500, this
parameter is ignored (and logging is to Error).

Examples:

```python
from landregistry.exceptions import ApplicationError

raise ApplicationError("Critical error", "DB")
# or
raise ApplicationError("Title number invalid", "E102", http_code=400)
# or
raise ApplicationError("Title number invalid", "E102", http_code=400, force_logging=True)
```
