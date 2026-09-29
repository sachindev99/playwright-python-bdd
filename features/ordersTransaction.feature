Feature: Order Transaction

    Scenario Outline: Verify order details success message shown in details page
      Given place the item order with <username> and <password>
      And user is on landing page
      When I login to portal with <username> and <password>
      And navigate to orders page
      And select the orderId
      Then order message is successfully displayed
      Examples:
        | username          | password  |
        | testys@gmail.com  | Test@1234 |
        | test123@gmail.com | Test@1234 |


    Scenario Outline: Remove a product from the cart
      Given place the item order with <username> and <password>
      And user is on landing page
      When I login to portal with <username> and <password>
      When the user removes product from the cart
      Then the cart should not contain the product
      Examples:
        | username         | password  |
        | testys@gmail.com | Test@1234 |


    Scenario Outline: Add product to cart
      Given user logs in using <username> and <password>
      When user adds a product to the cart
      Then the product should be displayed in the cart
      Examples:
        | username          |  password |
        | testys@gmail.com  | Test@1234 |


    Scenario Outline: Add and delete selected products from cart
      Given user logs in using <username> and <password>
      When user adds "<Item1>" "<Item2>" "<Item3>" to cart
      Then all the products should be displayed in the cart
      When user removes "<Item1>" and "<Item3>" from the cart
      Then "<Item2>" should be displayed in the cart
      And "<Item1>" should not be displayed in the cart
      And "<Item3>" should not be displayed in the cart

    Examples:
      | username         | password  | Item1           | Item2       | Item3          |
      | testys@gmail.com | Test@1234 | ADIDAS ORIGINAL | ZARA COAT 3 | iphone 13 pro  |

    Scenario Outline: Order items through UI
      Given user logs in using <username> and <password>
      When user adds "<Item1>" "<Item2>" "<Item3>" to cart
      Then all the products should be displayed in the cart
      And checkout button is clicked
      And payment details are added
      Then order is placed successfully


      Examples:
      | username         | password  | Item1           | Item2       | Item3          |
      | testys@gmail.com | Test@1234 | ADIDAS ORIGINAL | ZARA COAT 3 | iphone 13 pro  |


    Scenario Outline: User adds another product after reviewing the cart
        Given user logs in using <username> and <password>
        When user adds the following products to cart
          | ADIDAS ORIGINAL |
          | ZARA COAT 3     |
        And all the products should be displayed in the cart
        And user continues shopping
        And user adds the following products to cart
          |iphone 13 pro|
        Then all the products should be displayed in the cart
        And checkout button is clicked
        And payment details are added
        Then order is placed successfully
        And user signs out

        Examples:
          | username         | password  |
          | testys@gmail.com | Test@1234 |
