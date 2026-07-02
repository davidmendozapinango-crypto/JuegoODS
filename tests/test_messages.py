from ui.messages import get_ods_messages


def test_ods_messages_available():
    messages = get_ods_messages()

    assert len(messages) >= 20
    assert all(isinstance(message, str) and message.strip() for message in messages)
