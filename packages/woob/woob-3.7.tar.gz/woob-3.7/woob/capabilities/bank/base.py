# Copyright(C) 2010-2016 Romain Bignon
#
# This file is part of woob.
#
# woob is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# woob is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with woob. If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

from binascii import crc32
import re
from typing import Iterable, List

from woob.capabilities.account import CapCredentialsCheck
from woob.capabilities.base import (
    BaseObject, Capability, Field, StringField, DecimalField, IntField,
    BoolField, UserError, Currency, NotAvailable, EnumField, Enum, empty,
    find_object, NotLoaded, NotLoadedType, NotAvailableType
)
from woob.capabilities.date import DateField
from woob.capabilities.collection import CapCollection
from woob.exceptions import BrowserIncorrectPassword


__all__ = [
    'CapBank', 'BaseAccount', 'Account', 'Loan', 'Transaction', 'AccountNotFound',
    'AccountType', 'AccountOwnership', 'Balance', 'AccountSchemeName', 'TransactionCounterparty',
    'PartyIdentity', 'AccountParty', 'AccountIdentification', 'PartyRole', 'CapAccountCheck',
    'NoAccountsException', 'BalanceType', 'BankTransactionCode',
]


class NoAccountsException(Exception):
    """
    Raised by :meth:`CapBank.iter_accounts()` if we are sure there is no accounts.

    Sometimes we can't parse find accounts on websites but that's a scraping
    error. To attest we know that's a real case, this exception is raised.
    """


class ObjectNotFound(UserError):
    pass


class AccountNotFound(ObjectNotFound):
    """
    Raised when an account is not found.
    """

    def __init__(self, msg: str = 'Account not found'):
        super().__init__(msg)


class BaseAccount(BaseObject, Currency):
    """
    Generic class aiming to be parent of :class:`Recipient` and
    :class:`Account`.
    """
    label =          StringField('Pretty label')
    currency =       StringField('Currency', default=None)
    bank_name =      StringField('Bank Name', mandatory=False)

    # TODO add iban field here

    def __init__(
        self,
        id: str = '0',
        url: str | NotLoadedType | NotAvailableType = NotLoaded
    ):
        super().__init__(id, url)

    @property
    def currency_text(self) -> str:
        return Currency.currency2txt(self.currency)

    @property
    def ban(self) -> str | NotAvailableType:
        """ Bank Account Number part of IBAN"""
        if not self.iban:
            return NotAvailable
        return self.iban[4:]


class AccountType(Enum):
    UNKNOWN          = 0
    CHECKING         = 1
    "Transaction, everyday transactions"
    SAVINGS          = 2
    "Savings/Deposit, can be used for every banking"
    DEPOSIT          = 3
    "Term of Fixed Deposit, has time/amount constraints"
    LOAN             = 4
    "Loan account"
    MARKET           = 5
    "Stock market or other variable investments"
    JOINT            = 6
    "Joint account"
    CARD             = 7
    "Card account"
    LIFE_INSURANCE   = 8
    "Life insurances"
    PEE              = 9
    "Employee savings PEE"
    PERCO            = 10
    "Employee savings PERCO"
    ARTICLE_83       = 11
    "Article 83"
    RSP              = 12
    "Employee savings RSP"
    PEA              = 13
    "Share savings"
    CAPITALISATION   = 14
    "Life Insurance capitalisation"
    PERP             = 15
    "Retirement savings"
    MADELIN          = 16
    "Complementary retirement savings"
    MORTGAGE         = 17
    "Mortgage"
    CONSUMER_CREDIT  = 18
    "Consumer credit"
    REVOLVING_CREDIT = 19
    "Revolving credit"
    PER = 20
    "Pension plan PER"
    REAL_ESTATE = 21
    "Real estate investment such as SCPI, OPCI, SCI"
    CROWDLENDING = 22
    "Crowdlending accounts"
    LDDS = 23
    "LDD/LDDS Livret de développement durable et solidaire"
    PEL = 24
    "Plan épargne logement"
    CSL = 25
    "Compte sur Livret"
    CEL = 26
    "Compte épargne logement"
    CAT = 27
    "Compte à terme"
    LIVRET_A = 28
    "Livret A"
    LIVRET_B = 29
    "Livret B"


