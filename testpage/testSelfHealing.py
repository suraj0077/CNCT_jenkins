import time

import pytest

from locators.locatorsxpath import SelfHealing
from pages.objectselfhealing import Healing

@pytest.mark.usefixtures("setup")
class TestSelfHealing:

    def test_self_healing(self):
        self.self_healing = Healing(self.driver)

        time.sleep(5)

        # self.self_healing.click_next_Button()

        self.self_healing.click_next_Button_SelfHealing(SelfHealing.locators)