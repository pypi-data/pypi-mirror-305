from .core import BaseComponent
from .core import ValueReceiverBaseComponent

from .button_component import Button


def test_is_receiver_subclass():
    assert issubclass(Button, ValueReceiverBaseComponent)


def test_is_concrete():
    Button("id")


def test_gets_registered():
    cid = "id"
    c = Button(cid)
    assert BaseComponent.registry.get(cid) == c


def test_callback(mocker):
    mock = mocker.Mock()

    def fn():
        mock()

    c = Button("id")
    c.add_callback(fn)

    c.receive_value(None)
    mock.assert_called_once_with()
