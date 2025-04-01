import os

from shiny import App, render, ui

app_ui = ui.page_fixed(
    ui.output_text("user"),
)


def server(input, output, session):
    @render.text()
    def user():
        try:
            user = os.getlogin()
        except OSError:
            user = None

        user = user if session.user is None else session.user
        return f"Current user: {user}"


app = App(app_ui, server)
