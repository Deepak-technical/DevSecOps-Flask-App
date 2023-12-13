from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple dictionary acting as a mock database
users = {
    1: {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    2: {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
}

# Route to display all users
@app.route('/users', methods=['GET'])
def get_users():
    return render_template('users.html', users=users)

# Route to display a specific user by ID
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return "User not found", 404
    return render_template('user.html', user=user)

# Route to handle form submission for adding a new user
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # For simplicity, generate an ID based on the number of current users
        new_user_id = len(users) + 1
        new_user = {'id': new_user_id, 'name': name, 'email': email}
        users[new_user_id] = new_user
        return redirect(url_for('get_users'))
    return render_template('add_user.html')

# Route to delete a user by ID
@app.route('/user/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    if request.method == 'POST':
        user = users.get(user_id)
        if not user:
            return "User not found", 404
        del users[user_id]
        return redirect(url_for('get_users'))

if __name__ == '__main__':
    app.run(debug=True)
