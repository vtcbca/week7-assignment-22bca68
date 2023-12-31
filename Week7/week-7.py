import csv
import pandas as pd
header=['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']
with open("C:\\sqlite3\\csv\\selling.csv","w",newline='') as csvfile:
    data=csv.writer(csvfile)
    data.writerow(header)
#Add 12 Records. by taking input from user.
l=[]
with open("c:\\sqlite3\\csv\\selling.csv",'a',newline="") as file:
    insert =csv. writer(file)
    for i in range(12):
        prod_no = input("Enter Product Number: ")
        prod_name = input("Enter Product Name: ")
        jan = int(input("Enter January Sales: "))
        feb = int(input("Enter February Sales: "))
        mar = int(input("Enter March Sales: "))
        apr = int(input("Enter April Sales: "))
        may = int(input("Enter May Sales: "))
        jun = int(input("Enter June Sales: "))
        data=[prod_no,prod_name,jan,feb,mar,apr,may,jun]
        l.append(data)
    insert.writerows(l)
#Change Column Name Product No, Product Name, January, February, March, April, May, June.
df=pd.header=['Product_NO','Product_Name','January','February','March','April','May',' June']
print(df)
#Add column "Total Sell" to count total of all month and "Average Sell"
header=['Product_NO','Product_Name','January','February','March','April','May',' June']
df=pd.read_csv("c:\\sqlite3\\csv\\product_selling.csv")
row=df.values.tolist()
total=[sum(i[2::]) for i in row]
average=[int(sum(i[2::])/6) for i in row]

df = pd.DataFrame(row,columns=header)
df['Total']=total
df['Average']=average

print(df)
#Add 2 row at the end.
new_rows = {'Product No': '', 'Product Name': '', 'January': '', 'February': '', 'March': '', 'April': '', 'May': '', 'June': ''}
for i in range(2):
    for column in new_rows:
        new_rows[column] = input(f"Enter value for {column}: ")
df = df.append(new_rows, ignore_index=True)
df.reset_index(drop=True, inplace=True)
#add 2 row after 3rd row
h=['Prod_No', 'prod_Name', 'Jan', 'Feb', 'March', 'Apr', 'May', 'June','Total','Average']
df.loc[2.5] = [1, 'ac',1290,7128,7456,4325,3874,2002,26075,4345.8333333]
df = df.sort_index().reset_index(drop=True)
df.loc[3.5] = [16, 'laptop',1140,1148,2260,2245,2256,2221,11270,1878.333333]
df = df.sort_index().reset_index(drop=True)
#Print first 5 row.
print("FIRST FIVE ROWS")
print(df.head())
#Print Last 5 row.
print("LAST 5 ROWS")
print(df.tail())
# Print row 6 to 10.
print("ROW BETWEEN 6 TO 10")
print(df.loc[6:10])
#Print only product name.
print(df["Product Name"])
# Print sell of January month with product id and product name.
print(df[["Product No", "Product Name", "Jan"]])
