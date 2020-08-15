from flask import Flask,render_template,url_for,request
from modules import create_graph, graph_query, train_word2vec, word2vec_query 
from updates import check_updates

graph = create_graph() 

app = Flask(__name__)

@app.route("/")
#@app.route("/<name>")
def home():
    if check_updates():         #I have decided data update through API call 
        graph = create_graph()  #is not so often required (only once in a week)
        train_word2vec()
    
    return render_template("index.html")

@app.route('/updateresult',methods = ['POST'])
def updateresult():
         
    if request.method == 'POST':
        try:
             SName = request.form['name'] 
        finally:
             return render_template('search.html', tag=SName, graph=graph_query(graph, SName), word2vec=word2vec_query(SName))  
              
  
    
if __name__ == "__main__":
    app.run(debug=True)
