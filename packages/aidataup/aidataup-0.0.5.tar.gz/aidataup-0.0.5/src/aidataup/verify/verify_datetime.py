from dateutil.parser import parse
from datetime import datetime

    
def verify_datetime_format(date_input, format_list=None, strict_format=False):
    # """
    # verify input is datetime and match with format input 
    # Parameters:
    # - date_input: date input 
    # - format_list: List format ['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y', '%Y/%m/%d'] and (ค่าเริ่มต้นเป็น None)
    # - strict_format: ถ้า True จะตรวจสอบเฉพาะรูปแบบที่ระบุใน format_list

    # Returns:
    # - tuple (is_date, matched_format): is_date = True/False, matched_format = รูปแบบที่ตรงหรือ None
    # """
    if format_list is None:
        format_list = ['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y', '%Y/%m/%d']  # รูปแบบเริ่มต้น

    for fmt in format_list:
        try:
            parsed_date = datetime.strptime(date_input, fmt)
            return True, fmt 
        except ValueError:
            continue

    # if strict_format = False use dateutil 
    if not strict_format:
        try:
            parsed_date = parse(date_input)
            return True, None  
        except ValueError:
            pass

    return False, None


# inputs = [
#     "2024-10-08",    #  %Y-%m-%d
#     "08/10/2024",    #  %d/%m/%Y
#     "08-10-2567",    #  %d-%m-%Y
#     "2024/10/08",    #  %Y/%m/%d
#     "InvalidDate",   # Invalid value
# ]
# for date_str in inputs: 
#     is_date, matched_format = verify_datetime_format(date_str, strict_format=True)
#     print(f"Input: {date_str} -> Is Date: {is_date}, Format: {matched_format}")