from flask import Flask, render_template,request,redirect  
app = Flask(__name__)
List_Up =[]

@app.route("/")
def Main():
    return render_template("index.html", List_Up=List_Up)

@app.route("/Add", methods=["POST"])
def Add():
    Up_ = request.form.get("Up_")
    List_Up.append(Up_)
    return redirect('/')

@app.route("/Delete", methods=["POST"])
def Delete():
    Up_ = request.form.get("Up_")
    List_Up.remove(Up_)
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)    