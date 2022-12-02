import unittest

import json

from wrappers.blast_output2.BlastOutput2Wrapper import BlastOutput2Wrapper


examples_directory_path = 'wrappers/blast_output2/example_blast_output2s/'

with open(examples_directory_path + 'unkeyed.json', 'r') as f:
    unkeyed = json.loads(f.read())

with open(examples_directory_path + 'keyed.json', 'r') as f:
    keyed = json.loads(f.read())


class TestBlastOutput2Property(unittest.TestCase):
    def test_unkeyed(self):
        blast_output2 = BlastOutput2Wrapper(unkeyed)
        self.assertIs(blast_output2.blast_output2, unkeyed)

    def test_keyed(self):
        blast_output2 = BlastOutput2Wrapper(keyed)
        self.assertIs(blast_output2.blast_output2, keyed['BlastOutput2'])
