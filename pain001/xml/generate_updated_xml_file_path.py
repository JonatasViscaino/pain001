# Copyright (C) 2023 Sebastien Rousseau.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

# Generate the path to the updated XML file based on the path to the
# original XML file


def generate_updated_xml_file_path(
    xml_file_path,
    payment_initiation_message_type
):
    print(os.path.splitext(xml_file_path)[0])
    base_directory = os.path.dirname(xml_file_path)
    base_name = os.path.basename(xml_file_path)
    file_name, _ = os.path.splitext(base_name)

    new_file_name = payment_initiation_message_type + ".xml"
    new_file_path = os.path.join(base_directory, new_file_name)

    return new_file_path
