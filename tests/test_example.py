from hextel_pytest.example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'
    assert reverse('') == ''


def test_reverse_with_file():
    with open('fixtures/forreverse.txt', 'r', encoding='utf-8') as f:
        result = f.read().strip()

    test1 = reverse(result).strip()
    exepted_result = result[::-1]
    assert test1 == exepted_result
