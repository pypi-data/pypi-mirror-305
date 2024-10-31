# kpi_library/one_variable_methods/text.py
import re
import json
import nltk
import pandas as pd
import contractions
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from spellchecker import SpellChecker

from typing import List, Dict, Tuple, Set, Union, Optional

from ..result_types import ResultTypes
from ..uni_variable import OneVarMethods

nltk.download('punkt')
nltk.download('stopwords')


class TextMethods(OneVarMethods):
    """
    Text column quality profiling methods.

    Parameters
    ----------
    dataset: :obj:`pandas.Series`
        Data to be processed.

    Attributes
    ----------
    data: :obj:`pandas.Series`
        Object containing the text data to be processed.
    __word_tokenized_data: None or :obj:`pandas.Series`
        Object containing the text data tokenized into words.
    __tokenized_sentences_count: Optional[pd.Series]
        Number of sentences per entry.
    __tokenized_characters_count: Optional[pd.Series]
        Number of characters per entry.

    Methods
    -------
    count_sentences:
        Sentences count distribution.
    count_words:
        Word count distribution.
    count_characters:
        Character count distribution.
    distribution_most_frequent_elements:
        Most frequent element distribution.
    distribution_less_frequent_elements:
        Less frequent element distribution.
    longest_words:
        Words longer than the given length.
    longest_frequent_words:
        Words longer than the given length and with a higher frequency than the given frequency.
    collocations_distribution:
        Collocation distribution of two, three or both words.
    abbreviation_distribution:
        Total or average number of abbreviations.
    acronym_distribution:
        Total or average number of acronyms.
    uppercase_distribution:
        Total or average number of upper words.
    spell_mistakes_distribution:
        Total or average number of misspellings.
    lexical_diversity:
        Total number of words, number of distinct words or percentage of distinct words.

    Examples
    --------
    >>> tm = TextMethods(dataset=pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", \
    "Please. Help me."], name='text'))
    >>> tm.to_dqv(method_name='lexical_diversity', parameters=[])
    [{'dqv_isMeasurementOf': 'text.lexical_diversity_total', 'dqv_computedOn': 'text', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '19'}, {'dqv_isMeasurementOf': 'text.lexical_diversity_distinct', \
'dqv_computedOn': 'text', 'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '16'}, {\
'dqv_isMeasurementOf': 'text.lexical_diversity_uniqueness', 'dqv_computedOn': 'text', 'rdf_datatype': 'Float', \
'ddqv_hasParameters': [], 'dqv_value': '84.21'}]
    """
    LANGUAGES_STOPWORDS: List[str] = stopwords.fileids()
    # attributes
    __word_tokenized_data: Optional[pd.Series]
    __tokenized_sentences_count: Optional[pd.Series]
    __tokenized_characters_count: Optional[pd.Series]

    def __init__(self, dataset: pd.Series):
        super(TextMethods, self).__init__(class_name='text', dataset=dataset)
        self.data = dataset.dropna(inplace=False).astype('string')

    def count_sentences(self) -> List[Dict[str, int]]:
        """
        Computes the length in sentences of each entry and gets the frequency of each length in the data, i.e., obtains
        the sentence-length frequency distribution of the given data.

        See also
        --------
        count_sentences_percent: obtains the sentence-length frequency distribution, but the frequency is the percent\
        age of occurrence, rather than the number of items.

        Examples
        --------
        >>> tm = TextMethods(dataset=pd.Series(["how are you", "I like to eat pasta.", None, \
        "I don't know how to do it", "Please. Help me."], name='text'))
        >>> tm.count_sentences()
        [{'item': 1, 'frequency': 3}, {'item': 2, 'frequency': 1}]
        >>> tm = TextMethods(dataset=pd.Series([None, None, None], name='text'))
        >>> tm.count_sentences()
        []

        Return
        ------
        _: :obj:`list` of :obj:`dict`
            Contains the frequency distribution of the number of sentences, being `item` the amount of sentences in each
            entry, and 'frequency' the number of entries with that length.
        """
        self.data_type = ResultTypes.DISTRIBUTION_INT.value
        # sentence tokenization and count number of sentence per entry
        if not hasattr(self, '__tokenized_sentences_count'):
            self.__tokenized_sentences_count = self.data.transform(
                lambda entry: len(sent_tokenize(entry))
            ).value_counts(sort=False)
        return [{'item': length, 'frequency': count} for length, count in self.__tokenized_sentences_count.items()]

    def count_sentences_percent(self) -> List[Dict[str, Union[int, float]]]:
        """
        Computes the length in sentences of each entry and gets the percentage of occurrence of each length in the data,
        i.e., obtains the sentence-length frequency distribution of the given data.

        See also
        --------
        count_sentences: obtains the sentence-length frequency distribution, but the frequency is the number of items, \
        rather than the percentage of occurrence.

        Examples
        --------
        >>> tm = TextMethods(dataset=pd.Series(["how are you", "I like to eat pasta.", None, \
        "I don't know how to do it", "Please. Help me."], name='text'))
        >>> tm.count_sentences_percent()
        [{'item': 1, 'frequency': 60.0}, {'item': 2, 'frequency': 20.0}]
        >>> tm = TextMethods(dataset=pd.Series([None, None, None], name='text'))
        >>> tm.count_sentences_percent()
        []

        Return
        ------
        _: :obj:`list` of :obj:`dict`
            Contains the frequency distribution of the number of sentences being `item` the amount of sentences in each
            entry, and 'frequency' the number or percentage of entries with that length.
        """
        self.data_type = ResultTypes.DISTRIBUTION_FLOAT.value
        # sentence tokenization and count number of sentence per entry
        if not hasattr(self, '__tokenized_sentences_count'):
            self.__tokenized_sentences_count = self.data.transform(
                lambda entry: len(sent_tokenize(entry))
            ).value_counts(sort=False)
        # return frequency distribution
        return [{
            'item': length, 'frequency': float(round(count/self.n_rows*100, 2))
        } for length, count in self.__tokenized_sentences_count.items()]

    def count_words(self) -> List[Dict[str, int]]:
        """
        Word count distribution.

        Examples
        --------
        >>> tm = TextMethods(dataset=pd.Series(["how are you", "I like to eat pasta.", None, \
        "I don't know how to do it", "Please. Help me."], name='text'))
        >>> tm.count_words()
        [{'item': 3, 'frequency': 2}, {'item': 5, 'frequency': 1}, {'item': 8, 'frequency': 1}]
        >>> tm = TextMethods(dataset=pd.Series([None, None, None], name='text'))
        >>> tm.count_words()
        []

        Return
        ------
        _: list of dict
            Contains the frequency distribution of the number of words being `item` the amount of words in each
            entry, and 'frequency' the number or percentage of entries with that length.
        """
        # check parameter
        self.data_type = ResultTypes.DISTRIBUTION_INT.value
        # word tokenization and count number of words per entry
        if not hasattr(self, '__word_tokenized_data'):
            self.__word_tokenized_data = self.data.transform(self.__word_tokenize)
        # compute frequency distribution of the word-length
        lengths = self.__word_tokenized_data.str.len().value_counts(sort=False)
        return [{'item': int(length), 'frequency': int(count)} for length, count in lengths.items()]

    def count_words_percent(self) -> List[Dict[str, Union[int, float]]]:
        """
        Word count distribution.

        Examples
        --------
        >>> tm = TextMethods(dataset=pd.Series(["how are you", "I like to eat pasta.", None, \
        "I don't know how to do it", "Please. Help me."], name='text'))
        >>> tm.count_words_percent()
        [{'item': 3, 'frequency': 40.0}, {'item': 5, 'frequency': 20.0}, {'item': 8, 'frequency': 20.0}]
        >>> tm = TextMethods(dataset=pd.Series([None, None, None, None], name='text'))
        >>> tm.count_words_percent()
        []

        Return
        ------
        _: list of dict
            Contains the frequency distribution of the number of words being `item` the amount of words in each
            entry, and 'frequency' the number or percentage of entries with that length.
        """
        self.data_type = ResultTypes.DISTRIBUTION_FLOAT.value
        # word tokenization and count number of words per entry
        if not hasattr(self, '__word_tokenized_data'):
            self.__word_tokenized_data = self.data.transform(self.__word_tokenize)
        # compute frequency distribution of the word-length
        lengths = self.__word_tokenized_data.str.len().value_counts(sort=False)
        return [{
            'item': int(length), 'frequency': float(round((count/self.n_rows)*100, 2))
        } for length, count in lengths.items()]

    @staticmethod
    def __word_tokenize(entry: str):
        """"""
        return [word for word in re.split(r'\W+', entry.lower()) if word != '']

    def count_characters(self) -> List[Dict[str, int]]:
        """
        Computes the length in characters of each entry and gets the frequency of each length in the data, i.e., obta\
        ins the character-length frequency distribution of the given data.

        See also
        --------
        count_characters_percent: obtains the character-length frequency distribution, but the frequency is the percen\
        tage of occurrence, rather than the number of items.

        Examples
        --------
        >>> tm = TextMethods(dataset=pd.Series(["how are you", "I like to eat pasta.", None, \
        "I don't know how to do it", "Please. Help me."], name='text'))
        >>> tm.count_characters()
        [{'item': 11, 'frequency': 1}, {'item': 20, 'frequency': 1}, {'item': 25, 'frequency': 1}, \
{'item': 16, 'frequency': 1}]
        >>> tm = TextMethods(dataset=pd.Series([None, None, None], name='text'))
        >>> tm.count_characters()
        []

        Return
        ------
        _: list of dict
            Contains the frequency distribution of the number of characters, being `item` the amount of characters in \
            each entry, and `frequency` the number of items with that length.
        """
        # check parameter
        self.data_type = ResultTypes.DISTRIBUTION_INT.value
        # compute character length and character distribution
        if not hasattr(self, '__tokenized_characters_count'):
            self.__tokenized_characters_count = self.data.str.len().value_counts(sort=False)
        return [{
            'item': int(length), 'frequency': int(count)
        } for length, count in self.__tokenized_characters_count.items()]

    def count_characters_percent(self) -> List[Dict[str, Union[int, float]]]:
        """
        Computes the length in characters of each entry and gets the percentage of occurrence of each length in the d\
        ata, i.e., obtains the character-length frequency distribution of the given data.

        See also
        --------
        count_characters: obtains the character-length frequency distribution, but the frequency is the number of \
        items, rather than the percentage of occurrence.

        Examples
        --------
        >>> tm = TextMethods(dataset=pd.Series(["how are you", "I like to eat pasta.", None, \
        "I don't know how to do it", "Please. Help me."], name='text'))
        >>> tm.count_characters_percent()
        [{'item': 11, 'frequency': 20.0}, {'item': 20, 'frequency': 20.0}, {'item': 25, 'frequency': 20.0}, \
{'item': 16, 'frequency': 20.0}]
        >>> tm = TextMethods(dataset=pd.Series([None, None, None], name='text'))
        >>> tm.count_characters_percent()
        []

        Return
        ------
        _: list of dict
            Contains the frequency distribution of the number of characters, being `item` the amount of characters in \
            each entry, and `frequency` the number of items with that length.
        """
        # check parameter
        self.data_type = ResultTypes.DISTRIBUTION_FLOAT.value
        # compute character length and character distribution
        if not hasattr(self, '__tokenized_characters_count'):
            self.__tokenized_characters_count = self.data.str.len().value_counts(sort=False)
        return [{
            'item': int(length), 'frequency': float(round(count/self.n_rows*100, 2))
        } for length, count in self.__tokenized_characters_count.items()]

    @staticmethod
    def __distribution_format(method_name: str, data: pd.DataFrame) -> List[Dict[str, str]]:
        """
        This method returns the elements of the distribution in the correct format.

        Parameters
        ----------
        method_name: str
            Name of the method.
        data: :obj:`pandas.DataFrame`
            Object containing the data to build the distribution.

        Return
        ------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the name of the method (`method_name`), the data type (`data_type`) and the
            result of the distribution (`value`).
        """
        return [{
            'method_name': method_name,
            'data_type': ResultTypes.DISTRIBUTION_INT.value,
            'value': json.dumps([
                {'item': word, 'frequency': int(frequency)} for word, frequency in data['count'].items()])
        }, {
            'method_name': f'{method_name}_percent',
            'data_type': ResultTypes.DISTRIBUTION_FLOAT.value,
            'value': json.dumps(
                [{'item': word, 'frequency': float(frequency)} for word, frequency in data['_percent'].items()])
        }]

    def distribution_most_frequent_elements(
            self, num_items: Union[str, int] = 10, tokenization: Union[str, bool] = True,
            stopwords_removal: Union[str, bool] = True, language: str = "english"
    ) -> List[Dict[str, str]]:
        """
        Study the frequency distribution of the first `num_items` most frequent elements.

        Parameters
        ----------
        num_items: str or int, default 10.
            Number of elements to show.
        tokenization: str or bool, default True.
            Express if the entry of srs have been tokenized.
        stopwords_removal: str or bool, default True.
            Express if stopwords must be removed.
        language: {"catalan", "czech", "german", "greek", "english", "spanish", "finnish", "french", "hungarian",
        "icelandic", "italian", "latvian", "dutch", "polish", "portuguese", "romanian", "russian", "slovak",
        "slovenian", "swedish", "tamil"}, default "english".
            Language in which the texts are written.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", \
        "Please. Help me."], name='text'))
        >>> tm.distribution_most_frequent_elements(num_items=3, tokenization=True, stopwords_removal=False, \
        language='english')
        [{'method_name': 'distribution_most_frequent_elements', 'data_type': 'List<Map<String,String>>', 'value': \
'[{"item": "how", "frequency": 2}, {"item": "i", "frequency": 2}, {"item": "to", "frequency": 2}]'}, {'method_name': \
'distribution_most_frequent_elements_percent', 'data_type': 'List<Map<String,String>>', 'value': '[{"item": "how", \
"frequency": 0.10526}, {"item": "i", "frequency": 0.10526}, {"item": "to", "frequency": 0.10526}]'}]

        Raises
        ------
        IncorrectParameterError
            If any of the parameters normalized, tokenization, stopwords_removal, num_items or language are incorrect.

        Returns
        -------
        : :obj:`list` of `dict`
            List of dictionaries where each of them show one of the most frequent elements (`item`) and its frequency
            (`frequency`).
        """
        # check parameters
        tokenization = self._check_boolean_parameter(parameter=tokenization, parameter_name='tokenization')
        stw_removal = self._check_boolean_parameter(parameter=stopwords_removal, parameter_name='stopwords_removal')
        num_items = self._check_int_parameter(parameter=num_items, parameter_name='num_items', ge=1)
        self._check_enum_parameter(parameter=language, parameter_name='language', values=self.LANGUAGES_STOPWORDS)
        # tokenize the words if it is necessary
        if tokenization:
            if not hasattr(self, '__word_tokenized_data'):
                self.__word_tokenized_data = self.data.transform(self.__word_tokenize)
            srs = self.__word_tokenized_data
        else:
            srs = self.data.copy()
        # remove stopwords if it is demanded
        if stw_removal:
            _stopwords = set(stopwords.words(language))
            srs = srs.apply(lambda entry: self.__stopwords_removal(entry, _stopwords))
        # study frequency distribution of the different words in the data
        srs = srs.explode()
        num_words = srs.size
        temp = srs.value_counts(sort=True, ascending=False, dropna=True).iloc[:num_items].to_frame()
        temp['_percent'] = temp['count'].div(num_words).round(5)
        # return the result of the number and percentage of words
        return self.__distribution_format(method_name='distribution_most_frequent_elements', data=temp)

    def distribution_less_frequent_elements(
            self, num_items: Union[str, int] = 10, tokenization: Union[str, bool] = True) -> List[Dict[str, str]]:
        """
        Study the frequency distribution of the first num_items less frequent elements

        Parameters
        ----------
        num_items: str or int, default 10.
            Number of elements to show.
        tokenization: str or bool, default True.
            Whether the entries of the data must be tokenized or not.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", \
        "Please. Help me."], name='text'))
        >>> tm.distribution_less_frequent_elements(num_items=3, tokenization=True)
        [{'method_name': 'distribution_less_frequent_elements', 'data_type': 'List<Map<String,String>>', 'value': \
'[{"item": "are", "frequency": 1}, {"item": "you", "frequency": 1}, {"item": "like", "frequency": 1}]'}, {\
'method_name': 'distribution_less_frequent_elements_percent', 'data_type': 'List<Map<String,String>>', 'value': \
'[{"item": "are", "frequency": 0.05263}, {"item": "you", "frequency": 0.05263}, {"item": "like", "frequency": 0.05263\
}]'}]

        Raises
        ------
        IncorrectParameterError
            If any of the parameters, normalized, tokenization or num_items, are incorrect.

        Returns
        -------
        _: :obj:`list` of `dict`
            List of dictionaries where each of them show one of the most frequent elements and its frequency
        """
        # check parameters
        num_items = self._check_int_parameter(parameter=num_items, parameter_name='num_items', ge=1)
        tokenization = self._check_boolean_parameter(parameter=tokenization, parameter_name='tokenization')
        # tokenize the result if its necessary
        if tokenization:
            if not hasattr(self, '__word_tokenized_data'):
                self.__word_tokenized_data = self.data.transform(self.__word_tokenize)
            srs = self.__word_tokenized_data.explode()
        else:
            srs = self.data.copy()
        # get frequency distribution of srs
        n_words = srs.size
        freq_dist = srs.value_counts(sort=True, ascending=True, dropna=False).iloc[:num_items].to_frame()
        freq_dist['_percent'] = freq_dist['count'].div(n_words).round(5)
        return self.__distribution_format(method_name='distribution_less_frequent_elements', data=freq_dist)

    def longest_words(self, length: Union[str, int] = 7) -> List[str]:
        """
        Returns those words that are longer than `length`.

        Parameters
        ----------
        length: int, default 7.
            Minimum length of the words to get.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", \
        "Please. Help me."], name='text'))
        >>> tm.longest_words(length=5)
        ['pasta', 'please']
        >>> tm.longest_words(length='5')
        ['pasta', 'please']
        >>> tm.longest_words()
        []

        Raises
        ------
        IncorrectParameterError
            If `length` is less than 1, since the length of the words must be greater than 0 characters.

        Returns
        -------
        _: :obj:`list` of :obj:`str`
            List with the words that meet the condition of length.
        """
        self.data_type = ResultTypes.LIST_STR.value
        # check parameter
        length = self._check_int_parameter(parameter=length, parameter_name='length', ge=1)
        # tokenize the data into words
        if not hasattr(self, '__word_tokenized_data'):
            self.__word_tokenized_data = self.data.transform(self.__word_tokenize)
        # get words and obtain those that are longer than `length`
        words = self.__word_tokenized_data.explode().unique()
        return [word for word in words if len(word) >= length]

    def longest_frequent_words(self, length: int = 7, frequency: int = 100) -> List[str]:
        """
        Returns those words that its length is larger than "length" and are sufficiently frequent

        Parameters
        ----------
        length: int, default 7
            Minimum length of the words to pick.
        frequency: int, default 100
            Minimum frequency of the words to pick.

        Examples
        --------
        >>> tm =TextMethods(pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", \
        "Please. Help me."], name='text'))
        >>> tm.longest_frequent_words(length=2, frequency=1)
        ['how', 'to']
        >>> tm.longest_frequent_words(length=3, frequency=1)
        ['how']
        >>> tm.longest_frequent_words()
        []

        Raises
        ------
        IncorrectParameterError
            If `length` or/and `frequency` are less than 1.

        Returns
        -------
        _: :obj:`list` of :obj:`str`
            List with the words in the data that meet the conditions of length and frequency.
        """
        self.data_type = ResultTypes.LIST_STR.value
        # check parameters
        length = self._check_int_parameter(parameter=length, parameter_name='length', ge=1)
        frequency = self._check_int_parameter(parameter=frequency, parameter_name='frequency', ge=1)
        # tokenize the data into words
        if not hasattr(self, '__word_tokenized_data'):
            self.__word_tokenized_data = self.data.transform(self.__word_tokenize)
        # get words and its frequency in data
        words = self.__word_tokenized_data.explode().value_counts(sort=False)
        return [word for word in words.loc[words.gt(frequency)].index if len(word) >= length]

    def collocations_distribution(
            self, collocation: str = 'bigram', language: str = 'english', num_items: Union[str, int] = 10
    ) -> List[Dict[str, Union[str, int]]]:
        """
        Show the collocation distribution of the first most common collocations in the data.

        Parameters
        ----------
        collocation: {'bigram', 'trigram', 'both'}, optional. Default, bigram
            Type of collocation to search. `both` means the method should search for bigram and trigram collocations.
        language: {}. Default, english.
            Language of the text.
        num_items: str or int, optional. Default, 10.
            Number of collocations to return.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", \
        "how are you doing", "Please. Help me."], name='text'))
        >>> tm.collocations_distribution(collocation='bigram', language='english', num_items=3)
        [{'item': 'like eat', 'frequency': 1}, {'item': 'eat pasta', 'frequency': 1}, \
{'item': 'please help', 'frequency': 1}]
        >>> tm.collocations_distribution(collocation='trigram', language='english', num_items=3)
        [{'item': 'like eat pasta', 'frequency': 1}]
        >>> tm.collocations_distribution(collocation='both', language='english', num_items=2)
        [{'item': 'like eat pasta', 'frequency': 1}, {'item': 'like eat', 'frequency': 1}]
        >>> tm = TextMethods(pd.Series([None, None, None], name='text'))
        >>> tm.collocations_distribution(collocation='bigram', language='english', num_items=3)
        []

        Raises
        ------
        IncorrectParameterError
            If the specified language is incorrect (i.e., it is not in the list of possible values), or the collocation
            method is not correct, neither bigram, nor trigram, nor both.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the collocation distribution. Each dictionary contains one collocation
            (`collocation`) and the number (`frequency`) and percentage (`frequency_distribution`) of times it appears
            in the data.
        """
        # save data type response
        self.data_type = ResultTypes.DISTRIBUTION_INT.value
        # check correct number of elements to show
        num_items = self._check_int_parameter(parameter=num_items, parameter_name='num_items', ge=1)
        self._check_enum_parameter(
            parameter=collocation, parameter_name='collocation', values=['bigram', 'trigram', 'both'])
        self._check_enum_parameter(
            parameter=language, parameter_name='language', values=self.LANGUAGES_STOPWORDS)
        # get collocations and its frequency
        collocations = self.__get_collocations(collocation=collocation, language=language)
        freq_dist = collocations.value_counts(sort=True, ascending=False, dropna=True)
        # compute distribution
        return [{'item': ' '.join(item), 'frequency': count} for item, count in freq_dist.iloc[:num_items].items()]

    def collocations_distribution_percent(
            self, collocation: str = 'bigram', language: str = 'english', num_items: Union[str, int] = 10
    ) -> List[Dict[str, Union[str, float]]]:
        """
        Show the collocation distribution of the first most common collocations in the data.

        Parameters
        ----------
        collocation: {'bigram', 'trigram', 'both'}, optional. Default, bigram
            Type of collocation to search. `both` means the method should search for bigram and trigram collocations.
        language: {}. Default, english.
            Language of the text.
        num_items: str or int, optional. Default, 10.
            Number of collocations to return.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", \
        "how are you doing", "Please. Help me."], name='text'))
        >>> tm.collocations_distribution_percent(collocation='bigram', language='english', num_items=3)
        [{'item': 'like eat', 'frequency': 33.33}, {'item': 'eat pasta', 'frequency': 33.33}, \
{'item': 'please help', 'frequency': 33.33}]
        >>> tm.collocations_distribution_percent(collocation='trigram', language='english', num_items=3)
        [{'item': 'like eat pasta', 'frequency': 100.0}]
        >>> tm.collocations_distribution_percent(collocation='both', language='english', num_items=2)
        [{'item': 'like eat pasta', 'frequency': 25.0}, {'item': 'like eat', 'frequency': 25.0}]
        >>> tm = TextMethods(pd.Series([None, None, None], name='text'))
        >>> tm.collocations_distribution_percent(collocation='bigram', language='english', num_items=3)
        []

        Raises
        ------
        IncorrectParameterError
            If the specified language is incorrect (i.e., it is not in the list of possible values), or the collocation
            method is not correct, neither bigram, nor trigram, nor both.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the collocation distribution. Each dictionary contains one collocation
            (`collocation`) and the number (`frequency`) and percentage (`frequency_distribution`) of times it appears
            in the data.
        """
        # save data type response
        self.data_type = ResultTypes.DISTRIBUTION_FLOAT.value
        # check correct number of elements to show
        num_items = self._check_int_parameter(parameter=num_items, parameter_name='num_items', ge=1)
        self._check_enum_parameter(
            parameter=collocation, parameter_name='collocation', values=['bigram', 'trigram', 'both'])
        self._check_enum_parameter(
            parameter=language, parameter_name='language', values=self.LANGUAGES_STOPWORDS)
        # get collocations
        collocations = self.__get_collocations(collocation=collocation, language=language).dropna()
        # compute the frequency distribution of each collocation and return distribution
        freq_dist = collocations.value_counts(sort=True, ascending=False)
        return [{
            'item': ' '.join(item), 'frequency': float(round(count/collocations.shape[0]*100, 2))
        } for item, count in freq_dist.iloc[:num_items].items()]

    def __get_collocations(self, collocation: str, language: str):
        """
        Obtains the collocations from the given data.

        Parameters
        ----------
        collocation: {'bigram', 'trigram', 'both'}, optional. Default bigram.
            Type of collocation to search. `both` means the method should search for bigram and trigram collocations.
        language: {}. Default, english.
            Language of the text.

        Returns
        -------
        : :obj:`pandas.Series`
            Object containing all collocations in the data.
        """
        # tokenize data into words
        if not hasattr(self, '__word_tokenized_data'):
            self.__word_tokenized_data = self.data.transform(self.__word_tokenize)
        # remove stopwords in data
        __stop_words = set(stopwords.words(language))
        srs = self.__word_tokenized_data.transform(lambda entry: self.__stopwords_removal(entry, __stop_words))
        # obtain collocations
        return srs.transform(getattr(self, f'_get_{collocation}')).explode()

    @staticmethod
    def _get_bigram(entry: List[str]) -> List[Tuple[str, str]]:
        """
        Return a list with the bigrams in entry.

        Parameters
        ----------
        entry: :obj:`list` of :obj:`str`
            List with words to transform.

        Returns
        -------
        _: :obj:`list` of :obj:`tuple`
            A list of tuples with the bigrams.
        """
        return list(zip(entry[:-1], entry[1:]))

    @staticmethod
    def _get_trigram(entry: List[str]) -> List[Tuple[str, str, str]]:
        """
        Return a list with trigrams of entry.

        Parameters
        ----------
        entry: :obj:`list` of :obj:`str`
            List with words to transform.

        Returns
        -------
        _: :obj:`list` of :obj:`tuple`
            A list of tuples with the trigrams.
        """
        return list(zip(entry[:-2], entry[1:-1], entry[2:]))

    @staticmethod
    def _get_both(entry: List[str]) -> List[Tuple[str, str, str]]:
        """
        Return a list with bigrams and trigrams of entry.

        Parameters
        ----------
        entry: :obj:`list` of :obj:`str`
            List with words to transform.

        Returns
        -------
        _: :obj:`list` of :obj:`tuple`
            A list of tuples with the bigrams and trigrams.
        """
        # compute trigrams
        grams = list(zip(entry[:-2], entry[1:-1], entry[2:]))
        # compute bigrams
        grams.extend(list(zip(entry[:-1], entry[1:])))
        # return
        return grams

    @staticmethod
    def __stopwords_removal(entry: List[str], stop_words: Set[str]) -> List[str]:
        """
        Removes the stopwords from the sentence given as input

        Parameters
        ----------
        entry: :obj:`list` of :obj:`str`
            List of words.
        stop_words: :obj:`set` of :obj:`str`
            Set of words considered as stopwords.

        Returns
        -------
        _: :obj:`list`of :obj:`str`
            List of words without stopwords (`stop_words`).
        """
        return [word for word in entry if word not in stop_words]

    def abbreviation_distribution(self) -> int:
        """
        Computes the total number of abbreviations in the given data.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", \
"Please, help me."], name='text'))
        >>> tm.abbreviation_distribution()
        1
        >>> tm = TextMethods(pd.Series([None, None, None], name='text'))
        >>> tm.abbreviation_distribution()
        0

        Returns
        -------
        _: int
            Total number of abbreviations in the given data.
        """
        self.data_type = ResultTypes.INT.value
        # get words from data
        words = self.data.str.split(" ").explode().dropna()
        # get number of abbreviations (if no words, no abbreviations)
        if words.shape[0] == 0:
            return 0
        total_num_abbr = 0
        for word in words:
            try:
                total_num_abbr += contractions.fix(word) != word
            except IndexError:
                # pass when this error happens
                pass
        return int(total_num_abbr)

    def abbreviation_distribution_percent(self) -> float:
        """
        Computes the average number of abbreviations per entry in the given data.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", \
"Please, help me."], name='text'))
        >>> tm.abbreviation_distribution_percent()
        5.56
        >>> tm = TextMethods(pd.Series([None, None, None], name='text'))
        >>> tm.abbreviation_distribution_percent()
        0

        Returns
        -------
        _: float
            Average number of abbreviations per entry in the given data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # get words from data
        words = self.data.str.split(" ").explode().dropna()
        # get number of abbreviations (if no words, no abbreviations)
        if words.shape[0] == 0:
            return 0
        total_num_abbr = 0
        for word in words:
            try:
                total_num_abbr += contractions.fix(word) != word
            except IndexError:
                # pass when this error happens
                pass
        return float(round(total_num_abbr/words.shape[0]*100, 2))

    def acronym_distribution(self) -> int:
        """
        Calculates the total number of acronyms in the given data.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["The United Nations (UN) are back.", "I like to eat pasta.", None, \
        "I don't know how to do it", "Please, help me."], name='text'))
        >>> tm.acronym_distribution()
        1
        >>> tm = TextMethods(pd.Series([None, None, None], name='text'))
        >>> tm.acronym_distribution()
        0

        Returns
        -------
        _: int
            Total number of acronyms.
        """
        self.data_type = ResultTypes.INT.value
        # compute the number of acronyms in data
        count = self.data.transform(lambda entry: len(re.findall(r'\b[A-Z.]{2,}s?\b', entry))).astype('float')
        return int(count.sum())

    def acronym_distribution_percent(self) -> float:
        """
        Calculates the percentage of acronyms in the given data.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["The United Nations (UN) are back.", "I like to eat pasta.", None, \
        "I don't know how to do it", "Please, help me."], name='text'))
        >>> tm.acronym_distribution_percent()
        4.55
        >>> tm = TextMethods(pd.Series([None, None, None], name='text'))
        >>> tm.acronym_distribution_percent()
        0

        Returns
        -------
        _: float
            Average number of acronyms in the data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # compute the number of acronyms in data
        count = self.data.transform(lambda entry: len(re.findall(r'\b[A-Z.]{2,}s?\b', entry))).astype('float')
        total_num_acronyms = count.sum()
        if total_num_acronyms == 0:
            return 0
        if not hasattr(self, '__word_tokenized_data'):
            self.__word_tokenized_data = self.data.transform(self.__word_tokenize)
        total_words = self.__word_tokenized_data.explode().dropna().shape[0]
        return float(round(total_num_acronyms/total_words*100, 2))

    def uppercase_distribution(self) -> int:
        """
        Calculates the number of capitalized words in the given data.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["The United Nations (UN) are back.", "I like to eat pasta.", None, \
        "I don't know how to do it", "Please, help me."], name='text'))
        >>> tm.uppercase_distribution()
        3
        >>> tm = TextMethods(pd.Series([None, None, None], name='text'))
        >>> tm.uppercase_distribution()
        0

        Returns
        -------
        _: int
            Number of captilized words in the data.
        """
        self.data_type = ResultTypes.INT.value
        # compute number of capitalized words in data
        words: pd.Series = self.data.transform(lambda entry: [word for word in re.split(r'\W+', entry) if word != ''])
        return int(sum(word.isupper() for word in words.explode()))

    def uppercase_distribution_percent(self) -> float:
        """
        Calculates the percentage of capitalized words in the given data.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["The United Nations (UN) are back.", "I like to eat pasta.", None, \
        "I don't know how to do it", "Please, help me."], name='text'))
        >>> tm.uppercase_distribution_percent()
        13.64
        >>> tm = TextMethods(pd.Series([None, None, None], name='text'))
        >>> tm.uppercase_distribution_percent()
        0

        Returns
        -------
        _: float
            Percentage of captilized words in the data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # compute number of capitalized words in data
        words: pd.Series = self.data.transform(lambda entry: [word for word in re.split(r'\W+', entry) if word != ''])
        words = words.explode()
        if words.shape[0] == 0:
            return 0
        num_upper_words = sum(word.isupper() for word in words)
        return float(round(num_upper_words/words.shape[0]*100, 2))

    def spell_mistakes_distribution(self, lang: str = 'en') -> Union[int, float]:
        """
        Find the total number of spell mistakes in the data.

        Parameters
        ----------
        lang: {'de', 'en', 'es', 'fr', 'pt', 'ru', 'ar'}, default 'en'
            Language in which the entries are written in

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["You re wrong.", "I like to eat pasta.", None, "I don't know how to do it", \
        "Please, help me."], name='text'))
        >>> tm.spell_mistakes_distribution()
        1
        >>> tm = TextMethods(pd.Series([None, None, None], name='text'))
        >>> tm.spell_mistakes_distribution()
        0

        Raises
        ------
        IncorrectParameterError
            Whether the average or lang parameter is incorrect.

        Returns
        -------
        _: int
            Total number of misspellings in the data.
        """
        self.data_type = ResultTypes.INT.value
        # check parameters
        self._check_enum_parameter(
            parameter=lang, parameter_name='lang', values=['de', 'en', 'es', 'fr', 'pt', 'ru', 'ar'])
        # tokenize data into words
        if not hasattr(self, '__word_tokenized_data'):
            self.__word_tokenized_data = self.data.transform(self.__word_tokenize)
        words = self.__word_tokenized_data.explode()
        # if no words, no misspelling
        if words.shape[0] == 0:
            return 0
        # compute number of misspellings in the data
        spell = SpellChecker(language=lang)
        return int(len(spell.unknown(words)))

    def spell_mistakes_distribution_percent(self, lang: str = 'en') -> float:
        """
        Find the average number of spell mistakes in the data.

        Parameters
        ----------
        lang: {'de', 'en', 'es', 'fr', 'pt', 'ru', 'ar'}, default 'en'
            Language in which the entries are written in

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["You re wrong.", "I like to eat pasta.", None, "I don't know how to do it", \
        "Please, help me."], name='text'))
        >>> tm.spell_mistakes_distribution_percent()
        5.26
        >>> tm = TextMethods(pd.Series([None, None, None], name='text'))
        >>> tm.spell_mistakes_distribution_percent(lang='en')
        0

        Raises
        ------
        IncorrectParameterError
            Whether the average or lang parameter is incorrect.

        Returns
        -------
        _: float
            Average number of misspellings in the data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # check parameters
        self._check_enum_parameter(
            parameter=lang, parameter_name='lang', values=['de', 'en', 'es', 'fr', 'pt', 'ru', 'ar'])
        # tokenize data into words
        if not hasattr(self, '__word_tokenized_data'):
            self.__word_tokenized_data = self.data.transform(self.__word_tokenize)
        words = self.__word_tokenized_data.explode()
        # if no words, no misspelling
        if words.shape[0] == 0:
            return 0
        # compute number of misspellings in the data
        spell = SpellChecker(language=lang)
        return float(round(len(spell.unknown(words))/words.shape[0]*100, 2))

    def lexical_diversity(self) -> List[Dict[str, str]]:
        """
        Computes the total number of words, the number of different words or the percentage of different words in the
        given data.

        Examples
        --------
        >>> tm = TextMethods(pd.Series(["You re wrong.", "I like to eat pasta.", None, "I don't know how to do it", \
        "Please, help me."], name='text'))
        >>> tm.lexical_diversity()
        [{'method_name': 'lexical_diversity_total', 'data_type': 'Integer', 'value': '19'}, \
{'method_name': 'lexical_diversity_distinct', 'data_type': 'Integer', 'value': '17'}, \
{'method_name': 'lexical_diversity_uniqueness', 'data_type': 'Float', 'value': '89.47'}]

        Return
        ------
        _: :obj:`list` of :obj:`dict`
            List containing the total number of words, the number of distinct words and the range.
        """
        # split the entries into words
        if not hasattr(self, '__word_tokenized_data'):
            self.__word_tokenized_data = self.data.transform(self.__word_tokenize)
        words = self.__word_tokenized_data.explode()
        # compute the total and unique number of words
        if words.shape[0] == 0:
            # if no words
            return [
                {'method_name': 'lexical_diversity_total', 'data_type': ResultTypes.INT.value, 'value': "0"},
                {'method_name': 'lexical_diversity_distinct', 'data_type': ResultTypes.INT.value, 'value': "0"},
                {'method_name': 'lexical_diversity_uniqueness', 'data_type': ResultTypes.FLOAT.value, 'value': "0.0"}]
        # if words
        return [
            {'method_name': 'lexical_diversity_total', 'data_type': ResultTypes.INT.value, 'value': str(words.size)},
            {'method_name': 'lexical_diversity_distinct', 'data_type': ResultTypes.INT.value,
             'value': str(words.unique().size)},
            {'method_name': 'lexical_diversity_uniqueness', 'data_type': ResultTypes.FLOAT.value,
             'value': str(round((words.unique().size/words.size)*100, 2))}]
