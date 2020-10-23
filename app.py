from flask import Flask, render_template,request
from tweets import QueryTwitter
import pandas as pd
import json

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
	if request.method == "GET":
            (a,b,c,d,e,f,aa,bb,cc,dd,ee,ff,aaa,bbb,ccc,ddd,eee,fff,g)=QueryTwitter("trend")
            f=f.replace("%23","#")
            ff=ff.replace("%23","#")
            fff=fff.replace("%23","#")
            return render_template('index.html',doughnut=json.dumps(a),tweet_map=b,sources_plot=json.dumps(c),sentiment_pie=json.dumps(d),table=json.dumps(e), tt_table= json.dumps(g), search=f, doughnut1=json.dumps(aa),tweet_map1=bb,sources_plot1=json.dumps(cc),sentiment_pie1=json.dumps(dd),table1=json.dumps(ee), search1=ff,doughnut2=json.dumps(aaa),tweet_map2=bbb,sources_plot2=json.dumps(ccc),sentiment_pie2=json.dumps(ddd),table2=json.dumps(eee), search2=fff)

	else:
		search = request.form["srch-term"]
		(a,b,c,d,e)=QueryTwitter(search)
		return render_template('index.html',doughnut=json.dumps(a),tweet_map=b,sources_plot=json.dumps(c),sentiment_pie=json.dumps(d),table=json.dumps(e),search=search)

	return "<h1>Something went wrong !! </h1>"

if __name__ == "__main__":
	app.run(host="0.0.0.0")
