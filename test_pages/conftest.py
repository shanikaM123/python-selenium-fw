import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path='C:/Automation/Python/chromedriver.exe')
        driver.maximize_window()
        print("Launching chrome driver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path='C:/Automation/Python/geckodriver.exe')
        driver.maximize_window()
        print("Launching Firefox driver")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# pytest HTML Report #

def pytest_configure(config):
    config._metadata["project name"] = "Automation Test"
    config._metadata["module name"] = "Login and Home PAge"
    config._metadata["tested"] = "Shanika"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
