CREATE TABLE IF NOT EXISTS data_player (
    matricula CHAR(10) PRIMARY KEY,
    first_name VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL,
    middle_name VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL,
    last_name_paternal VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL,
    last_name_maternal VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL,
    date_of_birth DATE NULL,
    position VARCHAR(5) NULL,
    academic_program VARCHAR(5) NULL,
    date_of_entry DATE NULL,
    origin VARCHAR(10) NULL,
    curp CHAR(18) NULL
)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS physical_test (
    test_id INT AUTO_INCREMENT PRIMARY KEY,
    matricula CHAR(10) NULL,
    test_date DATE NULL,
    yds_10_1 FLOAT NULL,
    yds_10_2 FLOAT NULL,
    yds_40_1 FLOAT NULL,
    yds_40_2 FLOAT NULL,
    pro_rt FLOAT NULL,
    pro_lt FLOAT NULL,
    l_rt FLOAT NULL,
    l_lt FLOAT NULL,
    bj_1 FLOAT NULL,
    bj_2 FLOAT NULL,
    vj_1 FLOAT NULL,
    vj_2 FLOAT NULL,
    bp_1 FLOAT NULL,
    bp_2 FLOAT NULL,
    clean_1 INT NULL,
    clean_2 INT NULL,
    squat_1 INT NULL,
    squat_2 INT NULL,
    FOREIGN KEY (matricula) REFERENCES data_player(matricula)
)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS biometric (
    biometric_id INT AUTO_INCREMENT PRIMARY KEY,
    matricula CHAR(10) NULL,
    date DATE NULL,
    height FLOAT NULL,
    weight FLOAT NULL,
    acl FLOAT NULL,
    mass FLOAT NULL,
    mme FLOAT NULL,
    bmi FLOAT NULL,
    pgc FLOAT NULL,
    aec_act FLOAT NULL,
    protein FLOAT NULL,
    minerals FLOAT NULL,
    FOREIGN KEY (matricula) REFERENCES data_player(matricula)
)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;