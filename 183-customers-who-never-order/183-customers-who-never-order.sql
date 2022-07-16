/* Write your T-SQL query statement below */
select name as Customers from Customers where Not Exists (select * from Orders where Orders.customerId = Customers.Id)