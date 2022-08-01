from gateways.create_note import CreateNoteGateway
from notes.models import Note


class TestNote:

    def test_note_create(self):
        """Тестирование создание заявки."""
        text_body = Note.random_note()
        response = CreateNoteGateway.send_request(data=text_body)
        assert response.status_code == 201
