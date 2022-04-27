from selenium import webdriver
try:
    f = open(input("File: "), "a")
    driver = webdriver.Chrome("driver/chromedriver")
    start = input("Start link: ")
    if input("Limit links? (y/n): ") == "y":
        limit = True
        limit_term = input("Limit to this URL path: ")
    else:
        limit = False
    if input("Would you like to log the links in the Terminal? (y/n): ") == "y":
        log = True
    else:
        log = False
    driver.get(start)
    seen = []
    current = []
    current.append(start)
    while len(current) > 0:
        for i in range(len(current)):
            link = current.pop(i)
            driver.get(link)
            elems = driver.find_elements_by_tag_name('a')
            for elem in elems:
                newlink = elem.get_attribute('href')
                if newlink != None:
                    if elem not in seen:
                        seen.append(elem)
                        current.append(newlink)
                        if limit:
                            if limit_term in newlink:
                                f.write(newlink + "\n")
                                if log:
                                    print(newlink)
                        else:
                            f.write(newlink + "\n")
                            if log:
                                print(newlink)
    driver.close()
    f.close()
except Exception as e:
    driver.close()
    f.close()
    print(e)
    print("Exited successfully")