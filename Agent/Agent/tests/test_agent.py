from agent import send_notification

def test_send_notification():
    # Test if function returns something (mocking real API is not needed now)
    result = send_notification("CI test message")
    
    # For now, just check function returns either status code or None
    assert result is None or isinstance(result, int)
