# SNEAKER 10 INVENTORY HANDLER
#### Video demo: https://youtu.be/cfUng1Xw9PQ
#### Description:
This project is a terminal application written in the python language and was created in order to help retail stores to be able to manage a large volume of codes, to create lists with defective products, simultaneously it helps in the reservation of products for customers and the validity of SKU codes.

The application was created so as to replace manual recordings using a system strictly and carefully structured which has the ability to read and update data through CSV files, using checks in the log in of the staff.

## PROJECT FILES

- **project.py**: This file is the main execution file of the application and contains the main() function which uses the following functions:
    * load_inventory(filename): With this function the CSV file that includes the store's inventory is read and it converts it into a list of dictionaries making simultaneously the correct conversions in prices, sizes and stock to float.
    * check_stock(inventory,size,id) , get_stock(inventory, expectedStock): These functions search and return the stock of an item as well as locate products with little stock based on the limit set by the store manager
    * reserve(inventory,size, id): Because of this function any salesperson can reserve a product and decrease its stock, while simultaneously the product is added to a list with other reserved products
    * defective(inventory,size,id): This function facilitates the store manager in managing the defective pieces by adding them to a list of defective products in the defective.csv file
    * valid_sku(sku,brand): Here the re library was used so that the products are checked. Additionally extra rules have been applied for the adidas codes where we want 2 letters 4 numbers.

- **test_project.py**: This is the control file which uses pytest checking the functions check_stock, valid_sku, get_stock

- **requirements.txt**: It does not include anything as built-in python libraries were used

** Design Choices
1.**Data management with CSV**: With the choice of the csv library the program can run fast and without burdening the computers of the store while simultaneously they can be easily opened by Excel.
2.**Recording of log-ins**: With the datetime library as well as with the code of each salesperson the time at which they entered the application is saved in the employer_log.csv file, helping in this way the daily recording.
3.**SKU Check with RegEx**: Because of this the store reduces the probabilities of mistake during the typing of an SKU saving time.