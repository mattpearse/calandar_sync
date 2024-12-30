import modules
from datetime import date
import pytest

@pytest.mark.parametrize("start, end, output", [("2025-03-03", "2025-03-08", [date(2025,3,3), date(2025,3,4), date(2025,3,5), date(2025,3,6), date(2025,3,7), date(2025,3,8)])])
def test_get_list_of_dates(start, end, output):
    result = modules.get_list_of_dates(start, end)
    assert result == output
