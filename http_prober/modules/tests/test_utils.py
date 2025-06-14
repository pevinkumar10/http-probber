try:
    from http_prober.modules.utils.utils import read_from_file

except ImportError as Ie:
    print(f"[ + ] Import Error [modules.tests.utils]: {Ie}")
    exit(1)

# Default test file.
test_file = 'urls.txt'

def test_read_from_file() -> bool:
    """
        Function to test the read_from_file in utils with expected result. 

        Args:
            None
            
        Returns:
            bool    :   Returns True if expected result match with test result.
                
    """
    expected = ["google.com\n","facebook.com\n","instagram.com\n","asddsadsf.com\n"]
    content = read_from_file(test_file)

    assert expected == content