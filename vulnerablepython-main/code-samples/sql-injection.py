from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route('/search')
def search():
    query = request.args.get('query')

    # Vulnerable to SQL injection
    sql = f"SELECT * FROM users WHERE name = '{query}'"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    results = cursor.execute(sql)

    # Fetch and display results
    items = cursor.fetchall()
    return render_template('search.html', items=items)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

# InstructLLM response:
# The code is vulnerable to SQL injection. The following piece of code is the source of the vulnerability: python query = request.args.get('query')  sql = f"SELECT * FROM users WHERE name = '{query}'"
# The problem is that the query variable is not properly sanitized before being used in a SQL query. An attacker could potentially inject malicious SQL code into the query variable, allowing them to execute arbitrary SQL commands on the database. This could lead to sensitive information being leaked, data being modified, or the entire database being compromised.
# To fix this vulnerability, the query variable should be properly sanitized before being used in the SQL query, for example by using the escape_string() function provided by the sqlite3 module.