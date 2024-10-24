import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        string = "vowel"
        expected = 2
        actual = hw1.vowel_count(string)
        self.assertEqual(expected, actual)

    def test_vowel_count_2(self):
        string = "vowel count"
        expected = 4
        actual = hw1.vowel_count(string)
        self.assertEqual(expected, actual)

    # Part 2
    def test_short_lists_1(self):
        integer_lists = [[1,2], [3,4,5], [6,7]]
        expected = [[1,2], [6,7]]
        actual = hw1.short_lists(integer_lists)
        self.assertEqual(expected, actual)

    def test_short_lists_2(self):
        integer_lists = [[1,2,3], [4,5,6], [-7,8]]
        expected = [[-7,8]]
        actual = hw1.short_lists(integer_lists)
        self.assertEqual(expected, actual)

    # Part 3
    def test_ascending_pairs_1(self):
        integer_lists = [[1,2], [3,4,5], [6,7]]
        expected = [[1,2], [3,4,5], [6,7]]
        actual = hw1.ascending_pairs(integer_lists)
        self.assertEqual(expected, actual)

    def test_ascending_pairs_2(self):
        integer_lists = [[2,1], [3,4,5], [6,7]]
        expected = [[1,2], [3,4,5], [6,7]]
        actual = hw1.ascending_pairs(integer_lists)
        self.assertEqual(expected, actual)

    # Part 4
    def test_add_prices_1(self):
        price1 = data.Price(1, 20)
        price2 = data.Price(4, 19)
        expected = data.Price(5, 39)
        actual = hw1.add_prices(price1, price2)
        self.assertEqual(expected, actual)

    def test_add_prices_2(self):
        price1 = data.Price(1, 20)
        price2 = data.Price(4, 89)
        expected = data.Price(6, 9)
        actual = hw1.add_prices(price1, price2)
        self.assertEqual(expected, actual)

    # Part 5
    def test_rectangle_area_1(self):
        rectangle = data.Rectangle(data.Point(1,5), data.Point(3,2))
        expected = 6
        actual = hw1.rectangle_area(rectangle)
        self.assertEqual(expected, actual)

    def test_rectangle_area_2(self):
        rectangle = data.Rectangle(data.Point(-1,5), data.Point(3,2))
        expected = 12
        actual = hw1.rectangle_area(rectangle)
        self.assertEqual(expected, actual)

    # Part 6
    def test_books_by_author_1(self):
        author_name = "Suzanne Collins"
        book_list = [data.Book(["Suzanne Collins"], "The Hunger Games"),
                     data.Book(["Suzanne Collins"], "Catching Fire"),
                     data.Book(["Suzanne Collins"], "Mockingjay"),
                     data.Book(["Lois Lowry"], "The Giver")]
        expected = [data.Book(["Suzanne Collins"], "The Hunger Games"),
                     data.Book(["Suzanne Collins"], "Catching Fire"),
                     data.Book(["Suzanne Collins"], "Mockingjay")]
        actual = hw1.books_by_author(author_name, book_list)
        self.assertEqual(expected, actual)

    def test_books_by_author_2(self):
        author_name = "Neil Gaiman"
        book_list = [data.Book(["Suzanne Collins"], "The Hunger Games"),
                     data.Book(["Suzanne Collins"], "Catching Fire"),
                     data.Book(["Suzanne Collins"], "Mockingjay"),
                     data.Book(["Neil Gaiman", "Terry Pratchett"], "Good Omens")]
        expected = [data.Book(["Neil Gaiman", "Terry Pratchett"], "Good Omens")]
        actual = hw1.books_by_author(author_name, book_list)
        self.assertEqual(expected, actual)

    # Part 7
    def test_circle_bound_1(self):
        rectangle = data.Rectangle(data.Point(1,6), data.Point(3,2))
        expected = data.Circle(data.Point(2,4),2)
        actual = hw1.circle_bound(rectangle)
        self.assertEqual(expected, actual)

    def test_circle_bound_2(self):
        rectangle = data.Rectangle(data.Point(1,6), data.Point(7,2))
        expected = data.Circle(data.Point(4,4),3)
        actual = hw1.circle_bound(rectangle)
        self.assertEqual(expected, actual)

    # Part 8
    def test_below_pay_average_1(self):
        employee_list = [data.Employee("Neil", 5),
                         data.Employee("Terry", 6),
                         data.Employee("Suzanne", 4)]
        expected = ["Suzanne"]
        actual = hw1.below_pay_average(employee_list)
        self.assertEqual(expected, actual)

    def test_below_pay_average_2(self):
        employee_list = [data.Employee("Neil", 10),
                         data.Employee("Terry", 6),
                         data.Employee("Suzanne", 4)]
        expected = ["Terry", "Suzanne"]
        actual = hw1.below_pay_average(employee_list)
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
