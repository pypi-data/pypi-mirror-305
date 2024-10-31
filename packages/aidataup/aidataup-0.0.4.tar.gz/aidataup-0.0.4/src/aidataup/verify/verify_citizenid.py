
def checkPID(pid):
    if len(pid) != 13:  # ถ้า pid ไม่ใช่ 13 ให้คืนค่า False
        return False
    num = 0  # ค่าสำหรับอ้างอิง index list ข้อมูลบัตรประชาชน
    num2 = 13  # ค่าประจำหลัก
    listdata = list(pid)  # list ข้อมูลบัตรประชาชน
    total = 0  # ผลลัพธ์
    # Calculate the checksum
    while num < 12:
        total += int(listdata[num]) * (num2 - num)  # นำค่า num เป็น index list แต่ละตัว * (num2 - num) แล้วรวมเข้ากับ sum
        num += 1  # เพิ่มค่า num อีก 1
    digit13 = total % 11  # sum หาร 11 เอาเศษ
    # Determine the value of the last digit
    if digit13 == 0:  # ถ้าเศษ = 0
        digit13 = 1  # ค่าหลักที่ 13 คือ 1
    elif digit13 == 1:  # ถ้าเศษ = 1
        digit13 = 0  # ค่าหลักที่ 13 คือ 0
    else:
        digit13 = 11 - digit13  # ถ้าเศษไม่ใช่กับอะไร ให้เอา 11 - digit13
    # Check if the last digit is correct
    if digit13 == int(listdata[12]):  # ถ้าค่าหลักที่ 13 เท่ากับค่าหลักที่ 13 ที่ป้อนข้อมูลมา คืนค่า True
        return True
    else:  # ถ้าค่าหลักที่ 13 ไม่เท่ากับค่าหลักที่ 13 ที่ป้อนข้อมูลมา คืนค่า False
        return False
    


def verify_citizenid_format(cid):
    if cid is None:
        return False

    # Remove non-numeric characters from the ID tax
    validate_cid = ''.join(char for char in cid if char.isdigit())

    # Check if the cleaned ID tax is exactly 13 digits
    if len(validate_cid) != 13:
        return False

    # Validate the ID tax using the checkPID function
    if checkPID(validate_cid):
        return True
    else:
        return False
    

