WITH star_wars_sets AS (
	SELECT set_num
    FROM themes 
	INNER JOIN sets
    	ON themes.id = sets.theme_id
    WHERE parent_id = (
        SELECT id FROM themes 
        WHERE name = 'Star Wars' 
        	AND parent_id IS NULL)
),

star_wars_sets_info AS (
    SELECT
    	set_num,
    	set_name, 
    	year, 
    	num_parts, 
    	color_name, 
    	rgb,
		ROW_NUMBER() OVER(PARTITION BY set_num ORDER BY number_per_color DESC) AS color_rank
    FROM (
        SELECT
        	sets.set_num AS set_num,
            rgb, 
            colors.name AS color_name, 
            sets.name AS set_name, 
            year, 
            num_parts, 
            SUM(quantity) AS number_per_color
		FROM inventory_parts
            INNER JOIN inventories
                ON inventory_parts.inventory_id = inventories.id
            INNER JOIN sets
                ON inventories.set_num = sets.set_num
            INNER JOIN colors
                ON inventory_parts.color_id = colors.id
		WHERE sets.set_num IN (SELECT set_num FROM star_wars_sets)
		GROUP BY sets.set_num, rgb, color_name, set_name, year, num_parts) AS sub
)

SELECT * FROM star_wars_sets_info 
WHERE color_rank = 1