class AccountOwnerType:
    """
    Specifies the usage of the account
    """
    PRIVATE = 'PRIV'
    """private personal account"""
    ORGANIZATION = 'ORGA'
    """professional account"""
    ASSOCIATION = 'ASSO'
    """association account"""


class AccountOwnership:
    """
    Relationship between the credentials owner (PSU) and the account
    """
    OWNER = 'owner'
    """The PSU is the account owner"""
    CO_OWNER = 'co-owner'
    """The PSU is the account co-owner"""
    ATTORNEY = 'attorney'
    """The PSU is the account attorney"""


class AccountSchemeName(Enum):
    IBAN = 'iban'
    """IBAN as defined in ISO 13616"""

    BBAN = 'bban'
    """Basic Bank Account Number, represents a country-specific bank account number"""

    SORT_CODE_ACCOUNT_NUMBER = 'sort_code_account_number'
    """Account Identification Number sometimes employed instead of IBAN (e.g.: in UK)"""

    CPAN = 'cpan'
    """Card PAN (masked or plain)"""

    TPAN = 'tpan'
    """Tokenized card PAN issued by a Token Service Provider to obfuscate the real PAN"""

    MPAN = 'mpan'
    """Card PAN where some digits were replaced for security reason"""

    BANK_PARTY_IDENTIFICATION = 'bank_party_identification'
    """
    BankPartyIdentification - Unique and unambiguous assignment made by a specific bank or
    similar financial institution to identify a relationship between the bank and its client.

    Its definition can be found at page 13 of https://www.stet.eu/assets/files/PSD2/1-6-3/api-dsp2-stet-v1.6.3.1-part-2-functional-model.pdf
    """


class AccountManagementType(Enum):
    UNKNOWN = 'unknown'
    CAPITALIZATION = 'capitalization'
    FIXED_FUNDS = 'fixed_funds'
    PROFILED = 'profiled'
    DISCRETIONARY = 'discretionary'
    DELEGATED = 'delegated'
    UNIT_LINKED = 'unit_linked'


class TransactionCounterparty(BaseObject):
    label = StringField('Name of the other stakeholder (Creditor or debtor)', default=None)
    account_scheme_name = EnumField('Type of account Scheme', AccountSchemeName, default=None)
    account_identification = StringField('ID of the account', default=None)
    debtor = BoolField('Type of the counterparty (debtor/creditor/null)', default=None)

    def __repr__(self):
        return f'<label={self.label} debtor={self.debtor} account_scheme_name={self.account_scheme_name} account_identification={self.account_identification}>'


class PartyRole(Enum):
    UNKNOWN = 'unknown'
    HOLDER = 'holder'
    CO_HOLDER = 'co_holder'
    ATTORNEY = 'attorney'
    CUSTODIAN_FOR_MINOR = 'custodian_for_minor'
    LEGAL_GUARDIAN = 'legal_guardian'
    NOMINEE = 'nominee'
    BENEFICIARY = 'beneficiary'
    SUCCESSOR_ON_DEATH = 'successor_on_death'
    TRUSTEE = 'trustee'


class AccountIdentification(BaseObject):
    """
    Defines the identification of a account:
    - scheme_name: Name of the account scheme type
    - identification: ID of the account
    """
    scheme_name = EnumField('Name of the account scheme type', AccountSchemeName, default=None)
    identification = StringField('ID of the account', default=None)

    def __repr__(self):
        return f'<AccountIdentification scheme_name={self.scheme_name} identification={self.identification}>'


