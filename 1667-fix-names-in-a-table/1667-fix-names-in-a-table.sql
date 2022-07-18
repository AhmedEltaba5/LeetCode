/* Write your T-SQL query statement below */
SELECT user_id, concat(upper(substring(name,1,1)),lower(substring(name,2,len(name)))) as name FROM Users
order by user_id