SELECT * FROM articles;

DROP TABLE articles;
DROP TABLE users;

CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50) NOT NULL,
content VARCHAR(100) NOT NULL,
userId INTEGER NOT NULL,
FOREIGN KEY (userId) -- userId 컬럼은 외래키 제약 조건인데
  REFERENCES users(id) -- users 테이블의 id 컬럼 값 참조
--   ON DELETE SET NULL -- 지울때 널로
--   ON DELETE CASCADE -- 지우면 다지워짐
);

PRAGMA table_info('users');
PRAGMA table_info('articles');

INSERT INTO
  users (name)
VALUES
  ('하석주'),
  ('송윤미'),
  ('유하선');


INSERT INTO
  articles (title, content, userId)
VALUES
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 3),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);

-- 1번 게시글의 작성자 찾기
SELECT userId FROM articles WHERE id = 1;

SELECT name FROM users WHERE id = 1;

-- INNER JOIN
SELECT *
FROM articles
INNER JOIN users
ON users.id = articles.userId
WHERE users.id = 3;

-- LEFT JOIN
SELECT *
FROM articles
LEFT JOIN users
ON users.id = articles.userId;

-- 테이블 레코드 삭제시
DELETE FROM users
WHERE id = 3;

SELECT * FROM articles;
SELECT * FROM users;

SELECT * FROM artists;

-- 한명의 아티스트가 몇개의 앨범을 냈는지 알고 싶다
-- 출력할 데이터 : 앨범 개수, 아이트스 ID, 아티스트 이름
SELECT count(*) AS AlbumCount, artists.ArtistId, artists.name AS ArtistName
FROM albums
INNER JOIN artists
ON albums.ArtistId = artists.ArtistId
GROUP BY artists.ArtistId;

-- 22번 아티스트가 몇개의 앨범을 냈을까
SELECT count(*) 
FROM albums
WHERE ArtistId = 22;