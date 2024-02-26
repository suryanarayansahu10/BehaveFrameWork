Feature: Orange HRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch chrome browser
    When I open orange HRM home page
    And enter username "admin" and password "admin123"
    And click on login button
    Then user must successfully login to the dashboard page


  Scenario Outline:  Login to OrangeHRM with multiple parameters
    Given I launch chrome browser
    When I open orange HRM home page
    And enter username "<username>" and password "<password>"
    And click on login button
    Then user must successfully login to the dashboard page

    Examples:
      | username | Password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | adminmnp | 2222     |
