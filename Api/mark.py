from selenium import webdriver
import pytest
import time
from flaky import flaky


class TestAllure:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/Hp/Desktop/New nani/chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    @flaky(max_runs=3, min_passes=1)
    @pytest.mark.run(order=3)
    def test_logo(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status = self.driver.find_element_by_xpath("//body/div[@id='wrapper']/div[@id='content']/div["
                                                   "@id='divLogin']/div[@id='divLogo']/img[1]").is_displayed()
        if status == True:
            assert True
        else:
            assert False

    @flaky(max_runs=3, min_passes=1)
    @pytest.mark.run(order=2)
    def test_listemp(self, setup):
        pytest.skip("skipping this method")

    @flaky(max_runs=3, min_passes=1)
    @pytest.mark.run(order=1)
    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        actualtitle = self.driver.title
        if actualtitle == "OrangeHRM1":
            assert True
        else:
            # allure.attach(self.driver.get_screenshot_as_png(), name="testscreenshot",attachment_type=AttachmentType.PNG)
            assert False
