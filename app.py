from flask import Flask, render_template, redirect, url_for, session, request
import os
import random
import string

app = Flask(__name__)
# Set the secret key for sessions (ensure it's kept secret in production)
app.secret_key = os.urandom(24)


@app.route('/question1', methods=['POST', 'GET'])
def question1():
    if request.method == 'POST':
        user_code = request.form.get('user_code')
        correct_code = "1969"  # The correct answer for Question 1

        if user_code == correct_code:
            session['question1_verified'] = True
        else:
            session['question1_verified'] = False

        # Generate a random string (for example, 10 characters long)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return redirect(url_for('question_result', question_id='question1', random_string=random_string))

    return render_template('question1_index.html')


@app.route('/question2', methods=['POST', 'GET'])
def question2():
    if request.method == 'POST':
        user_code = request.form.get('user_code')
        correct_code = "h2o"  # The correct answer for Question 2

        if user_code.lower() == correct_code:
            session['question2_verified'] = True
        else:
            session['question2_verified'] = False

        # Generate a random string (for example, 10 characters long)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return redirect(url_for('question_result', question_id='question2', random_string=random_string))

    return render_template('question2_index.html')


@app.route('/question3', methods=['POST', 'GET'])
def question3():
    if request.method == 'POST':
        user_code = request.form.get('user_code')
        correct_code = "paris"  # The correct answer for Question 3

        if user_code.lower() == correct_code:
            session['question3_verified'] = True
        else:
            session['question3_verified'] = False

        # Generate a random string (for example, 10 characters long)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return redirect(url_for('question_result', question_id='question3', random_string=random_string))

    return render_template('question3_index.html')


# WARNING:Only works for less than 9 ques need to restructure if more
@app.route('/<question_id>/<random_string>/result')
def question_result(question_id, random_string):
    # Check verification status based on the question ID
    verified = session.get(f'{question_id}_verified', False)
    return render_template(f'result{question_id[-1]}.html', verified=verified, question_id=question_id, random_string=random_string)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)

