import pandas as pd
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

iphone_df = pd.read_csv('iphone.csv')
#print(iphone_df)
"""1 - The column names have spaces . rename the column names to have underscore '_' instead of space 
(try to do in one go instead of specifying each column nam in rename method)"""
iphone_df.columns = iphone_df.columns.str.replace(" ", "_")
# print(iphone_df.columns)
"""2- start rating for some of the models is missing in the dataset. fill those missing values with the average rating all the models."""
# avg_rating = iphone_df.Star_Rating.mean()
# iphone_df.Star_Rating = iphone_df.Star_Rating.fillna(value = avg_rating)
# print(iphone_df)
"""3- Now instead of filling missing values with avg rating of full dataset , fill with avg rating based on RAM. 
example :  if rating for a 2 gb phone is missing then take average of all other 2 gb phones rating and fill that value. """
# average_ratings_by_ram = iphone_df.groupby('Ram')['Star_Rating'].mean().reset_index()
# average_ratings_by_ram.rename(columns={'Star_Rating': 'Average_Rating'}, inplace=True)
# iphone_df = iphone_df.merge(average_ratings_by_ram, on='Ram', how='left')
# iphone_df['Star_Rating'].fillna(iphone_df['Average_Rating'], inplace=True)
# iphone_df.drop(columns=['Average_Rating'], inplace=True)
# print(iphone_df)
# iphone_df.to_csv('res.csv')
"""4- create a new column in the dataframe "Discount_Percentage" based on MRP and sale value"""
# iphone_df["Discount_Percentage"] = round(((iphone_df.Mrp - iphone_df.Sale_Price) / iphone_df.Mrp)*100,1)
# print(iphone_df)
# iphone_df.to_csv('res.csv')
"""5- which model has highest percent discount ?"""
# iphone_df.sort_values(by = "Discount_Percentage", ascending=False, inplace=True)
# model_with_highest_discount = iphone_df.iloc[0]['Product_Name']
# highest_discount_percentage = iphone_df.iloc[0]['Discount_Percentage']
# print(model_with_highest_discount, highest_discount_percentage)
"""6- find total no of models  each space configuration (128 GB , 64 GB etc)"""
# space_configuration_counts = iphone_df['Ram'].value_counts()
# space_configuration_counts.columns = ['Space Configuration', 'Total Models']
# print(space_configuration_counts)
# def getgb(product_name):
#     color_gb = product_name.split('(')
#     gb = color_gb[1].split(',')
#     return gb[1].strip()
# iphone_df['Space'] = iphone_df.Product_Name.apply(getgb)
# print(iphone_df['Space'].value_counts())
"""7- find total number of models for each color """
# def getcolor(product_name):
#     color_gb = product_name.split('(')
#     gb = color_gb[1].split(',')
#     return gb[0].strip()
# iphone_df['color'] = iphone_df.Product_Name.apply(getcolor)
# print(iphone_df['color'].value_counts())
"""8- find total number of models by iphone version : eg
iphone 8:  9
iphone XR : 5"""
# def getname(product_name):
#     color_gb = product_name.split('(')
#     gb = color_gb[0].split(' ')
#     return " ".join(gb[1:3])
# iphone_df['name'] = iphone_df.Product_Name.apply(getname)
# print(iphone_df['name'].value_counts().reset_index())
"""9- list top 5 models having highest no of reviews 
"""
# def getname(product_name):
#     color_gb = product_name.split('(')
#     gb = color_gb[0].split(' ')
#     return " ".join(gb[1:3])
# iphone_df['name'] = iphone_df.Product_Name.apply(getname)
# df = iphone_df.groupby('name').Number_Of_Reviews.sum().reset_index()
# print(df.sort_values(by='Number_Of_Reviews', ascending=False))
"""10 - what is the price difference between highest price and lowest price iphone (based on mrp)"""
# res = iphone_df.Mrp.max() - iphone_df.Mrp.min()
# print(res)
"""11 - find total no of reviews for iphone 11 and iphone 12 category . Output should have only 2 rows (for 11 and 12).
"""
# def getname(product_name):
#     name_sep = product_name.split("(")
#     model = name_sep[0].split(" ")
#     return " ".join(model[1:3])
# iphone_df["name"]= iphone_df.Product_Name.apply(getname)
# res_df = iphone_df.groupby("name").Number_Of_Reviews.sum().reset_index()
# print(res_df.loc[res_df.name.isin(["iPhone 11","iPhone 12"])])
"""12- which iphone has 3rd highest MRP"""
# sorted_df = iphone_df.sort_values(by = 'Mrp', ascending=False)
# print(sorted_df.iloc[2])
"""13- what is the average mrp of iphones which costs above 100,000"""
# res_df = iphone_df[iphone_df.Mrp > 100000]
# print(round(res_df.Mrp.mean(),2))
"""14- which iphone with 128 GB space has highest ratings to review ratio"""
# df = iphone_df[iphone_df.Product_Name.str.contains('128')]
# df['R2r_ratio'] = round(df.Number_Of_Ratings / df.Number_Of_Reviews,2)
# df.sort_values(by = 'R2r_ratio', ascending=False,inplace = True)
# print(df.iloc[0])
'PROJECT COMPLETED FULL IPHONE DATA ANALYSIS DONE ! '




