# Helper class for handling emails
import boto3


class EmailHelper:
    SENDER = "Finvoice Event Notifications <rohan@finvoice.co>"
    CHARSET = "UTF-8"

    @classmethod
    def send_mail(cls, to_address, email_html, email_text, subject):
        destination = {"ToAddresses": to_address}
        message = {
            "Body": {
                "Html": {
                    "Charset": EmailHelper.CHARSET,
                    "Data": email_html
                },
                "Text": {
                    "Charset": EmailHelper.CHARSET,
                    "Data": email_text
                }
            },
            "Subject": {
                "Charset": EmailHelper.CHARSET,
                "Data": subject
            }
        }

        return cls.send_using_ses(destination, message)

    @classmethod
    def send_using_ses(cls, destination, message):
        return boto3.client('ses').send_email(
            Destination=destination,
            Message=message,
            Source=EmailHelper.SENDER)
