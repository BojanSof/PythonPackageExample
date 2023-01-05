from package_example.calculator import ops


def test_addition():
    assert ops.addition(b'\x10\x10', b'\x22\x22') == 12850
