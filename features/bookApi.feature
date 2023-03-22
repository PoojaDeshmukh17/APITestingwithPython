# Created by GS2534 at 09-03-2023
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here

  Scenario: Verify AddBook API functionality
    Given the book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added