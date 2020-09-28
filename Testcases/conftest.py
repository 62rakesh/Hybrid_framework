from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


path = "D:\\Hybrid_framework\\drivers\\geckodriver.exe"


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=".//drivers//geckodriver.exe")
    elif browser == 'Ie':
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


# def screenshot():
#     screen = pyscreenshot.grab()
#     screen.show()
#     screen.save(screenshoot_path)
#     return screen


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Generate HTML Report

# It is a hook for adding environment information to the HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop commerce'
    config._metadata['Customer Name'] = 'Amazon'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester Name'] = 'Rakesh Patra'


# It is a hook for delete and modify information from the HTML report


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
