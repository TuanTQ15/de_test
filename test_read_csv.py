import unittest
from main import read_csv

class Testing(unittest.TestCase):
    #Testcase csv không có dấu nháy đôi và không có dấu phẩy trong các cột
    def test_csv_no_quotes_comma(self):
        path = "data_unit_test/no_quotes_comma.csv"
        result = read_csv(path=path)
        data_expect=[['TOK', 'UPDATE', 'DATE', 'SHOT'], ['JET', '20031201', '20001006', '53521']]
        self.assertEqual(result, data_expect)
        print("Testcase: dont have quote, dont have comma pass")
        print()
        print(data_expect)
        print(result)
        print("----------------------------------------------------------------------")
    #Testcase csv không có dấu phẩy và có dấu nháy đôi trong các cột
    def test_csv_have_quotes(self):
        path = "data_unit_test/have_quotes.csv"
        result = read_csv(path=path)
        data_expect=[['TOK', 'UPDATE', 'DATE', 'SHOT'], ['JET', '20031201', '20001006', '53521']]
        self.assertEqual(result, data_expect)
        print()
        print("Testcase: have quotes, dont have comma pass")
        print(data_expect)
        print(result)
        print("----------------------------------------------------------------------")
    #Testcase csv có dấu phẩy và không có dấu nháy đôi trong các cột
    def test_csv_have_quotes_and_comma(self):
        path = "data_unit_test/have_comma_and_quotes.csv"
        result = read_csv(path=path)
        data_expect=[['TIK,TOK', 'UPDATE', 'DATE', 'SHOT'], ['JET', '20031201', '20001006', '53521']]
        self.assertEqual(result, data_expect)
        print()
        print("Testcase: have quotes, have comma pass")
        print(data_expect)
        print(result)
        print("----------------------------------------------------------------------")
    def test_csv_not_exists(self):
        path = "data_unit_test/not_exists.csv"
        data_expect="Error opening file"
        result = read_csv(path=path)
        self.assertEqual(result, data_expect)
        print()
        print(data_expect)
        print(result)
        print("Testcase: not exists pass")
        print("----------------------------------------------------------------------")

if __name__ == '__main__':
    unittest.main()