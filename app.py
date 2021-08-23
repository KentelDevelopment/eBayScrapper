from flask import Flask,render_template,request,redirect
import requests
from bs4 import BeautifulSoup



app  = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/whatMachineSees')
def whatMachineSees():
    q = request.args.get('q')
    #Getting the page for webdata
    page = requests.get(f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={q}&_sacat=0")
    return page.content

@app.route('/search')
def search():
    q = request.args.get('q')
    #Getting the page for webdata
    page = requests.get(f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={q}&_sacat=0")
    soup = BeautifulSoup(page.content,"html.parser")
    items = soup.find_all("h3",{"class":"s-item__title"})
    items_html = []
    for i in items:
        items_html.insert(0,i.parent.parent.parent)


    
    return render_template("results.html",items=items,q=q)


app.run(debug=True)