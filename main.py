from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
a = ['chris', 'idf9ujer9tuswdiw9peowf0h9uf0iwef9h80chrissjieujiugrjfeowihhgwoif9ghfwuhfw8f']
@app.route("/")
def home():
    return render_template('index.html')
@app.route('/<n>/')
def home2(n):
    return render_template('index.html', n=' '+n)

@app.route('/buber/')
def buber():
    return render_template('buber.html')

@app.route('/admin/<n>/')
def admin(n):
    if n in a:
        return redirect(url_for('admin_link', u='idf9ujer9tuswdiw9peowf0h9uf0iwef9h80'+n+'sjieujiugrjfeowihhgwoif9ghfwuhfw8f', n=n))
    else:
        return redirect(url_for("permission_admin", n='admin'))
        

@app.route('/admin/<u>/user/<n>')
def admin_link(u, n):
    if n in a and u in a:
        return render_template('admin_user.html', n=n)
    else:
        return redirect(url_for('permission_admin', n='admin'))

@app.route('/chris/')
def chris():
    return render_template('chris.html')

@app.route('/mum/')
def mum():
    return render_template('mum.html')

@app.route('/dad/')
def dad():
    return render_template('dad.html')

@app.route('/permission_denied/<n>/')
def permission_admin(n):
    return render_template('permission.html', n=n)

if __name__ == "__main__":
  app.run(debug=True)