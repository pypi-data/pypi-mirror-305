"""This module contains tests to test the signal processing utilities."""

import unittest
import logging
from scipy.io import wavfile
import numpy as np
from brainwire import encode

# Importing local version of "process_signal" file
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader

spec = spec_from_loader(
    "process_signal",
    SourceFileLoader(
        "process_signal", "./signal_processing_utilities/process_signal.py"
    ),
)
process_signal = module_from_spec(spec)
spec.loader.exec_module(process_signal)

logging.basicConfig(level=logging.DEBUG)


class TestProcessSignal(unittest.TestCase):
    """This class is used to define tests to test the process signal module.

    Args:
        unittest (module): This is the module that enables unittests.
    """

    def setUp(self):
        self.file_path = "tests/test_data/0ab237b7-fb12-4687-afed-8d1e2070d621.wav"

    def tearDown(self):
        pass

    def test01_compare_for_equality(self):
        logging.info("test01: This is a test to ensure testing is operational. ")
        test_passes = True
        self.assertTrue(test_passes)
        if test_passes:
            print("Test Passes")

    def test02_compare_for_equality_in_length(self):
        logging.info(
            "test02: This is a test to ensure that the byte strings are of "
            + "equal length. The lengths are unequal and the return value "
            + "is intended to be 'False'."
        )
        byte_string1 = b"010101010001"
        byte_string2 = b"100101011001101"
        self.assertEqual(
            process_signal.compare_for_equality(byte_string1, byte_string2), False
        )

    def test03_compare_for_equality_in_value(self):
        logging.info(
            "test03: This is a test to ensure that the byte strings are of "
            + "equal value. The values are unequal and the return value "
            + "is intended to be 'False'."
        )
        byte_string1 = b"010101010001"
        byte_string2 = b"100101011001"
        self.assertEqual(
            process_signal.compare_for_equality(byte_string1, byte_string2), False
        )

    def test04_compare_for_equality_in_type(self):
        logging.info(
            "test04: This is a test to ensure that the byte strings are of "
            + "equal type. The types are unequal and the return value "
            + "is intended to be 'False'."
        )
        byte_string1 = "010101010001"
        byte_string2 = b"100101011001"
        self.assertEqual(
            process_signal.compare_for_equality(byte_string1, byte_string2), False
        )

    def test05_test_signal_processing_utilities_print_file_size(self):
        logging.info(
            "test05: This is a test to ensure that "
            + "signal_processing_utilities has been locally"
            + "imported and is readily available for use."
        )
        process_signal.print_file_size(file_path=self.file_path)

    def test06_process_neural_spikes(self):
        logging.info(
            "test06: This is a test to ensure that the spikes of the "
            + "raw neural data may be processed & that the data may be "
            + "processed in a timely manner. "
        )

        _, data = wavfile.read(self.file_path)
        spike_train_time_index_list = process_signal.detect_neural_spikes(
            neural_data=data, single_spike_detection=False, real_time=True
        )
        self.assertEqual(type(spike_train_time_index_list), list)

    def test07_compare_compression_ratio(self):
        logging.info(
            "test07: This is a test to ensure that the compression "
            + "ratio is appropriately compared."
        )
        _, original_data = wavfile.read(self.file_path)
        byte_string = encode.compress(file=self.file_path)
        process_signal.compare_compression_ratio(
            original_data=original_data,
            compressed_data=byte_string,
            method="brainwire.encode.compress(file=self.file_path)",
        )


if __name__ == "__main__":
    unittest.main()
