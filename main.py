from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
a = ['chris', 'idf9ujer9tuswdiw9peowf0h9uf0iwef9h80chrissjieujiugrjfeowihhgwoif9ghfwuhfw8f', "701"]
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        i = request.form.get('search')
        if i == "buber":
            return redirect(url_for('buber'))
        if i == "mum":
            return redirect(url_for("mum"))
        if i == "dad":
            return redirect(url_for("dad"))
        if i == "chris":
            return redirect(url_for("chris"))
        if i == "admin":
            return redirect(url_for("admin1"))
        if i == "pages":
            return redirect(url_for('pages'))
        else:
            return redirect(url_for("err", e="400"))
    return render_template('index.html')

@app.route('/err/<e>/')
def err(e):
    return render_template('error.html', e=e)


@app.route('/<n>/')
def home2(n):
    return render_template('index.html', n=' '+n)

@app.route('/buber/')
def buber():
    return render_template('buber.html')

@app.route('/admin/<n>/<p>')
def admin2(n, p):
    if n in a and p in a:
        return redirect(url_for('admin_link', u='idf9ujer9tuswdiw9peowf0h9uf0iwef9h80'+n+'sjieujiugrjfeowihhgwoif9ghfwuhfw8f', n=n, p=p))
    else:
        return redirect(url_for("permission_admin", n='admin'))

@app.route("/admin/", methods=["GET", "POST"])
def admin1():
    if request.method == "POST":
        req = request.form
        print(req)
        name = request.form.get("name")
        pas = request.form.get("pas")
        if name in a and pas in a:
            return redirect(url_for('admin_link', n=name, u='idf9ujer9tuswdiw9peowf0h9uf0iwef9h80'+name+'sjieujiugrjfeowihhgwoif9ghfwuhfw8f', p=pas))
        else:
            return redirect(url_for('permission_admin', n='admin', u=name, p=pas))
    return render_template('admin.html')

@app.route('/admin/<u>/user/<n>/<p>/')
def admin_link(u, n, p):
    if n in a and u in a and p in a:
        return render_template('admin_user.html', n=n)
    else:
        return redirect(url_for('permission_admin', n='admin', u=n))

@app.route('/chris/')
def chris():
    return render_template('chris.html')

@app.route('/mum/')
def mum():
    return render_template('mum.html')

@app.route('/dad/')
def dad():
    return render_template('dad.html')

@app.route('/permission_denied/<n>/<u>/<p>/')
def permission_admin(n, u, p):
    return render_template('permission.html', n=n, u=u, p=p)

@app.route('/pages/')
def pages():
    return render_template('pages.html')

if __name__ == "__main__":
  app.run(debug=True)