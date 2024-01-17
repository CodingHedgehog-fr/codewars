from unittest import TestCase
from katas.Kyu_3 import (expand)


class TestKyu3(TestCase):
    """TestKyu3 class aims at unit testing Kyu_3.py module"""

    def test_expand(self):

        self.assertEqual(expand("(x+1)^0"), "1")
        self.assertEqual(expand("(x+1)^1"), "x+1")
        self.assertEqual(expand("(x+1)^2"), "x^2+2x+1")

        self.assertEqual(expand("(x-1)^0"), "1")
        self.assertEqual(expand("(x-1)^1"), "x-1")
        self.assertEqual(expand("(x-1)^2"), "x^2-2x+1")
        self.assertEqual(expand("(-x-1)^2"), "x^2+2x+1")

        self.assertEqual(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
        self.assertEqual(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
        self.assertEqual(expand("(7x-7)^0"), "1")

        self.assertEqual(expand("(-5m+3)^4"), "625m^4-1500m^3+1350m^2-540m+81")
        self.assertEqual(expand("(-2k-3)^3"), "-8k^3-36k^2-54k-27")
        self.assertEqual(expand("(-7x-7)^0"), "1")

        self.assertEqual(expand("(p-1)^3"), "p^3-3p^2+3p-1")
        self.assertEqual(expand("(2f+4)^6"), "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096")
        self.assertEqual(expand("(-2a-4)^0"), "1")
        self.assertEqual(expand("(-12t+43)^2"), "144t^2-1032t+1849")
        self.assertEqual(expand("(-r+0)^203"), "-r^203")

        self.assertEqual(expand("(P-1)^3"), "P^3-3P^2+3P-1")
        self.assertEqual(expand("(2F+4)^6"), "64F^6+768F^5+3840F^4+10240F^3+15360F^2+12288F+4096")
        self.assertEqual(expand("(-12T+43)^2"), "144T^2-1032T+1849")
        self.assertEqual(expand("(R+0)^203"), "R^203")