class PartyIdentity(BaseObject):
    """
    Defines the identity of a party:
    - full_name: Full name of the party
    - role: Role of the party
    - is_user: Defines the link between the party and the connected PSU
    """
    ROLE_UNKNOWN = PartyRole.UNKNOWN
    ROLE_HOLDER = PartyRole.HOLDER
    ROLE_CO_HOLDER = PartyRole.CO_HOLDER
    ROLE_ATTORNEY = PartyRole.ATTORNEY
    ROLE_CUSTODIAN_FOR_MINOR = PartyRole.CUSTODIAN_FOR_MINOR
    ROLE_LEGAL_GUARDIAN = PartyRole.LEGAL_GUARDIAN
    ROLE_NOMINEE = PartyRole.NOMINEE
    ROLE_BENEFICIARY = PartyRole.BENEFICIARY
    ROLE_SUCCESSOR_ON_DEATH = PartyRole.SUCCESSOR_ON_DEATH
    ROLE_TRUSTEE = PartyRole.TRUSTEE

    full_name = StringField('Full name of the party.', default=None)
    is_user = BoolField('Is the party the connected PSU?', default=None)
    role = EnumField('Role of the party.', PartyRole, default=ROLE_UNKNOWN)

    def __repr__(self):
        return f'<PartyIdentity full_name={self.full_name} role={self.role} is_user={self.is_user}>'


class AccountParty(BaseObject):
    """
    Defines all the information related to an account party:
    - party_identities: list of PartyIdentity elements
    - account_identifications : list of AccountIdentification elements
    """
    party_identities = Field('Identities of the account party', list, default=[])
    account_identifications = Field('Identification information of the account', list, default=[])

    def __repr__(self):
        return f'<AccountParty party_identities={self.party_identities} account_identifications={self.account_identifications}>'


class Account(BaseAccount):
    """
    Bank account.
    """
    TYPE_UNKNOWN          = AccountType.UNKNOWN
    TYPE_CHECKING         = AccountType.CHECKING
    TYPE_SAVINGS          = AccountType.SAVINGS
    TYPE_DEPOSIT          = AccountType.DEPOSIT
    TYPE_LOAN             = AccountType.LOAN
    TYPE_MARKET           = AccountType.MARKET
    TYPE_JOINT            = AccountType.JOINT
    TYPE_CARD             = AccountType.CARD
    TYPE_LIFE_INSURANCE   = AccountType.LIFE_INSURANCE
    TYPE_PEE              = AccountType.PEE
    TYPE_PERCO            = AccountType.PERCO
    TYPE_ARTICLE_83       = AccountType.ARTICLE_83
    TYPE_RSP              = AccountType.RSP
    TYPE_PEA              = AccountType.PEA
    TYPE_CAPITALISATION   = AccountType.CAPITALISATION
    TYPE_PERP             = AccountType.PERP
    TYPE_MADELIN          = AccountType.MADELIN
    TYPE_MORTGAGE         = AccountType.MORTGAGE
    TYPE_CONSUMER_CREDIT  = AccountType.CONSUMER_CREDIT
    TYPE_REVOLVING_CREDIT = AccountType.REVOLVING_CREDIT
    TYPE_PER              = AccountType.PER
    TYPE_REAL_ESTATE      = AccountType.REAL_ESTATE
    TYPE_CROWDLENDING     = AccountType.CROWDLENDING
    TYPE_LDDS             = AccountType.LDDS
    TYPE_PEL              = AccountType.PEL
    TYPE_CSL              = AccountType.CSL
    TYPE_CEL              = AccountType.CEL
    TYPE_CAT              = AccountType.CAT
    TYPE_LIVRET_A         = AccountType.LIVRET_A
    TYPE_LIVRET_B         = AccountType.LIVRET_B

    type =      EnumField('Type of account', AccountType, default=TYPE_UNKNOWN)
    owner_type = StringField('Usage of account')  # cf AccountOwnerType class
    balance =   DecimalField('Balance on this bank account')
    coming =    DecimalField('Sum of coming movements')
    iban =      StringField('International Bank Account Number', mandatory=False)
    ownership = StringField('Relationship between the credentials owner (PSU) and the account')  # cf AccountOwnership class

    # card attributes
    paydate =   DateField('For credit cards. When next payment is due.')
    paymin =    DecimalField('For credit cards. Minimal payment due.')
    cardlimit = DecimalField('For credit cards. Credit limit.')

    number =    StringField('Shown by the bank to identify your account ie XXXXX7489')

    # Wealth accounts (market, life insurance...)
    valuation_diff = DecimalField('+/- values total')
    valuation_diff_ratio = DecimalField('+/- values ratio')
    management_type = EnumField('Management type of account', AccountManagementType, default=None)

    # Employee savings (PERP, PERCO, Article 83...)
    company_name = StringField('Name of the company of the stock - only for employee savings')

    # parent account
    #  - A checking account parent of a card account
    #  - A checking account parent of a recurring loan account
    #  - An investment account parent of a liquidity account
    #  - ...
    parent = Field('Parent account', BaseAccount)

    opening_date = DateField('Date when the account contract was created on the bank')

    all_balances = Field('List of balances', list, default=[])

    party = Field('Party associated to the account', AccountParty, default=None)

    def __repr__(self):
        return "<%s id=%r label=%r>" % (type(self).__name__, self.id, self.label)

    # compatibility alias
    @property
    def valuation_diff_percent(self):
        return self.valuation_diff_ratio

    @valuation_diff_percent.setter
    def valuation_diff_percent(self, value):
        self.valuation_diff_ratio = value


