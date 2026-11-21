Feature: Browser Actions
  Scenario: Open Playwright website
    Given I open the Playwright website
    Then the page title should contain "Playwright"

   Scenario: Browser Actions
    Given I navigate to a webpage
    Then I navigate to page two
    Then I go back
    And I come forward
    And I reload the page
    And I close the page

  @button   
   Scenario: Buttons and Clicks
   Given I navigate to a webpage "https://demoqa.com/buttons" 
   Then I perform all the click actions

  @textbox
  Scenario:Textbox Actions
  Given I navigate to a webpage "https://demoqa.com/text-box"
  Then I enter all details "Aparna" "aparna1234@gmail.com" "House 12, JNagar" "House 23,ABC road"
  
  @radio
  Scenario: Radio button Actions
  Given I navigate to a webpage "https://demoqa.com/automation-practice-form"
  Then I click the radio button
  Then I click the check box

  @dropdown
  Scenario: Dropdown Actions
  Given I navigate to a webpage "https://demoqa.com/automation-practice-form"
  Then I select the dropdown value

  @fileupload
  Scenario:Upload/download actions
  Given I navigate to a webpage "https://demoqa.com/upload-download"
  Then I upload the file "Data/sauce_demo.feature"

  @filedownload
  Scenario:Download file action
  Given I navigate to a webpage "https://demoqa.com/upload-download"
  Then I downloaded the file

  @dragdrop
  Scenario:Simple drag and drop action
  Given I navigate to a webpage "https://demoqa.com/droppable"
  Then I drag and drop the item

  @mouseover
  Scenario:Mouse over action
  Given I navigate to a webpage "http://uitestingplayground.com/mouseover"
  Then I mouse over the item

  @alerts
  Scenario: Handling alerts
  Given I navigate to a webpage "https://demoqa.com/alerts"
  Then I handled all the alerts


