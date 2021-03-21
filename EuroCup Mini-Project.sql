#1. Write a SQL query to find the date EURO Cup 2016 started on.
SELECT 
    play_date
FROM
    Test.match_mast
ORDER BY play_date
LIMIT 1;

# 2. Write a SQL query to find the number of matches that were won by penalty shootout.
SELECT 
    COUNT(match_no)
FROM
    euro_cup_2016.match_details
WHERE
    win_lose = 'W' AND decided_by = 'P';
    
 # 3. Write a SQL query to find the match number, date, and score for matches in which no stoppage time was added in the 1st half.
-- I don't think the goal_score field is displayed correctly, the data type should be int. Thoughts?
SELECT 
    match_no, play_date, goal_score
FROM
    euro_cup_2016.match_mast
WHERE
    stop1_sec = 0;
    
# 4. Write a SQL query to compute a list showing the number of substitutions that happened in various stages of play for the entire tournament
-- How to define susbstitution and whether I'm picking the correct base ?
SELECT 
    COUNT(player_id) AS substitution_num
FROM
    euro_cup_2016.player_in_out po
        JOIN
    match_mast mm ON po.match_no = mm.match_no
WHERE
    in_out = 'I';

# 5. Write a SQL query to find the number of bookings that happened in stoppage time.
SELECT 
    COUNT(player_id) AS booking_num
FROM
    (SELECT 
        pb.*, stop1_sec, stop2_sec
    FROM
        euro_cup_2016.player_booked pb
    JOIN match_mast mm ON pb.match_no = mm.match_no
    WHERE booking_time != 0
        AND (stop1_sec = 0
        OR stop2_sec = 0)) nt;

# 6. Write a SQL query to find the number of matches that were won by a single point, but do not include matches decided by penalty shootout.
SELECT 
    COUNT(match_no)
FROM
    euro_cup_2016.match_details
WHERE
    win_lose = 'W' AND decided_by != 'P'
        AND goal_score = 1;

# 7. Write a SQL query to find all the venues where matches with penalty shootouts were played.
SELECT DISTINCT
    (sv.venue_name)
FROM
    euro_cup_2016.penalty_shootout ps
        JOIN
    match_mast mm ON ps.match_no = mm.match_no
        JOIN
    soccer_venue sv ON mm.venue_id = sv.venue_id;

# 8. Write a SQL query to find the match number for the game with the highest number of penalty shots, and which countries played that match.
SELECT 
    nt.match_no, sc.country_name
FROM
    (SELECT 
        md.*, ar.country_id
    FROM
        euro_cup_2016.match_details md
    LEFT JOIN asst_referee_mast ar ON md.ass_ref = ar.ass_ref_id) nt
        LEFT JOIN
    soccer_country sc ON nt.country_id = sc.country_id
ORDER BY penalty_score DESC
LIMIT 1;

# 9. Write a SQL query to find the goalkeeper’s name and jersey number, playing for Germany, who played in Germany’s group stage matches.
SELECT DISTINCT
    (player_name), jersey_no
FROM
    euro_cup_2016.match_details md
        JOIN
    player_mast pm ON md.player_gk = pm.player_id
        JOIN
    soccer_country sc ON md.team_id = sc.country_id
WHERE
    play_stage = 'G'
        AND country_name = 'Germany';
        
# 10. Write a SQL query to find all available information about the players under contract to Liverpool F.C. playing for England in EURO Cup 2016.
SELECT 
    pm.*, country_name
FROM
    euro_cup_2016.player_mast pm
        JOIN
    soccer_country sc ON pm.team_id = sc.country_id
WHERE
    playing_club LIKE '%Liverpool%'
        AND country_name = 'England';

#11. Write a SQL query to find the players, their jersey number, and playing club who were the goalkeepers for England in EURO Cup 2016.
SELECT 
    player_name, jersey_no, playing_club
FROM
    euro_cup_2016.player_mast pm
        JOIN
    soccer_country sc ON pm.team_id = sc.country_id
WHERE
    posi_to_play = 'GK'
        AND country_name = 'England';
        
# 12. Write a SQL query that returns the total number of goals scored by each position on each country’s team. Do not include positions which scored no goals.
SELECT 
    country_name,
    pm.team_id,
    posi_to_play,
    COUNT(goal_id) AS goal_num
FROM
    euro_cup_2016.goal_details gd
        JOIN
    player_mast pm ON gd.player_id = pm.player_id
        JOIN
    soccer_country sc ON pm.team_id = sc.country_id
GROUP BY country_name , pm.team_id , posi_to_play;

# 13. Write a SQL query to find all the defenders who scored a goal for their teams.
SELECT DISTINCT
    (player_name) AS GO
FROM
    euro_cup_2016.goal_details gd
        JOIN
    player_mast pm ON gd.player_id = pm.player_id
WHERE
    posi_to_play IN ('FD' , 'DF');

# 14. Write a SQL query to find referees and the number of bookings they made for the entire tournament. Sort your answer by the number of bookings in descending order.
SELECT 
    rm.referee_name, COUNT(match_no) AS bookings_num
FROM
    euro_cup_2016.match_mast mm
        LEFT JOIN
    referee_mast rm ON mm.referee_id = rm.referee_id
GROUP BY rm.referee_name
ORDER BY bookings_num DESC;

# 15. Write a SQL query to find the referees who booked the most number of players.  
# Q:  Can a match have the same player booked twice?
 SELECT 
    referee_name, COUNT(player_id) AS bookings_num
FROM
    (SELECT 
        mm.*, rm.referee_name, pb.player_id
    FROM
        euro_cup_2016.match_mast mm
    LEFT JOIN player_booked pb ON mm.match_no = pb.match_no
    LEFT JOIN referee_mast rm ON mm.referee_id = rm.referee_id) nt
GROUP BY rm.referee_name
ORDER BY bookings_num DESC
LIMIT 1;

# 16. Write a SQL query to find referees and the number of matches they worked in each venue.
SELECT 
    venue_name, referee_name, COUNT(match_no) AS match_num
FROM
    euro_cup_2016.match_mast mm
        JOIN
    soccer_venue sv ON mm.venue_id = sv.venue_id
        JOIN
    referee_mast rm ON mm.referee_id = rm.referee_id
GROUP BY venue_name , referee_name
ORDER BY venue_name;

# 17. Write a SQL query to find the country where the most assistant referees come from, and the count of the assistant referees.
SELECT 
    country_name, COUNT(ass_ref_name) AS ass_ref_num
FROM
    euro_cup_2016.asst_referee_mast rm
        JOIN
    soccer_country sc ON rm.country_id = sc.country_id
GROUP BY country_name
ORDER BY ass_ref_num DESC
LIMIT 1;

# 18. Write a SQL query to find the highest number of foul cards given in one match.
SELECT 
    COUNT(kick_id) AS foul_num
FROM
    euro_cup_2016.penalty_shootout
GROUP BY match_no
ORDER BY foul_num DESC
LIMIT 1;

# 19. Write a SQL query to find the number of captains who were also goalkeepers.
SELECT 
    COUNT(player_captain) AS captain_num
FROM
    euro_cup_2016.match_captain mc
        JOIN
    player_mast pm ON mc.player_captain = pm.player_id
WHERE
    posi_to_play = 'GK';

# 20. Write a SQL query to find the substitute players who came into the field in the first half of play, within a normal play schedule.
SELECT 
    player_name
FROM
    euro_cup_2016.player_in_out po
        JOIN
    match_mast mm ON po.match_no = mm.match_no
        JOIN
    player_mast pm ON po.player_id = pm.player_id
WHERE
    play_schedule = 'NT' AND play_half = 1;
