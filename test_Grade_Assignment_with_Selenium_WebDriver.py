""" Created by Võ Nguyễn Minh Tú"""

# import json
import os
import time
# from typing import Generator

import pandas
import pytest
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.common.exceptions import NoSuchElementException

os.chdir(os.path.dirname(os.path.realpath(__file__)))


class EnvironmentAndFlow(object):
    """doc"""

    __test__ = False

    # def __init__(self, grade_input):
    #     self.grade_input = grade_input

    # grade_input = ""

    def setup_method(self, method):
        # ops = webdriver.ChromeOptions()
        # ops.add_argument('headless')
        # self.driver = webdriver.Chrome(options=ops)
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_script(self, username: str, password: str, grade_input: str) -> str:
        while True:
            try:
                self.setup_method("")
                self.driver.get("https://school.moodledemo.net/login/index.php")
                self.driver.set_window_size(945, 1012)
                # self.driver.find_element(By.ID, "username").click()
                self.driver.find_element(By.ID, "username").clear()
                self.driver.find_element(By.ID, "password").clear()
                self.driver.find_element(By.ID, "username").send_keys(username)
                self.driver.find_element(By.ID, "password").send_keys(password)
                self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
                # WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                #     (By.CSS_SELECTOR, "#course-info-container-69-4 .multiline")))
                self.driver.find_element(
                    By.CSS_SELECTOR, "#course-info-container-69-4 .multiline"
                ).click()
                self.driver.find_element(
                    By.CSS_SELECTOR, ".modtype_assign .aalink"
                ).click()
                self.driver.find_element(By.LINK_TEXT, "Grade").click()
                # time.sleep(1)
                # try:
                #     self.driver.switch_to.alert.dismiss()
                # except NoAlertPresentException:
                #     pass
                # undefined_popup_check = self.driver.find_elements(By.XPATH, "/html/body/div[6]/div[3]/div/div[1]/span/button")
                # if undefined_popup_check:
                #     #     self.driver.find_element(By.XPATH, '//*[@title="Close"]').click()
                #     # WebDriverWait(self.driver, 30).until(
                #     #     expected_conditions.element_to_be_clickable(
                #     #         (By.XPATH, "//fieldset/div/div/div/input")
                #     #     )
                #     # )
                #     # self.driver.refresh()
                #     # undefined_popup_check[0].click()
                #     self.driver.execute_script("arguments[0].click();", undefined_popup_check[0])
                # grade_elements = []
                # grade_elements.extend(
                #     self.driver.find_elements(
                #         By.XPATH,
                #         "/html/body/div[4]/section/div[2]/div[3]/div/div[2]/form/fieldset/div[2]/div[2]/div[2]/div[1]/span/a",
                #     )
                # )
                # grade_elements.extend(
                #     self.driver.find_elements(
                #         By.XPATH,
                #         "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[2]/div[2]/div[1]/span[1]/a[1]",
                #     )
                # )
                # if grade_elements:
                #     grade_before = grade_elements[0].text
                # elif self.driver.find_elements(
                #     By.XPATH,
                #     "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[2]/div[2]/div[1]/span[1]/a[1]",
                # ):
                #     grade_before = self.driver.find_element(
                #         By.XPATH,
                #         "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[2]/div[2]/div[1]/span[1]/a[1]",
                #     ).text
                # else:
                #     grade_before = None
                # WebDriverWait(self.driver, 30).until(
                #     expected_conditions.element_to_be_clickable(
                #         (
                #             By.XPATH,
                #             "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[2]/div[2]/div[1]/span[1]/a[1]",
                #         )
                #     )
                # )
                # print(
                grade_before = self.driver.find_element(
                    By.XPATH,
                    "//div[@id='fitem_id_currentgrade']/div[2]/div/span/a",
                ).text
                # )
                # undefined_popup_check = self.driver.find_elements(By.XPATH, "/html/body/div[6]/div[3]/div/div[1]/span/button")
                # if undefined_popup_check:
                #     #     self.driver.find_element(By.XPATH, '//*[@title="Close"]').click()
                #     # WebDriverWait(self.driver, 30).until(
                #     #     expected_conditions.element_to_be_clickable(
                #     #         (By.XPATH, "//fieldset/div/div/div/input")
                #     #     )
                #     # )
                #     # self.driver.refresh()
                #     # undefined_popup_check[0].click()
                #     self.driver.execute_script("arguments[0].click();", undefined_popup_check[0])
                # grade_input_elements = []
                # grade_input_elements.extend(
                #     self.driver.find_elements(
                #         By.XPATH,
                #         "/html/body/div[4]/section/div[2]/div[3]/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/input",
                #     )
                # )
                # grade_input_elements.extend(
                #     self.driver.find_elements(
                #         By.XPATH,
                #         "//fieldset/div/div/div/input",
                #     )
                # )
                # if grade_input_elements:
                #     grade_input_box = grade_input_elements[0]
                # # elif self.driver.find_elements(
                # #     By.XPATH, "//fieldset/div/div/div/input"
                # # ):
                # #     grade_input_box = self.driver.find_element(
                # #         By.XPATH, "//fieldset/div/div/div/input"
                # #     )
                # else:
                #     raise NoSuchElementException
                grade_input_box = self.driver.find_element(
                    By.XPATH,
                    "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[1]/div[2]/input[1]",
                )
                WebDriverWait(self.driver, 30).until(
                    expected_conditions.element_to_be_clickable(grade_input_box)
                )
                grade_input_box.click()
                grade_input_box.clear()
                grade_input_box.send_keys(grade_input)
                self.driver.find_element(By.NAME, "savechanges").click()
                # WebDriverWait(self.driver, 30).until(
                #     expected_conditions.element_to_be_clickable((By.NAME, "savechanges")))
                # if self.driver.find_elements(By.XPATH, "/html/body/div[6]/div[3]/div/div[1]/span/button"):
                #     #     self.driver.find_element(By.XPATH, '//*[@title="Close"]').click()
                #     WebDriverWait(self.driver, 30).until(
                #         expected_conditions.element_to_be_clickable(
                #             (By.XPATH, "//fieldset/div/div/div/input")
                #         )
                #     )
                #     self.driver.refresh()
                # self.driver.find_element(By.NAME, "savechanges").click()
                # assert self.driver.find_element(By.ID, "id_error_grade").text == "Grade must be greater than or equal to zero."
                # print(self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[2]/div[2]/div[1]/span[1]/a[1]").text)
                # WebDriverWait(self.driver, 30).until(
                #     expected_conditions.element_to_be_clickable(
                #         (By.XPATH, "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[2]/div[2]/div[1]/span[1]/a[1]")
                #     )
                # )
                # try:
                #     self.driver.switch_to.alert.dismiss()
                # except NoAlertPresentException:
                #     pass
                time.sleep(1)
                if float(grade_input) < 0 or float(grade_input) > 100:
                    WebDriverWait(self.driver, 30).until(
                        expected_conditions.visibility_of_element_located(
                            (By.ID, "id_error_grade")
                        )
                    )
                    # print(
                    message = self.driver.find_element(By.ID, "id_error_grade").text
                    # )
                else:
                    message = None
                # WebDriverWait(self.driver, 30).until(
                #     expected_conditions.element_to_be_clickable(
                #         (
                #             By.XPATH,
                #             "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[2]/div[2]/div[1]/span[1]/a[1]",
                #         )
                #     )
                # )
                # if self.driver.find_elements(By.XPATH, "/html/body/div[6]/div[3]/div/div[1]/span/button"):
                #     #     self.driver.find_element(By.XPATH, '//*[@title="Close"]').click()
                #     WebDriverWait(self.driver, 30).until(
                #         expected_conditions.element_to_be_clickable(
                #             (By.XPATH, "//fieldset/div/div/div/input")
                #         )
                #     )
                #     self.driver.refresh()
                # WebDriverWait(self.driver, 30).until(
                #     expected_conditions.element_to_be_clickable(
                #         (
                #             By.XPATH,
                #             "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[2]/div[2]/div[1]/span[1]/a[1]",
                #         )
                #     )
                # )
                # print(
                self.driver.refresh()
                # print(grade_elements[0].text)
                # grade_elements.clear()
                # grade_elements.extend(
                #     self.driver.find_elements(
                #         By.XPATH,
                #         "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[2]/div[2]/div[1]/span[1]/a[1]",
                #     )
                # )
                # grade_elements.extend(
                #     self.driver.find_elements(
                #         By.XPATH,
                #         "/html/body/div[5]/section/div[2]/div[3]/div/div[2]/form/fieldset/div[2]/div[2]/div[2]/div[1]/span/a",
                #     )
                # )
                # if grade_elements:
                #     grade_after = grade_elements[0].text
                # # elif self.driver.find_elements(
                # #     By.XPATH,
                # #     "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[2]/div[2]/div[1]/span[1]/a[1]",
                # # ):
                # #     grade_before = self.driver.find_element(
                # #         By.XPATH,
                # #         "/html[1]/body[1]/div[5]/section[1]/div[2]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/div[2]/div[2]/div[2]/div[1]/span[1]/a[1]",
                # #     ).text
                # else:
                #     grade_after = None
                # )
                time.sleep(3)
                # self.driver.refresh()
                # time.sleep(1)
                grade_after = self.driver.find_element(
                    By.XPATH,
                    "//div[@id='fitem_id_currentgrade']/div[2]/div/span/a",
                ).text
                # time.sleep(5)
                # if self.driver.find_elements(By.XPATH, "/html/body/div[6]/div[3]/div/div[1]/span/button"):
                #     #     self.driver.find_element(By.XPATH, '//*[@title="Close"]').click()
                #     WebDriverWait(self.driver, 30).until(
                #         expected_conditions.element_to_be_clickable(
                #             (By.LINK_TEXT, "Assignment: Timed Task")
                #         )
                #     )
                #     self.driver.refresh()
                # WebDriverWait(self.driver, 30).until(
                #     expected_conditions.element_to_be_clickable(
                #         (By.LINK_TEXT, "Assignment: Timed Task")
                #     )
                # )
                # self.driver.find_element(By.LINK_TEXT, "Assignment: Timed Task").click()
                self.driver.get("https://school.moodledemo.net/my/courses.php")
                # WebDriverWait(self.driver, 30).until(
                #     expected_conditions.presence_of_element_located(
                #         (By.ID, "user-menu-toggle"))
                # )
                self.driver.find_element(By.ID, "user-menu-toggle").click()
                self.driver.find_element(By.LINK_TEXT, "Log out").click()
                # close_undefined_popup_process.result()
                # self.driver.close()
            # except Exception:  # as e:
            except Exception as e:
                print(e)
                print("Something went wrong. Retrying...")
                self.teardown_method("")
                self.setup_method("")
            else:
                break
            finally:
                self.teardown_method("")
        print(
            {
                "input": grade_input,
                "grade_before": grade_before,
                "grade_after": grade_after,
                "message": message,
            }
        )
        if message:
            return message
        else:
            return grade_after


