import unittest
import os

# Interested only that the software is present. Version isn't important.
def version_output(input):
    cmd = '{0} --version'.format(input)
    string = os.popen(cmd).read().strip()
    return string.join(string.split(' ')[0:1])

# alternative for when output of -version command doesn't exist or is problematic
def which_output(input):
    cmd = 'which {0}'.format(input)
    return os.popen(cmd).read().strip()

# If any test fails the build fails due to an exit code unittest provides.
class TestVersions(unittest.TestCase):

    def test_bash(self):
        self.assertEqual(version_output('bash'), "GNU")

    def test_Fluxbox(self):
        self.assertEqual(version_output('fluxbox'), "Fluxbox")

    def test_GCC_Path(self):
        self.assertEqual(which_output('gcc'), "/usr/bin/gcc")

    def test_Git(self):
        self.assertEqual(version_output('git'), "git")

    def test_Make(self):
        self.assertEqual(version_output('make'), "GNU")

    def test_Nano(self):
        self.assertEqual(version_output('nano'), "GNU")

    def test_Python3(self):
        self.assertEqual(version_output('python3'), "Python")

    def test_Supervisord(self):
        self.assertEqual(version_output('supervisord'), "4.1.0")

    def test_Unzip(self):
        self.assertEqual(which_output('unzip'), "/usr/bin/unzip")

    def test_Wget(self):
        self.assertEqual(version_output("make"), "GNU")

    def test_Xterm(self):
        cmd = 'xterm -version'
        string = os.popen(cmd).read().strip()
        string.join(string.split(' ')[0:1])
        self.assertTrue(string.startswith("XTerm"))

    def test_Xvnc(self):
        self.assertEqual(version_output('x11vnc'), "x11vnc:")

if __name__ == '__main__':
    unittest.main()