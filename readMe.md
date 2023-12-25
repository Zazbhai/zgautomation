# ZG-AUTOMATION
_This Module Will Help You To Intract With Your Browser With Selenium Framework_

> [!IMPORTANT]
> This Is Trial Version Of This **_zgautomation_** Module.
> More Updates Will Be Available.

# Installation

```python 
pip install zgautomation

```
# Examples Of Using Our Module

```python
from zgautomation import zgautomate

driver = zgautomate(url="https://github.com/zazbhai",
                     browser="chrome",
                     headless= False )

driver.text_by_xpath("//span[@itemprop='name']")
driver.click_by_css("a.btn.btn-block")
```
No Need To Close use Close Syntax It Will Close It By Its Own.

# Parameters And Functions
## Basic Parameters
- url = Takes Url Which You Want To Open
- browser = Name Of Browser You Want To Use
- headless =  Choose Whether Open Browser In Headless Mode Or Not
- wait = Time To Wait For Elements To Appear
## Basic Functions 
- refresh = Refresh The Web Page
- back = Go Back
- forward = Go Forward
- script = Executes Javascript Commands On Web Page
## Text Functions
- text_by_name = Gives The Outer HTML Text Associated With Given Name Attribute
- text_by_css = Gives The Outer HTML Text Associated With Given Css Attribute
- text_by_class = Gives The Outer HTML Text Associated With Given Class Attribute
- text_by_id = Gives The Outer HTML Text Associated With Given Id Attribute
- text_by_link_text = Gives The Outer HTML Text Associated With Given Link Text
- text_by_xpath = Gives The Outer HTML Text Associated With Given Xpath
- text_by_partial_link_text = Gives The Outer HTML Text Associated With Given Partial Link Text
- text_by_tag = Gives The Outer HTML Text Associated With Given Tag Name
## Click Functions
- click_by_name = Click On Given Element Associated With Given Name Attribute
- click_by_class = Click On Given Element Associated With Given Class Attribute
- click_by_id = Click On Given Element Associated With Given Id Attribute
- click_by_css = Click On Given Element Associated With Given Css Attribute
- click_by_tag = Click On Given Element Associated With Given Tag Name
- click_by_xpath = Click On Given Element Associated With Given Xpath
- click_by_link_text = Click On Given Element Associated With Given Link Text
- click_by_partial_link_text = Click On Given Element Associated With Given Partial Link Text
- screenshot = Saves Screenshot Of The Web Page In The Given Path
## Type Functions
- type_by_class = Type Given Text In Selected Class's Input Field
- type_by_css = Type Given Text In Selected Css's Input Field
- type_by_xpath = Type Given Text In Selected Xpath's Input Field
- type_by_id = Type Given Text In Selected Id's Input Field
- type_by_tag = Type Given Text In Selected Tag Attribute's Input Field
- type_by_name = Type Given Text In Selected Name's Input Field
- type_by_link_text = Type Given Text In Selected Link Text's Input Field
- type_by_partial_link_text = Type Given Text In Selected Partial Link Text's Input Field
> [!NOTE]
> Getting Outer HTML And Title Text Will Directly Printed So There Is No Need To Declare Any Variable And Print It.

# Example Of screenshot function 

```python
from zgautomation import zgautomate
driver = zgautomate(url="https://github.com/zazbhai",
                     browser="chrome",
                     headless= False )

#This Code Will Open The Given Web Url, Take A Screenshot And Save It As test_img.png
driver.screenshot("test_img.png")
```


# Giving Input In Google TextFeild With get_by_class Function
```python
#keys Is Special Class To Give Keyboard Functionality 
from zgautomation import zgautomate, keys
from time import sleep
driver = zgautomate(url="https://google.com",
                     browser="chrome",
                     headless= False)
#Keys.ENTER Will Press Enter After Typing @zaz_bhai In Search Box
driver.type_by_class("gLFyf", "@zaz_bhai"+keys.ENTER)
sleep(4)

```

# Keys List
* Normal Keys
NULL, CANCEL, HELP, BACKSPACE, BACK_SPACE, TAB, CLEAR, RETURN, ENTER, SHIFT, LEFT_SHIFT, CONTROL, LEFT_CONTROL, ALT, LEFT_ALT, PAUSE, ESCAPE, SPACE, PAGE_UP, PAGE_DOWN, END, HOME, LEFT, ARROW_LEFT , UP, ARROW_UP, RIGHT, ARROW_RIGHT, DOWN, ARROW_DOWN, INSERT, DELETE, SEMICOLON, EQUALS

* Number Pad Keys
NUMPAD0, NUMPAD1, NUMPAD2, NUMPAD3, NUMPAD4, NUMPAD5, NUMPAD6, NUMPAD7, NUMPAD8, NUMPAD9, MULTIPLY, ADD, SEPARATOR, SUBTRACT, DECIMAL, DIVIDE

* Function Keys
F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, META , COMMAND, ZENKAKU_HANKAKU 

**This Module Is Made By [Zaz Yagmi](https://instagram.com/zaz_bhai)**

To Report Bugs And Errors You Can Contact Me On [Telegram](https://t.me/zazbhai)



