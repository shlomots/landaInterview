
import time
from selenium import webdriver
from orm import sale, session, Base, engine


driver = webdriver.Chrome(r'C:\Users\shlom\Downloads\chromedriver_win32')
while True:
    time.sleep(1800)#every half hour
    driver.get('https://www.nadlan.gov.il/?search=%D7%A9%D7%9E%D7%A2%D7%95%D7%A0%D7%99%20%D7%AA%D7%9C%20%D7%90%D7%91%D7%99%D7%91%20-%D7%99%D7%A4%D7%95')
    time.sleep(4)  # wait till the page loads.
    tablerow = driver.find_element_by_class_name('tablerow')
    sales = []
    for row in tablerow:
        rowcoulums = row.find_element_by_class_name('tableCol')
        for coulum in rowcoulums:
            list = []
            list.append(coulum.title)
            sale = sale(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8])
            sales.append(sale)

    Base.metadata.create_all(engine)
    for p in len(sales) - 1:
        session.add(sales[p])





#source = requests.get('https://www.nadlan.gov.il/?search=%D7%A9%D7%9E%D7%A2%D7%95%D7%A0%D7%99%203,%20%D7%91%D7%90%D7%A8%20%D7%A9%D7%91%D7%A2').text

#print(source)

#soup = BeautifulSoup(source.content, 'lxml')

#print(soup.prettify())

#body= soup.find('body')

#print(body.prettify())


