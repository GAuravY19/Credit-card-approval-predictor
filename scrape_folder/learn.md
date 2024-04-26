# Let's do Webscraping

webscrapping ko aise samajh ki ismein hone wale saare steps jo hai na woh wohi steps hote hai jo tu ek website pe karega to get some information.

Bas difference yeh ho jata hai ki yaha pe tu ek information ke liye nahi balki bohot saare information ke liye karta hai and yeh sab kucch automated hota hai.

### 1. Creating Virtual environment and setting it up
    open the terminal in the folder in which you want to work.
```
1. virtualenv venv
2. .\venv\Scripts\activate.ps1
```

### Installation
```
    pip install selenium
    pip install webdriver
```

### Initial Setup of selenum
```
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_experimental_option('detach', True)

    os.environ['PATH'] = r'D:/WebScrapping/WebDrivers/'

    DRIVER = webdriver.Chrome(options=options)

    DRIVER.get('https://www.goibibo.com/')

    DRIVER.maximize_window()
```

### scrapping now starts -->

You will get to see this screen on running above code.

<img src = 'C:\Users\sunil\OneDrive\Desktop\New folder\scrape folder\Screenshot 2024-04-26 185452.png'>


<br><br><br>

ab webscraping kaise hogi yeh samajhte...

Mera pehla kaam hai login/signup wala dialog box ko hatana using selenium.

<img src = 'C:\Users\sunil\OneDrive\Desktop\New folder\scrape folder\Screenshot 2024-04-26 185701.png'>

<br><br>
ab yeh soch tu is dialogue box ko hatane ke liye kya karega, is cross button ko click karega. Toh bas ab hum bhi wohi karenge.

Dekh kaise hoga.

<img src = 'C:\Users\sunil\OneDrive\Desktop\New folder\scrape folder\Screenshot 2024-04-26 190354.png'>

#### Cross box right click > Inspect pe click

<hr>

<img src = 'C:\Users\sunil\OneDrive\Desktop\New folder\scrape folder\Screenshot 2024-04-26 190429.png'>

toh kucch aisa open hoga.Yaha pe cross box ka code highlight hoga. Now comes the `xpath` in picture.

```
    dialogCross = DRIVER.find_element('xpath', '//div//span[@class = "logSprite icClose"]')

    dialogCross.click()
```

Iss code mein kucch yun ki tu `DRIVER` ko provide karega the path of the cross box. Driver usko find karega and then click karega. Is tarah se woh hat jayega.

### The end ...

Ab issi tarah se tujhe aage bhi karna hai.

Maine tujhe books wali website ko scrape karne bola taki tu ek basic website pe scrapping karke pehle comfortable ho za.. kyunki flights ke website thode se complex hote hai. Waha pe tujhe bohot error jhelna padta hai.

And don't give up too early. Hoga, it takes time. For the first time, maine scrapping ka project 4 baar kharab kiya tha. 5 th time pe woh abhi bhi aadha hai.

thik hai.

Pehle itna code run kar. Samajh kaise chalrha. tab tak main dekhta koi aur resoruce hai kya ...

Have patience. I'm sure, tu kalse webscrapping karne lagega.


