class BalanceType(Enum):
    CLOSING = 1
    """Current balance of the account"""
    PENDING = 2
    """Forecast balance of the account"""


class Balance(BaseObject):
    """
    Object made to receive balance on one Account
    """

    amount = DecimalField('Amount on this balance')
    type = EnumField('Type of balance', BalanceType)
    currency = StringField('Currency')
    reference_date = DateField('date of the balance')
    last_update = DateField('Last time balance was updated')
    credit_included = BoolField('If factoring is included in balance', default=False)
    label = StringField('Bank name of the balance')
    calculated = BoolField('If computation has been made on the balance', default=False)

    def __repr__(self):
        # Ex: '< Balance: label="Solde en Valeur" amount=972.94 type=1 credit_included=False reference_date=2023-06-09 >'
        return ' '.join((
            '<',
            f'{type(self).__name__}:',
            f'label="{self.label}"',
            f'amount={self.amount}',
            f'type={self.type}',
            f'credit_included={self.credit_included}',
            f'reference_date={self.reference_date}',
            '>'
        ))


class Loan(Account):
    """
    Account type dedicated to loans and credits.
    """

    name = StringField('Person name')
    account_label = StringField('Label of the debited account')
    insurance_label = StringField('Label of the insurance')

    total_amount = DecimalField('Total amount loaned')
    available_amount = DecimalField('Amount available') # only makes sense for revolving credit
    used_amount = DecimalField('Amount already used') # only makes sense for revolving credit

    insurance_amount = DecimalField("Amount of the loan's insurance")
    insurance_rate = DecimalField("Rate of the loan's insurance")

    subscription_date = DateField('Date of subscription of the loan')
    maturity_date = DateField('Estimated end date of the loan')
    start_repayment_date = DateField('Date of start repayment of the loan')
    deferred = BoolField('If loan is deferred')
    duration = IntField('Duration of the loan given in months')
    rate = DecimalField('Monthly rate of the loan')

    nb_payments_left = IntField('Number of payments still due')
    nb_payments_done = IntField('Number of payments already done')
    nb_payments_total = IntField('Number total of payments')

    last_payment_amount = DecimalField('Amount of the last payment done')
    last_payment_date = DateField('Date of the last payment done')
    next_payment_amount = DecimalField('Amount of next payment')
    next_payment_date = DateField('Date of the next payment')


class TransactionType(Enum):
    UNKNOWN       = 0
    TRANSFER      = 1
    ORDER         = 2
    CHECK         = 3
    DEPOSIT       = 4
    PAYBACK       = 5
    WITHDRAWAL    = 6
    CARD          = 7
    LOAN_PAYMENT  = 8
    BANK          = 9
    CASH_DEPOSIT  = 10
    CARD_SUMMARY  = 11
    DEFERRED_CARD = 12
    INSTANT       = 13
    MARKET_ORDER  = 14
    MARKET_FEE    = 15
    ARBITRAGE     = 16
    PROFIT        = 17


