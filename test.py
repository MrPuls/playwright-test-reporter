import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def test_google_title(page: Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")

def test_search_input_exists(page: Page):
    page.goto("https://www.google.com")
    search_box = page.locator('textarea[name="q"]')
    expect(search_box).to_be_visible()

def test_search_functionality(page: Page):
    page.goto("https://www.google.com")
    search_box = page.locator('textarea[name="q"]')
    search_box.fill("playwright python")
    search_box.press("Enter")
    expect(page).to_have_url(r"https://www.google.com/search\?q=playwright\+python.*")
