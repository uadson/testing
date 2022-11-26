from ...game.core import fizz_buzz


def test_if_fizz_buzz_receive_1_then_returns_1():
    """
        3 steps for the tests;
        
        GWT:
        
            - Given
            - When
            - Then
            
        or
        
        AAA:
        
            - Arrange
            - Act
            - Assert
    """
    # given
    input_value = 1
    # given
    expected = 1
    # when
    result = fizz_buzz(input_value)
    # then
    assert result == expected


def test_if_fizz_buzz_receive_2_then_returns_2():
    assert fizz_buzz(2) == 2


def test_if_fizz_buzz_receive_3_then_returns_fizz():
    assert fizz_buzz(3) == 'fizz'
    

def test_if_fizz_buzz_receive_5_then_returns_buzz():
    assert fizz_buzz(5) == 'buzz'
    

def test_if_fizz_buzz_receive_n_and_the_module_of_n_for_3_and_5_equal_0_then_returns_fizz_buzz():
    assert fizz_buzz(30) == 'fizz buzz'  