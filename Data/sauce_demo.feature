Feature: Test the end to end process of online shopping

Scenario: Sauce Demo shopping
Given I navigate to a webpage "https://www.saucedemo.com/"
And I login to the application with credentials "standard_user" "secret_sauce"
And I verify the page title is "Products"
Then I added "3" products in the cart
And I delete one item
And verify the count is updated to "2"
Then I check out the cart
And fill the customer details as "Jane" "Stone" "223322"
Then I verify order and finish the order

