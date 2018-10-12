import pytest

from senseme.senseme import decode_discovery


@pytest.mark.parametrize(
    'raw_message, expected_output',
    [
        (("(NAME;DEVICE;ID;MAC;MODEL,SERIES)".encode("utf-8"), ("127.0.0.1", "3101")),
         ("NAME", "MAC", "MODEL", "SERIES", "127.0.0.1")),
    ]
)
def test_discovery_message_decoding(raw_message, expected_output):
    test_message = raw_message
    name, mac, model, series, ip = decode_discovery(test_message)
    assert expected_output == (name, mac, model, series, ip)
