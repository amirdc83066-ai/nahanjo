
#محاسبه های اماری روی دیتا (تحلیل ناهنجاری : z-score , IQR )



# کتابخانه‌های تحلیل آماری


import numpy as np



# استانداردسازی شکل داده

def prepare_array(data_array):
        
        if len(data_array.shape) == 1 :
            data_array = data_array.reshape(-1, 1)
            return(data_array)
        elif len(data_array.shape) == 2:
            return(data_array)
        else : 
            raise TypeError("شکل دیتا نادرست است.")
        
        

# محاسبه اطلاعات آماری پایه       
 
        
def calculate_basic_stats(data_array):
    mean = np.mean(data_array, axis = 0)
    std = np.std(data_array, axis = 0, ddof=1)
    shape = data_array.shape
    
      
    status_data = {
  "میانگین": mean.item() ,
  "انحراف معیار": std.item(),
  "تعداد ردیف ها": shape[0],
  "تعداد ستون ها": shape[1]
}
    
    return(status_data, mean, std)  


# محاسبه محدوده ناهنجاری با IQR


def calculate_IQR_Bounds(data_array):
    
    data_array = data_array.flatten()
    
    data_array_sorted = np.sort(data_array) 
    
    q_1 = np.percentile(data_array_sorted, 25)
    
    q_3 = np.percentile(data_array_sorted, 75)
    
    iqr = q_3 - q_1
        
    if iqr == 0:
        return(0, None, None)
    
    lower_bound = q_1 - 1.5 * iqr
    
    upper_bound = q_3 + 1.5 * iqr
    
    return(iqr, lower_bound, upper_bound)



# تشخیص ناهنجاری با روش IQR
    
    
def detect_anomalies_IQR(data_array, lower_bound, upper_bound, iqr):
        
    data_array = data_array.flatten()
    
    anomaly_count = 0
    
    total_count = len(data_array)
    
    iqr_list = []
            

    for i in range(total_count):
        index = i
        
        value = data_array[i]
        
        if value < lower_bound or value > upper_bound :
            
            anomalies_value = value
            
            anomaly_count += 1
            
        # محاسبه شدت ریسک
            
        if value > upper_bound:
            distance = value - upper_bound
            
            risk_score = (distance / iqr) * 100
        
            risk_score = min(risk_score, 100)
            
            if risk_score < 30:
                category_iqr = "کم"
            elif risk_score < 70:
                category_iqr = "متوسط"
            else:
                category_iqr = "شدید" 

            
        elif value < lower_bound :
            distance = lower_bound - value 
            
            risk_score = (distance / iqr) * 100
        
            risk_score = min(risk_score, 100)
            
            if risk_score < 30:
                category_iqr = "کم"
            elif risk_score < 70:
                category_iqr = "متوسط"
            else:
                category_iqr = "شدید" 
                
                
               
            
        if value < lower_bound or value > upper_bound :
            
            result_iqr_dict = {
                "داده ناهنجار " : value,
                "نمره ریسک" : risk_score,
                "شدت ناهنجاری " : category_iqr
            }
            
            iqr_list.append(result_iqr_dict)
            
                
    percentage = (anomaly_count / total_count) * 100
            
    final_dict_iqr = {
        "نوع فرمول محاسبه ناهنجاری" : "IQR (Interquartile Range)",
        "مجموع تمام داده ها " : total_count,
        "تعداد ناهنجاری ها " : anomaly_count,
        "نسبت ناهنجاری ها به کل" : percentage,
        "ناهنجاری ها " : iqr_list
    }
            
        
    return(final_dict_iqr)                


# محاسبه مقادیر Z-Score

    
def calculate_z_scores(data_array, mean, std):
    
    
    if np.any(std == 0) :
        
        raise ValueError("انحراف معیار خالی شد!دیتا مشکل دارد")
            
    z_score = (data_array - mean) / std
    z_score = z_score.flatten()
    
    return(z_score)


# تنظیم پویا آستانه Z-Score

def auto_threshold_zscore(data_array):

    data_array = data_array.flatten()

    zero_ratio = np.sum(data_array == 0) / len(data_array)

    mean = np.mean(data_array)

    std = np.std(data_array, ddof=1)

    if std == 0:
        return 3

    if zero_ratio >= 0.5:
        threshold = 2
    elif zero_ratio >= 0.2:
        threshold = 2.5
    else:
        threshold = 3

    return threshold


# تشخیص ناهنجاری با Z-Score

def detect_anomalies_zscores(data_array, z_scores, threshold):
    anomaly_table = []
    abs_z = np.abs(z_scores)
    mask = abs_z > threshold
    mask = mask.flatten()

    for i in range(len(data_array)):
        if mask[i]:
            value = data_array.item(i)
            risk_score = min(100, (abs_z[i] / threshold) * 100)
            if abs_z[i] < 3:
                category = "کم"
            elif abs_z[i] < 5:
                category = "متوسط"
            else:
                category = "شدید"




            anomaly_dict = {
                "نوع فرمول محاسبه ": "z-score",
                "شماره": i,
                "مقدار": value,
                "مقدار ریسک": risk_score,
                "اندازه ناهنجاری": category
            }
            anomaly_table.append(anomaly_dict)

            
            
                
                              
    
    mask_sum = np.sum(mask)
    
    len_data = int(len(data_array))
    
    perctage = (int(mask_sum)/len_data) * 100
    
        
    result_dict_zscores = {
        "تعداد دیتا های دریافت شده" : len_data,
        
        "تعداد ناهنجاری ها" : int(mask_sum),
        
        "درصد ناهنجاری به کل" : perctage,
        
        "داده های ناهنجار" : anomaly_table
        
    }
    
    return(result_dict_zscores)

