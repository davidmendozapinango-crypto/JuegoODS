from core.card import Card


def test_card_generation():
    card = Card(dimension=5, theme_id=1)
    assert card.dimension == 5
    assert len(card.cells) == 5
    assert len(card.cells[0]) == 5
    flat = [num for row in card.cells for num in row]
    assert sorted(flat) == list(range(1, 26))
    assert len(set(flat)) == 25


def test_card_mark_and_winner():
    card = Card(dimension=3, theme_id=1)
    card.figure_mask = [[True] * 3 for _ in range(3)]
    for number in range(1, 10):
        card.mark_number(number)
    assert card.is_winner()


def test_card_pair():
    main, complement = Card.create_pair(5, 2)
    assert main.dimension == 5
    assert complement.dimension == 5
    assert main.theme_id == 2
