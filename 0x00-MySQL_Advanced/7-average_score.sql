-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER ##
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN

DECLARE av_score DECIMAL(10, 2);
DECLARE total_scores INT;
DECLARE score_counts INT;

SELECT SUM(score) INTO total_scores FROM corrections WHERE user_id = user_id;
SELECT COUNT(score) INTO score_counts FROM corrections WHERE user_id = user_id;
SET av_score = total_scores / score_counts;

UPDATE users SET average_score = av_score WHERE id = user_id;

END ##
DELIMITER ;
