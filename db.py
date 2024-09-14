import sqlite3

db_name = "quiz.db"
connection = None
cursor = None

def open():
    global connection, cursor
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

def close():
    cursor.close()
    connection.close()

def get_questions(quiz_id):
    open()
    SQL = ''' 
        SELECT question.question,
                question.answer,
                question.wrong1,
                question.wrong2,
                question.wrong3,
                quiz.name
        FROM question, quiz, quiz_connect
        WHERE question_id == quiz_connect.question_id
        AND quiz.id == quiz_connect.quiz_id
        AND quiz_connect.quiz_id == ?;
    '''
    cursor.execute(SQL, [quiz_id])
    result = cursor.fetchall()
    close()
    return result

def get_quizes():
    open()
    SQL = '''
            SELECT * FROM quiz;
    '''
    cursor.execute(SQL)
    result = cursor.fetchall()
    close()
    return result

if __name__ == "__main__":
    open()

    cursor.execute("SELECT * FROM quiz")
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM question")
    print(cursor.fetchall())

    close()