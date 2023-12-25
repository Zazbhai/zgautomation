StaleElementReferenceException_text = """ 
Stale means the element no longer appears on the DOM of the page.


    Possible causes of StaleElementReferenceException include, but not limited to:
        * You are no longer on the same page, or the page may have refreshed since the element
          was located.
        * The element may have been removed and re-added to the screen, since it was located.
          Such as an element being relocated.
          This can happen typically with a javascript framework when values are updated and the
          node is rebuilt.
        * Element may have been inside an iframe or another context which was refreshed.
"""

InvalidElementStateException_text = "This can be caused by attempting to clear an element that isn't both editable and resettable."
UnexpectedAlertPresentException_text = "Usually raised when  an unexpected modal is blocking the webdriver from executing commands."
NoAlertPresentException_text = "This can be caused by calling an operation on the Alert() class when an alert is not yet on the screen."
ElementNotVisibleException_text = "Most commonly encountered when trying to click or read text of an element that is hidden from view."
InvalidSelectorException_text = """
Currently this only happens when the selector is an xpath expression
    and it is either syntactically invalid (i.e. it is not a xpath
    expression) or the expression does not select WebElements (e.g.
    "count(//input)").
"""

ImeNotAvailableException_text =  "This exception is thrown for every IME-related method call if IME support is not available on the machine."
NoSuchCookieException_text ="""
No cookie matching the given path name was found amongst the associated
cookies of the current browsing context's active document
"""
ElementClickInterceptedException_text = """
The Element Click command could not be completed because the element
receiving the events is obscuring the element that was requested to be clicked
"""