
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/

SELECT 
CASE
    when a+b<=c or a+c<=b or b+c<=a then 'Not A Triangle'
    when a=b and b=c then 'Equilateral'
    when a=b and not(a=c) Then 'Isosceles'
    when a=b and not(b=c) Then 'Isosceles'
    when a=c and not(a=b) Then 'Isosceles'
    when a=c and not(c=b) Then 'Isosceles'
    when b=c and not(c=a) Then 'Isosceles'
    when b=c and not(b=a) Then 'Isosceles'
    else 'Scalene'
END AS TypeText
FROM TRIANGLES;