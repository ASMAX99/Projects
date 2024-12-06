from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_algorithm", methods=["POST"])
def run_algorithm():
    data = request.json
    array = data.get("array", [])
    sorted_array = sorted(array)  # Example: Replace with actual algorithm logic.
    return jsonify({"sorted_array": sorted_array})

if __name__ == "__main__":
    app.run(debug=True)
