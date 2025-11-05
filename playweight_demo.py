from playwright.sync_api import sync_playwright

def search_latest_cricket_match():
    with sync_playwright() as p:
        # Launch browser with realistic settings
        browser = p.chromium.launch(
            headless=False,  # Show the browser for visibility
            args=[
                "--start-maximized",
                "--disable-blink-features=AutomationControlled"
            ]
        )
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/118.0.5993.90 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800}
        )

        page = context.new_page()

        # ✅ Use DuckDuckGo instead of Google to avoid CAPTCHA
        page.goto("https://duckduckgo.com/")

        # Search for the latest cricket match
        query = "latest cricket match"
        page.fill("input[name='q']", query)
        page.keyboard.press("Enter")

        # Wait for results
        page.wait_for_selector("a.result__a")

        # Get top result
        results = page.query_selector_all("a.result__a")
        if results:
            print("Top search result:")
            print(results[0].inner_text())
            print("URL:", results[0].get_attribute("href"))
        else:
            print("No results found.")

        # Optional screenshot
        page.screenshot(path="duckduckgo_cricket_search.png")

        # Close browser
        #browser.close()

if __name__ == "__main__":
    search_latest_cricket_match()
