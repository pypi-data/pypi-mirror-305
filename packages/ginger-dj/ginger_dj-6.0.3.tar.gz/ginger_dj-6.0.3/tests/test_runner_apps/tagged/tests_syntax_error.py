from unittest import TestCase

from gingerdj.test import tag


@tag('syntax_error')
class SyntaxErrorTestCase(TestCase):
    pass


1syntax_error  # NOQA
