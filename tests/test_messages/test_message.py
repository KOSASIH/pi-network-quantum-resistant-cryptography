import unittest
import uuid
import datetime
from unittest.mock import patch
from mock import Mock

from app.models import Message

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.message = Message(
            id=str(uuid.uuid4()),
            text="Hello, world!",
            created_at=datetime.datetime.utcnow()
        )

    @patch('app.models.uuid.uuid4')
    def test_message_creation(self, mock_uuid):
        mock_uuid.return_value = self.message.id
        message = Message(text="Hello, world!")
        self.assertIsInstance(message, Message)
        self.assertEqual(message.id, self.message.id)
        self.assertEqual(message.text, self.message.text)
        self.assertIsInstance(message.created_at, datetime.datetime)

    @patch('app.models.uuid.uuid4')
    def test_message_to_dict(self, mock_uuid):
        mock_uuid.return_value = self.message.id
        message_dict = self.message.to_dict()
        self.assertIsInstance(message_dict, dict)
        self.assertIn('id', message_dict)
        self.assertIn('text', message_dict)
        self.assertIn('created_at', message_dict)
        self.assertEqual(message_dict['id'], self.message.id)
        self.assertEqual(message_dict['text'], self.message.text)
        self.assertIsInstance(message_dict['created_at'], str)

    @patch('app.models.uuid.uuid4')
    def test_message_from_dict(self, mock_uuid):
        mock_uuid.return_value = self.message.id
        message_dict = self.message.to_dict()
        message = Message.from_dict(message_dict)
        self.assertIsInstance(message, Message)
        self.assertEqual(message.id, self.message.id)
        self.assertEqual(message.text, self.message.text)
        self.assertIsInstance(message.created_at, datetime.datetime)

    @patch('app.models.uuid.uuid4')
    def test_message_equality(self, mock_uuid):
        mock_uuid.return_value = self.message.id
        message = Message(text="Hello, world!")
        self.assertEqual(self.message, message)
        self.assertEqual(hash(self.message), hash(message))

    @patch('app.models.uuid.uuid4')
    def test_message_inequality(self, mock_uuid):
        mock_uuid.return_value = self.message.id
        message = Message(text="Goodbye, world!")
        self.assertNotEqual(self.message, message)
        self.assertNotEqual(hash(self.message), hash(message))

    @patch('app.models.uuid.uuid4')
    def test_message_str(self, mock_uuid):
        mock_uuid.return_value = self.message.id
        message_str = str(self.message)
        self.assertIsInstance(message_str, str)
        self.assertIn(self.message.id, message_str)
        self.assertIn(self.message.text, message_str)
        self.assertIn(self.message.created_at.isoformat(), message_str)

    @patch('app.models.uuid.uuid4')
    def test_message_save(self, mock_uuid):
        mock_uuid.return_value = self.message.id
        mock_db = Mock()
        self.message.save(db=mock_db)
        mock_db.session.add.assert_called_once_with(self.message)

    @patch('app.models.uuid.uuid4')
    def test_message_delete(self, mock_uuid):
        mock_uuid.return_value = self.message.id
        mock_db = Mock()
        self.message.delete(db=mock_db)
        mock_db.session.delete.assert_called_once_with(self.message)

if __name__ == '__main__':
    unittest.main()
