from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        ampm = request.form['ampm']
        hours = int(request.form['hours'])
        cacl_datetime = date + ' ' + time + ' ' + ampm
        initial_datetime = datetime.datetime.strptime(cacl_datetime, '%m/%d/%Y %I:%M %p')
        final_datetime = initial_datetime + datetime.timedelta(hours=hours)
        format_datetime = final_datetime.strftime("%b %d, %I:%M %p")
        return render_template('index.html', result=format_datetime, hours=hours)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
