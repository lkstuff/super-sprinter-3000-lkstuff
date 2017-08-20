from flask import Flask, render_template, redirect, request, session
import csv
import os
import uuid

app = Flask(__name__)

def get_id():
    new_id = uuid.uuid4()
    return str(new_id)


def read_csv(file_name):
    data = []
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            data.append(row)
    return data


def write_csv(file_name):
    with open(file_name, "w") as csvfile:
        datawriter = csv.writer(csvfile, delimiter=';')
        datawriter.writerows(file_name)

# def data_for_csv(**kwargs):
#     data_list = []
#     for name, value in kwargs.items():
#         data_list.appened(value)
#     return data_list


@app.route('/')
def route_index():
    data_list = read_csv("story.csv")
    return render_template('list.html', table=data_list)


@app.route('/edit-note')
def route_edit():
    note_text = None
    if 'note' in session:
        note_text = session['note']
    return render_template('form.html')


@app.route('/save-note', methods=['POST'])
def route_save():
    print('POST request received!')
    #data_for_csv("form.html")
    session['note'] = request.form['note']
    #write_csv('note')
    return redirect('/')


if __name__ == '__main__':
    app.secret_key = '123321mmm'
    app.run(
        debug=True,
        port=5000
    )