class BankTransactionCode(BaseObject):
    """
    Object dedicating to bank transaction codes
    It follows the ISO20022 standards.
    See https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets
    """
    domain = StringField('Domain of the transaction')
    family = StringField('Family of the transaction')
    sub_family = StringField('Sub-family of the transaction')


class Transaction(BaseObject):
    """
    Bank transaction.
    """
    TYPE_UNKNOWN       = TransactionType.UNKNOWN
    TYPE_TRANSFER      = TransactionType.TRANSFER
    TYPE_ORDER         = TransactionType.ORDER
    TYPE_CHECK         = TransactionType.CHECK
    TYPE_DEPOSIT       = TransactionType.DEPOSIT
    TYPE_PAYBACK       = TransactionType.PAYBACK
    TYPE_WITHDRAWAL    = TransactionType.WITHDRAWAL
    TYPE_CARD          = TransactionType.CARD
    TYPE_LOAN_PAYMENT  = TransactionType.LOAN_PAYMENT
    TYPE_BANK          = TransactionType.BANK
    TYPE_CASH_DEPOSIT  = TransactionType.CASH_DEPOSIT
    TYPE_CARD_SUMMARY  = TransactionType.CARD_SUMMARY
    TYPE_DEFERRED_CARD = TransactionType.DEFERRED_CARD
    TYPE_INSTANT       = TransactionType.INSTANT
    TYPE_MARKET_ORDER  = TransactionType.MARKET_ORDER
    TYPE_MARKET_FEE    = TransactionType.MARKET_FEE
    TYPE_ARBITRAGE     = TransactionType.ARBITRAGE
    TYPE_PROFIT        = TransactionType.PROFIT

    date =      DateField('Debit date on the bank statement')
    rdate =     DateField('Real date, when the payment has been made; usually extracted from the label or from credit card info')
    vdate =     DateField('Value date, or accounting date; usually for professional accounts')
    bdate =     DateField('Bank date, when the transaction appear on website (usually extracted from column date)')
    type =      EnumField('Type of transaction, use TYPE_* constants', TransactionType, default=TYPE_UNKNOWN)
    raw =       StringField('Raw label of the transaction')
    category =  StringField('Category of the transaction')
    label =     StringField('Pretty label')
    amount = DecimalField('Net amount of the transaction, used to compute account balance')
    coming = BoolField('True if the transaction is not yet booked')

    card =              StringField('Card number (if any)')
    commission =        DecimalField('Commission part on the transaction (in account currency)')
    gross_amount = DecimalField('Amount of the transaction without the commission')

    # International
    original_amount = DecimalField('Original net amount (in another currency)')
    original_currency = StringField('Currency of the original amount')
    country =           StringField('Country of transaction')

    original_commission =          DecimalField('Original commission (in another currency)')
    original_commission_currency = StringField('Currency of the original commission')
    original_gross_amount = DecimalField('Original gross amount (in another currency)')

    attachments =       Field('List of files attached to the transaction', list)
    # Financial arbitrations
    investments =       Field('List of investments related to the transaction', list, default=[])

    counterparty = Field('Counterparty of transaction', TransactionCounterparty)

    bank_transaction_code = Field('Bank transaction code of transaction', BankTransactionCode)

    def __repr__(self):
        return "<Transaction date=%r label=%r amount=%r>" % (self.date, self.label, self.amount)

    def unique_id(self, seen: set | None = None, account_id: str | None = None) -> str:
        """
        Get an unique ID for the transaction based on date, amount and raw.

        :param seen: if given, the method uses this set as a cache to
                     prevent several transactions with the same values to have the same
                     unique ID.
        :type seen: :class:`set`
        :param account_id: if given, add the account ID in data used to create
                           the unique ID. Can be useful if you want your ID to be unique across
                           several accounts.
        :type account_id: :class:`str`
        :returns: an unique ID encoded in 8 length hexadecimal string (for example ``'a64e1bc9'``)
        :rtype: :class:`str`
        """
        crc = crc32(str(self.date).encode('utf-8'))
        crc = crc32(str(self.amount).encode('utf-8'), crc)
        if not empty(self.raw):
            label = self.raw
        else:
            label = self.label

        crc = crc32(re.sub('[ ]+', ' ', label).encode("utf-8"), crc)

        if account_id is not None:
            crc = crc32(str(account_id).encode('utf-8'), crc)

        if seen is not None:
            while crc in seen:
                crc = crc32(b"*", crc)

            seen.add(crc)

        return "%08x" % (crc & 0xffffffff)


