from datetime import datetime
from typing import Any, List, Optional


class AudioWidgetConfig:
    def __init__(self, autoplay: Optional[bool] = None):
        self.autoplay = autoplay


class FormWidgetConfig:
    def __init__(self, schema: Any):
        self.schema = schema


class ModelWidgetConfig:
    def __init__(
        self,
        audio: Optional[AudioWidgetConfig] = None,
        form: Optional[FormWidgetConfig] = None,
    ):
        self.audio = audio
        self.form = form


class ModelTypes:
    def __init__(self, inputs: List[str], output: str):
        self.inputs = inputs
        self.output = output


class ConnectionModel(object):
    def __init__(
        self,
        id: str,
        name: str,
        types: ModelTypes,
        invited_user_id: Optional[List[str]] = None,
        access: str = None,
        schema: Optional[Any] = None,
        description: Optional[str] = None,
        widget_config: Optional[ModelWidgetConfig] = None,
    ):
        self.id = id
        self.name = name
        self.types = types
        self.invited_user_id = invited_user_id
        self.access = access
        self.schema = schema
        self.description = description
        self.widget_config = widget_config


class ConnectOptions:
    server_url: Optional[str] = None


class ResultValue:
    def __init__(self, uri: str, description: str, date: datetime):
        self.uri = uri
        self.description = description
        self.date = date


class ConnectionInput:
    def __init__(
        self,
        id: str,
        binary: bytes,
        mime_type: str,
        user_id: str,
        connection_model_id: str,
        pipe_id: str,
        model_id: str,
        result_id: str,
        layer_id: str,
        config: Any,
        values: List[ResultValue] = None,
    ):
        self.id = id
        self.binary = binary
        self.mime_type = mime_type
        self.user_id = user_id
        self.connection_model_id = connection_model_id
        self.pipe_id = pipe_id
        self.model_id = model_id
        self.result_id = result_id
        self.layer_id = layer_id
        self.config = config
        self.values = values
