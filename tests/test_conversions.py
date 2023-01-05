from package_example.utils import conversions


def test_bytes_to_uint16():
    assert conversions.bytes_to_uint16(b'\x10\x23') == 8976
