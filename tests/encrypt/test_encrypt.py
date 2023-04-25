from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(2, 'Jhuly')

    assert encrypt_message("Jhuly", 0) == "yluhJ"
    assert encrypt_message("Jhuly", 1) == "J_yluh"
    assert encrypt_message("Jhuly", 2) == "ylu_hJ"
    assert encrypt_message("Jhuly", 3) == "uhJ_yl"
    assert encrypt_message("Jhuly", 4) == "y_luhJ"
