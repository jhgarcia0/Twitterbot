def cotacao_dolar(asfloat=False, formated=False):
    """
    Made by: Joao Henrique Garcia
    Linkedin : 'https://www.linkedin.com/in/jo%C3%A3o-henrique-a166641b7/'
    free to use anywhere
    :param asfloat: PT: Retorna dolar como um float
                    EN : Returns dolar as a float
    :param formated: PT:Retorna o numero formatado com R$(ex:'R$5,64')
                     EN: Returns a formated number with R$(e.g.:'R$5,64')
    :return: PT: cotacao do dolar para R$
             EN: dollar quotation for R$
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    URL = 'https://www.google.com/search?q=dolar'
    option = Options()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    option.headless = True
    driver = webdriver.Chrome(options=option)
    driver.get(URL)

    elem = driver.find_element_by_css_selector('span.SwHCTb')
    dolar = elem.text
    if not asfloat and not formated:
        return dolar
    elif asfloat and not formated:
        dolar = dolar.replace(',','.')
        asfloat = float(dolar)
        return asfloat
    elif not asfloat and formated:
        formated = f"R${dolar}"
        return formated
    else:
        raise Exception('Only use one parameter as True')


def cotacao_euro(asfloat = False,formated = False):
    """
        Made by: Joao Henrique Garcia
        Linkedin : 'https://www.linkedin.com/in/jo%C3%A3o-henrique-a166641b7/'
        free to use anywhere
        :param asfloat: PT: Retorna euro como um float
                        EN : Returns euro as a float
        :param formated: PT:Retorna o numero formatado com R$(ex:'R$5,64')
                         EN: Returns a formated number with R$(e.g.:'R$5,64')
        :return: PT: cotacao do euro para R$
                 EN: euro quotation for R$
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    URL = 'https://www.google.com/search?q=euro'
    option = Options()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    option.headless = True
    driver = webdriver.Chrome(options=option)
    driver.get(URL)
    elem = driver.find_element_by_css_selector('span.SwHCTb')
    euro = elem.text
    if not asfloat and not formated:
        return euro
    elif asfloat and not formated:
        euro = euro.replace(',','.')
        asfloat = float(euro)
        return asfloat
    elif not asfloat and formated:
        formated = f"R${euro}"
        return formated
    else:
        raise Exception('Only use one parameter as True')


def cotacao_libra(asfloat = False, formated = False):
    """
    Made by: Joao Henrique Garcia
    Linkedin : 'https://www.linkedin.com/in/jo%C3%A3o-henrique-a166641b7/'
    free to use anywhere
    :param asfloat: PT: Retorna libra como um float
                    EN : Returns pound as a float
    :param formated: PT:Retorna o numero formatado com R$(ex:'R$5,64')
                     EN: Returns a formated number with R$(e.g.:'R$5,64')
    :return: PT: cotacao do libra para R$
             EN: pound quotation for R$
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    URL = 'https://www.google.com/search?q=libraparareal'
    option = Options()
    option.headless = True
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=option)
    driver.get(URL)
    elem = driver.find_element_by_css_selector('span.SwHCTb')
    libra = elem.text
    if not asfloat and not formated:
        return libra
    elif asfloat and not formated:
        libra = libra.replace(',', '.')
        asfloat = float(libra)
        return asfloat
    elif not asfloat and formated:
        formated = f"R${libra}"
        return formated