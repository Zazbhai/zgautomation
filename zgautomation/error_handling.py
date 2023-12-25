from selenium.common.exceptions import *

from .vars import *
from colorama import Fore, Style
import sys





def errors(func):

    def try_except_decorator(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(Fore.RED+"")
            if TimeoutException:
                # print(format_exc())
                print("NO ELEMENT LOCATED")
                exc_type, exc_value, exc_tb = sys.exc_info()

            # Get the filename and line number where the exception occurred
                filename, line_no, func_name, text = exc_tb.tb_next.tb_frame.f_code.co_filename, exc_tb.tb_next.tb_frame.f_lineno, exc_tb.tb_next.tb_frame.f_code.co_name, exc_tb.tb_next.tb_frame.f_globals['__file__']

            # Print the error message and line number
                print(f"Error at {filename}, Line No: {line_no}")
            
            elif NoSuchFrameException:
                print("Target Frame Not Found")
            elif NoSuchWindowException:
                print("Window Target To Be Switched Doesn't Exist")
                print("Element Not Found By Given Name")
            elif NoSuchAttributeException:
                print("The Tttribute Of Element Could Not Be Found")
            elif NoSuchShadowRootException:
                print("The Shadow Root Of An Element When It Does Not Have A Shadow Root Attached")
            elif StaleElementReferenceException:
                print("Reference To An Element Is Now 'Stale'")
                print(StaleElementReferenceException_text)
            elif InvalidElementStateException:
                print("command could not be completed because the element is in an invalid state")
                print(InvalidElementStateException_text)
            elif UnexpectedAlertPresentException:
                print("an unexpected alert has appeared")
                print(UnexpectedAlertPresentException_text)
            elif NoAlertPresentException:
                print("switching to no presented alert")
                print(NoAlertPresentException_text)
            elif ElementNotVisibleException:
                print("element is present on the DOM, but it is not visible, and so is not able to be interacted with")
                print(ElementNotVisibleException_text)
            elif ElementNotInteractableException:
                print(" element is present in the DOM but interactions with that element will hit another element due to paint order")
            elif ElementNotSelectableException:
                print("trying to select an unselectable element\nFor example, selecting a 'script' element.")
            elif InvalidCookieDomainException:
                print("attempting to add a cookie under a different domain than the current URL")
            elif UnableToSetCookieException:
                print("driver failed to set cookie")
            elif MoveTargetOutOfBoundsException:
                print("target provided to the `ActionsChains` move() method is invalid, i.e. out of document")
            elif UnexpectedTagNameException:
                print("Didn't Get An Expected Element")
            elif InvalidSelectorException:
                print("selector which is used to find an element does not return a WebElement")
                print(InvalidSelectorException_text)
            elif ImeNotAvailableException:
                print("Thrown when IME support is not available")
                print(ImeNotAvailableException_text)
            elif ImeActivationFailedException:
                print("activating an IME engine has failed")
            elif InvalidArgumentException:
                print("The arguments passed to a command are either invalid or malformed")
            elif JavascriptException:
                print("An error occurred while executing JavaScript supplied by the user")
            elif NoSuchCookieException:
                print(NoSuchCookieException_text)
            elif ScreenshotException:
                print("A screen capture was made impossible")
            elif ElementClickInterceptedException:
                print(ElementClickInterceptedException_text)
            elif InsecureCertificateException:
                print("Navigation caused the user agent to hit a certificate warning, which is usually the result of an expired or invalid TLS certificate")
            elif InvalidCoordinatesException:
                print("The coordinates provided to an interaction's operation are invalid")
            elif InvalidSessionIdException:
                print("the given session id is not in the list of active sessions, meaning the session either does not exist or that it's not active")
            elif SessionNotCreatedException:
                print("A new session could not be created")
            elif UnknownMethodException:
                print("The requested command matched a known URL but did not match any methods for that URL")
            elif NoSuchDriverException:
                print("Either Driver Is Not Specified Or Cannot Be Located")
            else:
                pass
            print(Style.RESET_ALL)
            exit()
        
            
    return try_except_decorator