
def test_home_page_heading(home_page):
    home_page.debug()

    home_page.verify_main_heading()


def test_learning_button_visible(home_page):

    home_page.verify_learning_button()


def test_games_button_visible(home_page):

    home_page.verify_games_button()


def test_topics_navigation_visible(home_page):

    home_page.verify_topics_navigation()

def test_next_word(home_page):

    home_page.click_next()

    home_page.verify_word("cat")
    home_page.verify_translation("חתול")
    home_page.verify_counter("2 / 8")


def test_previous_word(home_page):

    home_page.click_previous()

    home_page.verify_word("dog")
    home_page.verify_translation("כלב")
    home_page.verify_counter("1 / 8")
    
def test_animals_topic(home_page):

    home_page.click_animals()

    home_page.verify_word("dog")
    home_page.verify_translation("כלב")
    home_page.verify_counter("1 / 8")
