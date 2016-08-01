import unittest
from social_net_analyer.sn_analyzer.analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):

    def test_read_data_good_file_name(self):
        a = Analyzer()
        a.read_data('data/data.csv')
        self.assertIsNotNone(a._ss)

    def test_read_data_bad_file_name(self):
        a = Analyzer()
        self.assertRaises(Exception, a.read_data, 'data/badfilename.csv')

    def test_sample_analysis(self):
        a = Analyzer('data/data.csv')
        a.read_data()
        self.assertDictEqual(a.get_aggregates(), {1: 350, 7: 480})

    def test_complex_analysis(self):
        a = Analyzer('data/data.csv')
        a.read_data()
        self.assertDictEqual(a.get_aggregates(), {1: 350, 7: 480, })

    def test_sample_analysis_end_with_original_post(self):
        a = Analyzer('data/data_test_1.csv')
        a.read_data()
        self.assertDictEqual(a.get_aggregates(), {1: 350, 7: 480, 10: 1000})

    def test_sample_analysis_one_original_post(self):
        a = Analyzer('data/one_post.csv')
        a.read_data()
        self.assertDictEqual(a.get_aggregates(), {3: 6})

    def test_sample_analysis_one_original_post_multiple_repost(self):
        a = Analyzer('data/one_post_multiple_repost.csv')
        a.read_data()
        self.assertDictEqual(a.get_aggregates(), {3: 6})

    def test_three_unique_posts(self):
        a = Analyzer('data/three_unique_posts.csv')
        a.read_data()
        self.assertDictEqual(a.get_aggregates(), {0: 1, 1: 2, 2: 3})

    def test_text_data(self):
        a = Analyzer('data/bad_data_2.csv')
        a.read_data()
        self.assertDictEqual(a.get_aggregates(), {})

    def test_no_data(self):
        a = Analyzer('data/no_posts.csv')
        a.read_data()
        self.assertDictEqual(a.get_aggregates(), {})

    def test_bad_data(self):
        a = Analyzer('data/bad_data.csv')
        a.read_data()
        self.assertRaises(Exception, a.get_aggregates)

    def test_call_aggregates_on_empty_dataframe(self):
        a = Analyzer()
        self.assertRaises(Exception, a.get_aggregates)

if __name__ == '__main__':
    unittest.main()