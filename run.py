from dash_app_template import create_app


if __name__ == "__main__":
    app = create_app()
    app.run_server(port=8050)
