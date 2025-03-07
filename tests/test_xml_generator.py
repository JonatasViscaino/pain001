import unittest

from pain001.xml.xml_generator import xml_generator


class TestXmlGenerator(unittest.TestCase):
    def test_xml_generator_with_invalid_input(self):
        # Arrange
        data = {
            "amount": "100.00",
            "currency": "USD",
            "beneficiary_bic": "ABCDE123",
            "beneficiary_iban": "DE8937060198000001234567",
            "creditor_bic": "DEFGH456",
            "creditor_iban": "DE893706019800000234567",
        }
        mapping = {
            "amount": "Amount",
            "currency": "Currency",
            "beneficiary_bic": "BeneficiaryBIC",
            "beneficiary_iban": "BeneficiaryIBAN",
            "creditor_bic": "CreditorBIC",
            "creditor_iban": "CreditorIBAN",
        }
        payment_initiation_message_type = "invalid_message_type"
        xml_file_path = "test.xml"
        xsd_file_path = "schema.xsd"

        # Act
        with self.assertRaises(SystemExit):
            xml_generator(
                data,
                mapping,
                payment_initiation_message_type,
                xml_file_path,
                xsd_file_path,
            )

        # Assert
        # self.assertEqual(sys.exitcode, 1)


if __name__ == "__main__":
    unittest.main()
