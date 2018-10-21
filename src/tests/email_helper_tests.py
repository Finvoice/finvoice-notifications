from src.helpers.email_helper import EmailHelper
from unittest import TestCase
from unittest.mock import MagicMock


class EmailHelperTest(TestCase):

    def test_send_email(self):
        EmailHelper.send_using_ses = MagicMock(return_value={})
        EmailHelper.send_mail(to_address=["test@mail.com"], email_html="<b>in bold</b>", email_text="plain text", subject="email subject")

        print("send using ses arguments {}".format(EmailHelper.send_using_ses.call_args[0]))
        self.assertEqual(EmailHelper.send_using_ses.call_args[0][0]["ToAddresses"], ["test@mail.com"])
        self.assertEqual(EmailHelper.send_using_ses.call_args[0][1]["Body"]["Html"]["Charset"], "UTF-8")
        self.assertEqual(EmailHelper.send_using_ses.call_args[0][1]["Body"]["Html"]["Data"], "<b>in bold</b>")
        self.assertEqual(EmailHelper.send_using_ses.call_args[0][1]["Body"]["Text"]["Charset"], "UTF-8")
        self.assertEqual(EmailHelper.send_using_ses.call_args[0][1]["Body"]["Text"]["Data"], "plain text")
        self.assertEqual(EmailHelper.send_using_ses.call_args[0][1]["Subject"]["Charset"], "UTF-8")
        self.assertEqual(EmailHelper.send_using_ses.call_args[0][1]["Subject"]["Data"], "email subject")

