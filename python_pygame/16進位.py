# 接收數入
a = input("您要轉換為多少進位：")
# 判斷要怎麼轉換
if a == "16":
    # 執行16進位轉換
    decimal_number = int(input("輸入十進位數字: "))  # 輸入十進位數字
    hex_number = hex(decimal_number)  # 將十進位數字轉換為16進位數字
    print("16進位數字:", hex_number)  # 輸出16進位數字
elif a == "10":
    # 執行10進位轉換
    def hex_to_decimal(hex_str):
        try:
            decimal_num = int(hex_str, 16)
            return decimal_num
        except ValueError:
            return None

    hex_input = input("請輸入16進位數值：")
    decimal_output = hex_to_decimal(hex_input)
    if decimal_output is not None:
        print("轉換後的10進位數值為", decimal_output)
    else:
        print("輸入的不是有效的16進位數值。")

