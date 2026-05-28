-- SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) FROM Scores 
-- ORDER BY score DESC;

select s1.score,
    (select COUNT(DISTINCT s2.score)
        from Scores s2
        where s2.score >= s1.score
    ) as rank -- find how many unique ranks are greater than the score in question we do it for each score
from Scores s1
order by s1.score desc;