import data

# Write your functions for each part in the space below.

# Part 1
# counts the number of vowels in an input string
# input: string
# output: integer number of vowels in the input string
def vowel_count(string:str) -> int:
    string_lower = str.lower(string)
    count = 0
    for l in string_lower:
        if l == "a":
            count = count + 1
        if l == "e":
            count = count + 1
        if l == "i":
            count = count + 1
        if l == "o":
            count = count + 1
        if l == "u":
            count = count + 1
    return count

# Part 2
# return a list of only nested lists of length 2 from a list of lists of integers
# input: a list of lists of integers
# output: a list of the elements of the input list that are of length 2
def short_lists(integer_lists:list[list[int]]) -> list[list[int]]:
    short_integer_lists = []
    for l in integer_lists:
        if len(l) == 2:
            short_integer_lists.append(l)
    return short_integer_lists

# Part 3
# make nested lists of length 2 be in ascending order given a list of lists of integers
# input: a list of lists of integers
# output: a list of lists of integers where nested lists of length 2 are in ascending order
def ascending_pairs(integer_lists:list[list[int]]) -> list[list[int]]:
    new_list = []
    for l in integer_lists:
        if len(l) == 2 and l[0] > l[1]:
            new_l = [l[1], l[0]]
            new_list.append(new_l)
        else:
            l = l
            new_list.append(l)
    return new_list

# Part 4
# add 2 prices
# input: 2 prices
# output: sum of the input prices
def add_prices(price1:data.Price, price2:data.Price) -> data.Price:
    sum_dollars = price1.dollars + price2.dollars
    sum_cents = price1.cents + price2.cents
    if sum_cents >= 100:
        sum_cents = price1.cents + price2.cents - 100
        sum_dollars = price1.dollars + price2.dollars + 1
    sum_prices = data.Price(sum_dollars, sum_cents)
    return sum_prices

# Part 5
# return the area of a rectangle
# input: a rectangle
# output: area of the provided rectangle
def rectangle_area(rectangle:data.Rectangle) -> float:
    width = abs(rectangle.bottom_right.x - rectangle.top_left.x)
    height = abs(rectangle.bottom_right.y - rectangle.top_left.y)
    area = width * height
    return area

# Part 6
# find books from a list of books written by an author
# input: an intended author name and a list of Books
# output: a list of books from the input list of books written by the author specified
def books_by_author(author_name:str, book_list:list[data.Book]) -> list[data.Book]:
    books_by_author_list = []
    for book in book_list:
        if author_name in book.authors:
            books_by_author_list.append(book)
    return books_by_author_list

# Part 7
# find a bounding circle for a given rectangle
# input: a rectangle
# output: a bounding circle for the provided rectangle
def circle_bound(rectangle:data.Rectangle) -> data.Circle:
    width = abs(rectangle.bottom_right.x - rectangle.top_left.x)
    height = abs(rectangle.bottom_right.y - rectangle.top_left.y)
    if width > height:
        radius = width / 2
        center_x = rectangle.top_left.x + radius
        center_y = rectangle.bottom_right.y + height / 2
    else:
        radius = height / 2
        center_x = rectangle.top_left.x + width / 2
        center_y = rectangle.bottom_right.y + radius
    return data.Circle(data.Point(center_x, center_y), radius)

# Part 8
# find the names of employees that are being paid less than the average pay from a given list of employees
# input: a list of Employees
# output: a list of the names of employees that are being paid less than the average pay of the employees in the
# input list
def below_pay_average(employee_list:list[data.Employee]) -> list[str]:
    pay_total = 0
    below_pay_average_list = []
    for employee in employee_list:
        pay_total = pay_total + employee.pay_rate
    pay_average = pay_total / len(employee_list)
    for employee in employee_list:
        if employee.pay_rate < pay_average:
            below_pay_average_list.append(employee.name)
    return below_pay_average_list

