from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.funtrivia.com/playquiz/quiz19080615d9558.html")

#Identify items

q1_css_locator = "input[value='Tart Tatin']"
q2_css_locator = "input[value='Chocolate & Coffee']"
q3_css_locator = "input[value='Ganache']"
q4_css_locator = "input[value='low peaks']"
q5_css_locator = "input[value='Mechanically']"
q6_css_locator = "input[value='St. Honore']"
q7_css_locator = "input[value='Mascarpone']"
q8_css_locator = "input[value='Baking Power']"
q9_css_locator = "input[value='f']"
q10_css_locator = "input[value='pate choux']"
end_css_locator = "input[value='Submit my Answers!']"

#Assign elements

Q1 = browser.find_element_by_css_selector(q1_css_locator)
Q2 = browser.find_element_by_css_selector(q2_css_locator)
Q3 = browser.find_element_by_css_selector(q3_css_locator)
Q4 = browser.find_element_by_css_selector(q4_css_locator)
Q5 = browser.find_element_by_css_selector(q5_css_locator)
Q6 = browser.find_element_by_css_selector(q6_css_locator)
Q7 = browser.find_element_by_css_selector(q7_css_locator)
Q8 = browser.find_element_by_css_selector(q8_css_locator)
Q9 = browser.find_element_by_css_selector(q9_css_locator)
Q10 = browser.find_element_by_css_selector(q10_css_locator)
End = browser.find_element_by_css_selector(end_css_locator)

#Manipulate elements

Q1.click()
Q2.click()
Q3.click()
Q4.click()
Q5.click()
Q6.click()
Q7.click()
Q8.click()
Q9.click()
Q10.click()
End.click()



