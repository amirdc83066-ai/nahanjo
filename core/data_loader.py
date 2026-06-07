#لود کردن دیتا فایل (excel & csv)


# کتابخانه‌های مدیریت و تحلیل داده

import pandas as pd

import os

from numpy_analysis import run_numpy_analysis

from ai_client import run_ai_analysis



# بارگذاری فایل داده

def read_file(file_path):
    
    file_path = file_path.lower()
        
    if file_path.endswith(".csv") :
            
        data_frame = pd.read_csv(file_path)
            
    elif file_path.endswith((".xlsx" , ".xls")):
            
        data_frame = pd.read_excel(file_path)
                
    else:
        raise TypeError("پسوند فایل اشتباه است.")
                
    if not os.path.exists(file_path):
        raise FileNotFoundError("فایل پیدا نشد و بارگزاری نشد.")

    

    return(data_frame)



# استخراج نام ستون‌ها

def columns_name(data_frame):
    columns = data_frame.columns
    
    columns = list(columns)
    
    return(columns)



# بررسی عددی بودن ستون انتخاب‌شده

def validate_numeric_column(data_frame, column_name):
    
    if column_name not in data_frame.columns:
        raise ValueError("ستون وجود ندارد")
    
    column_data = data_frame[column_name]
    
    data_type = column_data.dtype
    
    numeric_check = pd.api.types.is_numeric_dtype(data_type)
    
    if numeric_check is not True:
        raise TypeError("ستون عددی نیست")
    
    return(numeric_check)


# آماده‌سازی داده برای تحلیل آماری

def prepare_column_for_numpy(data_frame, column_name):
    
    column_data = data_frame[column_name]
    
    column_data = column_data.dropna()
    
    column_data = pd.to_numeric(column_data)
    
    array_column = column_data.to_numpy()
    
    array_column = array_column.reshape(-1, 1)
    
    return(array_column)


# اجرای کامل فرایند تحلیل داده

def run_full_analysis(file_path, column_name):
    
    try:
    
        df = read_file(file_path)
    
        validate_numeric_column(df, column_name)
    
        array = prepare_column_for_numpy(df, column_name)
    
        numpy_result = run_numpy_analysis(array)
    
        ai_result = run_ai_analysis(array)
    
        final_result = {
            "اسم فایل" : file_path,
            "ستون انالیز شده" : column_name,
            "تعداد سطر ها" : len(array),
            "انالیز و تحلیل عددی" : numpy_result,
            "انالیز و تحلیل هوش مصنوعی" : ai_result
        }
    
        return(final_result)
    
    
    except Exception as e :
        return{"ارور : " : str(e)}
        
    
    
    
    