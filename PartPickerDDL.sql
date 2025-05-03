-- For the actual database schema creation I used SQLAlchemy and their method of creating tables. This is the .SQL which is a representation of said method.


drop table if exists user;
drop table if exists gpu;
drop table if exists cpu;
drop table if exists motherboard;
drop table if exists ram;
drop table if exists storage;
drop table if exists psu;
drop table if exists cases;
drop table if exists build;

CREATE  TABLE  user (
  user_id INTEGER PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  Budget INTEGER NOT NULL,
  BuildID INTEGER,
  FOREIGN KEY (BuildID) REFERENCES build(BuildID)
);

CREATE  TABLE  gpu (
  gpu_id INTEGER PRIMARY KEY,
  gpu_name VARCHAR(50) NOT NULL,
  manufacturer VARCHAR(50) NOT NULL,
  gpu_brand VARCHAR(10) NOT NULL,
  VRAM INTEGER NOT NULL,
  VRAM_type VARCHAR(10) NOT NULL,
  msrp INTEGER NOT NULL,
  PCIe INTEGER NOT NULL,
  ReleaseDate DATE NOT NULL
);

CREATE TABLE cpu (
  cpu_id INTEGER PRIMARY KEY,
  cpu_name VARCHAR(50) NOT NULL,
  manufacturer VARCHAR(50) NOT NULL,
  cpu_brand VARCHAR(10) NOT NULL,
  cores INTEGER NOT NULL,
  threads INTEGER NOT NULL,
  base_clock INTEGER NOT NULL,
  boost_clock INTEGER NOT NULL,
  socket_type VARCHAR(10) NOT NULL,
  TDP INTEGER NOT NULL,
  msrp INTEGER NOT NULL,
  ReleaseDate DATE NOT NULL
);

CREATE TABLE motherboard (
    motherboard_id INTEGER PRIMARY KEY,
    motherboard_name VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(50) NOT NULL,
    socket_type VARCHAR(20) NOT NULL,
    chipset VARCHAR(20) NOT NULL,
    form_factor VARCHAR(20) NOT NULL,
    max_memory INTEGER NOT NULL,
    memory_slots INTEGER NOT NULL,
    max_memory_speed INTEGER NOT NULL,
    msrp INTEGER NOT NULL,
    ReleaseDate DATE NOT NULL
);

CREATE TABLE ram (
  ram_id INTEGER PRIMARY KEY,
  ram_name VARCHAR(50) NOT NULL,
  manufacturer VARCHAR(50) NOT NULL,
  capacity INTEGER NOT NULL,
  ram_type VARCHAR(10) NOT NULL,
  speed INTEGER NOT NULL,
  msrp INTEGER NOT NULL,
  ReleaseDate DATE NOT NULL
);

CREATE TABLE storage (
  storage_id INTEGER PRIMARY KEY,
  storage_name VARCHAR(50) NOT NULL,
  manufacturer VARCHAR(50) NOT NULL,
  storage_type VARCHAR(10) NOT NULL,
  capacity VARCHAR(15) NOT NULL,
  msrp INTEGER NOT NULL,
  speed VARCHAR(15) NOT NULL,
  ReleaseDate DATE NOT NULL
);

CREATE TABLE psu (
  psu_id INTEGER PRIMARY KEY,
  psu_name VARCHAR(50) NOT NULL,
  manufacturer VARCHAR(50) NOT NULL,
  wattage INTEGER NOT NULL,
  efficiency_rating VARCHAR(10) NOT NULL,
  modular VARCHAR(10) NOT NULL,
  msrp INTEGER NOT NULL,
  ReleaseDate DATE NOT NULL
);

CREATE TABLE cases (
    case_id INTEGER PRIMARY KEY,
    case_name VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(50) NOT NULL,
    form_factor VARCHAR(30) NOT NULL,
    color VARCHAR(20) NOT NULL,
    msrp DECIMAL(6,2) NOT NULL,
    ReleaseDate DATE NOT NULL
);

CREATE TABLE build (
  BuildID INTEGER PRIMARY KEY,
  user_id INTEGER NOT NULL,
  gpu_id INTEGER NOT NULL,
  cpu_id INTEGER NOT NULL,
  motherboard_id INTEGER NOT NULL,
  ram_id INTEGER NOT NULL,
  storage_id INTEGER NOT NULL,
  psu_id INTEGER NOT NULL,
  case_id INTEGER NOT NULL,
  total_cost INTEGER NOT NULL,
  build_date TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES user(user_id),
  FOREIGN KEY (gpu_id) REFERENCES gpu(gpu_id),
  FOREIGN KEY (cpu_id) REFERENCES cpu(cpu_id),
  FOREIGN KEY (motherboard_id) REFERENCES motherboard(motherboard_id),
  FOREIGN KEY (ram_id) REFERENCES ram(ram_id),
  FOREIGN KEY (storage_id) REFERENCES storage(storage_id),
  FOREIGN KEY (psu_id) REFERENCES psu(psu_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id)
);



