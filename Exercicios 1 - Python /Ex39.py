def verificador():
    number = [4,8,7,0]

    fnumber = number[0] * 5
    snumber = number[1] * 4
    tnumber = number[2] * 3
    qnumber = number[3] * 2
    sum_numbers = (fnumber + snumber + tnumber + qnumber) % 11
    agency_number = 11 - sum_numbers

    print(f"Número da Agência: {number} - {agency_number}")

verificador()