drop table if exists files;
create table files (
  id integer primary key autoincrement,
  file_id text not null, 
  timestamp integer not null, 
  ip text not null,
  originalname text not null
);