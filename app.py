from flask import Flask, render_template, request


app = Flask("__name__")

def filesToList(result):
    stringResult = str(result)
    #removes unnecessary text in begining and end
    stringResult = stringResult[20:-3]
    print("StringResult after slicing:", stringResult)
    lstResult = stringResult.split("),")
    print("lstResult:", lstResult)
    for i in range(len(lstResult)):
        x = lstResult[i].replace("(\'state\'", "")
        x = x.replace("(\'state\'", "")
        x = x.replace("(\'state\'", "")
        x = x.replace("(\'zip-code\'", "")
        x = x.replace("(\'price_range\'", "")
        x = x.replace("(\'renaming\'", "")
        x = x.replace("(\'newName\'", "")
        x = x.replace(", \'", "")
        x = x.replace("\'", "")
        x = x.replace(" ", "")
        lstResult[i] = x
    print("lstResult after removal:", lstResult)
    return lstResult

#Landing page
@app.route("/")
def home():
    return render_template("index3.html")

@app.route("/infoForm")
def form():
        return render_template("main.html")

@app.route("/resultForm", methods = ["POST", "GET"])
def resultForm():
        if request.method == "POST":
            results = request.form
            print(results)
            print("After converting")
            filesToList(results)
            return render_template("index2.html")
        else:
              "error in result form"

if __name__ == "__main__":
    #app.run(host = '192.168.8.180', port = 5051, debug = True)
    app.run(debug = True)