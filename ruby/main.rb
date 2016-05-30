# https://github.com/SeleniumHQ/selenium/wiki/Ruby-Bindings

require 'selenium-webdriver'
# require 'active_support/core_ext'
# require 'headless'

# class FakeWait
#   def until
#     yield
#   end
# end

# env_up GR + OP

# cel:
# - skrypt startuje testy i

# oz_host = ...
# op1_host = ...

# Headless.ly do

# driver = Selenium::WebDriver.for :firefox
driver = Selenium::WebDriver.for :chrome
driver.manage.window.resize_to 1280, 1024
driver.navigate.to 'https://veilfsdev.com'

wait = Selenium::WebDriver::Wait.new(timeout: 4) # seconds
# wait = FakeWait.new

wait.until do
  driver.find_element(class: 'oneicon-social-plgrid')
end

# driver.find_element(id: 'nav-home.login').click
driver.find_element(class: 'oneicon-social-plgrid').click


user1_dev_login = wait.until do
  begin
    driver.find_elements(tag_name: 'a').find { |e| e.text == 'user1' }
  rescue
    puts $!
    false
  end
end
user1_dev_login.click

wait.until do
  driver.current_url =~ /onezone/i
end

p_collapse = driver.find_elements(class: 'main-accordion-toggle').find do |e|
  e.attribute(:href) =~ /#collapse-providers/
end
p_collapse.click

provider_link = wait.until do
  driver.find_elements(class: 'provider-header').find do |e|
    e.text == 'p1'
  end
end
provider_link.click

go_to_provider_btn = wait.until do
  el = driver.find_element(class: 'provider-place-drop')
  el and el.find_element(class: 'btn')
end
go_to_provider_btn.click

wait.until do
  driver.title =~ /oneprovider/i
end

(wait.until { driver.find_element(id: 'main-spaces') }).click

# driver.find_element(id: 'main-spaces')

create_button = wait.until do
  driver.find_element(id: 'create-space-button')
end

wait.until do
  begin
    create_button.click
    true
  rescue
    puts $!
    false
  end
end


create_space_modal = wait.until do
  driver.find_element(id: 'create-space-modal')
end

text_input = (wait.until { create_space_modal.find_element(class: 'create-space-input') })

require 'securerandom'
space_name = "selenium space #{SecureRandom.hex(4)}"

# time hack
sleep 1

text_input.send_keys space_name
text_input.send_keys :enter

wait.until do
  driver.find_elements(class: 'item-label').find do |e|
    e.text == space_name
  end
end

# element.send_keys 'Hello WebDriver!'
# element.submit

sleep(15)

puts driver.title

driver.quit

# end
