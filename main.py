## 통합

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from datetime import datetime


def on_button_a_click():
    # ... (A 코드 내용)
    # 파일 입출력을 통해 데이터 읽어오기
    infile = open("your_data.txt", "r", encoding='UTF-8')  # 파일 읽어오기
    lines = len(infile.readlines())  # 줄 수 탐색
    infile.seek(0)  # 파일 처음으로 돌아가기
    line = infile.readline()  # 한 줄 읽기
    data = line.split("\t")  # Tab키를 기준으로 구분된 데이터 분리
    len_data = len(data)
    table = [[0 for j in range(len(data))] for i in range(0, lines)]  # 2차원 배열 선언 (줄 수 x 데이터 수)

    # 2차원 배열에 데이터 저장
    while line != "":  # 라인이 비어있지 않으면
        for col in range(0, lines):  # 반복 column
            for row in range(0, len(data)):  # 반복 row
                table[col][row] = int(data[row])
            line = infile.readline()  # 다음줄 읽기
            data = line.split("\t")  # 데이터 분리

    # 작업자용 화면 출력 프로그램
    window = tk.Tk()
    window.resizable(False, False)  # 창 크기 고정
    window.title("작업자용")


    def view_click():
        order_text.config(state="normal")  # 텍스트 박스 4개의 상태를 normal 로 만들고 비우기
        order_text.delete(0, tk.END)
        production_text.config(state="normal")
        production_text.delete(0, tk.END)
        reject_text.config(state="normal")
        reject_text.delete(0, tk.END)
        processing_text.config(state="normal")
        processing_text.delete(0, tk.END)

        order, production, reject, processing = 0, 0, 0, 0  ##주문량,생산량,불량,진행률

        # 콤보박스 선택값 로드 .get()문자열로 반환
        bx1, bx2, bx3, bx4 = Combx1.get(), Combx2.get(), Combx3.get(), Combx4.get()  # 년,월,품목,부서

        for a in range(0, lines):  ##품목별 주문량 로드
            if (bx1 == str(table[a][0]) and bx2 == str(table[a][1])):  ##선택한 (년,월)이 데이터테이블과 같으면
                if (bx3 == '품목1'):
                    order = table[a][3]
                if (bx3 == '품목2'):
                    order = table[a][4]
                if (bx3 == '품목3'):
                    order = table[a][5]
                if (bx3 == '품목4'):
                    order = table[a][6]
                if (bx3 == '품목5'):
                    order = table[a][7]

        for a in range(0, lines):  ##품목별 가공부 생산량 로드
            if (bx1 == str(table[a][0]) and bx2 == str(table[a][1]) and bx4 == '가공부'):
                if (bx3 == '품목1'):
                    production = table[a][8]
                if (bx3 == '품목2'):
                    production = table[a][9]
                if (bx3 == '품목3'):
                    production = table[a][10]
                if (bx3 == '품목4'):
                    production = table[a][11]
                if (bx3 == '품목5'):
                    production = table[a][12]

        for a in range(0, lines):  ##품목별 품질관리부 생산량 로드
            if (bx1 == str(table[a][0]) and bx2 == str(table[a][1]) and bx4 == '품질관리부'):
                if (bx3 == '품목1'):
                    production = table[a][13]
                if (bx3 == '품목2'):
                    production = table[a][14]
                if (bx3 == '품목3'):
                    production = table[a][15]
                if (bx3 == '품목4'):
                    production = table[a][16]
                if (bx3 == '품목5'):
                    production = table[a][17]

        for a in range(0, lines):  ##품목별 가공부 불량 로드
            if (bx1 == str(table[a][0]) and bx2 == str(table[a][1]) and bx4 == '가공부'):
                if (bx3 == '품목1'):
                    reject = table[a][18]
                if (bx3 == '품목2'):
                    reject = table[a][19]
                if (bx3 == '품목3'):
                    reject = table[a][20]
                if (bx3 == '품목4'):
                    reject = table[a][21]
                if (bx3 == '품목5'):
                    reject = table[a][22]

        for a in range(0, lines):  ##품목별 품질관리부 불량 로드
            if (bx1 == str(table[a][0]) and bx2 == str(table[a][1]) and bx4 == '품질관리부'):
                if (bx3 == '품목1'):
                    reject = table[a][23]
                if (bx3 == '품목2'):
                    reject = table[a][24]
                if (bx3 == '품목3'):
                    reject = table[a][25]
                if (bx3 == '품목4'):
                    reject = table[a][26]
                if (bx3 == '품목5'):
                    reject = table[a][27]

        ## 출력창 끝(tkinter.END)위치에 로드한 값 입력
        order_text.insert(tk.END, order)
        order_text.config(state="readonly")
        production_text.insert(tk.END, production)
        production_text.config(state="readonly")
        reject_text.insert(tk.END, reject)
        reject_text.config(state="readonly")
        processing = format(production / order if production and order > 0 else 0, '.0%')  ## 진행률 order-complete 를 변경
        processing_text.insert(tk.END, processing)
        processing_text.config(state="readonly")

    def save_click():
        try:
            reject = int(reject_text.get())
            reject_text.config(state="normal")
            reject_text.delete(0, tk.END)

            new_reject = int(new_reject_text.get())
            new_reject_text.config(state="normal")
            new_reject_text.delete(0, tk.END)

            bx1, bx2, bx3, bx4 = Combx1.get(), Combx2.get(), Combx3.get(), Combx4.get()  # 년,월,품목,부서

            if askyesno("확인", "정말 진행하시겠습니까?"):
                for a in range(0, lines):
                    if (bx1 == str(table[a][0]) and bx2 == str(table[a][1]) and bx4 == '가공부'):
                        if (bx3 == '품목1'):  ##년,월,가공부의 품목1에 대해
                            table[a][18] += new_reject  ##데이터테이블 값을 입력창입력 값으로 교체 -> 추가불량만큼 더하게 변경
                            reject = table[a][18]
                        if (bx3 == '품목2'):
                            table[a][19] += new_reject
                            reject = table[a][19]
                        if (bx3 == '품목3'):
                            table[a][20] += new_reject
                            reject = table[a][20]
                        if (bx3 == '품목4'):
                            table[a][21] += new_reject
                            reject = table[a][21]
                        if (bx3 == '품목5'):
                            table[a][22] += new_reject
                            reject = table[a][22]

                for a in range(0, lines):
                    if (bx1 == str(table[a][0]) and bx2 == str(table[a][1]) and bx4 == '품질관리부'):
                        if (bx3 == '품목1'):
                            table[a][23] += new_reject
                            reject = table[a][23]
                        if (bx3 == '품목2'):
                            table[a][24] += new_reject
                            reject = table[a][24]
                        if (bx3 == '품목3'):
                            table[a][25] += new_reject
                            reject = table[a][25]
                        if (bx3 == '품목4'):
                            table[a][26] += new_reject
                            reject = table[a][26]
                        if (bx3 == '품목5'):
                            table[a][27] += new_reject
                            reject = table[a][27]
                reject_text.insert(tk.END, reject)
                reject_text.config(state="readonly")
                infile_write = open("your_data.txt", "w", encoding='UTF-8')
                for L in range(0, lines):
                    for D in range(0, len_data):
                        if D != len_data - 1:
                            infile_write.write(str(table[L][D]) + "\t")
                        else:
                            infile_write.write(str(table[L][D]))
                    infile_write.write("\n")
                infile_write.close()
            else:
                reject_text.insert(tk.END, reject)
                reject_text.config(state="readonly")
        except ValueError:
            showerror("오류", "숫자를 입력해주세요")
        # 날짜 고르기 콤보박스

    def save_click2():
        try:
            production = int(production_text.get())
            order = int(order_text.get())
            production_text.config(state="normal")
            production_text.delete(0, tk.END)
            new_production = int(new_production_text.get())
            new_production_text.config(state="normal")
            new_production_text.delete(0, tk.END)
            bx1, bx2, bx3, bx4 = Combx1.get(), Combx2.get(), Combx3.get(), Combx4.get()  # 년,월,품목,부서

            if askyesno("확인", "정말 진행하시겠습니까?"):
                for a in range(0, lines):  ##품목별 가공부 생산량 로드
                    if (bx1 == str(table[a][0]) and bx2 == str(table[a][1]) and bx4 == '가공부'):
                        if (bx3 == '품목1'):
                            table[a][8] += new_production
                            production = table[a][8]
                        if (bx3 == '품목2'):
                            table[a][9] += new_production
                            production = table[a][9]
                        if (bx3 == '품목3'):
                            table[a][10] += new_production
                            production = table[a][10]
                        if (bx3 == '품목4'):
                            table[a][11] += new_production
                            production = table[a][11]
                        if (bx3 == '품목5'):
                            table[a][12] += new_production
                            production = table[a][12]

                for a in range(0, lines):  ##품목별 품질관리부 생산량 로드
                    if (bx1 == str(table[a][0]) and bx2 == str(table[a][1]) and bx4 == '품질관리부'):
                        if (bx3 == '품목1'):
                            table[a][13] += new_production
                            production = table[a][13]
                        if (bx3 == '품목2'):
                            table[a][14] += new_production
                            production = table[a][14]
                        if (bx3 == '품목3'):
                            table[a][15] += new_production
                            production = table[a][15]
                        if (bx3 == '품목4'):
                            table[a][16] += new_production
                            production = table[a][16]
                        if (bx3 == '품목5'):
                            table[a][17] += new_production
                            production = table[a][17]

                production_text.insert(tk.END, production)
                production_text.config(state="readonly")
                infile_write = open("your_data.txt", "w", encoding='UTF-8')
                for L in range(0, lines):
                    for D in range(0, len_data):
                        infile_write.write(str(table[L][D]) + "\t")
                    infile_write.write("\n")
                infile_write.close()
                processing = format(production / order if production and order > 0 else 0,
                                    '.0%')  ## 진행률 order-complete 를 변경
                processing_text.insert(tk.END, processing)
                processing_text.config(state="readonly")
            else:
                production_text.insert(tk.END, production)
                productiont_text.config(state="readonly")
        except ValueError:
            showerror("오류", "숫자를 입력해주세요")
            production_text.insert(tk.END, production)
            production_text.config(state="readonly")

        # 날짜 고르기 콤보박스

    years = set()  ## 집합 자료형 생성 함수 add=하나 update=여러개 remove=제거 discard=안전 제거
    for Y in range(0, lines):
        years.add(table[Y][0])  # 첫 번째 열 값(년도)을 집합에 추가

    months = set()
    for M in range(0, lines):
        months.add(table[M][1])

    window.grid_columnconfigure(0, minsize=20)
    window.grid_columnconfigure(5, minsize=20)
    window.grid_rowconfigure(0, minsize=20)
    window.grid_rowconfigure(5, minsize=10)
    window.grid_rowconfigure(7, minsize=10)
    window.grid_rowconfigure(9, minsize=10)  ## 7열 10만큼 간격 rowconfigure 는 행

    Combx1_label = tk.Label(window, text="년", font=("Arial", 20))  ## 년
    Combx1_label.grid(row=1, column=2)
    Combx1 = tk.ttk.Combobox(window, width=10, font=("Arial", 20))
    Combx1['values'] = tuple(sorted(years))  # 정렬된 튜플로 설정
    Combx1.current()  ## 콤보박스 기본설정된 값 0=1행 1=2행
    Combx1.grid(row=1, column=1)

    Combx2_label = tk.Label(window, text="월", font=("Arial", 20))  ## 월
    Combx2_label.grid(row=2, column=2)
    Combx2 = tk.ttk.Combobox(window, width=10, font=("Arial", 20))
    Combx2['value'] = tuple(sorted(months))
    Combx2.current()
    Combx2.grid(row=2, column=1)

    Combx3 = tk.ttk.Combobox(window, width=10, font=("Arial", 20))  ## 품목
    Combx3['value'] = ('품목1', '품목2', '품목3', '품목4', '품목5')
    Combx3.current()
    Combx3.grid(row=3, column=1)

    Combx4 = tk.ttk.Combobox(window, width=10, font=("Arial", 20))  ## 부서
    Combx4['value'] = ('가공부', '품질관리부')
    Combx4.current()
    Combx4.grid(row=4, column=1)

    view_btn = tk.Button(window, text="보기", command=view_click, width=10, font=("Arial", 20))  ## 로드 버튼
    view_btn.grid(row=6, column=1)
    save_btn = tk.Button(window, text="양품 입력", command=save_click2, width=10, font=("Arial", 20))  ## 양품입력 버튼
    save_btn.grid(row=6, column=4)
    save_btn = tk.Button(window, text="불량 입력", command=save_click, width=10, font=("Arial", 20))  ## 불량입력 버튼
    save_btn.grid(row=8, column=4)

    new_production_text = tk.Entry(window, width=5, font=("Arial", 50), textvariable=int)  ## 추가생산량
    new_production_text.grid(row=6, column=3)

    new_reject_text = tk.Entry(window, width=5, font=("Arial", 50), textvariable=int)  ## 추가불량
    new_reject_text.grid(row=8, column=3)

    order_label = tk.Label(window, text="주문내역", font=("Arial", 20))
    order_label.grid(row=1, column=3)
    order_text = tk.Entry(window, width=15, font=("Arial", 20), state="readonly")  ## 주문량
    order_text.grid(row=1, column=4)

    production_label = tk.Label(window, text="양품", font=("Arial", 20))
    production_label.grid(row=2, column=3)
    production_text = tk.Entry(window, width=15, font=("Arial", 20), state="readonly")  ## 생산량
    production_text.grid(row=2, column=4)

    reject_label = tk.Label(window, text="불량품", font=("Arial", 20))
    reject_label.grid(row=3, column=3)
    reject_text = tk.Entry(window, width=15, textvariable=int, font=("Arial", 20), state="readonly")  ## 불량
    reject_text.grid(row=3, column=4)

    processing_label = tk.Label(window, text="진행률", font=("Arial", 20))
    processing_label.grid(row=4, column=3)
    processing_text = tk.Entry(window, width=15, font=("Arial", 20), state="readonly")  ## 진행률
    processing_text.grid(row=4, column=4)


