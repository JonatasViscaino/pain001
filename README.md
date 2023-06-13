# Pain001: Automate ISO 20022-Compliant Payment File Creation

![Pain001 banner][banner]

[![PyPI][pypi-badge]][3] [![License][license-badge]][1]
[![Codecov][codecov-badge]][6]

**Pain001** is a powerful Python library that enables you to create ISO 20022-
compliant payment files directly from CSV or SQLite Data Files.

## Overview

Today, the payment industry is experiencing a rapid evolution and
transformation as it moves towards adopting **[ISO 20022][1]** as the new norm.
ISO 20022 is a global standard for sharing financial information across
organisations. It provides a harmonised protocol used by banks, corporations,
and financial institutions to automate and standardise payment transactions.

Here are some of the benefits of using ISO 20022:

- **Improved data quality**: ISO 20022 messages are more structured and
  detailed than traditional payment messages, reducing errors and improving
  efficiency.
- **Increased transparency**: ISO 20022 messages provide more information
  about the payment transaction, which can help to improve the visibility and
  traceability of payments.
- **Enhanced compliance**: ISO 20022 messages can help organisations follow
  AML/CFT and PSD2 regulations.

Overall, ISO 20022 is a significant improvement over traditional payment
messaging standards. It provides a more efficient, transparent, and compliant
way to process payments.

## Pain001 in action

