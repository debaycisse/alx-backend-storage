-- script creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DELIMITER ##
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Declare of variables
    DECLARE subject_id INT;
    DECLARE no_more_subject INT DEFAULT FALSE;
    DECLARE subject_weight INT;
    DECLARE subject_score FLOAT;
    DECLARE av_w_score FLOAT;

    -- Followed by declaration of cursors
    DECLARE corrections_cursor CURSOR FOR SELECT project_id, score FROM corrections AS c WHERE c.user_id = user_id;

    -- And, lastly declaration of handlers
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET no_more_subject = TRUE;

    -- Temporarry table declaration
    CREATE TEMPORARY TABLE av_weight_scores (score FLOAT, weight INT, weight_factor FLOAT);

    OPEN corrections_cursor;
        read_subject: LOOP
            FETCH corrections_cursor INTO subject_id, subject_score;
            IF no_more_subject THEN
                LEAVE read_subject;
            END IF;
            SELECT weight INTO subject_weight FROM projects WHERE id = subject_id;
            INSERT INTO av_weight_scores (score, weight, weight_factor) VALUES(subject_score, subject_weight, subject_score * subject_weight);
        END LOOP;
    CLOSE corrections_cursor;

    SELECT SUM(weight_factor) / SUM(weight) INTO av_w_score FROM av_weight_scores;

    UPDATE users SET average_score = av_w_score WHERE users.id = user_id;

    DROP TABLE IF EXISTS av_weight_scores;

END ##
DELIMITER ;
