from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.support.wait import WebDriverWait
from colorama import Fore,Style
from pathlib import Path
from .error_handling import errors

from time import sleep

class zgautomate:
    
    def __init__(self,url,browser="chrome",wait=4, headless=False):
        
        if headless == True:
             self.option_edge = webdriver.EdgeOptions()
             self.option_edge.add_argument("--headless")
             self.option_chrome = webdriver.ChromeOptions()
             self.option_chrome.add_argument("--headless")
             self.option_firefox = webdriver.FirefoxOptions()
             self.option_firefox.add_argument("--headless")
        elif headless == False:
             self.option_chrome = webdriver.ChromeOptions()
             self.option_firefox = webdriver.FirefoxOptions()
             self.option_edge = webdriver.EdgeOptions()
             
        

        self.browser = browser
        if self.browser == "chrome":
          self.driver = webdriver.Chrome(options=self.option_chrome)
        elif self.browser == "firefox":
            self.driver = webdriver.Firefox(options=self.option_firefox)
        elif self.browser == "edge":
            self.driver = webdriver.Edge(options=self.option_edge)
        elif self.browser == "safari":
            self.driver = webdriver.Safari()
        elif self.browser == "webkit":
            self.driver = webdriver.WebKitGTK()
        else:
             
             print(Fore.RED+"Invalid Browser Selected \nKindly Choose From: Chrome, Firefox, Edge, Safarai And Webkit")
             print(Style.RESET_ALL)
             exit()
             
     #    self.wait = WebDriverWait(self.driver, self.wait)
        self.url =  url
        # self.find_type = find_type
        # self.value =  value
        
        self.wait = wait

        #Opening Url In Browser.
        self.driver.get(self.url)
        
    @errors  
    def type_by_name(self, element, key):
          self.key = key
          
          # self.keyword = Keys.ENTER
          WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.NAME, str(element))))
        
          self.driver.find_element(By.NAME, str(element)).send_keys(self.key)
        #   
       
          
        
        

             
             
    @errors
    def type_by_class(self, element, key):
        WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.CLASS_NAME, str(element))))
        
        self.driver.find_element(By.CLASS_NAME, str(element)).send_keys(key)
          
    @errors
    def type_by_xpath(self, element, key):
        WebDriverWait(self.driver,self.wait).until(ec.presence_of_element_located((By.XPATH, str(element))))
        
        self.driver.find_element(By.XPATH, str(element)).send_keys(key)
     
          
    @errors   
    def type_by_css(self, element, key):
        WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.CSS_SELECTOR, str(element))))
        
        self.driver.find_element(By.CSS_SELECTOR, str(element)).send_keys(key)
          
    @errors   
    def type_by_id(self, element, key):
        WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.ID, str(element))))
        
        self.driver.find_element(By.ID, str(element)).send_keys(key)
          
    @errors   
    def type_by_tag(self, element, key):
        WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.TAG_NAME, str(element))))
        
        self.driver.find_element(By.TAG_NAME, str(element)).send_keys(key)
          
    @errors   
    def type_by_link_text(self, element, key):
        WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.LINK_TEXT, str(element))))
        
        self.driver.find_element(By.LINK_TEXT, str(element)).send_keys(key)
          
    @errors   
    def type_by_partial_link_text(self, element, key):
        WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, str(element))))
        
        self.driver.find_element(By.PARTIAL_LINK_TEXT, str(element)).send_keys(key)
          


    @errors   
    def click_by_name(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.NAME, str(value))))
             self.driver.find_element(By.NAME, str(value)).click()
              
    @errors
    def click_by_xpath(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.XPATH, str(value))))
             self.driver.find_element(By.XPATH, str(value)).click()
               
    @errors
    def click_by_css(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.CSS_SELECTOR, str(value))))
             self.driver.find_element(By.CSS_SELECTOR, str(value)).click()
               
    @errors
    def click_by_class(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.CLASS_NAME, str(value))))
             self.driver.find_element(By.CLASS_NAME, str(value)).click()
               
    @errors
    def click_by_link_text(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.LINK_TEXT, str(value))))
             self.driver.find_element(By.LINK_TEXT, str(value)).click()
               
    @errors
    def click_by_partial_link_text(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, str(value))))
             self.driver.find_element(By.PARTIAL_LINK_TEXT, str(value)).click()
               
    @errors
    def click_by_id(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.ID, str(value))))
             self.driver.find_element(By.ID, str(value)).click()
               
    @errors
    def click_by_tag(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.TAG_NAME, str(value))))
             self.driver.find_element(By.TAG_NAME, str(value)).click()
               
     
             
             
        
        
      

    @errors   
    def text_by_name(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.NAME, str(value))))
             x = self.driver.find_element(By.NAME, str(value)).text
             print(x)
               
    @errors   
    def text_by_class(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.CLASS_NAME, str(value))))
             x = self.driver.find_element(By.CLASS_NAME, str(value)).text
             print(x)
               
    @errors   
    def text_by_id(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.ID, str(value))))
             x = self.driver.find_element(By.ID, str(value)).text
             print(x)

    @errors   
    def text_by_tag(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.TAG_NAME, str(value))))
             x = self.driver.find_element(By.TAG_NAME, str(value)).text
             print(x)
    @errors   
    def text_by_css(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.CSS_SELECTOR, str(value))))
             x = self.driver.find_element(By.CSS_SELECTOR, str(value)).text
             print(x)
               
    @errors   
    def text_by_link_text(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.LINK_TEXT, str(value))))
             x = self.driver.find_element(By.LINK_TEXT, str(value)).text
             print(x)
               
    @errors   
    def text_by_partial_link_text(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, str(value))))
             x = self.driver.find_element(By.PARTIAL_LINK_TEXT, str(value)).text
             print(x)
               
    @errors   
    def text_by_xpath(self, value):
             WebDriverWait(self.driver, self.wait).until(ec.presence_of_element_located((By.XPATH, str(value))))
             x = self.driver.find_element(By.XPATH, str(value)).text
             print(x)
               
    def script(self, dom):
           self.driver.execute_script(dom)
           
        
    def refresh(self):
           self.driver.refresh()
    def back(self):
           self.driver.back()
    def forward(self):
           self.driver.forward()
    def title(self):
           print(self.driver.title)
     
                    
        

        
    @errors
    def screenshot(self, path):
          
         
         
         file = Path(path)


         if ".png" in path:
              if file.is_file() == False:
                   
                  self.path = self.driver.save_screenshot(path)
                  print(f"The Screenshot Is Saved As {path}")

              else:
                   print(Fore.RED+"File Already Exists In Given Directory, Kindly Change File Name!")
                   print(Style.RESET_ALL)
              

         



         elif ".png" not in path:
                     split_img = path.split(".",1)
                     rename = path.replace(split_img[1], "png")

                     self.path = self.driver.save_screenshot(rename)

              

                     print(Fore.RED+ """File Must Save With .png Format 
Don't Worry Your Screenshot Is Saved Use .png Format From Next Time!
                    """)
                     print(Style.RESET_ALL)
                     print(f"The Screenshot Is Saved As {rename}")
      
    


       






              
              


     


         

     
     

    

    



            
               


        






        


