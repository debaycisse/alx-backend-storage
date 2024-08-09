-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER ##
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN

DECLARE av_scores INT;

SELECT AVG(score) INTO av_scores FROM corrections AS cr WHERE cr.user_id = user_id;

UPDATE users SET average_score = av_scores WHERE id = user_id;

END ##
DELIMITER ;
