name_1=input("what is name_1 :")
name_2=input("what is name_2 :")
name_3=input("what is name_3 :")

no_of_slice=input("how many slices in pizza: ")
price_of_pizza=input("what is the price of pizza: ")

percentage_ate_pizza_name_1=input(name_1+"what is the percentage of pizza by ate:")
percentage_ate_pizza_name_2=input(name_2+"what is the percentage of pizza by ate:")
percentage_ate_pizza_name_3=input(name_3+"what is the percentage of pizza by ate:")

num_of_slices_ate_person_1=float(percentage_ate_pizza_name_1)*float(no_of_slice)
num_of_slices_ate_person_2=float(percentage_ate_pizza_name_2)*float(no_of_slice)
num_of_slices_ate_person_3=float(percentage_ate_pizza_name_3)*float(no_of_slice)

price_payed_by_num_1=float(percentage_ate_pizza_name_1)*float(price_of_pizza)
price_payed_by_num_2=float(percentage_ate_pizza_name_2)*float(price_of_pizza)
price_payed_by_num_3=float(percentage_ate_pizza_name_3)*float(price_of_pizza)

print(name_1+"have ate "+str(num_of_slices_ate_person_1)+" slice and have "+str(price_payed_by_num_1)+"$ payed for his meal")
print(name_2+"have ate "+str(num_of_slices_ate_person_2)+" slice and have "+str(price_payed_by_num_2)+"$ payed for his meal")
print(name_3+"have ate "+str(num_of_slices_ate_person_3)+" slice and have "+str(price_payed_by_num_3)+"$ payed for his meal")

