# Write your MySQL query statement below
update Salary
SET
    sex = CASE sex
        when 'm' then 'f'
        else 'm'
    end