Feature: Вход

  Scenario: Вход под админом
    Given Я открыл страницу "Входа"
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    Then Я должен быть на главной странице

  Scenario: Не успешный вход
    Given Я открыл страницу "Входа"
    When Я ввожу следующий текст в следующие поля
      | text | field    |
      | a    | username |
      | b    | password |
    And Я отправляю форму
    Then Я должен быть на странице входа
    And Я должен видеть сообщение об ошибке с текстом "Please enter a correct username and password. Note that both fields may be case-sensitive."
