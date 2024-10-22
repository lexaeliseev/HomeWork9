import os
from selene import browser, have


def test_practice_form():
    browser.open('/automation-practice-form')
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    """ WHEN """
    browser.element("#firstName").type("Алексей")
    browser.element("#lastName").set_value("Елисеев")
    browser.element("#userEmail").type("qaguru@test.com")
    browser.element('//label[contains(text(),"Male")]').click()
    browser.element("#userNumber").set_value("9999999999")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").click().element('[value="1992"]').click()
    browser.element(".react-datepicker__month-select").click().element('//option[contains(text(),"April")]').click()
    browser.element(".react-datepicker__day--004").click()

    browser.element("#subjectsInput").type("g")
    browser.element("//div[contains(@class, 'subjects-auto-complete__option') and text()='English']").click()
    browser.element("//label[text()='Reading']").click()
    browser.element("//label[text()='Sports']").click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("../image/test_image.jpg"))

    browser.element('#currentAddress').type("Test Country, test city, test street, test house")
    browser.element("#state").click().element("//div[contains(@id, 'react-select-3-option-0') and text()='NCR']").click()
    browser.element("#react-select-4-input").type("Noida").press_enter()
    browser.element("#submit").click()

    """ THEN """
    browser.element("//tr[td[contains(text(), 'Student Name')]]").should(have.text("Алексей Елисеев"))
    browser.element("//tr[td[contains(text(), 'Student Email')]]").should(have.text("qaguru@test.com"))
    browser.element("//tr[td[contains(text(), 'Gender')]]").should(have.text("Male"))
    browser.element("//tr[td[contains(text(), 'Mobile')]]").should(have.text("9999999999"))
    browser.element("//tr[td[contains(text(), 'Date of Birth')]]").should(have.text("04 April,1992"))
    browser.element("//tr[td[contains(text(), 'Subjects')]]").should(have.text("English"))
    browser.element("//tr[td[contains(text(), 'Hobbies')]]").should(have.text("Reading, Sports"))
    browser.element("//tr[td[contains(text(), 'Picture')]]").should(have.text("test_image.jpg"))
    browser.element("//tr[td[contains(text(), 'Address')]]").should(have.text("Test Country, test city, test street, test house"))
    browser.element("//tr[td[contains(text(), 'State and City')]]").should(have.text("NCR Noida"))