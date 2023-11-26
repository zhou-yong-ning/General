from PyPDF2 import PdfReader, PdfWriter
import os


def split_pdf(input_path, page_numbers, path):
    input_pdf = PdfReader(input_path)
    output_pdf = PdfWriter()
    output_path = os.path.join(path, input_path + '.pdf')  # 拆分后的文件名
    for page_number in page_numbers:
        output_pdf.add_page(input_pdf.pages[(page_number - 1)])  # 页码从0开始，所以需要减1
        output_path = os.path.join(path, input_path + '.pdf')  # 拆分后的文件名
    with open(output_path, "wb") as output_file:
        output_pdf.write(output_file)


def get_pdf_page_count(file_path):
    pdf = PdfReader(file_path)
    page_count = len(pdf.pages)
    return page_count


# 在当前路径创建文件夹
Current_Folder_path = os.getcwd()
if not os.path.exists(Current_Folder_path + '\\NewFolder'):
    os.mkdir(os.path.join(Current_Folder_path, 'NewFolder'))
# 获取指定文件夹内所有文件
file_list = os.listdir(Current_Folder_path)
# 指定存储路径
pdfpath = os.path.join(Current_Folder_path, 'NewFolder')
# 利用推导式获取所有后缀为”.pdf“的文件
pdf_list = [a for a in file_list if a.endswith('.pdf')]
for pdf in pdf_list:
    # 所有页码拆分
    pages_to_split = [i for i in range(1, 1 + get_pdf_page_count(pdf))]
    # 指定需要删除的页面
    del_list = [0, 1]
    for i in del_list:
        del pages_to_split[i]
    # 调用pdf拆分函数
    split_pdf(pdf, pages_to_split, pdfpath)
