from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/get-excel-data', methods=['GET'])
def get_excel_data():
    # 用pandas读取Excel文件
    excel_data = pd.read_excel('path/to/your/excel/file.xlsx')

    # 将数据转换为JSON格式并返回
    return jsonify(excel_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5700)