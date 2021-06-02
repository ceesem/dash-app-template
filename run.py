from dash_app_template import create_app

###########################################################
# This run.py will work for local testing of the dash app #
###########################################################

config = {
    "VALUE": "your_parameter_here",
}

if __name__ == "__main__":
    app = create_app(config=config)
    app.run_server(port=8050)
