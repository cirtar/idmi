def find_element_by_id(driver, name, ignore_message=False):
    """Finds an element by its id.

    Args:
        driver: A selenium WebDriver.
        name: The id of the element to find.
        ignore_message: Whether to ignore the message if the element is not found.

    Returns:
        An instance of selenium.webdriver.remote.webelement.WebElement or None
        if the element is not found.
    """

    try:
        return driver.find_element_by_id(name)
    except NoSuchElementException:
        if not ignore_message:
            raise
        else:
            return None

