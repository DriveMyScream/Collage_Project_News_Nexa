import streamlit as st
from streamlit_option_menu import option_menu
from pages import fake_news_classification, news_classification, news_summarization, news_translation
st.set_page_config(page_title="News Nexa")


class MultiApp:
    """ Framework for creating a multi-page Streamlit application. """

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """ Adds a new page to the application.

        Args:
            title (str): The title of the page.
            func (callable): The function that renders the content of the page.
        """
        self.apps.append({"title": title, "function": func})

    def run(self):
        """ Runs the Streamlit application. """

        selected_app = option_menu(
            menu_title="News Nexa: Beyond Headlines",
            options=[app["title"] for app in self.apps],
            icons=["newspaper", "filter", "book", "translate"],
            menu_icon="chat-text-fill",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "black"},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},
            },
        )
        for app in self.apps:
            if app["title"] == selected_app:
                app["function"]()
                break


if __name__ == "__main__":
    app = MultiApp()
    app.add_app("Fake News Classification", fake_news_classification.app)
    app.add_app("News Category Classification", news_classification.app)
    app.add_app("News Summarization", news_summarization.app)
    app.add_app("News Translation", news_translation.app)
    app.run()
