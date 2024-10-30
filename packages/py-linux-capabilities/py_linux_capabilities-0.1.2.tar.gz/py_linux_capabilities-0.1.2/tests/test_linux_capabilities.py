import unittest

from context import LinuxCapabilities

class TestLinuxCapabilities(unittest.TestCase):
    def test_enum_members(self):
        self.assertTrue(hasattr(LinuxCapabilities, "CAP_SYS_ADMIN"))
        self.assertEqual(LinuxCapabilities.CAP_SYS_ADMIN.value, "CAP_SYS_ADMIN")

    def test_enum_count(self):
        self.assertEqual(len(LinuxCapabilities), 41)

if __name__ == "__main__":
    unittest.main()

