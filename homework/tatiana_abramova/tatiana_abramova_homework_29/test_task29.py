from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_alert(page: Page):
    def accept_alert(alert: Dialog):
        alert.accept()
    page.on('dialog', accept_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    expect(page.locator('#result-text')).to_have_text('Ok')


def test_tabs_enabled(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(link).to_be_enabled()


def test_color_change(page: Page):
    page.goto("https://demoqa.com/dynamic-properties", wait_until="domcontentloaded", timeout=60000)
    color_button = page.locator("#colorChange")
    expect(color_button).to_have_css("color", "rgb(220, 53, 69)", timeout=20000)
    color_button.click()
