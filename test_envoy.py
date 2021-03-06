import unittest
import envoy

from os.path import isdir, exists

class SimpleTest(unittest.TestCase):

    def test_input(self):
        r = envoy.run("sed s/i/I/g", "Hi")
        self.assertEqual(r.std_out.rstrip(), "HI")
        self.assertEqual(r.status_code, 0)

    def test_pipe(self):
        r = envoy.run("echo -n 'hi'| tr [:lower:] [:upper:]")
        self.assertEqual(r.std_out, "HI")
        self.assertEqual(r.status_code, 0)

    def test_timeout(self):
        r = envoy.run('yes | head', timeout=1)
        self.assertEqual(r.std_out, 'y\ny\ny\ny\ny\ny\ny\ny\ny\ny\n')
        self.assertEqual(r.status_code, 0)

    def test_slist(self):
        sl = envoy.run('ls -lF').sl
        for actual in sl.fields(-1):
            if actual[-1] == "*":
                actual = actual[:-1]

            self.assertTrue( exists(actual), "Expected field 8, value [%s] to equal an existing file" % actual)

            if actual[-1] == "/":
                self.assertTrue( isdir(actual ), "Expected field 8, value [%s] to equal an existing directory" % actual )

    def test_slist_index(self):
        filenames = envoy.run('ls -lF')[-1]
        for actual in filenames:
            if actual[-1] == "*":
                actual = actual[:-1]

            self.assertTrue( exists(actual), "Expected field 8, value [%s] to equal an existing file" % actual)

            if actual[-1] == "/":
                self.assertTrue( isdir(actual ), "Expected field 8, value [%s] to equal an existing directory" % actual )

    def test_slist_slice(self):
        #This is somewhat problematic in testing
        #response = envoy.run('ls -lF')
        #for actual in response[5:8]:



if __name__ == "__main__":
    unittest.main()
