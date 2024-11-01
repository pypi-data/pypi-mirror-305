# Tracability for Python applications

Convienience Flask extension for retrieving trace IDs from incoming requests.

This package depends on:
* Flask (Version 2.2.2 or higher)
* Python 3.9 or higher

## Usage

Instantiate it like a normal flask extension:

```python
from landregistry.trace_id import TraceID
from <somewhere> import app

# ...

trace_id_extn = TraceID()
trace_id_extn.init_app(app)

# retrieve the current trace ID
trace_id = trace_id_extn.current_trace_id
```

## Properties

TraceID.**current_trace_id**

If the application is serving a request, and the value in the request header `X-Trace-ID` is present and is a valid trace ID, then returns the header value.

If the application is serving a request, and the request header `X-Trace-ID` is absent or contains an invalid trace ID, returns a new trace ID. A new trace ID generated this way will be the same for all calls to **current_trace_id** for a given request.

If the application is not serving a request, returns `N/A`.

