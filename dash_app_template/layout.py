import dash_core_components as dcc
import dash_html_components as html
import flask
from .dash_url_helper import create_component_kwargs, State


#####################
# title must be set #
#####################

# The title gives the title of the app in the browser tab
title = "Dash App Template"


###################################################################
# page_layout must be defined to take a state and return a layout #
###################################################################


def page_layout(state: State = {}):
    """This function returns the layout object for the dash app.
    The state parameter allows for URL-encoded parameter values.

    Parameters
    ----------
    state : State, optional
        URL state, a series of dicts that can provide parameter values, by default None

    Returns
    -------
    layout : list
        List of layout components for the dash app.
    """
    layout = [
        html.H1("A Basic Dash App Layout"),
        html.Hr(),
        html.Div(id="config-output", children=""),
        html.Hr(),
        html.Div(id="client-output", children=""),
        html.Hr(),
        html.Div(
            [
                html.Div(
                    "This is a standard Dash parameter that is not saved in the URL."
                ),
                dcc.Input(
                    id="unsaved-input",
                    value="",
                    type="text",
                ),
                html.Div(id="unsaved-output", children=""),
            ]
        ),
        html.Hr(),
        html.Div(
            [
                html.Div(
                    "This is a URL-encoded parameter. The value in the URL is synchronized to the state of the input. Try changing the input value here while watching the URL and vice versa."
                ),
                dcc.Input(
                    **create_component_kwargs(
                        state,
                        id_inner="url-encoded-component",  # id_inner is used in place of the id field of a standard Input id.
                        value="default_value",
                        type="text",
                    )
                ),
                html.Div(id="url-encoded-output", children=""),
            ]
        ),
        html.Hr(),
        html.Div(
            [
                html.Div(
                    'Here we are refencing a hidden input, which allows parameters to be set by the URL (in this case after "example-hidden-value") but not displayed to the user. This can be useful for passing configurable parameters to callbacks.'
                ),
                html.Div(
                    dcc.Input(
                        **create_component_kwargs(
                            state,
                            id_inner="example-hidden-value",
                            value="Hidden Value",
                            type="text",
                        ),
                    ),
                    style={"display": "none"},
                ),
                html.Div(id="example-hidden-output", children=""),
            ]
        ),
    ]
    return layout


######################################################
# Leave this rest alone for making the template work #
######################################################

url_bar_and_content_div = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-layout")]
)


def app_layout():
    # https://dash.plotly.com/urls "Dynamically Create a Layout for Multi-Page App Validation"
    if flask.has_request_context():  # for real
        return url_bar_and_content_div
    # validation only
    return html.Div([url_bar_and_content_div, *page_layout()])
