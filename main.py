# -*- coding: utf-8 -*-
from managers.manager import StudentManager
from storage.jsonstorage import JsonStorage

# 定义数据文件路径
FILE_PATH = "student_management.txt"

def show_menu():
    """打印功能菜单"""
    print("=" * 30)
    print("===== 学生成绩管理系统 =====")
    print("1. 添加学生")
    print("2. 查看全部学生")
    print("3. 查询学生")
    print("4. 修改学生成绩")
    print("5. 删除学生")
    print("6. 保存数据到文件")
    print("7. 从文件加载数据")
    print("0. 退出系统")
    print("=" * 30)

def main():
    stu_manager = StudentManager()
    storage = JsonStorage(FILE_PATH)

    while True:
        show_menu()
        choice = input("请输入功能序号：")

        if choice == "1":
            # 添加学生
            stu_manager.add_student()

        elif choice == "2":
            # 查看所有学生
            print("\n----- 全部学生信息 -----")
            stu_manager.show_student()

        elif choice == "3":
            # 查询学生
            name = input("请输入要查询的学生姓名：")
            res = stu_manager.search_student(name)
            if res:
                print("\n查询结果：")
                print(res)
            else:
                print(f"未找到姓名为 {name} 的学生")

        elif choice == "4":
            # 修改成绩
            name = input("请输入要修改的学生姓名：")
            try:
                new_score = int(input("请输入新成绩："))
                flag = stu_manager.modify_student(name, new_score)
                if flag:
                    print("成绩修改成功！")
                else:
                    print("修改失败，该学生不存在")
            except ValueError:
                print("成绩必须是数字！")

        elif choice == "5":
            # 删除学生
            name = input("请输入要删除的学生姓名：")
            flag = stu_manager.delete_student(name)
            if flag:
                print("删除成功！")
            else:
                print("删除失败，该学生不存在")

        elif choice == "6":
            # 保存到文件
            storage.save(stu_manager.students)
            print(f"数据已保存至 {FILE_PATH}")

        elif choice == "7":
            # 加载文件数据
            try:
                students = storage.load()
                stu_manager.set_students(students)
                print("数据加载完成！")
            except FileNotFoundError:
                print("文件不存在，暂无数据")
            except Exception as e:
                print(f"加载失败：{e}")

        elif choice == "0":
            print("感谢使用，程序退出！")
            break

        else:
            print("输入错误，请选择0-7之间的数字！")

        input("\n按回车键返回菜单...")
        print("\n")

if __name__ == "__main__":
    main()