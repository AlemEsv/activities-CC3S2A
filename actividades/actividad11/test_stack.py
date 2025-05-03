from unittest import TestCase
from stack import Stack


class TestStack(TestCase):
    """Casos de prueba para la Pila"""

    def setUp(self) -> None:
        """Configuración antes de cada prueba."""
        self.stack = Stack()

    def tearDown(self) -> None:
        """Limpieza después de cada prueba."""
        self.stack = None

    def test_push(self):
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)


    def test_pop(self):
        """Prueba de eliminar un elemento de la pila."""
        self.stack.push(3)
        self.stack.push(5)
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.peek(), 3)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())   

    def test_peek(self):
        """Prueba de observar el elemento superior de la pila."""
        self.stack.push(3)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)

    def test_is_empty(self):
        """Prueba de si la pila está vacía."""
        stack = Stack()
        assert stack.is_empty() == True
        stack.push(5)
        assert stack.is_empty() == False