The Python library **Pain001** focuses specifically on payment initiation and
advice messages, commonly known as **pain**. Payments usually start with a
**pain.001 payment initiation message**. The payer sends it to the payee (or
the payee's bank) via a secure network. This network could be **SWIFT** or
**SEPA (Single Euro Payments Area)** network, or other payment networks such
as **CHAPS**, **BACS**, **Faster Payments**, etc. The message contains the
payer's and payee's bank account details, payment amount, and other information
required to process the payment.

**Pain001** can reduce payment processing complexity and costs by generating
ISO 20022-compliant payment files. These files automatically remove the need to
create and validate them manually, making the payment process more efficient
and cost-effective. It will save you time and resources and minimises the risk
of errors, making sure accurate and seamless payment processing.

If you are seeking to simplify and automate your payment processing, consider
leveraging the capabilities of **Pain001**.

## Installation

It takes just a few seconds to get up and running with **Pain001**. Open your
terminal and run the following command:

```sh
pip install pain001
```

## Usage

After installation, you can run **Pain001** directly from the command line.
Simply call the main function with the path of your XML template file, XSD
schema file and the path of your CSV file containing the payment data.

Once you have installed **Pain001**, you can generate and validate XML files
using the following command:

```sh
python3 -m pain001 \
    <xml_message_type> \
    <xml_file_path> \
    <xsd_file_path> \
    <data_file_path> \
    <output_file_path>
```

## Arguments

When running **Pain001**, you will need to specify four arguments:

- `xml_message_type`: This is the type of XML message you want to generate.
  Currently, the valid options are:
  - pain.001.001.03
  - pain.001.001.09
- `xml_file_path`: This is the path to the XML template file you are using.
- `xsd_file_path`: This is the path to the XSD template file you are using.
- `csv_file_path`: This is the path to the CSV data file you want to convert
  to XML.
- `output_file_path`: This is the path to the output XML file you want to save
  the generated XML file to.

## Examples

Here are a few example on how to use **Pain001** to generate a
pain.001.001.03 XML file from a CSV data file:

### Via the Command Line

```sh
python3 -m pain001 \
    pain.001.001.03 \
    /path/to/your/pain.001.001.03.xml \
    /path/to/your/pain.001.001.03.xsd \
    /path/to/your/pain.001.001.03.csv \
    /path/to/your/output.xml
```

**Note:** The XML file that **Pain001** generates will be automatically
validated against the XSD template file before the new XML file is saved. If
the validation fails, **Pain001** will stop running and display an error
message in your terminal.

### Embedded in an Application

To embed **Pain001** in a new or existing application, import the main function
and use it in your code.

Here's an example:

```python
from pain001 import main

if __name__ == '__main__':
  xml_message_type = 'pain.001.001.03'
  xml_file_path = 'template.xml'
  xsd_file_path = 'schema.xsd'
  csv_file_path = 'data.csv'
  main(xml_message_type, xml_file_path, xsd_file_path, csv_file_path)
```

### Validation

To validate the generated XML file against a given xsd schema, use the
following method:

```python
from pain001.core import validate_xml_against_xsd

xml_message_type = 'pain.001.001.03'
xml_file = 'generated.xml'
xsd_file = 'schema.xsd'

is_valid = validate_xml_against_xsd(
  xml_message_type,
  xml_file,
  xsd_file
)
print(f"XML validation result: {is_valid}")
```

## Documentation 📖

> ℹ️ **Info:** Do check out our [website][0] for more information.

### Payment Messages

The following **ISO 20022 Payment Initiation message types** are
currently supported:

- **pain.001.001.03** - Customer Credit Transfer Initiation

This message is used to transmit credit transfer instructions from the
originator (the party initiating the payment) to the originator's bank. The
message supports both bulk and single payment instructions, allowing for the
transmission of multiple payments in a batch or individual payments separately.
The pain.001.001.03 message format is part of the ISO 20022 standard and is
commonly used for SEPA Credit Transfers within the Single Euro Payments Area.
It includes relevant information such as the originator's and beneficiary's
details, payment amounts, payment references, and other transaction-related
information required for processing the credit transfers.

- **pain.001.001.09** - Customer Credit Transfer Initiation

This message format is part of the ISO 20022 standard and is commonly used for
SEPA Credit Transfers within the Single Euro Payments Area. It enables the
transmission of credit transfer instructions from the originator to the
originator's bank. The message includes essential information such as the
originator's and beneficiary's details, payment amounts, payment references,
and other transaction-related information required for processing the credit
transfers.

More message types will be added in the future. Please refer to the section
below for more details.

### Supported messages

This section gives access to the documentation related to the ISO 20022
message definitions supported by **Pain001**.

#### Bank-to-Customer Cash Management

Set of messages used to request and provide account information for
reconciliation and cash positioning between an account servicer and its
customer.

| Status | Message type | Name |
|---|---|---|
| ⏳ | [camt.052.001.10] | Bank-to-Customer Account Statement |
| ⏳ | [camt.060.001.10] | Customer Account Notification |
| ⏳ | [camt.054.001.10] | Customer Account Statement Request |
| ⏳ | [camt.053.001.10] | Customer Account Identification |

#### Payments Clearing and Settlement

Set of messages used between financial institutions for the clearing and
settlement of payment transactions.

| Status | Message type | Name |
|---|---|---|
| ⏳ | [pacs.002.001.12] | Credit Transfer Notification |
| ⏳ | [pacs.003.001.09] | Direct Debit Initiation |
| ⏳ | [pacs.004.001.11] | Direct Debit Reversal |
| ⏳ | [pacs.007.001.11] | Customer Direct Debit Confirmation |
| ⏳ | [pacs.008.001.10] | Credit Transfer Initiation |
| ⏳ | [pacs.009.001.10] | Credit Transfer Reversal |
| ⏳ | [pacs.010.001.05] | Account Identification |
| ⏳ | [pacs.028.001.05] | Account Statement Request |

#### Payments Initiation

Set of messages exchanged between a debtor (or buyer) and its bank or
between a creditor (or seller) and its bank to initiate, collect, manage
and monitor payments.

| Status | Message type | Name |
|---|---|---|
| ✅ | [pain.001.001.03][pain.001.001.03] | Customer Credit Transfer Initiation |
| ⏳ | [pain.001.001.04][pain.001.001.04] | Customer Direct Debit Initiation |
| ⏳ | [pain.001.001.05][pain.001.001.05] | Customer Direct Debit Reversal |
| ⏳ | [pain.001.001.06][pain.001.001.06] | Customer Credit Transfer Reversal |
| ⏳ | [pain.001.001.07][pain.001.001.07] | Customer Account Notification |
| ⏳ | [pain.001.001.08][pain.001.001.08] | Customer Account Statement |
| ✅ | [pain.001.001.09][pain.001.001.09] | Customer Credit Transfer Initiation |
| ⏳ | [pain.001.001.10][pain.001.001.10] | Customer Account Closure Request |
| ⏳ | [pain.001.001.11][pain.001.001.11] | Customer Account Change Request |

## License 📝

The project is licensed under the terms of both the MIT license and the
Apache License (Version 2.0).

- [Apache License, Version 2.0][1]
- [MIT license][2]

## Contribution 🤝

We welcome contributions to **Pain001**. Please see the
[contributing instructions][4] for more information.

Unless you explicitly state otherwise, any contribution intentionally
submitted for inclusion in the work by you, as defined in the
Apache-2.0 license, shall be dual licensed as above, without any
additional terms or conditions.

## Acknowledgements 💙

We would like to extend a big thank you to all the awesome contributors
of [Pain001][5] for their help and support.

[0]: https://Pain001.co
[1]: https://opensource.org/license/apache-2-0/
[2]: http://opensource.org/licenses/MIT
[3]: https://github.com/sebastienrousseau/pain001
[4]: https://github.com/sebastienrousseau/pain001/blob/main/CONTRIBUTING.md
[5]: https://github.com/sebastienrousseau/pain001/graphs/contributors
[6]: https://codecov.io/github/sebastienrousseau/pain001?branch=main

[camt.052.001.10]: docs/bank-to-customer-cash-management/messages/camt.052.001.10/README.md
[camt.060.001.10]: docs/bank-to-customer-cash-management/messages/camt.053.001.10/README.md
[camt.054.001.10]: docs/bank-to-customer-cash-management/messages/camt.054.001.10/README.md
[camt.053.001.10]: docs/bank-to-customer-cash-management/messages/camt.053.001.10/README.md
[pacs.002.001.12]: docs/payments-clearing-and-settlement/messages/pacs.002.001.12/README.md
[pacs.003.001.09]: docs/payments-clearing-and-settlement/messages/pacs.003.001.09/README.md
[pacs.004.001.11]: docs/payments-clearing-and-settlement/messages/pacs.004.001.11/README.md
[pacs.007.001.11]: docs/payments-clearing-and-settlement/messages/pacs.007.001.11/README.md
[pacs.008.001.10]: docs/payments-clearing-and-settlement/messages/pacs.008.001.10/README.md
[pacs.009.001.10]: docs/payments-clearing-and-settlement/messages/pacs.009.001.10/README.md
[pacs.010.001.05]: docs/payments-clearing-and-settlement/messages/pacs.010.001.05/README.md
[pacs.028.001.05]: docs/payments-clearing-and-settlement/messages/pacs.028.001.05/README.md
[pain.001.001.03]: docs/payments-initiation/messages/pain.001.001.03/README.md
[pain.001.001.04]: docs/payments-initiation/messages/pain.001.001.04/README.md
[pain.001.001.05]: docs/payments-initiation/messages/pain.001.001.05/README.md
[pain.001.001.06]: docs/payments-initiation/messages/pain.001.001.06/README.md
[pain.001.001.07]: docs/payments-initiation/messages/pain.001.001.07/README.md
[pain.001.001.08]: docs/payments-initiation/messages/pain.001.001.08/README.md
[pain.001.001.09]: docs/payments-initiation/messages/pain.001.001.09/README.md
[pain.001.001.10]: docs/payments-initiation/messages/pain.001.001.10/README.md
[pain.001.001.11]: docs/payments-initiation/messages/pain.001.001.11/README.md

[banner]: https://kura.pro/pain001/images/banners/banner-pain001.svg 'Pain001'
[codecov-badge]: https://img.shields.io/codecov/c/github/sebastienrousseau/pain001?style=for-the-badge&token=AaUxKfRiou 'Codecov badge'
[license-badge]: https://img.shields.io/pypi/l/pain001?style=for-the-badge 'License badge'
[pypi-badge]: https://img.shields.io/pypi/pyversions/pain001.svg?style=for-the-badge 'PyPI badge'
