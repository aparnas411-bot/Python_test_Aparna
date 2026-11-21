Feature: Test the end to end process of home loan

Scenario: Home loan 
Given I navigate to a webpage "https://www.anz.com.au/personal/home-loans/calculators-tools/borrowing-power-calculator/"
And I select the application type as Single
And the number of dependants as 0
And select the property type as Home to Live in
And the income as "100000" and other income as "10000"
And the living expense as 2000
And the current loan repayment as 0
And the other commitments as 0
And the total creditcard limits as 10000
And the borrowing estimate as 547000
Then I click the workout button