# B 코드를 실행하는 함수
def on_button_b_click():
    def calculate_defective_items():
        # 날짜별 불량품 수량을 저장할 딕셔너리 초기화
        defective_items_by_date = {}

        department = department_var.get()
        start_date_str = start_date_entry.get()
        end_date_str = end_date_entry.get()

        result_text.config(state="normal")  # 결과 텍스트 위젯을 수정 가능한 상태로 변경
        result_text.delete(1.0, tk.END)  # 이전 결과 지우기

        # 입력된 문자열을 날짜로 변환
        start_date = datetime.strptime(start_date_str, "%Y-%m")
        end_date = datetime.strptime(end_date_str, "%Y-%m")

        with open("your_data.txt", "r") as infile:
            for line in infile:
                data = line.strip().split('\t')
                year, month = int(data[0]), int(data[1])
                date = datetime(year, month, 1)  # 날짜를 datetime 객체로 생성

                if start_date <= date <= end_date:
                    if department == "가공부":
                        # 불량품 데이터는 19번째 열부터 23번째 열까지
                        defective_data = [int(data[i]) for i in range(18, 23)]
                    elif department == "품질관리팀":
                        # 불량품 데이터는 24번째 열부터 28번째 열까지
                        defective_data = [int(data[i]) for i in range(23, 28)]

                    # 불량품 수량 누적
                    defective_items_by_date[date] = defective_items_by_date.get(date, [0, 0, 0, 0, 0])
                    for i in range(5):
                        defective_items_by_date[date][i] += defective_data[i]

        # 결과 출력
        for date, defective_items in defective_items_by_date.items():
            result_text.insert(tk.END, f"{date.strftime('%Y-%m')} 불량품 수량:\n")
            result_text.insert(tk.END,
                               f"품목1: {defective_items[0]}, 품목2: {defective_items[1]}, 품목3: {defective_items[2]}, "
                               f"품목4: {defective_items[3]}, 품목5: {defective_items[4]}\n\n")

        result_text.config(state="disabled")

    def compare_quality():
        start_date_str = start_date_entry.get()
        end_date_str = end_date_entry.get()
        department = department_var.get()

        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)

        # 입력된 문자열을 날짜로 변환
        start_date = datetime.strptime(start_date_str, "%Y-%m")
        end_date = datetime.strptime(end_date_str, "%Y-%m")

        with open("your_data.txt", "r") as infile:
            for line in infile:
                data = line.strip().split('\t')
                year, month = int(data[0]), int(data[1])
                date = datetime(year, month, 1)  # 날짜를 datetime 객체로 생성
                if start_date <= date <= end_date:
                    quality_status = "미완료"
                    if department == "가공부":
                        a_values = list(map(int, data[3:8]))
                        b_values = list(map(int, data[8:13]))
                        a_sum = sum(a_values)
                        b_sum = sum(b_values)
                        quality_status = "완료" if a_sum == b_sum else "미완료"
                        b_values_desc = "품목1: {0}, 품목2: {1}, 품목3: {2}, 품목4: {3}, 품목5: {4}".format(*b_values)
                        if quality_status == "미완료":
                            difference = [str(-(a - b)) for a, b in zip(a_values, b_values)]
                            result_text.insert(tk.END, "품질관리팀의 남은 업무량:\n\n")
                            result_text.insert(tk.END,
                                               "품목1: {0}, 품목2: {1}, 품목3: {2}, 품목4: {3}, 품목5: {4}\n\n".format(
                                                   *difference))


                    elif department == "품질관리팀":
                        c_values = list(map(int, data[8:13]))
                        d_values = list(map(int, data[13:18]))
                        c_sum = sum(c_values)
                        d_sum = sum(d_values)
                        quality_status = "완료" if c_sum == d_sum else "미완료"
                        c_values_desc = "품목1: {0}, 품목2: {1}, 품목3: {2}, 품목4: {3}, 품목5: {4}".format(*c_values)
                        if quality_status == "미완료":
                            difference = [str(-(c - d)) for c, d in zip(c_values, d_values)]
                            result_text.insert(tk.END, "품질관리팀의 남은 업무량:\n\n")
                            result_text.insert(tk.END,
                                               "품목1: {0}, 품목2: {1}, 품목3: {2}, 품목4: {3}, 품목5: {4}\n\n".format(
                                                   *difference))

                    if department == "가공부":
                        # Insert for "가공부"
                        result_text.insert(tk.END, f"{year}년-{month}월\n\n주문 내역 (가공부):\n\n")
                        result_text.insert(tk.END,
                                           f"품목1: {data[3]}, 품목2: {data[4]}, 품목3: {data[5]}, 품목4: {data[6]}, 품목5: {data[7]}\n\n")
                        result_text.insert(tk.END, "가공부에서 생산한 양품 수량:\n\n")
                        result_text.insert(tk.END, f"{b_values_desc}\n\n")

                    if department == "품질관리팀":
                        result_text.insert(tk.END, f"{year}년-{month}월\n\n주문 내역 (품질관리팀):\n\n")
                        result_text.insert(tk.END,
                                           f"품목1: {data[8]}, 품목2: {data[9]}, 품목3: {data[10]}, 품목4: {data[11]}, 품목5: {data[12]}\n\n")
                        result_text.insert(tk.END, "가공부에서 생산한 양품 수량:\n\n")
                        result_text.insert(tk.END, f"{c_values_desc}\n\n")
                        print(c_values_desc)

    def calculate_and_filter():
        start_date_str = start_date_entry.get()
        end_date_str = end_date_entry.get()
        department = department_var.get()

        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)

        # 입력된 문자열을 날짜로 변환
        start_date = datetime.strptime(start_date_str, "%Y-%m")
        end_date = datetime.strptime(end_date_str, "%Y-%m")

        with open("your_data.txt", "r") as infile:
            for line in infile:
                data = line.strip().split('\t')
                year, month = int(data[0]), int(data[1])
                date = datetime(year, month, 1)  # 날짜를 datetime 객체로 생성

                if start_date <= date <= end_date:
                    result_text.insert(tk.END, f"{year}년-{month}월\n\n주문 내역:\n\n")
                    result_text.insert(tk.END, f"품목1: {data[3]}, 품목2: {data[4]}, 품목3: {data[5]}, "
                                               f"품목4: {data[6]}, 품목5: {data[7]}\n\n")
                    result_text.insert(tk.END, "-" * 40 + "\n")
        result_text.config(state="disabled")

    def calculate_results():
        start_date_str = start_date_entry.get()
        end_date_str = end_date_entry.get()

        try:
            # 날짜 문자열을 datetime 객체로 변환합니다.
            start_date = datetime.strptime(start_date_str, "%Y-%m")
            end_date = datetime.strptime(end_date_str, "%Y-%m")

            # 파일에서 데이터를 읽어옵니다. 파일 이름은 "your_data.txt"로 가정합니다.
            with open("your_data.txt", "r") as infile:
                data = [line.strip().split('\t') for line in infile]

            result_text.config(state="normal")
            result_text.delete("1.0", "end")  # 이전 텍스트 지우기

            results = []  # 결과를 저장할 리스트

            for row in data:
                year, month = int(row[0]), int(row[1])
                date = datetime(year, month, 1)  # 날짜를 datetime 객체로 생성

                if start_date <= date <= end_date:
                    x_values = [float(val) for val in row[3:8]]
                    y_values = [float(val) for val in row[8:13]]
                    z_values = [float(val) for val in row[13:18]]  # 괄호 추가

                    result_string = f"{year}년-{month}월\n\n"

                    # 각 품목에 대한 결과를 추가
                    for i, (x, y, z) in enumerate(zip(x_values, y_values, z_values)):  # 괄호 추가
                        if z == 0:
                            result_string += f"품목 {i + 1}: -\n"
                        else:
                            result = (x + y) / (z * 2) * 100
                            result_string += f"품목 {i + 1}: {result:.2f}%\n"

                    results.append(result_string)

                    # 결과를 텍스트 위젯에 추가
                    result_text.insert(tk.END, result_string)
                    result_text.insert(tk.END, "\n")

            result_text.config(state="disabled")

        except (ValueError, FileNotFoundError):
            result_text.config(state="normal")
            result_text.delete("1.0", "end")
            result_text.insert(tk.END, "날짜 형식이 올바르지 않거나 파일을 찾을 수 없습니다.")
            result_text.config(state="disabled")

    root = tk.Tk()
    root.title("작업자 모드")

    def calculate_loss():
        start_date_str = start_date_entry.get()
        end_date_str = end_date_entry.get()
        department = department_var.get()

        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)

        # 입력된 문자열을 날짜로 변환
        start_date = datetime.strptime(start_date_str, "%Y-%m")
        end_date = datetime.strptime(end_date_str, "%Y-%m")

        # 각 품목에 대한 계산법 딕셔너리 설정
        loss_calculation_methods = {
            1: {"가공부": 6000, "품질관리팀": 10000},
            2: {"가공부": 7000, "품질관리팀": 12000},
            3: {"가공부": 4000, "품질관리팀": 15000},
            4: {"가공부": 4000, "품질관리팀": 9000},
            5: {"가공부": 10000, "품질관리팀": 20000}
        }

        with open("your_data.txt", "r") as infile:
            for line in infile:
                data = line.strip().split('\t')
                year, month = int(data[0]), int(data[1])
                date = datetime(year, month, 1)

                if start_date <= date <= end_date:
                    x_values = list(map(int, data[18:23]))
                    y_values = list(map(int, data[23:28]))

                    result_string = f"{year}년-{month}월\n\n손실액 계산 (부서: {department}):\n\n"

                    for i in range(5):
                        material_price = loss_calculation_methods[i + 1][department]
                        if department == "가공부":
                            loss = x_values[i] * material_price
                            result_string += f"품목 {i + 1}: {loss} 원\n"
                        elif department == "품질관리팀":
                            loss = y_values[i] * material_price
                            result_string += f"품목 {i + 1}: {loss} 원\n"

                    result_text.insert(tk.END, result_string)
                    result_text.insert(tk.END, "\n")
        result_text.config(state="disabled")

    def on_department_selected(department):
        if department == "가공부" or department == "품질관리팀":
            calculate_button.config(state="normal")
        else:
            calculate_button.config(state="disabled")

    # "부서선택" 라벨 및 버튼 생성
    department_label = tk.Label(root, text="부서 선택")
    department_label.pack()

    department_var = tk.StringVar()
    department_var.set("선택하세요")

    department_option_menu = tk.OptionMenu(root, department_var, "선택하세요", "가공부", "품질관리팀",
                                           command=lambda x: on_department_selected(department_var.get()))
    department_option_menu.pack()

    # "시작 날짜 입력" 라벨 및 입력 필드 생성
    start_date_label = tk.Label(root, text="시작 날짜 (YYYY-MM):")
    start_date_label.pack()
    start_date_entry = tk.Entry(root)
    start_date_entry.pack()

    # "종료 날짜 입력" 라벨 및 입력 필드 생성
    end_date_label = tk.Label(root, text="종료 날짜 (YYYY-MM):")
    end_date_label.pack()
    end_date_entry = tk.Entry(root)
    end_date_entry.pack()

    # 결과를 표시할 텍스트 위젯 생성
    result_text = tk.Text(root, wrap=tk.WORD, width=80, height=30)
    result_text.pack()

    # "계산" 버튼 생성
    calculate_button = tk.Button(root, text="남은 업무량 확인", state="disabled", command=compare_quality)
    calculate_button.pack()
    calculate_button.config(state="normal")

    calculate_button = tk.Button(root, text="불량품 총 갯수 확인", state="disabled", command=calculate_defective_items)
    calculate_button.pack()
    calculate_button.config(state="normal")

    calculate_button = tk.Button(root, text="주문 내역 출력", state="disabled", command=calculate_and_filter)
    calculate_button.pack()
    calculate_button.config(state="normal")

    calculate_loss_button = tk.Button(root, text="손실액 계산", state="disabled", command=calculate_loss)
    calculate_loss_button.pack()
    calculate_loss_button.config(state="normal")

    # "진행률 확인" 버튼 생성
    calculate_button2 = tk.Button(root, text="진행률 확인", state="disabled", command=calculate_results)
    calculate_button2.pack()
    calculate_button2.config(state="normal")
    root.mainloop()

    # Tkinter 창 생성


window = tk.Tk()
window.title("작업 관리 창")
window.geometry("400x200")

# A 코드 실행 버튼
button_a = tk.Button(window, text="작업자형", command=on_button_a_click, width=25, height=5)
button_a.pack(side="left", padx=10)  # 버튼을 창에 추가하고 여백(pady)를 설정

# B 코드 실행 버튼
button_b = tk.Button(window, text="관리자형", command=on_button_b_click, width=25, height=5)
button_b.pack(side="right", padx=10)  # 버튼을 창에 추가하고 여백(pady)를 설정

# Tkinter 창 유지
window.mainloop()