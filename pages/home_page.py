
from playwright.sync_api import Page, expect

from pages.home_page_locators import HomePageLocators


class HomePage:

    def __init__(self, page: Page):

        self.page = page
        self.locators = HomePageLocators(page)

    # Verification methods
    def debug(self):
        self.page.pause()

    def verify_main_heading(self):
        expect(self.locators.main_heading).to_be_visible()

    def verify_learning_button(self):
        expect(self.locators.learning_button).to_be_visible()

    def verify_games_button(self):
        expect(self.locators.games_button).to_be_visible()

    def verify_topics_navigation(self):
        expect(self.locators.topics_navigation).to_be_visible()

    # Action methods

    def click_learning(self):
        self.locators.learning_button.click()

    def click_games(self):
        self.locators.games_button.click()

    def click_animals(self):
        self.locators.animals_button.click()

    def click_colors(self):
        self.locators.colors_button.click()

    def click_numbers(self):
        self.locators.numbers_button.click()

    def click_fruits(self):
        self.locators.fruits_button.click()

    # Learning actions

    def click_next(self):
        self.locators.next_button.click()


    def click_previous(self):
        self.locators.previous_button.click()


    # Learning verifications

    def verify_word(self, expected_word):
        expect(self.locators.word).to_contain_text(expected_word)


    def verify_translation(self, expected_translation):
        expect(self.locators.translation).to_contain_text(
            expected_translation
        )


    def verify_counter(self, expected_counter):
        expect(self.locators.counter).to_contain_text(
            expected_counter
        )
