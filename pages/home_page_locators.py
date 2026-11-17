
from playwright.sync_api import Page


class HomePageLocators:

    def __init__(self, page: Page):

        # Main heading
        self.main_heading = page.get_by_role(
            "heading",
            name="Let's Learn English!"
        )

        # Main buttons
        self.learning_button = page.get_by_role(
            "button",
            name="לומדים"
        )

        self.games_button = page.get_by_role(
            "button",
            name="משחקים"
        )

        # Topics navigation

        self.topics_navigation = page.get_by_role(
            "navigation",
            name="נושאים"
        )

        self.animals_button = self.topics_navigation.locator(
            '[data-k="animals"]'
        )

        self.colors_button = self.topics_navigation.locator(
            '[data-k="colors"]'
        )

        self.numbers_button = self.topics_navigation.locator(
            '[data-k="numbers"]'
        )

        self.fruits_button = self.topics_navigation.locator(
            '[data-k="fruits"]'
        )
        # Learning content
        self.word = page.locator("#word")

        self.translation = page.locator("#he")

        self.counter = page.locator("#count")

        # Navigation buttons
        self.next_button = page.get_by_role(
            "button",
            name="הבא"
        )

        self.previous_button = page.get_by_role(
            "button",
            name="הקודם"
        )

