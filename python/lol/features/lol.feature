Feature: Onezone login page
  A site where you can login to Onezone.

Scenario Outline: Onezone login page renders with proper title
  Given I'm visiting Onezone site
  When I go to the <page> page
  Then The page title should contain <title>

  Examples:
  | page         | title |
  | /home/login  | login |
  | /a           | b     |


#Scenario Outline: Rendering multiple login buttons
#  Given I'm visiting Onezone site
#  When I go to the login page
#  Then I should see at least <btn_count> login button
#
#  Examples:
#  | btn_count |
#  | 1         |
#  | 2         |
#  | 3         |
#
#Scenario Outline: Rendering particular login buttons
#  Given I'm visiting Onezone site
#  When I go to the login page
#  Then I should see a <provider_name> login button
#
#  Examples:
#  | provider_name |
#  | plgrid        |
#  | dropbox       |
#  | github        |
#  | google        |

#Scenario: Hello world
#  Given I have some object
#  When I invoke foo method <times> times
#  Then The some_val property of object should equal <value>
#
#  Examples:
#  | times | value |
#  | 0     | 0     |
#  | 1     | 42    |
#  | 2     | 84    |

