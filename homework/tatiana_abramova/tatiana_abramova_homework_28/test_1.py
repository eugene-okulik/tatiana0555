from playwright.sync_api import Page, expect


def test_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name="Form Authentication").click()
    page.get_by_role('textbox', name="Username").fill('test_user')
    page.get_by_role('textbox', name="Password").fill('test_password')
    page.get_by_role('button', name='Login').click()


def test_complete_the_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form', wait_until='domcontentloaded')
    page.get_by_placeholder('First Name').fill('Ivan')
    page.get_by_placeholder('Last Name').fill('Petrov')
    page.get_by_placeholder('name@example.com').fill('example@mail.ru')
    page.locator('label[for="gender-radio-1"]').click()
    page.get_by_placeholder('Mobile Number').fill('9876543211')
    page.locator('#dateOfBirthInput').click()
    popup = page.locator('div.react-datepicker-popper')
    expect(popup).to_be_visible()
    page.locator('.react-datepicker__year-select').select_option('2000')
    page.locator('.react-datepicker__month-select').select_option('October')
    page.locator('.react-datepicker__day--015').click()
    selected_date = '15 Oct 2000'
    expect(page.locator('#dateOfBirthInput')).to_have_value(selected_date)
    page.locator('#subjectsInput').fill('a')
    page.locator('#react-select-2-option-2').click()
    page.locator("//label[@for='hobbies-checkbox-3']").check()
    page.locator('#currentAddress').fill('Test Street, 11, 55б, Delhi, India')
    page.locator('#react-select-3-input').fill('NCR')
    page.locator('#react-select-3-input').press('Enter')
    page.locator('#react-select-4-input').fill('Delhi')
    page.locator('#react-select-4-input').press('Enter')
    page.get_by_role('button', name='Submit').click()
