from package_example.utils import conversions


def test_two_bytes_to_uint16():
    assert conversions.bytes_to_uint16(b'\x10\x23')[0] == 8976


def test_multiple_bytes_to_uint16():
    assert (
        conversions.bytes_to_uint16(b'\x11\x22\x33\x44\x55\x66') ==
        [8721, 17459, 26197]
    ).all()
