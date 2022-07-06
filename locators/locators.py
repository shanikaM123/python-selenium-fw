from selenium.webdriver.common.by import By


class LoginLocators:
    login_username_txt = (By.ID, "email")
    login_password_txt = (By.ID, "passwd")
    login_submit_btn = (By.ID, "SubmitLogin")
    logout_btn = (By.ID, "")
    women_link = (By.XPATH, "//a[@class='sf-with-ul']")


class WomenPageLocators:
    tops_lnk = (By.LINK_TEXT, "Tops")
    shirts_lnk = (By.LINK_TEXT, "T-shirts")
    tops_lnk = (By.LINK_TEXT, "Tops")
    blouse_link = (By.LINK_TEXT, "Blouses")


class HomePageLocators:
    women_lnk = (By.LINK_TEXT, "Women")
    dresses_lnk = (By.LINK_TEXT, "Dresses")
    shirts_lnk = (By.LINK_TEXT, "T-Shirts")


class TShirtsLocators:
    product_link = (By.XPATH, "//div[@class='product-container']")
    addtoCarttxt = (By.XPATH, "//i[@class='icon-ok']")
    continue_shopping_btn = (By.XPATH, "//i[@class='icon-chevron-left left']")
    proceedto_checkout_btn = (By.XPATH, "//i[@class='icon-chevron-right right']")
    popup_close_btn = (By.XPATH, "//span[@title='Close window']")
    sortby_dropbox = (By.XPATH, "//select[@id='selectProductSort']")


class ViewPageLocators:
    addtoCartbtn = (By.XPATH, "/html/body/div[1]/div/div[3]/form/div/div[3]/div[1]/p/button/span")
