try:
    from modules.utils.utils import read_from_file

except ImportError as Ie:
    print(f"[ + ] Import Error [modules.tests.prober]: {Ie}")
    exit(1)

test_file = 'urls.txt'

def test_read_from_file():
    expected = ["google.com\n","facebook.com\n","instagram.com\n","asddsadsf.com\n"]
    content = read_from_file(test_file)

    assert expected == content