#language: en
Feature: Validate the data returned by searches in Virtual Republica

    '''I as a user want to access the ranking page
    of the Brazilian Championship in the sport globe to consult the
    first place.'''

    Scenario: Query the data of an address by CEP code
        Given I am on Republica Virtuals CEP code search screen
        When I inform the CEP code "50030230"
        And I click on the button "buscar CEP"
        Then I see the address data