from flask import Flask, request, jsonify

app = Flask(__name__)

Contacts = [
    {
        "Contact": "2456789234",
        "Name":  "Yuwin",
        "done": False,
        "id": 1
    },
    {
        "Contact": "7492794291",
        "Name":  "Bittu",
        "done": False,
        "id": 2
    },
    {
        "Contact": "7845667826",
        "Name":  "Latha",
        "done": False,
        "id": 3
    },
    {
        "Contact": "3564298402",
        "Name":  "Rajesh",
        "done": False,
        "id": 4
    },
    {
        "Contact": "6724389123",
        "Name":  "Arun",
        "done": False,
        "id": 5
    }
]
@app.route("/")

@app.route("/add-data", methods=["POST"])

def add_contacts():
    if not request.json:
        return jsonify({
            "status": "Error",
            "message": "Please provide the data"
        }, 400)

        
    Contact = {
        "id": Contacts[-1]["id"] + 1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact", ""),
        "done": False
    }

    Contacts.append(Contact)

    return jsonify({
        "status": "Success",
        "message": "Contact added successfully"
    })

@app.route("/get-data")

def get_contacts():
    return jsonify({
        "data": Contacts
    })

if __name__ == "__main__":
    app.run(debug=True)