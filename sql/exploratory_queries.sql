-- Total Companies
SELECT COUNT(*) FROM companies;

-- Top 10 Companies by ROE
SELECT company_name, roe_percentage
FROM companies
ORDER BY roe_percentage DESC
LIMIT 10;

-- Top 10 Companies by ROCE
SELECT company_name, roce_percentage
FROM companies
ORDER BY roce_percentage DESC
LIMIT 10;

-- Total Profit & Loss Records
SELECT COUNT(*) FROM profit_loss;

-- Total Balance Sheet Records
SELECT COUNT(*) FROM balance_sheet;

-- Total Cash Flow Records
SELECT COUNT(*) FROM cash_flow;

-- Total Stock Price Records
SELECT COUNT(*) FROM stock_prices;

-- Total Financial Ratios Records
SELECT COUNT(*) FROM financial_ratios;

-- Total Market Cap Records
SELECT COUNT(*) FROM market_cap;