# def pytest_assertion():
# test_ins = EnvironmentAndFlow()
# grade_for_testing = ["-1", "0", "1"]
# for value in grade_for_testing:
#     print(test_ins.test_script("teacher", "moodle", value))


class TestCasesAndData(object):
    """Test cases and test data"""

    __test__ = True
    input_for_testing_Grade_Assignment = pandas.read_excel(
        "input_for_testing_Grade_Assignment.xlsx",
        sheet_name=None
    )
    credentials = (
        input_for_testing_Grade_Assignment["Credentials"]
        .astype("string")
        .replace({pandas.NA: None})
    )
    test_data = (
        input_for_testing_Grade_Assignment["Test Data"]
        .astype("string")
        .replace({pandas.NA: None})
    )
    test_instance = EnvironmentAndFlow()

    @pytest.mark.parametrize(
        "test_case",
        list(
            zip(
                test_data["Input"],
                test_data["Output"],
            )
        ),
    )
    def test_runner(
        self, test_case: tuple[str, object]
    ) -> None:
        # test_instance = TestDefaultTestCases()
        # test_instance.grade_input = "-1"
        # stop_event_manager = multiprocessing.Manager()
        # stop_event = stop_event_manager.Event()

        assert (
            self.test_instance.test_script(
                self.credentials["Username"].iloc[0],
                self.credentials["Password"].iloc[0],
                test_case[0],
            )
            == test_case[1]
        )

    # test_instance.teardown_method("")


# test_instance = EnvironmentAndFlow()
# test_instance.setup_method("")
# test_instance.test_script("90")
# test_instance.teardown_method("")
