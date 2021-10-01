import tabula
import pandas as pd
#df=tabula.read_pdf("/home/anwesan/Downloads/Test 3 - HSS F318  marks.pdf",pages='all')
#print(type(df))

def csv(df):

    f=tabula.convert_into(df,"output_csv.csv",output_format='csv',pages='all')

def excel(df):
    read_df=pd.DataFrame(df)
    read_df.to_excel("output_excel.xlsx")
def lateX(df):
    read_df=pd.DataFrame(df)
    read_df.to_latex("output_latex.bib")


if __name__ == "__main__":
    l=input("path of pdf stored(dont put space before entering path)")
    print("input number for each format(please restrict to tabular data) \n 1.csv \n 2. excel \n 3. LateX\n for ex: if I want csv then input is 1")
    f=int(input("enter value:"))
    df1=tabula.read_pdf(l, pages='all')
    if f==1:
        csv(l)
        print("done")
    elif f==2:
        excel(df1)
        print("done")
    elif f==3:
        lateX(df1)
        print("done")
    else:
        print("wrong input")


