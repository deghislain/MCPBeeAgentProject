from typing import List, Dict


def get_income_statement_keys() -> List:
    return [
        'fiscalDateEnding',
        'reportedCurrency',
        'grossProfit',
        'totalRevenue',
        'costOfRevenue',
        'costofGoodsAndServicesSold',
        'operatingIncome',
        'sellingGeneralAndAdministrative',
        'researchAndDevelopment',
        'operatingExpenses',
        'investmentIncomeNet',
        'netInterestIncome',
        'interestIncome',
        'interestExpense',
        'nonInterestIncome',
        'otherNonOperatingIncome',
        'depreciation',
        'depreciationAndAmortization',
        'incomeBeforeTax',
        'incomeTaxExpense',
        'interestAndDebtExpense',
        'netIncomeFromContinuingOperations',
        'comprehensiveIncomeNetOfTax',
        'ebit',
        'ebitda',
        'netIncome'
    ]


def get_balance_sheet_keys() -> List:
    return ['fiscalDateEnding',
            'reportedCurrency',
            'totalAssets',
            'totalCurrentAssets',
            'cashAndCashEquivalentsAtCarryingValue',
            'cashAndShortTermInvestments',
            'inventory',
            'currentNetReceivables',
            'totalNonCurrentAssets',
            'propertyPlantEquipment',
            'accumulatedDepreciationAmortizationPPE',
            'intangibleAssets',
            'intangibleAssetsExcludingGoodwill',
            'goodwill',
            'investments',
            'longTermInvestments',
            'shortTermInvestments',
            'otherCurrentAssets',
            'otherNonCurrentAssets',
            'totalLiabilities',
            'totalCurrentLiabilities',
            'currentAccountsPayable',
            'deferredRevenue',
            'currentDebt',
            'shortTermDebt',
            'totalNonCurrentLiabilities',
            'capitalLeaseObligations',
            'longTermDebt',
            'currentLongTermDebt',
            'longTermDebtNoncurrent',
            'shortLongTermDebtTotal',
            'otherCurrentLiabilities',
            'otherNonCurrentLiabilities',
            'totalShareholderEquity',
            'treasuryStock',
            'retainedEarnings',
            'commonStock',
            'commonStockSharesOutstanding'
            ]


def get_cash_flow_keys() -> List:
    return [
        'scalDateEnding',
        'reportedCurrency',
        'operatingCashflow',
        'paymentsForOperatingActivities',
        'proceedsFromOperatingActivities',
        'changeInOperatingLiabilities',
        'changeInOperatingAssets',
        'depreciationDepletionAndAmortization',
        'capitalExpenditures',
        'changeInReceivables',
        'changeInInventory',
        'profitLoss',
        'cashflowFromInvestment',
        'cashflowFromFinancing',
        'proceedsFromRepaymentsOfShortTermDebt',
        'paymentsForRepurchaseOfCommonStock',
        'paymentsForRepurchaseOfEquity',
        'paymentsForRepurchaseOfPreferredStock',
        'dividendPayout',
        'dividendPayoutCommonStock',
        'dividendPayoutPreferredStock',
        'proceedsFromIssuanceOfCommonStock',
        'proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet',
        'proceedsFromIssuanceOfPreferredStock',
        'proceedsFromRepurchaseOfEquity',
        'proceedsFromSaleOfTreasuryStock',
        'changeInCashAndCashEquivalents',
        'changeInExchangeRate',
        'netIncome'
    ]


def get_earnings_keys() -> List:
    return [
        'fiscalDateEnding',
        'reportedEPS'
    ]


def get_insider_tx_keys() -> List:
    return [
        'nsaction_date',
        'ticker',
        'executive',
        'executive_title',
        'security_type',
        'acquisition_or_disposal',
        'shares',
        'share_price'
    ]


def get_daily_adjusted_keys() -> List:
    return [
        '1. open',
        '2. high',
        '3. low',
        '4. close',
        '5. adjusted close',
        '6. volume',
        '7. dividend amount',
        '8. split coefficient'
    ]
