import re
import uuid
from typing import Optional

import flask
from flask import Flask, g


class TraceID(object):
    def __init__(self, app: Optional[Flask] = None) -> None:
        self.app = app
        self.trace_regex = re.compile("^[a-z0-9- ]{1,256}$", flags=re.IGNORECASE)

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        app.teardown_request(self.teardown_request)

        if not hasattr(app, "extensions"):  # pragma: no cover
            app.extensions = {}

        app.extensions["landregistry.trace_id"] = {"current_trace": None}

    def is_trace_valid(self, trace_id: str) -> bool:
        # Trace ID doesn't *need* to be a valid UUID, so validate that it's alpha-numerics and spaces
        # and that its length is sane.
        return trace_id is not None and self.trace_regex.match(trace_id) is not None

    def teardown_request(self, exception: Optional[BaseException]) -> None:
        g._hmlr_generated_trace_id = None

    @property
    def current_trace_id(self) -> str:
        if not flask.ctx.has_request_context():
            return "N/A"
        else:
            trace_id = flask.request.headers.get("X-Trace-ID")
            if not self.is_trace_valid(trace_id):
                trace_id = self._generated_trace_id

            return trace_id

    @property
    def _generated_trace_id(self) -> str:
        if "_hmlr_generated_trace_id" not in g:
            g._hmlr_generated_trace_id = uuid.uuid4().hex
        return g._hmlr_generated_trace_id
