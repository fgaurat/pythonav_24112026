from hello import bonjour

def test_hello_default():
    # Arrange
    expected = "Bonjour"
    
    # Act
    r = bonjour()
    
    # Assert
    assert r == expected


def test_bonjour_avec_nom():

    # Arrange
    name = "Fred"
    expected = "Bonjour Fred"

    # Act
    r = bonjour(name)

    # assert
    assert r == expected    