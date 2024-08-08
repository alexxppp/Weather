from project import generate_password, PASSWORD_LENGTH, register, fetch
import string


def test_generate_password():
    # Necessary code for testing
    full_set = (string.ascii_lowercase + string.ascii_uppercase +
                string.digits + string.punctuation)
    password = generate_password()
    # Tests
    for character in password:
        assert character in full_set
    assert len(generate_password()) == PASSWORD_LENGTH


def test_register():
    # Tests
    assert register("", "my_password", "my_password") == False
    assert register("my_username", "my_password", "not_my_password") == False
    assert register("my_username", "", "") == False


def test_fetch():
    assert fetch("fiftyville") == None
