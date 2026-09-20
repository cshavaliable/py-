# records = [
#     {"type1" = "收入", "amount": 100, "note" = "工资"},
#     {"type2" = "支出", "amount":20, "note" = "吃饭"}
# ])
records = []
while True:
    print("1. 记一笔收入")
    print("2. 记一笔支出")
    print("3. 查看所有记录")
    print("4. 查看统计")
    print("5. 退出")
    choice = input("你的选择为:")
    if choice == "1":
        amount = float(input("金额："))
        note = input("备注：")
        records.append({"amount": amount, "note": note, "type": "收入"})
        print("恭喜完成记录")
    elif choice == "2":
        amount= float(input("金额:"))
        note = input("备注:")
        records.append({"amount": amount, "note": note, "type": "支出"})
        print("恭喜完成记录")
    elif choice == "3":
        if not records:
            print("暂无记录")
        for r in records:
            st_amount = r["amount"]
            st_note = r["note"]
            print(f"金额:{st_amount}备注{st_note}", )
    elif choice == "4":
        income = sum(r["amount"] for r in records if r["type"] == "收入")
        expense = sum(r["amount"] for r in records if r["type"] == "支出")
        print(f"总收入：{income:.2f}")
        print(f"总支出：{expense:.2f}")
        print(f"结余：{income - expense:.2f}")
    elif choice == "5":
        break

