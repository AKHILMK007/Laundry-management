from flask import Flask, render_template,request
import mysql.connector
from datetime import date
app = Flask(__name__)

# MySQL configuration
mydb = mysql.connector.connect(
    host="localhost",
    user="employee",
    password="111",
    database="laundry"
)

@app.route('/')
def home():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM laundry")
    data = cursor.fetchall()
    return render_template('home.html', data=data)




@app.route('/clothes_count')
def clothes_count():
    sql = """
        SELECT cbag_id, COUNT(*) as clothes_count
        FROM clothes
        WHERE cbag_id IN (
            SELECT bag_id FROM laundry WHERE o_status != 'complete'
        )
        GROUP BY cbag_id
    """
    
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    results = mycursor.fetchall()

    return render_template('clothes_count.html', results=results)



mycursor = mydb.cursor()
@app.route('/update_status', methods=['GET', 'POST'])
def update_status():
    if request.method == 'POST':
        bag_id = request.form['bag_id']
        o_status = request.form['o_status']

        # Update o_status in the laundry table
        # update_sql = "UPDATE laundry SET o_status = %s WHERE bag_id = %s"
        # mycursor.execute(update_sql, (o_status, int(bag_id)))
       # today_date = date.today()
        # Update o_status in the laundry table for rows where bag_id matches and date is less than today
       # update_sql = "UPDATE laundry SET o_status = %s WHERE bag_id = %s AND date < %s"
       # mycursor.execute(update_sql, (o_status, int(bag_id), today_date))
       # mydb.commit()
        mycrsor = mydb.cursor()
        update_sql = "CALL update_status_and_clothes_v2(%s, %s)"
        mycrsor.execute(update_sql, (int(bag_id), o_status))
        mydb.commit()
        return "Status updated successfully!"

    return render_template('update_status.html')





@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        srn = request.form['srn']
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        hostel_block = request.form['hostel_block']
        room_number = request.form['room_number']

        # Insert student details into the student table
        insert_sql = "INSERT INTO student (SRN, Name, phone, email, hostel_block, room_number) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(insert_sql, (srn, name, phone, email, hostel_block, room_number))
        mydb.commit()

        return render_template('add_student.html')

    return render_template('add_student.html')





if __name__ == '__main__':
    app.run(debug=True)
    mycursor.close()
    mydb.close()