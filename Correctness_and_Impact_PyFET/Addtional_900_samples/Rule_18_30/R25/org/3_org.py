def test_match(brew_no_available_formula_one, brew_no_available_formula_two,
               brew_no_available_formula_three, brew_already_installed,
               brew_install_no_argument):
    assert match(Command('brew install giss',
                         brew_no_available_formula_one))
    assert match(Command('brew install elasticserar',
                         brew_no_available_formula_two))
    assert match(Command('brew install gitt',
                         brew_no_available_formula_three))
    assert not match(Command('brew install git',
                             brew_already_installed))
    assert not match(Command('brew install', brew_install_no_argument))
