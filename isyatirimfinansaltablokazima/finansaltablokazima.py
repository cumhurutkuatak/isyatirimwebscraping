import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time






# url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=ACSEL"
# r = requests.get(url)
# s = BeautifulSoup(r.text, "html.parser")
#
# s1 = s.find("select", {"id": "ddlAddCompare"})
#
# s2 = s1.find("optgroup").find_all("option")


hisseler = []
with open("hisseler.csv", "r") as dosya:
    okuyucu = csv.reader(dosya)
    for i in okuyucu:
        ("".join(i))
        hisseler.append("".join(str(x) for x in i))

def site():
  option = webdriver.ChromeOptions()
  option.add_argument("--headless")
  driver = webdriver.Chrome(options=option)
  driver.get("https://halkyatirim.com.tr/skorkart")

  time.sleep(5)

  sec = driver.find_element(By.XPATH,"//*[@id='DropDownEnstrumanKodu']")
  sec.click()
  time.sleep(5)

  s = Select(sec)
  s.select_by_value(hisse)
  time.sleep(10)

  return driver

def bir():
    page = site().page_source
    soup = BeautifulSoup(page,"html.parser")
    tablo = soup.find("table",{"id":"TBLPAZARENDEKSLERI"})
    tablo = pd.read_html(str(tablo),flavor="bs4")[0]
    # tablo2 = pd.DataFrame(tablo)
    tablo = tablo.rename(columns={"Unnamed: 0":"Özellikler", "Unnamed: 1":"Bilgiler"})
    tablo.to_excel("veriler.xlsx", sheet_name="Pazar ve Endeksleri", index=False)


def iki():
    page = site().page_source
    soup = BeautifulSoup(page,"html.parser")
    tablo = soup.find("table",{"id":"TBLFIYATPERFORMANSI"})
    tablo = pd.read_html(str(tablo),flavor="bs4")[0]
    tablo = tablo.rename(columns={"Unnamed: 0":"Kalemler"})
    print(tablo)
    tablo.to_excel("veriler.xlsx", sheet_name="Fiyat ve Performans", index=False)

def uc():
    page = site().page_source
    soup = BeautifulSoup(page,"html.parser")
    tablo = soup.find("table",{"id":"TBLPIYASADEGER"})
    tablo = pd.read_html(str(tablo),flavor="bs4")[0]
    tablo = tablo.rename(columns={"Unnamed: 0":"Kalemler", "Unnamed: 1":"Değerler"})
    print(tablo)
    tablo.to_excel("veriler.xlsx", sheet_name="Piyasa Değeri", index=False)
def dort():
    page = site().page_source
    soup = BeautifulSoup(page, "html.parser")
    tablo = soup.find("table", {"id": "TBLTEKNIKVERI"})
    tablo = pd.read_html(str(tablo), flavor="bs4")[0]
    tablo = tablo.rename(columns={"Unnamed: 0":"Teknik", "Unnamed: 1":"Değerler", "Unnamed: 2":"Yorumlar"})
    print(tablo)
    tablo.to_excel("veriler.xlsx", sheet_name="Teknik Veri", index=False)

def bes():
    page = site().page_source
    soup = BeautifulSoup(page, "html.parser")
    tablo = soup.find("table", {"id": "TBLTEMELANALIZ"})
    tablo = pd.read_html(str(tablo), flavor="bs4")[0]
    tablo = tablo.rename(columns={"Unnamed: 0":"Kalemler", "Unnamed: 1":"Değerler"})
    print(tablo)
    tablo.to_excel("veriler.xlsx", sheet_name="Temel Analiz", index=False)

def alti():
    page = site().page_source
    soup = BeautifulSoup(page, "html.parser")
    tablo = soup.find("table", {"id": "TBLFIYATOZET"})
    tablo = pd.read_html(str(tablo), flavor="bs4")[0]
    tablo = tablo.rename(columns={"Unnamed: 0":"Kalemler", "Unnamed: 1":"Değerler"})
    print(tablo)
    tablo.to_excel("veriler.xlsx", sheet_name="Fiyat ve Özet", index=False)

def yedi():
    page = site().page_source
    soup = BeautifulSoup(page, "html.parser")
    tablo = soup.find("table", {"id": "TBLFINANSALVERİLER3"})
    tablo = pd.read_html(str(tablo), flavor="bs4")[0]
    print(tablo)
    tablo.to_excel("veriler.xlsx", sheet_name="Finansal Veriler3", index=False)

def sekiz():
    page = site().page_source
    soup = BeautifulSoup(page, "html.parser")
    tablo = soup.find("table", {"id": "TBLFINANSALVERİLER2"})
    tablo = pd.read_html(str(tablo), flavor="bs4")[0]
    print(tablo)
    tablo.to_excel("veriler.xlsx", sheet_name="Finansal Veriler2", index=False)
def dokuz():
    page = site().page_source
    soup = BeautifulSoup(page, "html.parser")
    tablo = soup.find("table", {"id": "TBLFINANSALVERİLER1"})
    tablo = pd.read_html(str(tablo), flavor="bs4")[0]
    print(tablo)
    tablo.to_excel("veriler.xlsx", sheet_name="Finansal Veriler1", index=False)


while True:
    hisse = input("Lütfen Hisse Kodunu Giriniz:")
    hisse = hisse.upper()

    if hisse in hisseler:
        print("Devam Ediliyor...")
        time.sleep(5)

        s = ["Pazar ve Endeksleri", "Fiyat Performansı", "Piyasa Değeri", "Teknik Veriler", "Temel Analiz Verileri", "Fiyat Özeti", "Finansallar", "Kârlılık", "Çarpanlar"]

        print("1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n6 - {}\n7 - {}\n8 - {}\n9 - {}"
              .format(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8]))

        while True:
            giris = input("Lütfen istediğiniz tablo kodunu giriniz...")

            if giris in ["1","2","3","4","5","6","7","8","9"]:
                print("Devam Ediliyor...")
                time.sleep(5)

                if giris == "1":
                    bir()
                    break
                elif giris == "2":
                    iki()
                    break
                elif giris == "3":
                    uc()
                    break
                elif giris == "4":
                    dort()
                    break
                elif giris == "5":
                    bes()
                    break
                elif giris == "6":
                    alti()
                    break
                elif giris == "7":
                    yedi()
                    break
                elif giris == "8":
                    sekiz()
                    break
                elif giris == "9":
                    dokuz()
                    break

            else:
                print("Lütfen geçerli bir tablo kodu giriniz...\n")

        break

    else:
        print("Lütfen geçerli bir hisse kodu giriniz...")
        time.sleep(5)











