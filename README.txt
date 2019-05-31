The initial query:

CREATE TABLE FrequentBrowsers AS
SELECT COUNT(p.id) as counts, p.first_name, p.last_name 
FROM people as p 
INNER JOIN visits as v ON p.id = v.personId 
GROUP BY p.id 
ORDER BY counts 
DESC LIMIT 10;


To run
docker build -t solution .
docker run -p 5000:5000 solution
open http://127.0.0.1:5000/frequent in the browser

