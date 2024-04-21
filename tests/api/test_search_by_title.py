from autodoc_project.api.board_api import board_api


def test_search_by_title_and_number():
    resp = board_api.search_by_title_and_number('ZIC', '132661')
    assert resp[0] == 'ZIC'
    assert resp[1] == '132661'
