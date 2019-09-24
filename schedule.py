#!/usr/local/bin/python3

DEFAULT_CONFIRMER = 'luke'
DEFAULT_BLURB_SENDER = 'meagan'

from datetime import date

DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


class Jclub(object):

    def __init__(self, date, confirmer=DEFAULT_CONFIRMER, blurb_sender=DEFAULT_BLURB_SENDER):
        self.date = date
        self.confirmation_email_sent = False
        self.confirmed = None
        self.received_blurb = False
        self.sent_blurb = False
        self.confirmer = confirmer
        self.blurb_sender = blurb_sender

        day_of_week = DAYS_OF_WEEK[self.date.weekday()]
        if day_of_week != "Thursday":
            raise ValueError("Jclub must be on a Thursday, not %s" % (day_of_week))

    def get_action(self, now=None):
        if now is None:
            now = date.today()
        days_until_jclub = (self.date - now).days

        if days_until_jclub < 0:
            return {"person":None, "action":"Jclub already occurred, no action"}
        if days_until_jclub > 7:
            return {"person":None, "action":"Jclub too far in future, nothing to do"}

        # Ok, now it's in the right week
        day_of_week = DAYS_OF_WEEK[now.weekday()]
        if not self.confirmation_email_sent:
            return {"person":self.confirmer, "action":"Send confirmation email"}
        if self.confirmed is None:
            if days_until_jclub < 6: # Saturday or later
                return {"person":self.confirmer, "action":"Resend confirmation email"}
