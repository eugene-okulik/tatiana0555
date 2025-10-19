from playwright.sync_api import Page, expect, Route
import re
import json


def test_apple(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 17 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route(re.compile('/shop/api/digital-mat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role('heading', name='iPhone 17 Pro &').click()
    header = page.locator("h2.rf-digitalmat-overlay-header").first
    expect(header).to_contain_text("яблокофон 17 про")
    print(header.first.text_content())
