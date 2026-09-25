from data_generator import get_results_by_id


def test_public_v1_person_feed_is_reachable():
    person = get_results_by_id('2012PARK03')
    assert person is not None
    assert person['id'] == '2012PARK03'
    assert person['ranks']['singles']