# تشخیص ناهنجاری با Isolation Forest

def detect_anomalies_isolation_forest(data_series,):
    from sklearn.ensemble import IsolationForest
    import numpy as np
    import pandas as pd

    data_series = np.asarray(data_series).reshape(-1)

    clean_data = pd.to_numeric(data_series, errors="coerce")
    clean_data = pd.Series(clean_data).dropna()

    if clean_data.empty:
        return {
            "وضعیت": "داده معتبر برای تحلیل وجود ندارد."
        }

    values = clean_data.values.reshape(-1, 1)

    model = IsolationForest(
        n_estimators=300,
        contamination=0.05,
        random_state=42
    )

    # آموزش مدل

    model.fit(values)

    predictions = model.predict(values)

    raw_scores = model.score_samples(values)

    anomaly_indices = np.where(predictions == -1)[0]

    if len(anomaly_indices) == 0:
        return {
            "نوع فرمول محاسبه ناهنجاری": "Isolation Forest",
            "تعداد کل داده ها": len(values),
            "تعداد ناهنجاری ها": 0,
            "درصد ناهنجاری": 0,
            "داده های ناهنجار": []
        }

    anomaly_scores = raw_scores[anomaly_indices]
    
    min_score = anomaly_scores.min()
    
    max_score = anomaly_scores.max()

    mean_val = clean_data.mean()
    
    std_val = clean_data.std()

    anomalies = []

    all_final_risks = []
    
    temp_results = []
    
    for idx in anomaly_indices:
        
        value = float(values[idx][0])
        
        score = float(raw_scores[idx])
        
        normalized_score = ((max_score - score) / (max_score - min_score) if max_score != min_score else 0)
        
        z_score = abs((value - mean_val) / std_val) if std_val != 0 else 0
        
        final_risk = (normalized_score * 0.7) + (min(z_score / 6, 1) * 0.3)
        
        all_final_risks.append(final_risk)
        
        temp_results.append((idx, value, final_risk))

    thr_critical = np.percentile(all_final_risks, 95)
    
    thr_severe = np.percentile(all_final_risks, 85)
    
    thr_medium = np.percentile(all_final_risks, 65)

    for idx, value, final_risk in temp_results:
        
        risk_percent = round(final_risk * 100, 2)
        
        # محاسبه نمره ریسک ناهنجاری‌ها

        if final_risk >= thr_critical:
            severity = "بحرانی"
        elif final_risk >= thr_severe:
            severity = "شدید"
        elif final_risk >= thr_medium:
            severity = "متوسط"
        else:
            severity = "کم"

        anomalies.append({
            "نوع فرمول محاسبه": "Isolation Forest",
            "شماره": int(idx),
            "مقدار": value,
            "نمره ریسک": risk_percent,
            "شدت ناهنجاری": severity
        })

    anomalies = sorted(
        anomalies,
        key=lambda x: x["نمره ریسک"],
        reverse=True
    )

    return {
        "نوع فرمول محاسبه ناهنجاری": "Isolation Forest",
        "تعداد کل داده ها": len(values),
        "تعداد ناهنجاری ها": len(anomalies),
        "درصد ناهنجاری": round((len(anomalies) / len(values)) * 100, 2),
        "داده های ناهنجار": anomalies
    }


# اجرای کامل فرایند تحلیل    
    
    
def run_numpy_analysis(data_array):
        
    data_array = prepare_array(data_array)

    
    status_data, mean, std= calculate_basic_stats(data_array)
    
    z_scores = calculate_z_scores(data_array, mean, std)

    threshold = auto_threshold_zscore(data_array)

    anomaly_dict_zscores = detect_anomalies_zscores(data_array, z_scores, threshold)
 
    
    iqr, lower_bound, upper_bound = calculate_IQR_Bounds(data_array)

    if iqr == 0:
        iqr_dict = {
            "نوع فرمول محاسبه ناهنجاری": "IQR (Interquartile Range)",
            "وضعیت": "انجام نشد",
            "دلیل": "پراکندگی داده صفر است (IQR = 0)"
        }
    else:
        iqr_dict = detect_anomalies_IQR(data_array, lower_bound, upper_bound, iqr)
        
    isolation_dict = detect_anomalies_isolation_forest(data_array)


          
    final_result = {
        "وضعیت کلی داده" : status_data,
        "محاسبه با z-scores " : anomaly_dict_zscores,
        "محاسبه با IQR" : iqr_dict,
        "محاسبه با Isolation Forest": isolation_dict
    }    
    
    
    return(final_result)

    
