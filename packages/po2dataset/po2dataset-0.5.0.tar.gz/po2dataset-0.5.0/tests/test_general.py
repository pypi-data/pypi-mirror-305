import unittest
import os
import shutil
import json
from po2dataset.po2dataset import (
    create_workdir,
    create_dataset,
    create_metadata,
    add_readme,
)


TEST_BASE_PATH = ""
source_data_lines = ["Hellow World!\n", "This is a test po file\n"]
target_data_lines = ["Kaixo Mundua!\n", "Hau testerako po fitxategia da\n"]
all_source_data_lines = [
    "Hellow World!\n",
    "This is a test po file\n",
    "Lets see if we can detect the %@ placeholder\n",
    "Lets see if we can detect the %s placeholder\n",
    "Lets see if we can detect the %d placeholder\n",
    "Lets see if we can detect the %number% placeholder\n",
    "Lets see if we can detect the %(amount) placeholder\n",
    "Lets see if we can detect the %{amount} placeholder\n",
    "Lets see if we can detect the {amount} placeholder\n",
    "Lets see if we can detect the {{amount}} placeholder\n",
]
all_target_data_lines = [
    "Kaixo Mundua!\n",
    "Hau testerako po fitxategia da\n",
    "Ikus dezagun %@ aldagaia detekta dezakegun\n",
    "Ikus dezagun %s aldagaia detekta dezakegun\n",
    "Ikus dezagun %d aldagaia detekta dezakegun\n",
    "Ikus dezagun %number% aldagaia detekta dezakegun\n",
    "Ikus dezagun %(amount) aldagaia detekta dezakegun\n",
    "Ikus dezagun %{amount} aldagaia detekta dezakegun\n",
    "Ikus dezagun {amount} aldagaia detekta dezakegun\n",
    "Ikus dezagun {{amount}} aldagaia detekta dezakegun\n",
]
removed_source_data_lines = [
    "Hellow World!\n",
    "This is a test po file\n",
    "Lets see if we can detect the placeholder\n",
    "Lets see if we can detect the placeholder\n",
    "Lets see if we can detect the placeholder\n",
    "Lets see if we can detect the placeholder\n",
    "Lets see if we can detect the placeholder\n",
    "Lets see if we can detect the placeholder\n",
    "Lets see if we can detect the placeholder\n",
    "Lets see if we can detect the placeholder\n",
]
removed_target_data_lines = [
    "Kaixo Mundua!\n",
    "Hau testerako po fitxategia da\n",
    "Ikus dezagun aldagaia detekta dezakegun\n",
    "Ikus dezagun aldagaia detekta dezakegun\n",
    "Ikus dezagun aldagaia detekta dezakegun\n",
    "Ikus dezagun aldagaia detekta dezakegun\n",
    "Ikus dezagun aldagaia detekta dezakegun\n",
    "Ikus dezagun aldagaia detekta dezakegun\n",
    "Ikus dezagun aldagaia detekta dezakegun\n",
    "Ikus dezagun aldagaia detekta dezakegun\n",
]
TEST_DATA = {
    "name": "test",
    "source_code": "en",
    "target_code": "eu",
    "ref": "Some ref here",
    "po_file_path": "./tests/data/test_data.po",
    "readme_path": "./tests/data/README.md",
    "size": 2,
}
TEST_META = {
    "name": TEST_DATA["name"],
    "type": "data",
    "from_code": TEST_DATA["source_code"],
    "to_code": TEST_DATA["target_code"],
    "size": TEST_DATA["size"],
    "reference": TEST_DATA["ref"],
}


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.path = None

    def tearDown(self):
        if self.path:
            shutil.rmtree(self.path)

    def assertPathExists(self, path):
        if not os.path.exists(path):
            raise AssertionError("Path does not exist: %s" % str(path))

    def test_workdir(self):
        self.path = create_workdir(
            TEST_BASE_PATH,
            TEST_DATA["name"],
            TEST_DATA["source_code"],
            TEST_DATA["target_code"],
        )
        self.assertPathExists(self.path)

    def test_dataset(self):
        self.path = create_workdir(
            TEST_BASE_PATH,
            TEST_DATA["name"],
            TEST_DATA["source_code"],
            TEST_DATA["target_code"],
        )
        string_count = create_dataset(TEST_DATA["po_file_path"], self.path)
        self.assertPathExists(self.path + "/source")
        self.assertPathExists(self.path + "/target")
        with open(self.path + "/source", "r") as source:
            for i, line in enumerate(source):
                self.assertEqual(line, source_data_lines[i])
        with open(self.path + "/target", "r") as target:
            for i, line in enumerate(target):
                self.assertEqual(line, target_data_lines[i])
        self.assertEqual(string_count, 2)

    def test_dataset_do_nothing(self):
        self.path = create_workdir(
            TEST_BASE_PATH,
            TEST_DATA["name"],
            TEST_DATA["source_code"],
            TEST_DATA["target_code"],
        )
        string_count = create_dataset(
            TEST_DATA["po_file_path"], self.path, ph_policy="do_nothing"
        )
        with open(self.path + "/source", "r") as source:
            for i, line in enumerate(source):
                self.assertEqual(line, all_source_data_lines[i])
        with open(self.path + "/target", "r") as target:
            for i, line in enumerate(target):
                self.assertEqual(line, all_target_data_lines[i])
        self.assertEqual(string_count, 10)

    def test_dataset_remove(self):
        self.path = create_workdir(
            TEST_BASE_PATH,
            TEST_DATA["name"],
            TEST_DATA["source_code"],
            TEST_DATA["target_code"],
        )
        string_count = create_dataset(
            TEST_DATA["po_file_path"], self.path, ph_policy="remove"
        )
        with open(self.path + "/source", "r") as source:
            for i, line in enumerate(source):
                self.assertEqual(line, removed_source_data_lines[i])
        with open(self.path + "/target", "r") as target:
            for i, line in enumerate(target):
                self.assertEqual(line, removed_target_data_lines[i])
        self.assertEqual(string_count, 10)

    def test_metadata(self):
        self.path = create_workdir(
            TEST_BASE_PATH,
            TEST_DATA["name"],
            TEST_DATA["source_code"],
            TEST_DATA["target_code"],
        )
        string_count = create_dataset(TEST_DATA["po_file_path"], self.path)
        create_metadata(
            self.path,
            TEST_DATA["name"],
            TEST_DATA["source_code"],
            TEST_DATA["target_code"],
            TEST_DATA["ref"],
            string_count,
        )
        self.assertPathExists(self.path + "/metadata.json")
        with open(self.path + "/metadata.json", "r") as meta_file:
            self.assertEqual(json.loads(meta_file.read()), TEST_META)

    def test_readme(self):
        self.path = create_workdir(
            TEST_BASE_PATH,
            TEST_DATA["name"],
            TEST_DATA["source_code"],
            TEST_DATA["target_code"],
        )
        add_readme(self.path, TEST_DATA["readme_path"])
        self.assertPathExists(self.path + "/README.md")
        with open(self.path + "/README.md", "r") as readme_file:
            self.assertEqual(readme_file.read(), "# THIS IS A TEST README FILE\n")
