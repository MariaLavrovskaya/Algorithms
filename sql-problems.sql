-- Write an SQL query to report all the duplicate emails. https://leetcode.com/problems/duplicate-emails/
SELECT Email FROM(SELECT Email from Person group by Email having count(*)>1) Person2;



-- Please write a sql query to get the amount of each follower’s follower if he/she has one. https://leetcode.com/problems/second-degree-follower/
SELECT followee as follower, count(follower) as num from (SELECT distinct * FROM follow) A
WHERE followee IN (select follower from follow) 
GROUP BY followee
ORDER BY follower ASC
