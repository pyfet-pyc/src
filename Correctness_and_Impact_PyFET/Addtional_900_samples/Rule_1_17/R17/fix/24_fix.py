def test_credit_card_full(self, faker, num_samples):
    for _ in range(num_samples):
        card_data = faker.credit_card_full().split("\n")
        assert re.match("[A-Za-z]+", card_data[1]), 'invalid card %r' % card_data[1]
        assert card_data[4] in RuRuBankProvider.banks

