import unittest
from myapp.models import BankAccount
from channels.testing import WebsocketCommunicator
from django.test import TestCase
from myapp.routing import application


class BankAccountTestCase(unittest.TestCase):
    def test_balance_cannot_go_below_zero(self):
        account = BankAccount.objects.create(account_number='1234567890', balance=100)
        account.withdraw(150)
        self.assertEqual(account.balance, 0)

class ChatTests(TestCase):
    async def test_message_delivery(self):
        communicator = WebsocketCommunicator(application, "/ws/chat/")
        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        message = {"type": "chat.message", "text": "Hello, world!"}
        await communicator.send_json_to(message)

        response = await communicator.receive_json_from()
        self.assertEqual(response["type"], "chat.message")
        self.assertEqual(response["text"], "Hello, world!")

        await communicator.disconnect()

if __name__ == '__main__':
    unittest.main()