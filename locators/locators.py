from selenium.webdriver.common.by import By


class LoginLocators:
    login_username_txt = (By.ID, "email")
    login_password_txt = (By.ID, "passwd")
    login_submit_btn = (By.ID, "SubmitLogin")
    logout_btn = (By.ID, "")


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
    product_link = (By.XPATH, "//a[@class='product_img_link']")
    addtoCartbtn = (By.XPATH, "//p[@id='add_to_cart']")
    addtoCarttxt = (By.XPATH, "//i[@class='icon-ok']")
    continue_shopping_btn = (By.XPATH, "//i[@class='icon-chevron-left left']")
    proceedto_checkout_btn = (By.XPATH, "//i[@class='icon-chevron-right right']")
    popup_close_btn =(By.XPATH,"//span[@title='Close window']")
