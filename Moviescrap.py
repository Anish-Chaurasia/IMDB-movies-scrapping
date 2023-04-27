import bs4
import requests
import  openpyxl

excel=openpyxl.Workbook()
sheet=excel.active

sheet.title="Top 100 movies on imdb"

sheet.append(['top movies'])

url="https://www.imdb.com/list/ls055592025/"
source_code=requests.get(url)

soup=bs4.BeautifulSoup(source_code.text,'lxml')



lister_list=soup.find('div',class_="lister-list").find_all('div',class_="lister-item mode-detail")

for lstr_item_mode_detail in lister_list:

    detail=lstr_item_mode_detail.find('div',class_="lister-item-content").find('h3').a.text
    sheet.append([detail])
excel.save("D:\DATA\Projects\web scrapping\moviesList.xlsx")






