from flask import Flask, jsonify

app = Flask(__name__)

def calculate_metrics(marks_list):
    if not marks_list:
        return 0, 0
    total = sum(marks_list)
    average = total / len(marks_list)
    return total, round(average, 2)

@app.route('/')
def home():
    student_marks = [85, 90, 80]
    total, average = calculate_metrics(student_marks)
    
    return jsonify({
        "pipeline_status": "Push 1 Complete",
        "marks_received": student_marks,
        "total_marks": total,
        "average_marks": average
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
