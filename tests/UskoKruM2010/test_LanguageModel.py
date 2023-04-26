from src.UskoKruM2010.LanguageModel import LanguageModel


def test_get_languages_not_none():
    assert LanguageModel.get_languages() != None


def test_get_languages_has_elements():
    assert len(LanguageModel.get_languages()) > 0


def test_get_languages_check_elemenents_len():
    languages = LanguageModel.get_languages()
    for language in languages:
        assert len(language.strip()) > 0
