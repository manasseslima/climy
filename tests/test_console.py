from climy.console import ctable, cprogress

def test_print_table():


    columns = ['ID:10>', 'Name:0', 'Birth:15^', 'Weight:10>', 'Hight:10>', 'Gender:10^']
    data = [
        (1, 'Mark White', '26/12/1977', 1.75, 80.0, 'Male'),
        (2, 'Eva Wood', '30/11/1983', 1.59, 50.0, 'Female'),
        (3, 'John Apple', '26/06/1917', 1.20, 30.0, 'Male'),
        (4, 'Linda Jansen', '09/05/1961', 1.63, 61.0, 'Female')
    ]
    ctable(data, columns=columns)
    assert True


def test_print_progress():
    cprogress(size=50, max=300.0, value=20.0, color='green')
