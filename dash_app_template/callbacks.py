from dash.dependencies import Input, Output
from annotationframeworkclient import FrameworkClient
import flask

# Callbacks using data from URL-encoded parameters requires this import
from .dash_url_helper import _COMPONENT_ID_TYPE

######################################
# register_callbacks must be defined #
######################################

DEFAULT_SERVER_ADDRESS = "https://global.daf-apis.com"
DEFAULT_DATASTACK = "minnie65_phase3_v1"

# This function makes a FrameworkClient that is compatible with the meta-app authentication token.
# Note that the auth token comes from the flask global parameters if present,
# or else is set to None and thus uses your default credentials, for example for local testing.
def make_client(config):
    auth_token = flask.g.get("auth_token", None)
    datastack = config.get("DATASTACK", DEFAULT_DATASTACK)
    server_address = config.get("SERVER_ADDRESS", DEFAULT_SERVER_ADDRESS)
    client = FrameworkClient(
        datastack, server_address=server_address, auth_token=auth_token
    )
    return client


def register_callbacks(app, config):
    """This function must be present and add all callbacks to the app.
    Note that inputs from url-encoded values have a different structure than other values.
    A config dict is also allowed to configure standard parameter values for use in callback functions.

    Here, we show basic examples of using the three parameters defined in the layout.page_layout function.

    Parameters
    ----------
    app : Dash app
        Pre-made dash app
    config : dict
        Dict for standard parameter values
    """

    @app.callback(
        Output("config-output", "children"),
        Input("config-output", "children"),
    )
    def config_output(_):
        return f'Here is a parameter from the config: {config.get("VALUE")}'

    @app.callback(
        Output("client-output", "children"),
        Input("client-output", "children"),
    )
    def build_client(_):
        client = make_client(config)
        return f"I configured a client for the server {client.server_address}"

    @app.callback(
        Output("unsaved-output", "children"),
        Input("unsaved-input", "value"),
    )
    def unsaved_input_parameter(value):
        return f'The unsaved input value is "{value}"'

    @app.callback(
        Output("url-encoded-output", "children"),
        Input(
            {"id_inner": "url-encoded-component", "type": _COMPONENT_ID_TYPE}, "value"
        ),
    )
    def url_encoded_parameter(value):
        return f'The url-encoded value is "{value}"'

    @app.callback(
        Output("example-hidden-output", "children"),
        Input(
            {"id_inner": "example-hidden-value", "type": _COMPONENT_ID_TYPE}, "value"
        ),
    )
    def hidden_url_encoded_parameter(value):
        return f'The hidden url-encoded value is "{value}"'

    pass
