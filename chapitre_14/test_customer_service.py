from datetime import datetime
from unittest.mock import Mock, patch

import pytest

from customer_service import Customer, CustomerNotFound, CustomerService, salutation


# --- 1. Mock injecté : on remplace les dépendances passées au constructeur ---

def test_welcome_envoie_un_mail():

    # Arrange
    dao = Mock()
    dao.find_by_id.return_value = Customer(1, "Fred", "fred@mail.com")  # réponse simulée
    mailer = Mock()
    service = CustomerService(dao, mailer)

    # Act
    r = service.welcome(1)

    # Assert : le résultat...
    assert r is True
    # ... et les interactions avec les mocks
    dao.find_by_id.assert_called_once_with(1)
    mailer.send.assert_called_once()
    assert mailer.send.call_args.kwargs["to"] == "fred@mail.com"


def test_welcome_client_inconnu():

    # Arrange
    dao = Mock()
    dao.find_by_id.return_value = None
    mailer = Mock()
    service = CustomerService(dao, mailer)

    # Act / Assert
    with pytest.raises(CustomerNotFound):
        service.welcome(99)
    mailer.send.assert_not_called()          # aucun mail si le client n'existe pas


def test_welcome_base_indisponible():

    # Arrange : side_effect permet de simuler une exception
    dao = Mock()
    dao.find_by_id.side_effect = ConnectionError("base injoignable")
    service = CustomerService(dao, Mock())

    # Act / Assert
    with pytest.raises(ConnectionError):
        service.welcome(1)


# --- 2. patch : on remplace un objet utilisé À L'INTÉRIEUR du module ---------
# Règle : on patche là où l'objet est UTILISÉ ("customer_service.datetime"),
# pas là où il est défini ("datetime.datetime").

@patch("customer_service.datetime")
def test_salutation_le_matin(mock_datetime):

    # Arrange
    mock_datetime.now.return_value = datetime(2026, 11, 27, 9, 0)

    # Act
    r = salutation()

    # Assert
    assert r == "Bonjour"


def test_salutation_le_soir():

    # Arrange : patch peut aussi s'utiliser avec "with"
    with patch("customer_service.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2026, 11, 27, 20, 0)

        # Act
        r = salutation()

    # Assert
    assert r == "Bonsoir"





