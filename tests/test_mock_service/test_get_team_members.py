import pytest

from core_methods.member_list_methods import get_members_list
from core_methods.one_member_methods import get_one_member_info

"""
We need to move this list, but it is just for example
"""

NEEDED_KEYWORDS = [
    'position', 'level', 'first_name', 'last_name', 'ID'
]


def test_getting_list_of_members():
    """
    Gets full list of members and validate each received object.
    I don't have a time to create good asserts methods with check all needed types and values
    We can use pydentic for this
    But now we have simple check
    """
    response = get_members_list.fetch()
    data_for_check = response.json()['data']
    assert response.status_code == 200
    assert 'members' in data_for_check
    assert type(data_for_check['members']) is list


def test_get_member_without_id():
    """
    In this case we try to get member without id
    """
    response = get_one_member_info.fetch()
    assert response.status_code == 404


def test_getting_member_with_valid_id():
    """
    In this case we try to get member with valid id. I don't have a description or requirements,
    so I will use 428fab00290d as valid. I get this ID from get_members_list method
    """
    response = get_one_member_info.set_by_id("428fab00290d").fetch()
    data_for_check = response.json()['data']
    assert response.status_code == 200
    assert type(data_for_check) is dict
    # BAD WAY!!! Usually i don't do that, but I don't have a time. I prefer create check schema and compare
    for keyword in NEEDED_KEYWORDS:
        assert keyword in data_for_check


@pytest.mark.parametrize("wrong_id", [9999999, "11Ad", "41$as@a", "there", -1, 0])
def test_getting_member_by_invalid_id(wrong_id):
    """
    Try to get members info with wrong id
    """
    response = get_one_member_info.set_by_id(wrong_id).fetch()
    assert response.status_code == 404


