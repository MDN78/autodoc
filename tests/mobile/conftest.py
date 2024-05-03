import os
import pytest
from utils import resource
from selene import browser
from appium import webdriver
from dotenv import load_dotenv
from utils import attach_mobile
from allure_commons._allure import step
# from appium.options.android import UiAutomator2Options


def pytest_addoption(parser):
    parser.addoption('--context', default='local_emulator')


def pytest_configure(config):
    context = config.getoption("--context")
    env_file = f'.env.{context}'
    load_dotenv(dotenv_path=env_file)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    with step('Configurate options'):
        from project import config_app
        options = config_app.to_driver_options(context=context)
        browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    #     options = UiAutomator2Options()
    #     if context == 'local_emulator':
    #         options.set_capability('remote_url', os.getenv('URL'))
    #         options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
    #         options.set_capability('app', resource.relative_from_root(os.getenv('APP')))
    #
    #     if context == 'bstack':
    #         options.set_capability('remote_url', os.getenv('URL'))
    #         options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
    #         options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
    #         options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
    #         options.set_capability('app', os.getenv('APP_M'))
    #         options.set_capability(
    #             'bstack:options',
    #             {
    #                 "projectName": "First Python project",
    #                 "buildName": "browserstack-build-1",
    #                 "sessionName": "BStack first_test",
    #                 "userName": os.getenv('USER_NAME'),
    #                 "accessKey": os.getenv('ACCESS_KEY'),
    #             },
    #         )
    # browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    yield

    with step('Add screenshot'):
        attach_mobile.add_screenshot(browser)

    with step('Add html'):
        attach_mobile.add_html(browser)

    with step('Close driver'):
        browser.quit()

    if context == 'bstack':
        with step('Add video'):
            attach_mobile.add_video(browser)
