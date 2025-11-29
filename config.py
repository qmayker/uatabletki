user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

args = [
        f"--user-agent={user_agent}",
        "--window-size=1366,768",
        "--disable-blink-features=AutomationControlled",
    ]

search_field_class = ".form-control.w-100 searchPharmacy.input-gray.ui-autocomplete-input"