import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set the path to the Chrome binary (if needed)
chrome_options = Options()
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Adjust this path


@pytest.fixture()
def setup(browser):
    # Start the ChromeDriver with the specified binary
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")

    elif browser == "firefox":
        driver = webdriver.Firefox
        print("Launching firefox browser")

    return driver

def pytest_adoption(parser):  # This will get the value from CLI /hooks
    parser.adoption()

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

######pyTest HTML Report ############

# It is hook for Adding Environment info to HTML REport
def pytest_configure(config):
    config._metadata['project Name'] = 'nop Commerce'
    config._metadata['Module Name']= 'Customers'
    config._metadata['Tester']= 'Pavan'

#It is hook for delete/modify Environmenrt info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)