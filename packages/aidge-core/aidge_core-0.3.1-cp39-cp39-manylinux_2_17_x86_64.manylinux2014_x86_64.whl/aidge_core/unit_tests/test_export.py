"""
Copyright (c) 2023 CEA-List

This program and the accompanying materials are made available under the
terms of the Eclipse Public License 2.0 which is available at
http://www.eclipse.org/legal/epl-2.0.

SPDX-License-Identifier: EPL-2.0
"""

import aidge_core
from aidge_core.utils import run_command
import unittest
import os
import pathlib
import shutil
import subprocess
import sys


def initFiller(model):
    # Initialize parameters (weights and biases)
    for node in model.get_nodes():
        if node.type() == "Producer":
            prod_op = node.get_operator()
            value = prod_op.get_output(0)
            value.set_backend("cpu")
            tuple_out = node.output(0)[0]
            # No conv in current network
            if tuple_out[0].type() == "Conv" and tuple_out[1] == 1:
                # Conv weight
                aidge_core.xavier_uniform_filler(value)
            elif tuple_out[0].type() == "Conv" and tuple_out[1] == 2:
                # Conv bias
                aidge_core.constant_filler(value, 0.01)
            elif tuple_out[0].type() == "FC" and tuple_out[1] == 1:
                # FC weight
                aidge_core.normal_filler(value)
            elif tuple_out[0].type() == "FC" and tuple_out[1] == 2:
                # FC bias
                aidge_core.constant_filler(value, 0.01)
            else:
                pass


def clean_dir(dir: pathlib.Path) -> None:
    if not dir.is_dir():
        print(f"Error : directory {dir} doesn't exist. Exiting clean_dir().")
        return
    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
    return


class test_export(unittest.TestCase):
    """Test aidge export"""

    def setUp(self):
        self.EXPORT_PATH: pathlib.Path = pathlib.Path("dummy_export")
        self.BUILD_DIR: pathlib.Path = self.EXPORT_PATH / "build"
        self.INSTALL_DIR: pathlib.Path = (self.EXPORT_PATH / "install").absolute()

    def tearDown(self):
        pass

    def test_generate_export(self):
        # Create model

        model = aidge_core.sequential(
            [
                aidge_core.FC(
                    in_channels=32 * 32 * 3, out_channels=512, name="InputNode"
                ),
                aidge_core.ReLU(name="Relu0"),
                aidge_core.FC(in_channels=512, out_channels=256, name="FC1"),
                aidge_core.ReLU(name="Relu1"),
                aidge_core.FC(in_channels=256, out_channels=128, name="FC2"),
                aidge_core.ReLU(name="Relu2"),
                aidge_core.FC(in_channels=128, out_channels=10, name="OutputNode"),
            ]
        )

        initFiller(model)

        # Export model
        aidge_core.export(self.EXPORT_PATH, model)

        self.assertTrue(
            self.EXPORT_PATH.is_dir(), "Export folder has not been generated"
        )
        os.makedirs(self.BUILD_DIR, exist_ok=True)
        clean_dir(self.BUILD_DIR)  # if build dir existed already ensure its emptyness
        clean_dir(self.INSTALL_DIR)

        # Test compilation of export
        search_path = (
            os.path.join(sys.prefix, "lib", "libAidge")
            if "AIDGE_INSTALL" not in os.environ
            else os.environ["AIDGE_INSTALL"]
        )

        shutil.copyfile(
            pathlib.Path(__file__).parent / "static/main.cpp",
            self.EXPORT_PATH / "main.cpp",
        )

        ##########################
        # CMAKE EXPORT
        try:
            for std_line in run_command(
                [
                    "cmake",
                    str(self.EXPORT_PATH.absolute()),
                    "-DPYBIND=ON",
                    f"-DCMAKE_PREFIX_PATH={search_path}", # search dependencies
                    f"-DCMAKE_INSTALL_PREFIX:PATH={self.INSTALL_DIR}", # local install
                ],
                cwd=str(self.BUILD_DIR),
            ):
                print(std_line, end="")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}\nFailed to configure export.")
            raise SystemExit(1)

        ##########################
        # BUILD EXPORT
        try:
            for std_line in run_command(
                ["cmake", "--build", "."],
                cwd=str(self.BUILD_DIR),
            ):
                print(std_line, end="")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}\nFailed to build export.")
            raise SystemExit(1)

        ##########################
        # INSTALL EXPORT
        try:
            for std_line in run_command(
                ["cmake", "--install", "."],
                cwd=str(self.BUILD_DIR),
            ):
                print(std_line, end="")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}\nFailed to install export.")
            raise SystemExit(1)


if __name__ == "__main__":
    unittest.main()
