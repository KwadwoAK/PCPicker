-- Because of my method of implementing the database using SQLAlchemy, I did not use a traditional SQL language to this
-- .sql file is a representation of my queries from my views.py file.

-- Query for fetching the home page (user-specific data)
SELECT *
FROM user
WHERE id = :current_user_id;

-- Query for creating a new build
INSERT INTO build (user_id, gpu_id, cpu_id, motherboard_id, ram_id, psu_id, storage_id, case_id, total_cost, build_date)
VALUES (:user_id, :gpu_id, :cpu_id, :motherboard_id, :ram_id, :psu_id, :storage_id, :case_id, 0, CURRENT_TIMESTAMP);

-- Query for fetching all builds for the current user
SELECT *
FROM build
WHERE user_id = :current_user_id;

-- Query for calculating the total cost of a build
SELECT
    SUM(gpu.msrp, cpu.msrp, motherboard.msrp, ram.msrp, storage.msrp, psu.msrp, case.msrp) AS total_cost
FROM build
JOIN gpu ON build.gpu_id = gpu.gpu_id
JOIN cpu ON build.cpu_id = cpu.cpu_id
JOIN motherboard ON build.motherboard_id = motherboard.motherboard_id
JOIN ram ON build.ram_id = ram.ram_id
JOIN storage ON build.storage_id = storage.storage_id
JOIN psu ON build.psu_id = psu.psu_id
JOIN case ON build.case_id = case.case_id
WHERE build.user_id = :current_user_id;

-- Query for deleting a build
DELETE FROM build
WHERE build_id = :build_id AND user_id = :current_user_id;

-- Query for editing a build
UPDATE build
SET gpu_id = :gpu_id,
    cpu_id = :cpu_id,
    motherboard_id = :motherboard_id,
    ram_id = :ram_id,
    psu_id = :psu_id,
    storage_id = :storage_id,
    case_id = :case_id,
    total_cost = (
        SELECT gpu.msrp + cpu.msrp + motherboard.msrp + ram.msrp + storage.msrp + psu.msrp + case.msrp
        FROM gpu, cpu, motherboard, ram, storage, psu, case
        WHERE gpu.gpu_id = :gpu_id AND cpu.cpu_id = :cpu_id AND motherboard.motherboard_id = :motherboard_id
          AND ram.ram_id = :ram_id AND storage.storage_id = :storage_id AND psu.psu_id = :psu_id AND case.case_id = :case_id
    )
WHERE build_id = :build_id AND user_id = :current_user_id;

-- Query for listing all manufacturers
SELECT DISTINCT manufacturer
FROM (
    SELECT manufacturer FROM gpu
    UNION
    SELECT manufacturer FROM cpu
    UNION
    SELECT manufacturer FROM motherboard
    UNION
    SELECT manufacturer FROM ram
    UNION
    SELECT manufacturer FROM storage
    UNION
    SELECT manufacturer FROM psu
    UNION
    SELECT manufacturer FROM case
) AS manufacturers;

-- Query for deleting a user and their associated builds
DELETE FROM user
WHERE id = :current_user_id;
   (DELETE from Build
    WHERE user_id = :current_user_id);

-- Unimplemented queries; These queries are examples of more complex SQL queries that I had planned to implement but did not get around to.
-- I have still added them here to show my knowledge of sql language and potential future implementations.

-- Fetch the most expensive build for each user (uses aggregate function and grouping)
SELECT
    b.user_id, MAX(b.total_cost) AS max_cost
FROM
    build b
GROUP BY
    b.user_id;

-- Query 3: Fetch builds where the total cost is above the average cost of all builds (uses subquery)
SELECT
    b.BuildID, b.total_cost
FROM
    build b
WHERE
    b.total_cost > (SELECT AVG(total_cost) FROM build);

-- Fetch users who have builds with GPUs from a specific manufacturer (uses subquery)
SELECT
    u.username
FROM
    user u
WHERE
    u.user_id IN (
        SELECT
            b.user_id
        FROM
            build b
        JOIN
            gpu g ON b.gpu_id = g.gpu_id
        WHERE
            g.manufacturer = 'NVIDIA'
    );

-- Fetch the total number of builds for each user, but only include users with more than 2 builds
SELECT
    b.user_id, COUNT(b.BuildID) AS build_count
FROM
    build b
GROUP BY
    b.user_id
HAVING
    COUNT(b.BuildID) > 2;

-- Fetch all manufacturers that produce both GPUs and CPUs
SELECT
    g.manufacturer
FROM
    gpu g
INTERSECT
SELECT
    c.manufacturer
FROM
    cpu c;

--  Fetch the average MSRP of GPUs for each manufacturer, This was to be used to give users a recommendation on which
-- GPU to buy based on average price.
SELECT
    g.manufacturer, AVG(g.msrp) AS avg_msrp
FROM
    gpu g
GROUP BY
    g.manufacturer
HAVING
    AVG(g.msrp) > 500;

