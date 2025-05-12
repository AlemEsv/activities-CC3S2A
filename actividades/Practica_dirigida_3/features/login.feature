Feature: Login
  Scenario Outline: credenciales válidas
    Given el usuario "<user>" con contraseña "<pass>"
    When intenta iniciar sesión
    Then debe ver "Bienvenido, <user>"

  Examples:
    | user  | pass    |
    | alice | secret1 |