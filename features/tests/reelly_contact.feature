Feature: Tests for Contact us page

  Scenario: User can open the Contact us page
    Given Open main page
    And Log in to the page with email "bnszekely+test@gmail.com" and password "S9YuQm-qwfrRW42"
    When Click on the settings icon
    And Click on Contact us option
    Then Verify the right page opens
    And Verify there are at least 4 social media icons
    And Verify the Connect the company button is available and clickable