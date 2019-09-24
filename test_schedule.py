#!/usr/local/bin/python3

import unittest
from datetime import date

from schedule import Jclub
import copy


class TestAlert(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.date = date(2019, 9, 13) # Random Thursday

    def _day_of_week_to_date(self, day_of_week):

        if day_of_week == "ThursdayOfJclub":
            return copy.copy(self.date)
        date = self.date.day


    def test_day_of_week_to_date(self):

        def test_one(day_of_week, expected_day):
            date = self._day_of_week_to_date(day_of_week)
            self.assertEqual(expected_day, date.day)

        test_one("ThursdayOfJclub", 13)



    def test_get_action_in_week(self):

        def test_one(day_of_week, confirmation_email_sent, confirmed, received_blurb, sent_blurb):
            pass
            #if day_of_week == "
            #j = Jclub(date(2019, 9, 13))
            #foo

    def test_get_action_out_of_week(self):

        def test_one(days_until, expect_too_early, expect_too_late):
            j = Jclub(self.date)
            action = j.get_action(date(self.date.year, self.date.month, self.date.day - days_until))["action"]
            self.assertEqual(expect_too_late, action == "Jclub already occurred, no action")
            self.assertEqual(expect_too_early, action == "Jclub too far in future, nothing to do")

        test_one(0, False, False)
        test_one(-1, False, True)
        test_one(7, False, False)
        test_one(8, True, False)


if __name__ == '__main__': # pragma: no coverage
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAlert)

    ret = unittest.TextTestRunner(verbosity=2).run(suite)
    res = 0 if ret.wasSuccessful() else 1
    exit(res)
