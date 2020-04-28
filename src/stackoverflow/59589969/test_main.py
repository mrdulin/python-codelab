from unittest.mock import MagicMock, patch
from main import do


def test_check_process():
    with patch('main.check', side_effect=Exception('oops')) as mock_check:
        print(mock_check)
        do('http://something')

        assert mock_check.call_count == 1


def test_check_process_2():
    mock_checker = MagicMock(side_effect=Exception('oops'))
    with patch('main.check', new=mock_checker) as mock_check:
        print(mock_check)
        do('http://something')
        assert mock_check.call_count == 1


if __name__ == '__main__':
    test_check_process()
    test_check_process_2()
