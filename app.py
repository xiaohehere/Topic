from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

def process_excel(input_path, output_path, region):
    df = pd.read_excel(input_path)
    df['ID_prefix'] = df['ID'].str.split('_').str[0]
    grouped = df.groupby('ID_prefix').agg({
        '区域': 'first',
        '网元名': 'first',
        '逻辑站点名': 'first',
        '小区中文名': 'first',
        '经度': 'first',
        '纬度': 'first',
        'GB': 'sum',
        '日均话务量Erl': 'sum'
    }).reset_index()
    filtered = grouped[(grouped['区域'] == region) & (grouped['网元名'].str.contains('W'))]
    sorted_filtered = filtered.sort_values(by='日均话务量Erl', ascending=False)
    sorted_filtered.to_excel(output_path, index=False)

def compare_and_find_abnormal(file1, file2, id_column, value_column, output_file):
    table1 = pd.read_excel(file1)
    table2 = pd.read_excel(file2)
    merged_df = pd.merge(table1, table2, on=id_column, suffixes=('_table1', '_table2'))
    merged_df['difference'] = abs(merged_df[f'{value_column}_table1'] - merged_df[f'{value_column}_table2'])
    merged_df['max_value'] = merged_df[[f'{value_column}_table1', f'{value_column}_table2']].max(axis=1)
    merged_df['threshold'] = merged_df['max_value'] * 0.5
    abnormal_data_step2 = merged_df[merged_df['difference'] > merged_df['threshold']][id_column]
    abnormal_data_step3 = table1[table1[value_column] > 50][id_column]
    abnormal_ids = pd.Series(list(set(abnormal_data_step2).intersection(set(abnormal_data_step3))))
    abnormal_rows = table1[table1[id_column].isin(abnormal_ids)]
    abnormal_rows.to_excel(output_file, index=False)

@app.route('/upload', methods=['POST'])
def upload_files():
    file1 = request.files['file1']
    file2 = request.files['file2']
    region = request.form['region']
    
    file1.save('file1.xlsx')
    file2.save('file2.xlsx')

    output_file = '异常数据MID.xlsx'
    compare_and_find_abnormal('file1.xlsx', 'file2.xlsx', 'ID', 'GB', output_file)

    input_path = output_file
    output_path = f'异常数据_{region}.xlsx'
    process_excel(input_path, output_path, region)

    if os.path.exists(input_path):
        os.remove(input_path)
    if os.path.exists('file1.xlsx'):
        os.remove('file1.xlsx')
    if os.path.exists('file2.xlsx'):
        os.remove('file2.xlsx')
    
    return jsonify({"message": "Files processed successfully", "output_file": output_path})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5700)
