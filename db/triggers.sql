CREATE TRIGGER update_count
AFTER INSERT ON counts 
FOR EACH ROW
UPDATE total_counts
SET 
fatality = fatality + NEW.fatality_count,
infection = infection + NEW.infection_count
WHERE id=1;
