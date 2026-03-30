from flask import Flask, request, make_response
import os

app = Flask(__name__)
FLAG = open("flag.txt").read().strip()

@app.route("/")
def index():
    return """
    <h2>Fizztech SearchBot v0.1</h2>
    <form method='GET' action='/search'>
        Search: <input name='q'>
        <input type='submit' value='Search'>
    </form>
    """

@app.route("/search")
def search():
    query = request.args.get("q", "")
    # VULNERABLE: User input directly embedded in HTML without escaping
    html = f"""
    <h2>Search Results for: {query}</h2>
    <p>No results found. Try something else!</p>
    <a href='/'>Go back</a>
    """
    resp = make_response(html)
    # Flag is in the cookie — simulate admin bot visiting this page
    resp.set_cookie("flag", FLAG, httponly=False)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)