class CapBank(CapCollection, CapCredentialsCheck):
    """
    Capability of bank websites to see accounts and transactions.
    """

    def check_credentials(self) -> bool:
        """
        Check that the given credentials are correct by trying to login.

        The default implementation of this method check if the class using this capability
        has a browser, execute its do_login if it has one and then see if no error pertaining to the creds is raised.
        If any other unexpected error occurs, we don't know whether the creds are correct or not.
        """
        # TODO move this in a specific capability
        if getattr(self, 'BROWSER', None) is None:
            raise NotImplementedError()

        try:
            self.browser.do_login()
        except BrowserIncorrectPassword:
            return False

        return True

    def iter_resources(self, objs: List[BaseObject], split_path: List[str]) -> Iterable[BaseObject]:
        """
        Iter resources.

        Default implementation of this method is to return on top-level
        all accounts (by calling :func:`iter_accounts`).

        :param objs: type of objects to get
        :type objs: tuple[:class:`BaseObject`]
        :param split_path: path to discover
        :type split_path: :class:`list`
        :rtype: iter[:class:`BaseObject`]
        """
        if Account in objs:
            self._restrict_level(split_path)

            yield from self.iter_accounts()

    def iter_accounts(self) -> Iterable[Account]:
        """
        Iter accounts.

        :rtype: iter[:class:`Account`]
        """
        raise NotImplementedError()

    def get_account(self, id: str) -> Account | None:
        """
        Get an account from its ID.

        :param id: ID of the account
        :type id: :class:`str`
        :rtype: :class:`Account`
        :raises: :class:`AccountNotFound`
        """
        return find_object(self.iter_accounts(), id=id, error=AccountNotFound)

    def iter_history(self, account: Account) -> Iterable[Transaction]:
        """
        Iter history of transactions of a specific account.

        :param account: account to get history
        :type account: :class:`Account`
        :rtype: iter[:class:`Transaction`]
        :raises: :class:`AccountNotFound`
        """
        return self.iter_transactions(account, with_coming=False)

    def iter_coming(self, account: Account) -> Iterable[Transaction]:
        """
        Iter coming transactions of a specific account.

        :param account: account to get coming transactions
        :type account: :class:`Account`
        :rtype: iter[:class:`Transaction`]
        :raises: :class:`AccountNotFound`
        """
        return self.iter_transactions(account, with_history=False)

    def iter_transactions(
        self, account: Account, *, with_history: bool = True, with_coming: bool = True
    ) -> Iterable[Transaction]:
        """
        Iter all transactions (history and coming) of a specific account.

        :param account: account to get transactions
        :param with_history: if False, booked transactions will not be returned
        :param with_coming: if False, coming transactions will not be returned
        :type account: :class:`Account`
        :rtype: iter[:class:`Transaction`]
        :raises: :class:`AccountNotFound`
        """
        raise NotImplementedError()


class CapAccountCheck(Capability):
    """
    Capability to get accounts parties information.

    The expected structure is the following:
        - AccountParty object
            * party_identities (list of PartyIdentity elements):
                * full name
                * role
                * is_user
            * account_identifications (list of type AccountIdentification elements):
                * scheme name
                * identification
    """
