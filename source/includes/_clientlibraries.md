# Client Libraries
To simplify authorization and access to the PokitDok API, we provide client
libraries for a number of programming languages. These libraries offer full
access to the PokitDok API with minimal code, usually just a few lines.
These libraries are hosted on
[PokitDok's Github repo](https://github.com/pokitdok).

| Fully Supported Languages | &nbsp;                                                           |
|:--------------------|:-----------------------------------------------------------------|
| Python              | [pokitdok-python](https://github.com/pokitdok/pokitdok-python)   |
| Ruby                | [pokitdok-ruby](https://github.com/pokitdok/pokitdok-ruby)       |
| Java                | [pokitdok-java](https://github.com/pokitdok/pokitdok-java)       |
| C#                  | [pokitdok-csharp](https://github.com/pokitdok/pokitdok-csharp)   |

| Available languages | &nbsp;                                                           |
|:--------------------|:-----------------------------------------------------------------|
| PHP                 | [pokitdok-php](https://github.com/pokitdok/pokitdok-php)         |
| NodeJS              | [pokitdok-nodejs](https://github.com/pokitdok/pokitdok-nodejs)   |
| Swift               | [pokitdok-swift](https://github.com/pokitdok/pokitdok-swift)     |
| Salesforce Apex     | [pokitdok-apex](https://github.com/pokitdok/pokitdok-apex)       |

The following sections go into further detail on the underlying details of
connecting directly to the PokitDok API. This is of use if you're implementing
the APIs in a programming language for which we currently don't have a client
library.


## Installation

Please see each client's GitHub page for installation instructions from each language's specific distribution. For example, installing the Python Client via PyPi using pip:

```shell
$ pip install pokitdok
```

Then, creating an eligibility request and storing the response with Python:

```shell
import pokitdok
pd = pokitdok.api.connect('<your client id>', '<your client secret>')
# submit an eligibility request
response = pd.eligibility({
    "member": {
        "birth_date": "1970-01-01",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

Each client's GitHub page has language specific Quick Start guides. Check them out for more details.